from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base


class User(Base):
    __tablename__ = "users"

    id         = Column(Integer, primary_key=True, index=True)
    name       = Column(String, nullable=False)
    email      = Column(String, unique=True, index=True, nullable=False)
    password   = Column(String, nullable=False)
    role       = Column(String, default="student")
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    company      = relationship("Company",     back_populates="owner",   uselist=False)
    applications = relationship("Application", back_populates="student")
    profile      = relationship("Profile",     back_populates="user",    uselist=False)


class Profile(Base):
    __tablename__ = "profiles"

    id           = Column(Integer, primary_key=True, index=True)
    user_id      = Column(Integer, ForeignKey("users.id"), unique=True)
    headline     = Column(String)
    bio          = Column(Text)
    location     = Column(String)
    skills       = Column(String)
    photo_path   = Column(String)
    cover_path   = Column(String)
    cv_path      = Column(String)
    linkedin_url = Column(String)
    github_url   = Column(String)
    website_url  = Column(String)
    updated_at   = Column(DateTime(timezone=True), onupdate=func.now())

    user       = relationship("User",       back_populates="profile")
    education  = relationship("Education",  back_populates="profile", cascade="all, delete-orphan")
    experience = relationship("Experience", back_populates="profile", cascade="all, delete-orphan")


class Education(Base):
    __tablename__ = "education"

    id          = Column(Integer, primary_key=True, index=True)
    profile_id  = Column(Integer, ForeignKey("profiles.id"))
    school      = Column(String, nullable=False)
    degree      = Column(String)
    field       = Column(String)
    start_year  = Column(String)
    end_year    = Column(String)
    description = Column(Text)

    profile = relationship("Profile", back_populates="education")


class Experience(Base):
    __tablename__ = "experience"

    id          = Column(Integer, primary_key=True, index=True)
    profile_id  = Column(Integer, ForeignKey("profiles.id"))
    title       = Column(String, nullable=False)
    company     = Column(String, nullable=False)
    location    = Column(String)
    start_date  = Column(String)
    end_date    = Column(String)
    description = Column(Text)

    profile = relationship("Profile", back_populates="experience")


class Company(Base):
    __tablename__ = "companies"

    id           = Column(Integer, primary_key=True, index=True)
    company_name = Column(String, nullable=False)
    description  = Column(Text)
    location     = Column(String)
    owner_id     = Column(Integer, ForeignKey("users.id"))

    owner        = relationship("User",       back_populates="company")
    internships  = relationship("Internship", back_populates="company")


class Internship(Base):
    __tablename__ = "internships"

    id          = Column(Integer, primary_key=True, index=True)
    title       = Column(String, nullable=False)
    description = Column(Text)
    skills      = Column(String)
    city        = Column(String)
    duration    = Column(String)
    is_remote   = Column(Boolean, default=False)
    is_paid     = Column(Boolean, default=False)
    deadline    = Column(String)
    is_open     = Column(Boolean, default=True)
    company_id  = Column(Integer, ForeignKey("companies.id"))

    company      = relationship("Company",     back_populates="internships")
    applications = relationship("Application", back_populates="internship")


class Application(Base):
    __tablename__ = "applications"

    id            = Column(Integer, primary_key=True, index=True)
    student_id    = Column(Integer, ForeignKey("users.id"))
    internship_id = Column(Integer, ForeignKey("internships.id"))
    status        = Column(String, default="pending")
    cv_path       = Column(String)
    applied_at    = Column(DateTime(timezone=True), server_default=func.now())

    student    = relationship("User",       back_populates="applications")
    internship = relationship("Internship", back_populates="applications")
