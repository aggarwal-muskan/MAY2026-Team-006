# SocioNeed Backend (Flask)

Production-style Flask backend for SocioNeed with role-based auth, SQLite persistence, modular API blueprints, and frontend-aligned route coverage.

## Tech Stack
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-JWT-Extended
- Flask-CORS
- Werkzeug password hashing
- SQLite

## Architecture

```
backend/
  app/
    __init__.py
    api/
      __init__.py
      auth.py
      users.py
      societies.py
      units.py
      notices.py
      events.py
      complaints.py
      providers.py
      bookings.py
      visitors.py
      analytics.py
    core/
      config.py
      extensions.py
      responses.py
      security.py
    models/
      base.py
      entities.py
    services/
      auth_service.py
      query_service.py
      seed_service.py
  config/
    schema.sql
  instance/
  requirements.txt
  run.py
  .env.example
```

## Features Implemented

- JWT auth: register, login, logout, token verify, token refresh
- Role-based authorization via route decorators
- Users and profile management
- Societies CRUD
- Units + occupancies CRUD
- Notices CRUD + publish
- Events CRUD + attendee registration/unregistration + attendee listing
- Complaints full lifecycle with updates timeline and assignment
- Service categories/providers/slots/bookings/reviews flows
- Visitor entry/exit tracking
- Dashboard/analytics/report endpoints
- Auto-seed default users and service categories

## Roles
- admin
- owner
- tenant
- service_provider
- security

## Quick Start

1. Create a virtual environment and install dependencies:

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

2. Copy environment file:

```powershell
Copy-Item .env.example .env
```

3. Run backend:

```powershell
python run.py
```

Backend starts on http://localhost:5000

Health check:
- GET http://localhost:5000/health

## Default Seed Credentials

All default users use password: `123456`

- admin@socioneed.com (admin)
- resident@socioneed.com (owner)
- provider@socioneed.com (service_provider)
- provider.housemaid@socioneed.com (service_provider)
- provider.plumber@socioneed.com (service_provider)
- provider.electrician@socioneed.com (service_provider)
- provider.laundry@socioneed.com (service_provider)
- provider.carwash@socioneed.com (service_provider)
- provider.gardener@socioneed.com (service_provider)
- provider.tailor@socioneed.com (service_provider)
- provider.cook@socioneed.com (service_provider)
- security@socioneed.com (security)

## API Base URL
- http://localhost:5000/api

## Core Endpoint Groups

- `/api/auth`
- `/api/users`
- `/api/societies`
- `/api/units`, `/api/occupancies`
- `/api/notices`
- `/api/events`
- `/api/complaints`
- `/api/service-categories`
- `/api/providers`, `/api/slots`, `/api/bookings`, `/api/reviews`
- `/api/visitors`
- `/api/analytics`, `/api/reports`

## Database Notes

- SQLAlchemy models are source of runtime schema.
- `backend/config/schema.sql` is updated to include `event_registrations` for event attendee flows.
- App auto-runs `db.create_all()` on startup for quick local setup.

## Engineering Principles Applied

- App factory pattern
- Separation of concerns (api/core/models/services)
- Central response formatting helpers
- Centralized extension bootstrap
- Reusable pagination helper
- JWT + role guards at route level
- Explicit validation and consistent failure codes
- Minimal side effects and clear state transitions

## Next Recommended Hardening

- Add Alembic migration scripts for production-grade schema versioning
- Add request schema validation layer (Marshmallow/Pydantic)
- Add structured logging and correlation IDs
- Add unit/integration tests for all route modules
- Add rate limiting and token revocation store
- Extend revenue logic with booking amount columns and financial models
