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

**A full-stack internship portal connecting students with companies — built with FastAPI, Tailwind CSS, and The Muse API**

<br/>

![Status](https://img.shields.io/badge/Status-v3.0_Complete-gold?style=for-the-badge)
![Python](https://img.shields.io/badge/Python_3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=jsonwebtokens&logoColor=white)
![TailwindCSS](https://img.shields.io/badge/Tailwind_CSS-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge)

<br/>

</div>

---

<br/>

## 🚧 **Project Status**

> This project has completed **InternHub v3.0** — Full-Stack Portal with LinkedIn-Style Profiles, Global Job Listings, and Dark Premium UI.

---

## 💡 **Overview**

LinkedIn is built for professionals. Students get lost in the noise — their profiles look empty, they compete with senior engineers for the same listings, and nothing is designed for how they actually search for work.

**InternHub fixes this.** Every feature is built around the student-to-internship workflow. Companies post exclusively for interns. Students apply without noise. Profiles are built to show potential, not just experience. And with The Muse API integration, students get access to thousands of real jobs from Google, Netflix, Spotify — for free, no API key needed.

> 🎓 **Students** can browse, apply, track status, and build a public profile<br/>
> 🏢 **Companies** can post listings, review applicants, and manage everything from a dashboard<br/>
> 🌍 **Global Jobs** from The Muse API — thousands of real roles, search by keyword or category<br/>
> 👤 **Public Profiles** — LinkedIn-style with photo, CV, experience, education, social links

---

## 🎯 **Core Objectives**

* 🎓 Give students a dedicated space — not competing with professionals
* 🏢 Let companies reach intern-specific talent without noise
* 🔐 Secure role-based authentication — students and companies have different access
* ☁️ Store CVs, photos, and profiles in cloud storage
* 🌍 Combine local listings with global job discovery via The Muse API
* 👤 LinkedIn-style public profiles for every user
* 📊 Dashboards for both students (track applications) and companies (manage listings)

---

## ⚙️ **Technology Stack**

| Layer | Tools / Frameworks |
| --- | --- |
| **Backend** | FastAPI (Python) |
| **Database** | SQLite (dev) / PostgreSQL (prod) |
| **ORM** | SQLAlchemy |
| **Authentication** | OAuth2 + JWT + bcrypt |
| **Validation** | Pydantic |
| **Frontend** | Plain HTML + Tailwind CSS — no framework |
| **File Uploads** | FastAPI UploadFile — CV, photo, cover |
| **External API** | The Muse — free, no key required |
| **API Docs** | Swagger UI (auto-generated) |
| **Deployment** | Single command: `python Main.py` |

---

## ✨ **Key Features**

### 🎓 **For Students**
- **🔍 Browse & Search**: Filter internships by city, skill, remote, paid/unpaid
- **📄 Apply**: One-click apply with PDF CV upload — one application per listing
- **📊 Track Status**: Live status — Pending → Accepted / Rejected
- **👤 Public Profile**: LinkedIn-style profile with photo, bio, skills, experience, education, CV, social links

### 🏢 **For Companies**
- **✏️ Post Listings**: Title, skills, city, duration, deadline, paid/remote flags
- **👥 Review Applicants**: See everyone who applied and when
- **✅ Manage Status**: Accept, reject, or keep pending per applicant
- **🔒 Manage Listings**: Close or delete from dashboard

### 👤 **Profiles (Both Roles)**
- Profile photo + cover photo — click to upload, updates instantly
- Headline, bio, location — visible on public URL
- Skills as tags, work experience with company and dates
- Education with school, degree, field, years
- Resume PDF — uploaded and downloadable by anyone
- Social links — LinkedIn, GitHub, Portfolio

### 🌍 **Global Jobs — The Muse API**
- Free public API — no signup or key required
- Search by keyword or pick a category
- Quick-search chips: Software Engineer, Data Science, Marketing...
- Paginated results — browse thousands of listings
- Every card links directly to the real application page

---

## 🧩 **System Architecture**

### **Major Modules**

| Module | Description |
| --- | --- |
| 🔐 **Authentication** | JWT + bcrypt — role-based guards on every protected endpoint |
| 🎓 **Student System** | Browse, filter, apply with PDF, track status live |
| 🏢 **Company System** | Post listings, view applicants, update status |
| 👤 **Profile System** | LinkedIn-style profiles — photo, CV, experience, education |
| 🌍 **Global Jobs** | The Muse API integration — thousands of real roles |
| 📊 **Dashboards** | Separate dashboards for students and companies |

---

## 🔄 **System Workflow**

```
┌─────────────────────────────────────────────────────────────────────┐
│                         SYSTEM FLOW                                 │
└─────────────────────────────────────────────────────────────────────┘

  👤 User registers as Student or Company
          │
          ▼
  🔐 JWT token issued on login — role stored in token
          │
          ├─────────────────────┬──────────────────────┐
          ▼                     ▼                      ▼
  🎓 STUDENT                🏢 COMPANY            🌍 GLOBAL JOBS
  Browse internships        Post a listing         Search The Muse API
  Apply with PDF CV         View applicants        Filter by category
  Track status live         Accept / Reject        Click → apply direct
  Build public profile      Close / Delete         No API key needed
          │                     │
          ▼                     ▼
  📊 Student Dashboard      📊 Company Dashboard
  All my applications       All my listings
  Status per company        All applicants per role
          │                     │
          ▼                     ▼
  🗄️ Applications Table   🗄️ Internships Table
  CV stored in /uploads     Listings in database
```

---

## 🛠️ **Project Structure**

```
InternshipsPortal/
│
├── 📄 Main.py                    ← Entry point — run this
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

## 🚀 **API Endpoints**

### Authentication
| Method | Endpoint | Description |
| --- | --- | --- |
| POST | `/auth/register` | Register as student or company |
| POST | `/auth/login` | Login — returns JWT token + user_id |

### Internships
| Method | Endpoint | Description |
| --- | --- | --- |
| GET | `/internships/` | List all open listings — supports filters |
| GET | `/internships/{id}` | Single listing with company info |
| POST | `/internships/` | Create new internship (Company) |
| PUT | `/internships/{id}` | Update fields or close listing (Company) |
| DELETE | `/internships/{id}` | Permanently delete listing (Company) |

### Applications
| Method | Endpoint | Description |
| --- | --- | --- |
| POST | `/applications/apply/{id}` | Apply — upload PDF CV (Student) |
| GET | `/applications/student` | My applications + live status (Student) |
| GET | `/applications/company` | All applicants for my listings (Company) |
| PUT | `/applications/{id}/status` | pending / accepted / rejected (Company) |

### Profiles
| Method | Endpoint | Description |
| --- | --- | --- |
| GET | `/profiles/me` | Fetch own profile — creates if new |
| PUT | `/profiles/me` | Update bio, headline, location, links |
| POST | `/profiles/me/photo` | Upload profile photo (JPG/PNG/WEBP) |
| POST | `/profiles/me/cover` | Upload cover photo |
| POST | `/profiles/me/cv` | Upload resume PDF |
| POST | `/profiles/me/experience` | Add work experience entry |
| DELETE | `/profiles/me/experience/{id}` | Remove experience entry |
| POST | `/profiles/me/education` | Add education entry |
| DELETE | `/profiles/me/education/{id}` | Remove education entry |
| GET | `/profiles/{user_id}` | View any user's public profile |

---

## 🔄 **n8n Automation Workflow**

> InternHub's core pipelines — applying, reviewing, status updating — can be visualized and automated using **n8n**. The diagrams below show the full node-based flow for each major pipeline.

### Pipeline 1 — Student Applies for Internship

```mermaid
flowchart LR
    classDef trigger  fill:#ea4b71,stroke:#c73d60,color:#fff
    classDef process  fill:#1e293b,stroke:#475569,color:#e2e8f0
    classDef validate fill:#7c3aed,stroke:#6d28d9,color:#fff
    classDef storage  fill:#065f46,stroke:#059669,color:#fff
    classDef notify   fill:#92400e,stroke:#d97706,color:#fff
    classDef done     fill:#14532d,stroke:#16a34a,color:#fff

    A([🖱️ Webhook Trigger\nPOST /applications/apply]):::trigger
    B[🔐 JWT Auth Node\nVerify student token\nExtract user_id]:::process
    C[📋 HTTP Request\nGET /internships/id\nCheck is_open = true]:::process
    D{✅ Internship\nStill Open?}:::validate
    E[🚫 Error Response\nInternship closed\nReturn 404]:::notify
    F[🔍 DB Query Node\nCheck duplicate\napplication exists?]:::process
    G{👤 Already\nApplied?}:::validate
    H[🚫 Error Response\nDuplicate application\nReturn 400]:::notify
    I[📄 File Validator\nCheck CV = .pdf\nReject other formats]:::process
    J[💾 Save File Node\nuploads/cvs/\nstudent_id + filename]:::storage
    K[🗄️ Database Node\nINSERT application\nstatus = pending]:::storage
    L([✅ Success Response\nApplication submitted\nReturn 201]):::done

    A --> B --> C --> D
    D -->|Closed| E
    D -->|Open| F
    F --> G
    G -->|Yes| H
    G -->|No| I
    I --> J --> K --> L
```

### Pipeline 2 — Company Reviews & Updates Status

```mermaid
flowchart LR
    classDef trigger  fill:#ea4b71,stroke:#c73d60,color:#fff
    classDef process  fill:#1e293b,stroke:#475569,color:#e2e8f0
    classDef validate fill:#7c3aed,stroke:#6d28d9,color:#fff
    classDef storage  fill:#065f46,stroke:#059669,color:#fff
    classDef notify   fill:#92400e,stroke:#d97706,color:#fff
    classDef done     fill:#14532d,stroke:#16a34a,color:#fff

    A([🖱️ Webhook Trigger\nPUT /applications/id/status]):::trigger
    B[🔐 JWT Auth Node\nVerify company token\nExtract company_id]:::process
    C[🔍 DB Query Node\nFetch application\nwith internship info]:::process
    D{🏢 Company Owns\nThis Listing?}:::validate
    E[🚫 403 Forbidden\nNot your applicant]:::notify
    F[✏️ Set Node\nValidate status value\npending/accepted/rejected]:::process
    G{📋 Valid\nStatus?}:::validate
    H[🚫 400 Bad Request\nInvalid status value]:::notify
    I[🗄️ Database Node\nUPDATE application\nSET status = new_value]:::storage
    J([✅ Return Updated\nApplication object]):::done

    A --> B --> C --> D
    D -->|No| E
    D -->|Yes| F
    F --> G
    G -->|Invalid| H
    G -->|Valid| I --> J
```

### Pipeline 3 — Full Platform End to End

```mermaid
flowchart TD
    classDef student  fill:#1d4ed8,stroke:#1e40af,color:#fff
    classDef company  fill:#7c3aed,stroke:#6d28d9,color:#fff
    classDef api      fill:#1e293b,stroke:#475569,color:#e2e8f0
    classDef db       fill:#065f46,stroke:#059669,color:#fff
    classDef muse     fill:#92400e,stroke:#d97706,color:#fff
    classDef profile  fill:#0e7490,stroke:#0891b2,color:#fff

    S([👤 Student\nRegisters]):::student
    C([🏢 Company\nRegisters]):::company

    S --> SA[POST /auth/register\nrole = student]:::api
    C --> CA[POST /auth/register\nrole = company]:::api

    SA --> DB1[(Users Table\npassword hashed)]:::db
    CA --> DB1
    CA --> DB2[(Companies Table\nauto-created)]:::db

    DB1 --> LOGIN[POST /auth/login\nReturns JWT token]:::api
    LOGIN --> SF & CF & PF & MF

    subgraph SF [🎓 Student Journey]
        direction TB
        BR[GET /internships/\nBrowse + filter]:::api
        AP[POST /applications/apply\nUpload PDF CV]:::api
        TR[GET /applications/student\nTrack status live]:::api
        BR --> AP --> TR
    end

    subgraph CF [🏢 Company Journey]
        direction TB
        POST[POST /internships/\nCreate listing]:::api
        VIEW[GET /applications/company\nView applicants]:::api
        UPD[PUT /applications/id/status\nAccept or Reject]:::api
        POST --> VIEW --> UPD
    end

    subgraph PF [👤 Profile System]
        direction TB
        P1[PUT /profiles/me\nHeadline + bio + links]:::profile
        P2[POST /profiles/me/photo\nUpload profile photo]:::profile
        P3[POST /profiles/me/experience\nAdd work history]:::profile
        P4[GET /profiles/user_id\nPublic profile view]:::profile
        P1 --> P2 --> P3 --> P4
    end

    subgraph MF [🌍 Global Jobs]
        direction TB
        M1[Frontend calls\nThe Muse API directly]:::muse
        M2[Jobs from Google\nNetflix · Spotify]:::muse
        M3[Paginate + filter\ncategory + keyword]:::muse
        M1 --> M2 --> M3
    end

    SF --> DB3[(Applications Table\nCV stored in /uploads)]:::db
    CF --> DB3
    PF --> DB4[(Profiles + Education\n+ Experience Tables)]:::db
```

### n8n Node Reference

```
┌──────────────────────────────────────────────────────────────────────┐
│                      WORKFLOW NODES USED                             │
├──────────────────────┬───────────────────────────────────────────────┤
│  Webhook Trigger     │  Receives incoming HTTP requests from the app │
│  JWT Auth Node       │  Decodes and verifies Bearer token            │
│  HTTP Request Node   │  Calls FastAPI endpoints internally           │
│  IF / Switch Node    │  Validates conditions — open, duplicate, role │
│  Database Node       │  Direct SQLite / PostgreSQL queries           │
│  File Validator      │  Checks file extension before saving to disk  │
│  Save File Node      │  Writes CV / photo to the uploads/ directory  │
│  Set Node            │  Transforms and validates data between steps  │
│  Error Response      │  Returns 4xx with detail message on failure   │
│  Success Response    │  Returns 2xx with result data on success      │
└──────────────────────┴───────────────────────────────────────────────┘
```

### How to Import Into n8n

```bash
# 1. Install n8n
npm install -g n8n

# 2. Start
n8n start

# 3. Open browser
http://localhost:5678

# 4. Import workflow
Settings → Import Workflow → select internhub_workflow.json

# 5. Set credentials
HTTP Nodes    → Base URL: http://localhost:8000
Database Node → Path: ./internship_portal.db
```

> 💡 Workflow JSON is available in the `/n8n/` folder of this repository.

---

## 📊 **Database Design**

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

---

## 🔐 **Security**

```
Passwords       bcrypt hashed via passlib — plain text never stored
Tokens          JWT with 24-hour expiry — stored in localStorage
Role Guards     require_role("student") / require_role("company")
                applied as FastAPI dependency on every protected route
CV Uploads      .pdf only — validated server-side before saving
Photo Uploads   .jpg .jpeg .png .webp — all others rejected
CORS            Allow-all in dev — restrict allow_origins in production
Double Apply    DB-level check — one student per internship per listing
```

---

## 🧪 **Testing Strategy**

- ✅ Authentication flow (Register + Login + JWT decode)
- ✅ Role guards (student endpoints reject company tokens and vice versa)
- ✅ Internship CRUD (create, read, update, delete, close)
- ✅ Application flow (apply, duplicate check, status update)
- ✅ File upload validation (PDF for CV, image types for photos)
- ✅ Profile CRUD (create, update, add/remove experience and education)
- ✅ The Muse API integration (search, pagination, error handling)
- ✅ Manual testing via Swagger UI at `/docs`

---

## 🚀 **Getting Started**

```bash
# 1. Install dependencies
pip install -r Requirement.txt

# Python 3.12 fix — run this if registration crashes
pip install bcrypt==4.0.1

# 2. Start the server
python Main.py

# 3. Open in browser
http://localhost:8000          → Frontend
http://localhost:8000/profile  → Profile page
http://localhost:8000/docs     → Swagger API docs
```

### Switch to PostgreSQL

```python
# database.py — swap the URL
DATABASE_URL = "sqlite:///./internship_portal.db"   # default
DATABASE_URL = "postgresql://user:password@localhost/internhub"  # production
```

```bash
pip install psycopg2-binary
```

---

## 📈 **Expected Results**

* ✅ Students find internships filtered to their needs — no noise from full-time listings
* ✅ Companies reach intern-specific talent with clean applicant management
* ✅ CVs and profiles stored safely — accessible from any device
* ✅ Global job discovery via The Muse — no API key, no cost
* ✅ Public profiles shareable as URLs — like LinkedIn but for students
* ✅ Single command to run — zero deployment complexity

---

## 🔮 **Future Enhancements**

✨ *Planned Features...*

* 📧 **Email notifications** when application status changes
* 🤖 **AI recommendations** — suggest internships based on profile skills
* 🛡️ **Admin dashboard** — verify companies, remove fake listings
* 🐳 **Docker deployment** — one-command containerized setup
* ⚙️ **CI/CD via GitHub Actions** — automated testing and deployment
* 🔔 **Real-time notifications** via WebSockets
* 🏅 **Company verification badges** — trusted employer system

---

## 🧾 **What You Learn Building This**

```
Backend
  ├── REST API design with FastAPI — routes, methods, query params
  ├── JWT authentication — token creation, decoding, expiry
  ├── Role-based access control — guards on every protected endpoint
  ├── SQLAlchemy ORM — models, foreign keys, relationships, queries
  ├── Pydantic — request validation, response shaping, nested schemas
  └── File handling — multipart uploads, path storage, static serving

Frontend
  ├── Single-page application — no React, no Vue, plain JavaScript
  ├── fetch() API — GET, POST, PUT, DELETE with auth headers
  ├── localStorage — token, role, user_id across page reloads
  └── DOM manipulation — rendering cards, modals, dashboards

Real-World Skills
  ├── Debugging production errors — bcrypt, routing, redirect loops
  ├── Third-party API integration — The Muse REST API
  ├── Database design — normalized tables, relationships, constraints
  └── Layered architecture — routers, schemas, models, core separated
```

---

## 👥 **Development Team**

<br/>

<div align="center">

| | Name | Role | LinkedIn |
|---|---|---|---|
| 🔧 | **Ahmad** | Backend & API Design | [![LinkedIn](https://img.shields.io/badge/Connect-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ahmad0763) |

</div>

<br/>

---

## 🤝 **Contributing**

Contributions, feature ideas, and feedback are welcome!

```bash
# 1. Fork the repository
# 2. Create your feature branch
git checkout -b feature/your-feature-name

# 3. Commit your changes
git commit -m "Add: your feature description"

# 4. Push to your branch
git push origin feature/your-feature-name

# 5. Open a Pull Request
```

<div align="center">

<br/>

[![Star This Repo](https://img.shields.io/badge/⭐_Star_This_Repo-Click_Here-gold?style=for-the-badge&logo=github&logoColor=white)](https://github.com)
[![Watch Updates](https://img.shields.io/badge/👀_Watch_Updates-Coming_Soon-3b82f6?style=for-the-badge&logo=github&logoColor=white)](https://github.com)

</div>

<br/>

---

## 📧 **Contact**

<div align="center">

[![LinkedIn](https://img.shields.io/badge/Ahmad_—_LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ahmad0763)
[![GitHub](https://img.shields.io/badge/GitHub_—_Follow-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com)
[![Email](https://img.shields.io/badge/Email_—_Coming_Soon-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:)

</div>

<br/>

---

## 📜 **License**

This project is licensed under the **MIT License** — open for learning, innovation, and collaboration.

```
MIT License — free to use, modify, and distribute with attribution.
See LICENSE.md for full terms.
```

<p align="center">
  <a href="#"><img src="https://img.shields.io/badge/View_License-MIT-black?style=for-the-badge&logo=open-source-initiative" /></a>
</p>

---

## 🌟 **Acknowledgements**

Special thanks to:
- **FastAPI** team for the incredible Python web framework
- **The Muse** for providing a free, open job listings API
- **SQLAlchemy** for the powerful Python ORM
- **Tailwind CSS** for utility-first styling without a build step
- The open-source community for tools, inspiration, and feedback

---

<p align="center">
  <b>🚀 Bringing student-focused internship discovery to life!</b><br>
  <sub>Combining the power of FastAPI, JWT auth, and The Muse API in one platform</sub>
</p>

<p align="center">
  Made with ❤️ by Ahmad
</p>

---

<p align="center">
  <img src="https://img.shields.io/badge/Built_With-Python-3776AB?style=flat&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Powered_By-FastAPI-009688?style=flat&logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/Made_For-Students-gold?style=flat&logo=graduation-cap&logoColor=white" />
</p>
