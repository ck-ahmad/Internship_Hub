from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional, List
from database import get_db
from models.models import Internship, Company, User
from schemas.schemas import InternshipCreate, InternshipUpdate, InternshipOut
from core.security import get_current_user, require_role

router = APIRouter()


@router.post("/", response_model=InternshipOut, status_code=201)
def create_internship(
    data: InternshipCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role("company"))
):
    company = db.query(Company).filter(Company.owner_id == current_user.id).first()
    if not company:
        raise HTTPException(status_code=404, detail="Company profile not found")

    internship = Internship(**data.dict(), company_id=company.id)
    db.add(internship)
    db.commit()
    db.refresh(internship)
    return internship


@router.get("/", response_model=List[InternshipOut])
def list_internships(
    city: Optional[str] = Query(None),
    skills: Optional[str] = Query(None),
    is_remote: Optional[bool] = Query(None),
    is_paid: Optional[bool] = Query(None),
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=50),
    db: Session = Depends(get_db)
):
    query = db.query(Internship).filter(Internship.is_open == True)

    if city:
        query = query.filter(Internship.city.ilike(f"%{city}%"))
    if skills:
        query = query.filter(Internship.skills.ilike(f"%{skills}%"))
    if is_remote is not None:
        query = query.filter(Internship.is_remote == is_remote)
    if is_paid is not None:
        query = query.filter(Internship.is_paid == is_paid)

    offset = (page - 1) * limit
    return query.offset(offset).limit(limit).all()


@router.get("/{internship_id}", response_model=InternshipOut)
def get_internship(internship_id: int, db: Session = Depends(get_db)):
    internship = db.query(Internship).filter(Internship.id == internship_id).first()
    if not internship:
        raise HTTPException(status_code=404, detail="Internship not found")
    return internship


@router.put("/{internship_id}", response_model=InternshipOut)
def update_internship(
    internship_id: int,
    data: InternshipUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role("company"))
):
    internship = db.query(Internship).filter(Internship.id == internship_id).first()
    if not internship:
        raise HTTPException(status_code=404, detail="Internship not found")

    company = db.query(Company).filter(Company.owner_id == current_user.id).first()
    if internship.company_id != company.id:
        raise HTTPException(status_code=403, detail="You don't own this internship")

    for field, value in data.dict(exclude_unset=True).items():
        setattr(internship, field, value)

    db.commit()
    db.refresh(internship)
    return internship


@router.delete("/{internship_id}", status_code=204)
def delete_internship(
    internship_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role("company"))
):
    internship = db.query(Internship).filter(Internship.id == internship_id).first()
    if not internship:
        raise HTTPException(status_code=404, detail="Internship not found")

    company = db.query(Company).filter(Company.owner_id == current_user.id).first()
    if internship.company_id != company.id:
        raise HTTPException(status_code=403, detail="You don't own this internship")

    db.delete(internship)
    db.commit()
