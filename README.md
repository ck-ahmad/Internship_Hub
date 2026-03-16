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
![n8n](https://img.shields.io/badge/n8n-EA4B71?style=for-the-badge&logo=n8n&logoColor=white)

<br/>

</div>

---

## Table of Contents

- [Why InternHub Exists](#-why-internhub-exists)
- [Tech Stack](#-tech-stack)
- [Quick Start](#-quick-start)
- [Project Structure](#-project-structure)
- [Class Diagram](#-class-diagram)
- [ER Diagram](#-er-diagram)
- [n8n Workflow](#-n8n-workflow)
- [API Reference](#-api-reference)
- [Features](#-features)
- [Database Schema](#-database-schema)
- [Security Model](#-security-model)
- [Switch to PostgreSQL](#-switch-to-postgresql)
- [Bugs Encountered & Fixed](#-bugs-encountered--fixed)
- [What You Learn Building This](#-what-you-learn-building-this)
- [Roadmap](#-roadmap)

---

## ◈ Why InternHub Exists

LinkedIn is built for professionals with years of experience. Students get lost in the noise — their profiles look empty, they compete against senior engineers for the same listings, and nothing is built for how they actually search for work.

**InternHub fixes this.** Every single feature is designed around the student-to-internship workflow. Companies post exclusively for interns. Students apply without noise. Profiles are built to show potential, not just experience.

> *We built this to learn. But we built it properly.*

---

## ◈ Tech Stack

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
│  Automation          │  n8n workflows for notifications + AI     │
│  Deployment-ready    │  Single command: python Main.py           │
└──────────────────────┴──────────────────────────────────────────┘
```

---

## ◈ Quick Start

```bash
# 1. Install dependencies
pip install -r Requirement.txt

# 2. Run the app
python Main.py

# 3. Open in browser
http://localhost:8000          →  App
http://localhost:8000/profile  →  Profile page
http://localhost:8000/docs     →  Swagger API docs
```

> ⚠️ **Python 3.12 users** — run this before starting or registration will crash:
> ```bash
> pip install bcrypt==4.0.1
> ```

---

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

---

## ◈ Class Diagram

```
┌─────────────────────────────────────────────────────────┐
│                         User                            │
├─────────────────────────────────────────────────────────┤
│  + id          : Integer (PK)                           │
│  + name        : String                                 │
│  + email       : String  (unique)                       │
│  + password    : String  (bcrypt hashed)                │
│  + role        : Enum [student | company]               │
│  + created_at  : DateTime                               │
├─────────────────────────────────────────────────────────┤
│  + register()  + login()                                │
└────────────────┬────────────────────┬───────────────────┘
                 │ 1:1                 │ 1:1
                 ▼                    ▼
┌───────────────────────┐   ┌───────────────────────────┐
│        Profile        │   │          Company          │
├───────────────────────┤   ├───────────────────────────┤
│  + user_id   : FK     │   │  + id           : PK      │
│  + headline  : String │   │  + company_name : String  │
│  + bio       : Text   │   │  + description  : Text    │
│  + location  : String │   │  + location     : String  │
│  + skills    : String │   │  + owner_id     : FK→User │
│  + photo_path: String │   ├───────────────────────────┤
│  + cover_path: String │   │  + create()               │
│  + cv_path   : String │   │  + update()               │
│  + linkedin_url       │   │  + get_listings()         │
│  + github_url         │   └────────────┬──────────────┘
│  + website_url        │                │ 1:N
├───────────────────────┤                ▼
│  + update()           │   ┌───────────────────────────┐
│  + upload_cv()        │   │        Internship         │
│  + upload_photo()     │   ├───────────────────────────┤
└────────┬──────────────┘   │  + id          : PK       │
         │                  │  + title       : String   │
    ┌────┴────┐             │  + description : Text     │
    │ 1:N     │ 1:N         │  + skills      : String   │
    ▼         ▼             │  + city        : String   │
┌──────────┐ ┌───────────┐  │  + duration    : String   │
│Education │ │Experience │  │  + is_remote   : Boolean  │
├──────────┤ ├───────────┤  │  + is_paid     : Boolean  │
│profile_id│ │profile_id │  │  + deadline    : Date     │
│school    │ │title      │  │  + is_open     : Boolean  │
│degree    │ │company    │  │  + company_id  : FK       │
│field     │ │location   │  ├───────────────────────────┤
│start_year│ │start_date │  │  + create()               │
│end_year  │ │end_date   │  │  + close()                │
└──────────┘ │description│  │  + delete()               │
             └───────────┘  └────────────┬──────────────┘
                                         │ 1:N
                                         ▼
                            ┌───────────────────────────┐
                            │        Application        │
                            ├───────────────────────────┤
                            │  + id           : PK      │
                            │  + student_id   : FK→User │
                            │  + internship_id: FK      │
                            │  + status       : Enum    │
                            │    [pending|accepted      │
                            │     |rejected]            │
                            │  + cv_path      : String  │
                            │  + applied_at   : DateTime│
                            ├───────────────────────────┤
                            │  + apply()                │
                            │  + update_status()        │
                            └───────────────────────────┘
```

---

## ◈ ER Diagram

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                                                                                  │
│   USERS ──────────────── 1:1 ──────────────── PROFILES                          │
│     │                                             │                             │
│     │ 1:1                                    ┌────┴────┐                        │
│     │                                        │         │                        │
│     ▼                                       1:N       1:N                       │
│   COMPANIES                                  ▼         ▼                        │
│     │                                    EDUCATION  EXPERIENCE                  │
│     │ 1:N                                                                       │
│     │                                                                           │
│     ▼                                                                           │
│   INTERNSHIPS ─────────────────────────── 1:N ──── APPLICATIONS                 │
│                                                          │                      │
│                                                          │ N:1                  │
│                                                          │                      │
│                                                       USERS                     │
│                                                    (student_id)                 │
│                                                                                  │
└──────────────────────────────────────────────────────────────────────────────────┘

Table: USERS
  id · name · email (unique) · password (hashed) · role · created_at

Table: PROFILES
  user_id (FK) · headline · bio · location · skills
  photo_path · cover_path · cv_path
  linkedin_url · github_url · website_url

Table: EDUCATION
  id · profile_id (FK) · school · degree · field · start_year · end_year

Table: EXPERIENCE
  id · profile_id (FK) · title · company · location
  start_date · end_date · description

Table: COMPANIES
  id · company_name · description · location · owner_id (FK→Users)

Table: INTERNSHIPS
  id · title · description · skills · city · duration
  is_remote · is_paid · deadline · is_open · company_id (FK)

Table: APPLICATIONS
  id · student_id (FK→Users) · internship_id (FK)
  status · cv_path · applied_at
```

---

## ◈ n8n Workflow

InternHub integrates with **n8n** for automation — application notifications, AI-powered skill matching, and deadline reminders.

### Workflow 1 — Application Lifecycle (Real-Time)

```
[Webhook Trigger]          POST /applications/apply/{id}
        │
        ▼
[Function Node]            Validate PDF extension + JWT token
        │
        ▼
[IF Condition]             Is input valid?
        │
   ┌────┴────┐
  YES       NO
   │         │
   ▼         ▼
[Postgres]  [Error Response]
Save app     Return HTTP 400
status=      "Invalid file or
pending      unauthorized"
   │
   ├──────────────────────────────────────┐
   │                                      │
   ▼                                      ▼
[Gmail Node]                         [Slack Node]
Send to student:                     Alert company channel:
"Application received for            "New applicant for
 {internship_title}"                  {internship_title}"
                                          │
                                          ▼
                                    [OpenAI Node]
                                    Compare student skills
                                    vs internship skills
                                    → Generate match score
                                    → Rank among applicants
```

### Workflow 2 — Deadline Reminders (Scheduled)

```
[Cron Trigger]             Every day at 09:00 AM
        │
        ▼
[Postgres Node]            SELECT internships WHERE
                           deadline <= NOW() + 2 days
                           AND is_open = true
        │
        ▼
[Split In Batches]         Loop over expiring listings
        │
        ▼
[Postgres Node]            Find students who haven't
                           applied to this listing
        │
        ▼
[Gmail Node]               Send reminder:
                           "⏰ {title} closes in 2 days!
                            Don't miss your chance."
```

### Workflow 3 — Status Change Notification

```
[Webhook Trigger]          PUT /applications/{id}/status
        │
        ▼
[IF Condition]             status == "accepted" OR "rejected"?
        │
        ▼
[Gmail Node]               Send to student:
                           ✅ "Congratulations! You've been accepted"
                           ❌ "Your application was not selected"
        │
        ▼
[HTTP Request]             POST to InternHub API
                           Update application record in DB
```

### n8n Node Types Used

| Node | Purpose |
|------|---------|
| `Webhook` | Trigger workflows from InternHub API calls |
| `Function` | Custom JS validation logic |
| `IF` | Branch on conditions (valid/invalid, status type) |
| `Postgres` | Read/write directly to InternHub database |
| `Gmail` | Email notifications to students and companies |
| `Slack` | Company channel alerts for new applicants |
| `OpenAI` | AI skill-matching and applicant ranking |
| `Cron` | Scheduled triggers for deadline checks |
| `Split In Batches` | Loop over multiple listings/students |
| `HTTP Request` | Call back to InternHub REST API |

---

## ◈ API Reference

### 🔐 Authentication

| Method | Endpoint | Access | Description |
|--------|----------|--------|-------------|
| `POST` | `/auth/register` | Public | Register as student or company |
| `POST` | `/auth/login` | Public | Login → receive JWT token + user_id |

### 💼 Internships

| Method | Endpoint | Access | Description |
|--------|----------|--------|-------------|
| `GET` | `/internships/` | Public | List all open listings |
| `GET` | `/internships/{id}` | Public | Single listing with company info |
| `POST` | `/internships/` | Company | Create new internship listing |
| `PUT` | `/internships/{id}` | Company | Update fields or close listing |
| `DELETE` | `/internships/{id}` | Company | Permanently delete listing |

> Query params: `?city=Lahore&skills=Python&is_remote=true&is_paid=false`

### 📋 Applications

| Method | Endpoint | Access | Description |
|--------|----------|--------|-------------|
| `POST` | `/applications/apply/{id}` | Student | Apply — uploads PDF CV |
| `GET` | `/applications/student` | Student | My applications + live status |
| `GET` | `/applications/company` | Company | All applicants for my listings |
| `PUT` | `/applications/{id}/status` | Company | pending \| accepted \| rejected |

### 👤 Profiles

| Method | Endpoint | Access | Description |
|--------|----------|--------|-------------|
| `GET` | `/profiles/me` | Auth | Fetch own profile (creates if new) |
| `PUT` | `/profiles/me` | Auth | Update bio, headline, location, links |
| `POST` | `/profiles/me/photo` | Auth | Upload profile photo (JPG/PNG/WEBP) |
| `POST` | `/profiles/me/cover` | Auth | Upload cover photo |
| `POST` | `/profiles/me/cv` | Auth | Upload resume PDF |
| `POST` | `/profiles/me/experience` | Auth | Add work experience entry |
| `DELETE` | `/profiles/me/experience/{id}` | Auth | Remove experience entry |
| `POST` | `/profiles/me/education` | Auth | Add education entry |
| `DELETE` | `/profiles/me/education/{id}` | Auth | Remove education entry |
| `GET` | `/profiles/{user_id}` | Public | View any user's public profile |

---

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
- Search by keyword or category: Engineering, Data Science, Design, Marketing
- Quick-search chips for the most popular roles
- Paginated results — browse through everything
- Every card links directly to the real application page

---

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
│  user_id · headline · bio · location · skills                        │
│  photo_path · cover_path · cv_path                                   │
│  linkedin_url · github_url · website_url                             │
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

---

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

---

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

---

## ◈ Bugs Encountered & Fixed

> *These are real problems that came up during development — not theoretical.*

| # | Problem | Fix |
|---|---------|-----|
| 1 | `python Main.py` does nothing | FastAPI needs uvicorn — added `uvicorn.run()` |
| 2 | bcrypt crashes on Python 3.12 | `pip install bcrypt==4.0.1` |
| 3 | Every API route returns 404 | `app.mount("/")` caught all routes — removed it |
| 4 | 307 redirect on every API call | Added trailing slash to all `fetch()` URLs |
| 5 | Dashboard blinks then empties | Removed broken `apps` dependency in `loadPostings()` |
| 6 | Filters send `undefined` in the URL | Added value check before appending to URL string |
| 7 | `ModuleNotFoundError` on startup | Created `__init__.py` in every subfolder |
| 8 | Muse API shows blank results | API uses 0-indexed pages — UI was sending `1` |

---

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

Automation (n8n)
  ├── Webhook-driven workflows — trigger on API events
  ├── AI integration — OpenAI skill matching via HTTP node
  ├── Multi-channel notifications — Gmail + Slack in one flow
  └── Scheduled jobs — cron-based deadline reminders

Real-World Skills
  ├── Debugging real production errors — bcrypt, routing, redirects
  ├── Third-party API integration — consuming The Muse REST API
  ├── Database design — normalized tables, relationships, constraints
  └── Layered architecture — routers, schemas, models, core separated
```

---

## ◈ Roadmap

- [ ] Email notifications when application status changes
- [ ] AI-powered recommendations based on profile skills
- [ ] Admin dashboard — verify companies, remove fake listings
- [ ] Docker + docker-compose for one-command deployment
- [ ] CI/CD pipeline via GitHub Actions
- [ ] WebSocket real-time notifications
- [ ] Company verification badges
- [ ] n8n full workflow setup guide + exported JSON

---

<div align="center">

```
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║                      InternHub                           ║
║                                                          ║
║             Built to learn. Built to last.               ║
║                                                          ║
║    FastAPI · SQLAlchemy · JWT · Tailwind · The Muse      ║
║                  n8n · OpenAI · bcrypt                   ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
```

</div>
