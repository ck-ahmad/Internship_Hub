from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


# ----- Auth -----

class RegisterRequest(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: str = "student"


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    role: str
    name: str


# ----- Company -----

class CompanyCreate(BaseModel):
    company_name: str
    description: Optional[str] = None
    location: Optional[str] = None


class CompanyOut(BaseModel):
    id: int
    company_name: str
    description: Optional[str]
    location: Optional[str]

    class Config:
        from_attributes = True


# ----- Internship -----

class InternshipCreate(BaseModel):
    title: str
    description: Optional[str] = None
    skills: Optional[str] = None
    city: Optional[str] = None
    duration: Optional[str] = None
    is_remote: bool = False
    is_paid: bool = False
    deadline: Optional[str] = None


class InternshipUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    skills: Optional[str] = None
    city: Optional[str] = None
    duration: Optional[str] = None
    is_remote: Optional[bool] = None
    is_paid: Optional[bool] = None
    deadline: Optional[str] = None
    is_open: Optional[bool] = None


class InternshipOut(BaseModel):
    id: int
    title: str
    description: Optional[str]
    skills: Optional[str]
    city: Optional[str]
    duration: Optional[str]
    is_remote: bool
    is_paid: bool
    deadline: Optional[str]
    is_open: bool
    company: Optional[CompanyOut]

    class Config:
        from_attributes = True


# ----- Application -----

class ApplicationOut(BaseModel):
    id: int
    student_id: int
    internship_id: int
    status: str
    cv_path: Optional[str]
    applied_at: datetime
    internship: Optional[InternshipOut]

    class Config:
        from_attributes = True


class StatusUpdate(BaseModel):
    status: str  # accepted | rejected | pending


# ----- Profile -----

class EducationCreate(BaseModel):
    school: str
    degree: Optional[str] = None
    field: Optional[str] = None
    start_year: Optional[str] = None
    end_year: Optional[str] = None
    description: Optional[str] = None

class EducationOut(EducationCreate):
    id: int
    class Config:
        from_attributes = True

class ExperienceCreate(BaseModel):
    title: str
    company: str
    location: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    description: Optional[str] = None

class ExperienceOut(ExperienceCreate):
    id: int
    class Config:
        from_attributes = True

class ProfileUpdate(BaseModel):
    headline: Optional[str] = None
    bio: Optional[str] = None
    location: Optional[str] = None
    skills: Optional[str] = None
    linkedin_url: Optional[str] = None
    github_url: Optional[str] = None
    website_url: Optional[str] = None

class ProfileOut(BaseModel):
    id: int
    user_id: int
    headline: Optional[str]
    bio: Optional[str]
    location: Optional[str]
    skills: Optional[str]
    photo_path: Optional[str]
    cover_path: Optional[str]
    cv_path: Optional[str]
    linkedin_url: Optional[str]
    github_url: Optional[str]
    website_url: Optional[str]
    education: list[EducationOut] = []
    experience: list[ExperienceOut] = []
    class Config:
        from_attributes = True

class PublicProfileOut(BaseModel):
    id: int
    user_id: int
    headline: Optional[str]
    bio: Optional[str]
    location: Optional[str]
    skills: Optional[str]
    photo_path: Optional[str]
    cover_path: Optional[str]
    cv_path: Optional[str]
    linkedin_url: Optional[str]
    github_url: Optional[str]
    website_url: Optional[str]
    education: list[EducationOut] = []
    experience: list[ExperienceOut] = []
    user_name: Optional[str] = None
    user_role: Optional[str] = None
    class Config:
        from_attributes = True
