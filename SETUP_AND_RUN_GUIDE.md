# SETUP_AND_RUN_GUIDE

## Application Overview

SocioNeed is a multi-role society management platform with:
- Resident portal: complaints, notices, events, amenities/service bookings, profile
- Admin portal: residents/providers/users management, complaints assignment, notices/events, analytics, reports export
- Service provider portal: bookings lifecycle, profile/services, availability, reviews, earnings
- Security portal: visitor, vehicle, patrol, alerts, incidents

Key modules:
- Frontend SPA (Vue 3 + Vite + Pinia + Vue Router)
- Backend API (Flask + SQLAlchemy + JWT + CORS)
- SQLite persistence and seed bootstrap data

High-level architecture:
- Frontend calls REST APIs at VITE_API_BASE_URL (default: http://127.0.0.1:5000/api)
- Backend enforces role-based authorization and returns standardized success/error envelopes
- Backend auto-creates schema on startup and seeds baseline users/categories/data

## Prerequisites

Required software:
- Node.js 18+
- npm 9+
- Python 3.11+ (project is currently running on Python 3.14 locally)
- Git

Optional but recommended:
- Windows PowerShell 5.1+ or PowerShell 7+
- VS Code

Access requirements:
- Local file system access to repository
- Port access for:
  - Frontend: 5173 (or next free port, often 5174)
  - Backend: 5000

## Project Structure

Top-level:
- backend: Flask API, models, services, migrations, tests
- frontend: Vue app (active frontend source)
- docs: supporting project docs
- src, public, dist (legacy/previous frontend layout artifacts may exist)

Frontend folders:
- frontend/src/components/screens
- frontend/src/layouts
- frontend/src/router
- frontend/src/stores
- frontend/src/views
- frontend/public

Backend folders:
- backend/app/api
- backend/app/models
- backend/app/services
- backend/app/core
- backend/migrations
- backend/tests
- backend/instance

Configuration files:
- frontend/package.json
- frontend/vite.config.js
- backend/requirements.txt
- backend/.env.example
- backend/app/core/config.py

Important directories:
- backend/instance (SQLite DB location)
- backend/tests (test suite)
- backend/config/schema.sql (schema reference)

## Environment Configuration

### Backend Environment Variables

Create backend/.env from backend/.env.example.

Required variables:
- FLASK_ENV=development
- SECRET_KEY=<long-random-secret>
- JWT_SECRET_KEY=<long-random-jwt-secret>
- DATABASE_URL=sqlite:///../instance/socioneed.db
- CORS_ORIGINS=http://localhost:5173,http://127.0.0.1:5173,http://localhost:5174,http://127.0.0.1:5174

Notes:
- JWT_SECRET_KEY should be at least 32 characters.
- DATABASE_URL default points to backend/instance/socioneed.db.

Example backend/.env:

```env
FLASK_ENV=development
SECRET_KEY=replace-with-strong-secret-min-32-chars
JWT_SECRET_KEY=replace-with-strong-jwt-secret-min-32-chars
DATABASE_URL=sqlite:///../instance/socioneed.db
CORS_ORIGINS=http://localhost:5173,http://127.0.0.1:5173,http://localhost:5174,http://127.0.0.1:5174
```

### Frontend Environment Variables

Frontend reads:
- VITE_API_BASE_URL (optional)

If omitted, default is:
- http://127.0.0.1:5000/api

Example frontend/.env (optional):

```env
VITE_API_BASE_URL=http://127.0.0.1:5000/api
```

Secrets setup:
- Do not commit real secrets.
- Keep .env files local.

## Installation

### 1. Clone Repository

```bash
git clone <repository-url>
cd SE_CSP_PROJECT
```

### 2. Install Frontend Dependencies

```bash
cd frontend
npm install
```

### 3. Install Backend Dependencies

```bash
cd ../backend
python -m pip install -r requirements.txt
```

### 4. Database Setup

Default setup:
- Backend auto-creates tables on startup and seeds baseline data.

Optional migration-based setup:

```bash
cd backend
flask db upgrade
```

If flask command is unavailable, ensure Flask CLI is installed and FLASK_APP is set.

## Running the Application

### Frontend

Commands:

```bash
cd frontend
npm run dev
```

Default port:
- 5173

Note:
- If 5173 is busy, Vite may auto-switch to 5174.

Development mode:
- Hot module reload enabled.

### Backend

Commands:

```bash
cd backend
python run.py
```

Default port:
- 5000

API startup process:
- Loads configuration
- Initializes extensions (DB, JWT, CORS)
- Registers blueprints
- Creates DB tables
- Runs seed service for baseline data

### Database

Database type:
- SQLite

Startup behavior:
- DB file in backend/instance
- Tables created automatically if missing

Migrations:

```bash
cd backend
flask db migrate -m "describe change"
flask db upgrade
```

Seed data:
- Seed runs at startup through backend services.

## Running the Complete Application

Step-by-step:
1. Start backend first.
2. Verify backend health endpoint.
3. Start frontend.
4. Open frontend URL from Vite output.
5. Login using seeded credentials.

Verification steps:
- Backend health:
  - GET http://127.0.0.1:5000/health
- Frontend login screen loads
- Role dashboards load and API data is visible

Health check endpoints:
- http://127.0.0.1:5000/health
- API base: http://127.0.0.1:5000/api

## Testing

### Unit/Integration Tests (Backend)

```bash
cd backend
python -m pytest -q
```

Current validated status in this branch:
- 109 passed

### Frontend Build Check

```bash
cd frontend
npm run build
```

### E2E Tests

- No dedicated automated E2E command is currently configured in frontend scripts.
- Use manual role-based browser verification for now.

## Build Process

Production frontend build:

```bash
cd frontend
npm run build
```

Output:
- frontend/dist

Backend deployment preparation:
- Install backend requirements
- Configure production secrets and DB URL
- Run migrations where applicable
- Serve Flask app with production WSGI server

## Troubleshooting

Common startup issues:
- Port already in use (5173 or 5000)
  - Stop existing process or run on alternate port.
- Frontend starts on 5174 instead of 5173
  - Update CORS_ORIGINS and use shown Vite URL.

Environment issues:
- Missing env values
  - Create backend/.env from backend/.env.example.
- Weak JWT secret warnings
  - Use longer JWT_SECRET_KEY and restart backend.

Dependency issues:
- npm install errors
  - Delete frontend/node_modules and retry npm install.
- pip dependency mismatch
  - Reinstall from backend/requirements.txt.

Database connection issues:
- SQLite file path problems
  - Verify DATABASE_URL and backend/instance folder existence.
- Seed/constraint conflicts
  - Restart backend; current seed flow handles duplicate profiles safely.

API connection issues:
- Browser CORS failures
  - Ensure backend CORS_ORIGINS includes both localhost and 127.0.0.1 with active frontend port.
- Network error "Unable to reach backend service"
  - Confirm backend is running at http://127.0.0.1:5000.

## Developer Notes

Important architectural decisions:
- App factory pattern on backend
- Role-based API guards
- Standard response envelope and centralized error handling
- Query pagination helper used across list endpoints
- Frontend Pinia auth store as API abstraction layer

Key integrations:
- Header/global search uses route query parameter q and screen-level filtering
- API-powered search uses search query params in users/complaints/events/providers endpoints
- Admin and provider badges pull live metadata instead of hardcoded counters

Known requirements:
- Frontend source of truth is frontend directory
- Backend tests are comprehensive and should be run after backend changes
- Some security portal operations are currently mock-style UI actions and not fully API-backed yet
