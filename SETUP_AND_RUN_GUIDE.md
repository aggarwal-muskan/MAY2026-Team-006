# SocioNeed Setup and Run Guide

## 1. Application Overview
SocioNeed is a full-stack community management platform used by four role-based portals.

Roles:
- Resident
- Admin
- Service Provider
- Security

Main modules:
- Authentication and role routing
- Complaints lifecycle and assignment
- Notices and events
- Service provider bookings and availability
- Security visitor operations
- Family members and maintenance bills
- Admin analytics, settings, logs, and reports

## 2. Technology Stack
- Frontend framework: Vue 3 (Composition API)
- Frontend router/state: Vue Router, Pinia
- Frontend build tool: Vite
- Backend framework: Flask
- ORM and persistence: SQLAlchemy + SQLite
- Auth: Flask-JWT-Extended (JWT)
- Package managers: npm, pip
- Testing tools: pytest

## 3. Project Structure
Important folders/files:
- backend/: Flask API application
- backend/app/api/: API routes
- backend/app/models/: SQLAlchemy models
- backend/app/services/: seed and supporting services
- backend/tests/: backend test suite
- backend/instance/: runtime SQLite database and uploads
- frontend/: active Vue frontend application
- frontend/src/components/screens/: role-specific portal screens
- frontend/src/stores/authStore.js: centralized API/auth integration layer
- docs/: project documentation
- src/: legacy frontend artifacts

## 4. Prerequisites
- Node.js 18+
- npm 9+
- Python 3.11+
- Git

## 5. Environment Setup
Backend env setup:
1. Copy backend/.env.example to backend/.env
2. Update values for your environment

Required backend variables:
- FLASK_ENV
- SECRET_KEY
- JWT_SECRET_KEY
- DATABASE_URL
- CORS_ORIGINS
- GEMINI_API_KEY (only required for AI endpoints)
- GEMINI_MODEL

Frontend env setup:
- Optional variable: VITE_API_BASE_URL
- If not set, frontend defaults to http://127.0.0.1:5000/api

## 6. Clone and Pull Latest Code
Use:

```bash
git checkout main
git pull origin main
```

If you are on a feature branch, merge/rebase main into your branch after pulling.

## 7. Backend Setup
From project root:

```bash
cd backend
python -m pip install -r requirements.txt
python run.py
```

Health check:

```bash
http://127.0.0.1:5000/health
```

## 8. Frontend Setup
From project root:

```bash
npm install
npm run frontend:install
npm run dev
```

Equivalent direct frontend commands:

```bash
cd frontend
npm install
npm run dev
```

## 9. Running the Full Application Locally
Startup order:
1. Database: SQLite is created/updated automatically by backend startup.
2. Backend: run backend server first.
3. Frontend: run Vite dev server.
4. Browser URL: http://127.0.0.1:5173
5. Demo users:
- resident@socioneed.com / 123456
- admin@socioneed.com / 123456
- provider@socioneed.com / 123456
- security@socioneed.com / 123456

## 10. Running Tests
Backend tests:

```bash
cd backend
python -m pytest -q
```

Frontend lint/type check:
- No dedicated lint or type-check scripts are currently defined in package.json.

Frontend build:

```bash
npm run build
```

## 11. Production Build
Frontend production build:

```bash
npm run build
```

Build artifacts are generated in frontend/dist.

## 12. Troubleshooting
- Dependency install issues:
  - Re-run npm install and pip install -r backend/requirements.txt
  - Remove node_modules and reinstall if needed
- Backend not starting:
  - Verify backend/.env exists and is valid
  - Check port 5000 availability
- Frontend not starting:
  - Verify frontend dependencies are installed
  - Check port 5173 availability
- API connection issue:
  - Verify backend health endpoint is reachable
  - Verify VITE_API_BASE_URL if set
- CORS issue:
  - Include both localhost and 127.0.0.1 frontend origins in CORS_ORIGINS
- Database connection issue:
  - Verify DATABASE_URL and backend/instance path permissions
- Missing environment variables:
  - Recreate backend/.env from backend/.env.example
- Login issue:
  - Confirm role and credentials are correct
  - Ensure seed data loaded successfully
- Port already in use:
  - Stop conflicting process or change run port
- File upload issue:
  - Ensure backend can write to backend/instance/uploads
  - Ensure file type is jpg/jpeg/png/webp and size <= 5MB

## 13. Developer Notes
- Role routing:
  - Defined in frontend/src/router/index.js via token/role guards.
- Complaint assignment lifecycle:
  - Resident creates complaint (open).
  - Admin assigns to provider (assigned).
  - Provider moves status to in_progress, rejected, or resolved.
  - Resident/Admin see live status and timeline.
- Provider bookings lifecycle:
  - Provider portal handles booking actions and assigned complaint work actions.
- Profile image upload notes:
  - Endpoint: POST /api/users/me/profile-image
  - UI supports preview + save.
  - Path stored in users.profile_image_url and served from /uploads/...
- Flat number handling:
  - Admin resident creation supports flat_number.
  - Backend stores flat_number and maps to occupancy/unit for display/search where applicable.
- Security portal integration notes:
  - Visitor entry/approval, patrol, emergency, incidents, and dashboard stats are backend-driven.
- Known external integrations requiring credentials:
  - Gemini AI endpoints require GEMINI_API_KEY.
  - Payment gateway/email/SMS/external object storage are not configured by default in this repo.
- API-powered search uses search query params in users/complaints/events/providers endpoints
- Admin and provider badges pull live metadata instead of hardcoded counters

Known requirements:
- Frontend source of truth is frontend directory
- Backend tests are comprehensive and should be run after backend changes
- Some security portal operations are currently mock-style UI actions and not fully API-backed yet
