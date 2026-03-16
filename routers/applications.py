import os
import shutil
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from models.models import Application, Internship, Company, User
from schemas.schemas import ApplicationOut, StatusUpdate
from core.security import get_current_user, require_role

router = APIRouter()

UPLOAD_DIR = "uploads/cvs"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/apply/{internship_id}", response_model=ApplicationOut, status_code=201)
def apply_for_internship(
    internship_id: int,
    cv: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role("student"))
):
    # check internship is open
    internship = db.query(Internship).filter(
        Internship.id == internship_id,
        Internship.is_open == True
    ).first()
    if not internship:
        raise HTTPException(status_code=404, detail="Internship not found or already closed")

    # prevent applying twice
    already_applied = db.query(Application).filter(
        Application.student_id == current_user.id,
        Application.internship_id == internship_id
    ).first()
    if already_applied:
        raise HTTPException(status_code=400, detail="You already applied for this internship")

    # PDF only
    if not cv.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="CV must be a PDF file")

    # save the file
    cv_filename = f"{current_user.id}_{internship_id}_{cv.filename}"
    cv_path = os.path.join(UPLOAD_DIR, cv_filename)
    with open(cv_path, "wb") as f:
        shutil.copyfileobj(cv.file, f)

    application = Application(
        student_id=current_user.id,
        internship_id=internship_id,
        cv_path=cv_path
    )
    db.add(application)
    db.commit()
    db.refresh(application)
    return application


@router.get("/student", response_model=List[ApplicationOut])
def get_my_applications(
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role("student"))
):
    return db.query(Application).filter(
        Application.student_id == current_user.id
    ).all()


@router.get("/company", response_model=List[ApplicationOut])
def get_company_applications(
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role("company"))
):
    company = db.query(Company).filter(Company.owner_id == current_user.id).first()
    if not company:
        raise HTTPException(status_code=404, detail="Company profile not found")

    internship_ids = [i.id for i in company.internships]
    return db.query(Application).filter(
        Application.internship_id.in_(internship_ids)
    ).all()


@router.put("/{application_id}/status", response_model=ApplicationOut)
def update_application_status(
    application_id: int,
    data: StatusUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role("company"))
):
    if data.status not in ["pending", "accepted", "rejected"]:
        raise HTTPException(status_code=400, detail="Status must be pending, accepted, or rejected")

    application = db.query(Application).filter(Application.id == application_id).first()
    if not application:
        raise HTTPException(status_code=404, detail="Application not found")

    company = db.query(Company).filter(Company.owner_id == current_user.id).first()
    internship_ids = [i.id for i in company.internships]
    if application.internship_id not in internship_ids:
        raise HTTPException(status_code=403, detail="You don't have access to this application")

    application.status = data.status
    db.commit()
    db.refresh(application)
    return application
