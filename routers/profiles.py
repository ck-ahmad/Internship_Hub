import os, shutil
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from models.models import Profile, Education, Experience, User
from schemas.schemas import ProfileUpdate, ProfileOut, PublicProfileOut, EducationCreate, EducationOut, ExperienceCreate, ExperienceOut
from core.security import get_current_user

router = APIRouter()

PHOTO_DIR = "uploads/photos"
os.makedirs(PHOTO_DIR, exist_ok=True)


def get_or_create_profile(user: User, db: Session) -> Profile:
    profile = db.query(Profile).filter(Profile.user_id == user.id).first()
    if not profile:
        profile = Profile(user_id=user.id)
        db.add(profile)
        db.commit()
        db.refresh(profile)
    return profile


# ---- My profile ----
@router.get("/me", response_model=ProfileOut)
def get_my_profile(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return get_or_create_profile(current_user, db)


@router.put("/me", response_model=ProfileOut)
def update_my_profile(data: ProfileUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    profile = get_or_create_profile(current_user, db)
    for field, value in data.dict(exclude_unset=True).items():
        setattr(profile, field, value)
    db.commit()
    db.refresh(profile)
    return profile


@router.post("/me/photo", response_model=ProfileOut)
def upload_photo(photo: UploadFile = File(...), db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if not photo.filename.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
        raise HTTPException(status_code=400, detail="Photo must be JPG, PNG or WEBP")
    profile = get_or_create_profile(current_user, db)
    filename = f"photo_{current_user.id}_{photo.filename}"
    path = os.path.join(PHOTO_DIR, filename)
    with open(path, "wb") as f:
        shutil.copyfileobj(photo.file, f)
    profile.photo_path = path
    db.commit(); db.refresh(profile)
    return profile


@router.post("/me/cover", response_model=ProfileOut)
def upload_cover(cover: UploadFile = File(...), db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if not cover.filename.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
        raise HTTPException(status_code=400, detail="Cover must be JPG, PNG or WEBP")
    profile = get_or_create_profile(current_user, db)
    filename = f"cover_{current_user.id}_{cover.filename}"
    path = os.path.join(PHOTO_DIR, filename)
    with open(path, "wb") as f:
        shutil.copyfileobj(cover.file, f)
    profile.cover_path = path
    db.commit(); db.refresh(profile)
    return profile


@router.post("/me/cv", response_model=ProfileOut)
def upload_cv(cv: UploadFile = File(...), db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if not cv.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="CV must be a PDF")
    profile = get_or_create_profile(current_user, db)
    filename = f"cv_{current_user.id}_{cv.filename}"
    path = os.path.join(PHOTO_DIR, filename)
    with open(path, "wb") as f:
        shutil.copyfileobj(cv.file, f)
    profile.cv_path = path
    db.commit(); db.refresh(profile)
    return profile


# ---- Education ----
@router.post("/me/education", response_model=EducationOut, status_code=201)
def add_education(data: EducationCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    profile = get_or_create_profile(current_user, db)
    edu = Education(**data.dict(), profile_id=profile.id)
    db.add(edu); db.commit(); db.refresh(edu)
    return edu


@router.delete("/me/education/{edu_id}", status_code=204)
def delete_education(edu_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    profile = get_or_create_profile(current_user, db)
    edu = db.query(Education).filter(Education.id == edu_id, Education.profile_id == profile.id).first()
    if not edu:
        raise HTTPException(status_code=404, detail="Education entry not found")
    db.delete(edu); db.commit()


# ---- Experience ----
@router.post("/me/experience", response_model=ExperienceOut, status_code=201)
def add_experience(data: ExperienceCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    profile = get_or_create_profile(current_user, db)
    exp = Experience(**data.dict(), profile_id=profile.id)
    db.add(exp); db.commit(); db.refresh(exp)
    return exp


@router.delete("/me/experience/{exp_id}", status_code=204)
def delete_experience(exp_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    profile = get_or_create_profile(current_user, db)
    exp = db.query(Experience).filter(Experience.id == exp_id, Experience.profile_id == profile.id).first()
    if not exp:
        raise HTTPException(status_code=404, detail="Experience entry not found")
    db.delete(exp); db.commit()


# ---- Public profile view ----
@router.get("/{user_id}", response_model=PublicProfileOut)
def get_public_profile(user_id: int, db: Session = Depends(get_db)):
    user    = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    profile = db.query(Profile).filter(Profile.user_id == user_id).first()
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not set up yet")
    # attach user name and role for display
    result = PublicProfileOut(
        **{c.name: getattr(profile, c.name) for c in profile.__table__.columns},
        education=profile.education,
        experience=profile.experience,
        user_name=user.name,
        user_role=user.role
    )
    return result
