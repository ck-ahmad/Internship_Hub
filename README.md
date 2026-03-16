# Internships Portal

## Setup

1. Install dependencies:
```
pip install -r Requirement.txt
```

2. Run the server:
```
uvicorn Main:app --reload
```

3. Open browser:
```
http://localhost:8000          → Frontend
http://localhost:8000/docs     → Swagger API Docs
```

## Folder Structure

```
InternshipsPortal/
├── frontend/
│   └── index.html
├── models/
│   ├── __init__.py
│   └── models.py
├── routers/
│   ├── __init__.py
│   ├── auth.py
│   ├── internships.py
│   └── applications.py
├── schemas/
│   ├── __init__.py
│   └── schemas.py
├── core/
│   ├── __init__.py
│   └── security.py
├── uploads/
├── database.py
├── Main.py
└── Requirement.txt
```
