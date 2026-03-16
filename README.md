<div align="center">

```
██╗███╗   ██╗████████╗███████╗██████╗ ███╗   ██╗██╗  ██╗██╗   ██╗██████╗
██║████╗  ██║╚══██╔══╝██╔════╝██╔══██╗████╗  ██║██║  ██║██║   ██║██╔══██╗
██║██╔██╗ ██║   ██║   █████╗  ██████╔╝██╔██╗ ██║███████║██║   ██║██████╔╝
██║██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗██║╚██╗██║██╔══██║██║   ██║██╔══██╗
██║██║ ╚████║   ██║   ███████╗██║  ██║██║ ╚████║██║  ██║╚██████╔╝██████╔╝
╚═╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝
```

### *Your Career Starts Here.*

**A full-stack internship portal built with FastAPI, plain HTML, Tailwind CSS, and The Muse API**

<br/>

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Python](https://img.shields.io/badge/Python_3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=jsonwebtokens&logoColor=white)
![TailwindCSS](https://img.shields.io/badge/Tailwind_CSS-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white)

<br/>

</div>

---

<br/>

## ◈ Why InternHub Exists

LinkedIn is built for professionals with years of experience. Students get lost in the noise — their profiles look empty, they compete against senior engineers for the same listings, and nothing is built for how they actually search for work.

**InternHub fixes this.** Every single feature is designed around the student-to-internship workflow. Companies post exclusively for interns. Students apply without noise. Profiles are built to show potential, not just experience.

> *We built this to learn. But we built it properly.*

<br/>

---

<br/>

## ◈ What's Inside

```
┌─────────────────────────────────────────────────────────────────┐
│                        INTERNHUB v3.0                           │
├──────────────────────┬──────────────────────────────────────────┤
│  Backend             │  FastAPI + SQLAlchemy + JWT + bcrypt      │
│  Database            │  SQLite (dev) → PostgreSQL (prod)         │
│  Frontend            │  Plain HTML + Tailwind CSS — no framework │
│  Auth                │  OAuth2 + JWT tokens + role-based guards  │
│  File Uploads        │  CV (PDF) + Profile Photo + Cover Photo   │
│  External API        │  The Muse — free, no key required         │
│  Profiles            │  LinkedIn-style public profile pages      │
│  Deployment-ready    │  Single command: python Main.py           │
└──────────────────────┴──────────────────────────────────────────┘
```

<br/>

---

<br/>

## ◈ Quick Start

```bash
# 1. Install
pip install -r Requirement.txt

# 2. Run
python Main.py

# 3. Open
http://localhost:8000          → App
http://localhost:8000/profile  → Profile page
http://localhost:8000/docs     → Swagger API docs
```

> ⚠️ **Python 3.12 users** — run this before starting or registration will crash:
> ```bash
> pip install bcrypt==4.0.1
> ```

<br/>

---

<br/>

## ◈ Project Structure

```
InternshipsPortal/
│
├── 📄 Main.py                    ← Start here. uvicorn.run() lives here.
├── 📄 database.py                ← SQLAlchemy engine, session, Base
├── 📄 Requirement.txt            ← All pip dependencies
│
├── 📁 models/
│   ├── __init__.py
│   └── models.py                 ← User · Profile · Education · Experience
│                                    Company · Internship · Application
│
├── 📁 schemas/
│   ├── __init__.py
│   └── schemas.py                ← Pydantic models for every request/response
│
├── 📁 routers/
│   ├── __init__.py
│   ├── auth.py                   ← /auth/register  /auth/login
│   ├── internships.py            ← CRUD + search + pagination + filters
│   ├── applications.py           ← Apply · Track · Accept/Reject
│   └── profiles.py               ← Public profiles · Photo · CV · Exp · Edu
│
├── 📁 core/
│   ├── __init__.py
│   └── security.py               ← JWT · bcrypt · get_current_user · require_role
│
├── 📁 uploads/
│   ├── cvs/                      ← Student resume PDFs
│   └── photos/                   ← Profile photos + cover images
│
└── 📁 frontend/
    ├── index.html                ← Full SPA — Home, Browse, Auth, Dashboards
    └── profile.html              ← LinkedIn-style public profile page
```

<br/>

---

<br/>

## ◈ API Reference

### 🔐 Authentication
```
POST   /auth/register          Public     Register as student or company
POST   /auth/login             Public     Login → receive JWT token + user_id
```

### 💼 Internships
```
GET    /internships/           Public     List all open listings
                                          ?city=Lahore&skills=Python
                                          &is_remote=true&is_paid=false
GET    /internships/{id}       Public     Single listing with company info
POST   /internships/           Company    Create new internship listing
PUT    /internships/{id}       Company    Update fields or close listing
DELETE /internships/{id}       Company    Permanently delete listing
```

### 📋 Applications
```
POST   /applications/apply/{id}      Student    Apply — uploads PDF CV
GET    /applications/student         Student    My applications + live status
GET    /applications/company         Company    All applicants for my listings
PUT    /applications/{id}/status     Company    pending | accepted | rejected
```

### 👤 Profiles
```
GET    /profiles/me                   Auth      Fetch own profile (creates if new)
PUT    /profiles/me                   Auth      Update bio, headline, location, links
POST   /profiles/me/photo             Auth      Upload profile photo (JPG/PNG/WEBP)
POST   /profiles/me/cover             Auth      Upload cover photo
POST   /profiles/me/cv                Auth      Upload resume PDF
POST   /profiles/me/experience        Auth      Add work experience entry
DELETE /profiles/me/experience/{id}   Auth      Remove experience entry
POST   /profiles/me/education         Auth      Add education entry
DELETE /profiles/me/education/{id}    Auth      Remove education entry
GET    /profiles/{user_id}            Public    View any user's public profile
```

<br/>

---

<br/>

## ◈ Database Schema

```
┌──────────────────────────────────────────────────────────────────────┐
│ USERS                                                                │
│  id · name · email (unique) · password (hashed) · role · created_at │
└────────────────────────────┬─────────────────────────────────────────┘
                             │ one-to-one
                             ▼
┌──────────────────────────────────────────────────────────────────────┐
│ PROFILES                                                             │
│  user_id · headline · bio · location · skills                       │
│  photo_path · cover_path · cv_path                                  │
│  linkedin_url · github_url · website_url                            │
└─────────┬────────────────────────┬───────────────────────────────────┘
          │ one-to-many             │ one-to-many
          ▼                         ▼
┌──────────────────┐     ┌──────────────────────────────────────┐
│ EDUCATION        │     │ EXPERIENCE                           │
│  profile_id      │     │  profile_id                          │
│  school · degree │     │  title · company · location          │
│  field           │     │  start_date · end_date               │
│  start/end year  │     │  description                         │
└──────────────────┘     └──────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────┐
│ COMPANIES                                                            │
│  id · company_name · description · location · owner_id → Users      │
└────────────────────────────┬─────────────────────────────────────────┘
                             │ one-to-many
                             ▼
┌──────────────────────────────────────────────────────────────────────┐
│ INTERNSHIPS                                                          │
│  id · title · description · skills · city · duration                │
│  is_remote · is_paid · deadline · is_open · company_id              │
└────────────────────────────┬─────────────────────────────────────────┘
                             │ one-to-many
                             ▼
┌──────────────────────────────────────────────────────────────────────┐
│ APPLICATIONS                                                         │
│  id · student_id → Users · internship_id                            │
│  status (pending/accepted/rejected) · cv_path · applied_at          │
└──────────────────────────────────────────────────────────────────────┘
```

<br/>

---

<br/>

## ◈ Features

### For Students
- 🔍 Browse internships — filter by city, skill, remote, paid/unpaid
- 📄 Apply with one click — upload PDF CV, one application per listing
- 📊 Track status live — Pending → Accepted / Rejected
- 👤 Build a public profile — photo, bio, skills, experience, education, CV

### For Companies
- ✏️ Post internships — title, skills, city, duration, deadline, paid/remote flags
- 👥 View all applicants — see who applied and when
- ✅ Update status — accept, reject, or keep pending for each applicant
- 🔒 Close or delete listings from the dashboard

### LinkedIn-Style Profiles *(both roles)*
- Profile photo + cover photo — click to upload, updates instantly
- Headline, bio, and location visible on public URL
- Skills rendered as tags
- Work experience with company, location, dates, description
- Education with school, degree, field, years
- Resume PDF — uploaded and downloadable by anyone
- Social links — LinkedIn, GitHub, Portfolio website

### Global Jobs — The Muse API
- 🌍 Thousands of real jobs — no API key, completely free
- Search by keyword or category: Engineering, Data Science, Design, Marketing...
- Quick-search chips for the most popular roles
- Paginated results — browse through everything
- Every card links directly to the real application page

<br/>

---

<br/>

## ◈ Security Model

```
Passwords       bcrypt hashed via passlib — plain text never touches the database
Tokens          JWT with 24-hour expiry — stored client-side in localStorage
Role Guards     require_role("student") and require_role("company") decorators
                protect every sensitive endpoint at the FastAPI dependency level
CV Uploads      Server validates .pdf extension before saving — rejects anything else
Photo Uploads   Server validates .jpg .jpeg .png .webp — rejects everything else
CORS            Allow-all in development — change allow_origins in Main.py for prod
Double Apply    Database-level check — one student can only apply once per listing
```

<br/>

---

<br/>

## ◈ Switch to PostgreSQL

Open `database.py` and swap the URL:

```python
# Default — SQLite, zero setup
DATABASE_URL = "sqlite:///./internship_portal.db"

# Production — PostgreSQL
DATABASE_URL = "postgresql://username:password@localhost/internhub"
```

Then install the driver:
```bash
pip install psycopg2-binary
```

Everything else stays exactly the same.

<br/>

---

<br/>

## ◈ Bugs Encountered & Fixed

> *These are real problems that came up during development — not theoretical.*

```
┌────┬───────────────────────────────────────┬──────────────────────────────────────────────────┐
│ #  │ Problem                               │ Fix                                              │
├────┼───────────────────────────────────────┼──────────────────────────────────────────────────┤
│ 1  │ python Main.py does nothing           │ FastAPI needs uvicorn — added uvicorn.run()       │
│ 2  │ bcrypt crashes on Python 3.12         │ pip install bcrypt==4.0.1                        │
│ 3  │ Every API route returns 404           │ app.mount("/") caught all routes — removed it    │
│ 4  │ 307 redirect on every API call        │ Added trailing slash to all fetch() URLs         │
│ 5  │ Dashboard blinks then empties         │ Removed broken apps dependency in loadPostings() │
│ 6  │ Filters send undefined in the URL     │ Added value check before appending to URL string │
│ 7  │ ModuleNotFoundError on startup        │ Created __init__.py in every subfolder           │
│ 8  │ Muse API shows blank results          │ API uses 0-indexed pages — UI was sending 1      │
└────┴───────────────────────────────────────┴──────────────────────────────────────────────────┘
```

<br/>

---

<br/>

## ◈ What You Learn Building This

```
Backend
  ├── REST API design — routes, methods, status codes, query params
  ├── JWT authentication — token creation, decoding, expiry, guards
  ├── Role-based access control — decorators on every protected endpoint
  ├── SQLAlchemy ORM — models, foreign keys, relationships, queries
  ├── Pydantic — request validation, response shaping, nested schemas
  └── File handling — multipart form uploads, path storage, static serving

Frontend
  ├── Single-page application — no React, no Vue, just JavaScript
  ├── fetch() API — GET, POST, PUT, DELETE with auth headers
  ├── localStorage — token, role, user_id across page reloads
  └── DOM manipulation — rendering cards, modals, dashboards dynamically

Real-World Skills
  ├── Debugging real production errors — bcrypt, routing, redirects
  ├── Third-party API integration — consuming The Muse REST API
  ├── Database design — normalized tables, relationships, constraints
  └── Layered architecture — routers, schemas, models, core separated
```

<br/>

---

<br/>

## ◈ Roadmap

- [ ] Email notifications when application status changes
- [ ] AI-powered recommendations based on profile skills
- [ ] Admin dashboard — verify companies, remove fake listings
- [ ] Docker + docker-compose for one-command deployment
- [ ] CI/CD pipeline via GitHub Actions
- [ ] WebSocket real-time notifications
- [ ] Company verification badges

<br/>

---

<br/>

<div align="center">

```
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║                      InternHub                           ║
║                                                          ║
║             Built to learn. Built to last.               ║
║                                                          ║
║    FastAPI · SQLAlchemy · JWT · Tailwind · The Muse      ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
```

</div>
