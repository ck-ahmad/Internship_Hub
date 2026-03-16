from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from database import Base, engine
from routers import auth, internships, applications, profiles
import os

os.makedirs("uploads/photos", exist_ok=True)
os.makedirs("uploads/cvs",    exist_ok=True)

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Internship Portal API",
    description="Backend for connecting students with companies offering internships",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router,         prefix="/auth",         tags=["Authentication"])
app.include_router(internships.router,  prefix="/internships",  tags=["Internships"])
app.include_router(applications.router, prefix="/applications", tags=["Applications"])
app.include_router(profiles.router,     prefix="/profiles",     tags=["Profiles"])

# serve uploaded files (photos, CVs)
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

@app.get("/api")
def root():
    return {"message": "Internship Portal API is running"}

@app.get("/")
def home():
    return FileResponse("frontend/index.html")

@app.get("/profile")
def profile_page():
    return FileResponse("frontend/profile.html")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("Main:app", host="0.0.0.0", port=8000, reload=True)
