from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(String, default="student")  # student | company | admin
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # relationships
    company = relationship("Company", back_populates="owner", uselist=False)
    applications = relationship("Application", back_populates="student")


class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String, nullable=False)
    description = Column(Text)
    location = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="company")
    internships = relationship("Internship", back_populates="company")


class Internship(Base):
    __tablename__ = "internships"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text)
    skills = Column(String)         # comma-separated e.g. "Python,Django,SQL"
    city = Column(String)
    duration = Column(String)       # e.g. "3 months"
    is_remote = Column(Boolean, default=False)
    is_paid = Column(Boolean, default=False)
    deadline = Column(String)
    is_open = Column(Boolean, default=True)
    company_id = Column(Integer, ForeignKey("companies.id"))

    company = relationship("Company", back_populates="internships")
    applications = relationship("Application", back_populates="internship")


class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("users.id"))
    internship_id = Column(Integer, ForeignKey("internships.id"))
    status = Column(String, default="pending")  # pending | accepted | rejected
    cv_path = Column(String)
    applied_at = Column(DateTime(timezone=True), server_default=func.now())

    student = relationship("User", back_populates="applications")
    internship = relationship("Internship", back_populates="applications")