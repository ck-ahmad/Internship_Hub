from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.models import User, Company
from schemas.schemas import RegisterRequest, LoginRequest, TokenResponse
from core.security import hash_password, verify_password, create_access_token

router = APIRouter()


@router.post("/register", status_code=201)
def register(data: RegisterRequest, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.email == data.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    if data.role not in ["student", "company"]:
        raise HTTPException(status_code=400, detail="Role must be 'student' or 'company'")

    user = User(name=data.name, email=data.email, password=hash_password(data.password), role=data.role)
    db.add(user); db.commit(); db.refresh(user)

    if data.role == "company":
        company = Company(company_name=data.name, owner_id=user.id)
        db.add(company); db.commit()

    return {"message": "Registration successful", "user_id": user.id}


@router.post("/login")
def login(data: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == data.email).first()
    if not user or not verify_password(data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    token = create_access_token({"user_id": user.id, "role": user.role})

    # return user_id so frontend can build profile link
    return {
        "access_token": token,
        "token_type":   "bearer",
        "role":         user.role,
        "name":         user.name,
        "user_id":      user.id
    }
