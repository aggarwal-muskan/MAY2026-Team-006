# SocioNeed - Society Management System

SocioNeed is a full-stack residential society management platform. It gives residents, administrators, service providers, and security staff role-appropriate tools for handling community operations in one application.

## Project Overview

Society operations often depend on disconnected messages, spreadsheets, and manual follow-up. SocioNeed centralizes resident services, complaints, bookings, notices, events, visitor operations, billing-related data, and administrative reporting behind authenticated role-based portals.

The repository contains the active Vue frontend and Flask backend, with SQLite persistence for local development.

## Main Features

### Resident Portal

- Resident dashboard with society activity summaries
- Notices and community events, including event registration
- Complaint creation, tracking, details, status history, and updates
- Service discovery and provider details
- Service booking calendar, booking history, and amenity booking
- Family member management
- Maintenance bill viewing and payment actions
- Profile and profile-image management
- Notifications and help/support views
- SocioNeed AI Assistant access after login

### Admin Portal

- Dashboard statistics and analytics
- Resident, tenant, and user management
- Provider verification and service-provider management
- Complaint review, assignment, emerging-issue analysis, and status management
- Notice and event creation, editing, publishing, and deletion
- Settings, roles and permissions, reports, monthly CSV export, and system logs
- Administrative AI tools for notice generation, translations, event planning, analytics insights, complaint analysis, meeting minutes, notice summaries, maintenance guidance, feedback analysis, and amenity-booking suggestions

### Service Provider Portal

- Provider dashboard and profile management
- Assigned bookings and service work history
- Availability slot management
- Provider services, reviews, earnings, notifications, settings, and help views
- Booking acceptance, decline, and completion actions where permitted

### Security Portal

- Security dashboard and activity statistics
- Visitor entry, approval, rejection, and exit tracking
- Vehicle logs
- Patrol logs
- Emergency alerts
- Incident reports

### Shared Society Operations

- Notices and announcements
- Events and attendee registration
- Complaints with assignment and lifecycle status transitions
- Service categories, providers, availability slots, bookings, and reviews
- Units, occupancies, societies, tenants, family members, and maintenance bills
- Search and pagination support on applicable API resources

## User Roles

The frontend presents four portal roles. The backend uses the following role values:

| Portal label | Backend role | Main responsibility |
|---|---|---|
| Resident | `owner` | Use society services, view notices/events, submit complaints, and manage bookings and profile data |
| Admin | `admin` | Manage users, providers, complaints, notices, events, settings, analytics, reports, and logs |
| Service Provider | `service_provider` | Manage services, availability, assigned bookings, work history, and provider profile data |
| Security | `security` | Manage visitor, vehicle, patrol, emergency, and incident operations |

The backend also supports the `tenant` role for authenticated data and authorization flows. There is no separate tenant frontend portal; tenants use the resident-oriented application flows where applicable.

## AI Features / SocioNeed AI Assistant

### General AI Assistant

Authenticated users see a small floating **AI Assistant** button in the application. Selecting it opens the compact **SocioNeed AI Assistant** panel, where users can type natural-language questions and submit them with the Send button or Enter key.

The assistant is mounted at the application root and is available whenever a valid frontend session token is present. It is therefore available across the logged-in role portals, including Resident, Admin, Service Provider, and Security sessions.

The chatbot:

- Sends the question from the frontend to the backend API
- Uses the backend Gemini service to generate a response
- Focuses on society and residential management, bookings, complaints, notices, services, and general SocioNeed guidance
- Is instructed not to invent application-specific policies, fees, dates, user data, or other unavailable facts
- Should clearly indicate when it does not know something or when the user should check current society data in the application
- Shows user and assistant messages separately and displays a loading state while waiting

The Gemini API key is loaded by the backend from server-side configuration. It is never placed in frontend source code or sent to the browser.

### Other Implemented AI Tools

The backend also contains authenticated AI tools for administrative and resident workflows, including notice generation, announcement translation, event planning, analytics and complaint insights, complaint classification, meeting minutes, notice summarization, maintenance assistance, rules/document Q&A, feedback analysis, and amenity-booking suggestions. Role restrictions are enforced per endpoint; the general `/chat` endpoint requires authentication but does not require a specific role.

### Example Questions

| Example question | Purpose |
|---|---|
| What is SocioNeed? | General application guidance |
| What can I do with SocioNeed? | Overview of available society workflows |
| How can I check my bookings? | Booking-related guidance |
| How can I see the visitor entries? | Visitor and security guidance |

These are example questions for demonstration, not hard-coded commands.

## AI Architecture / Flow

```text
User
	|
	v
SocioNeed Frontend Chatbot
	|
	| Bearer token
	v
Authenticated Flask API: POST /api/ai/chat
	|
	v
Backend Gemini service/API
	|
	v
AI response
	|
	v
Chatbot UI
```

The Gemini API key must remain server-side. Never place it in frontend source code, frontend environment variables exposed to Vite, browser storage, or committed repository files.

## Technology Stack

### Frontend

- Vue 3 with Composition API
- Vue Router
- Pinia
- Chart.js and Vue-Chartjs for dashboard charts
- Vite

### Backend

- Python
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-CORS
- Werkzeug password hashing
- Modular Flask API blueprints

### Database

- SQLite for local persistence
- SQLAlchemy models and `db.create_all()` startup support
- Alembic/Flask-Migrate files for migration workflows

### Authentication

- Flask-JWT-Extended access tokens
- Role-based route decorators
- Frontend token/session persistence through the Pinia auth store

### AI

- Google Gemini through the `google-genai` Python package
- Backend-only Gemini client and response handling
- Configurable model, response cache TTL, and maximum output tokens

### Testing and Development Tools

- pytest for backend tests
- npm for frontend dependencies and scripts
- pip for backend dependencies
- Vite development server and production build

## Project Structure

```text
MAY2026-Team-006/
├── backend/
│   ├── app/
│   │   ├── api/                 # Flask route blueprints, including AI
│   │   ├── core/                # configuration, security, responses, extensions
│   │   ├── models/              # SQLAlchemy entities and base model
│   │   └── services/            # auth, queries, seed data, Gemini, AI prompts
│   ├── config/schema.sql
│   ├── instance/                # local SQLite database and uploads
│   ├── migrations/              # Flask-Migrate/Alembic files
│   ├── tests/                   # backend API and feature tests
│   ├── requirements.txt
│   ├── run.py
│   └── .env.example
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── assets/css/          # shared design tokens and styles
│   │   ├── components/          # portal screens and SocioNeedChatbot.vue
│   │   ├── data/                # frontend data used by the UI
│   │   ├── layouts/             # public, portal, and admin layouts
│   │   ├── router/              # routes and role guards
│   │   ├── stores/              # Pinia auth and notification stores
│   │   ├── views/               # public and authentication pages
│   │   ├── App.vue
│   │   └── main.js
│   ├── package.json
│   └── vite.config.js
├── docs/                        # database and API documentation
├── package.json                 # root convenience scripts
├── SETUP_AND_RUN_GUIDE.md
└── README.md
```

## Installation and Setup

### Prerequisites

- Git
- Node.js and npm
- Python 3.11 or newer

### Clone the repository

```bash
git clone <repository-url>
cd MAY2026-Team-006
```

### Backend setup

Create and activate a virtual environment in `backend` if one is not already available, then install the requirements:

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

On macOS/Linux, activate with:

```bash
source .venv/bin/activate
```

Copy the environment template and fill in local values. Never commit the resulting `.env` file:

```powershell
Copy-Item .env.example .env
```

At minimum, configure a valid `GEMINI_API_KEY` to use the AI endpoints. The backend creates or updates the local SQLite database during startup.

### Frontend setup

From the repository root, install the frontend dependencies:

```bash
npm run frontend:install
```

The equivalent direct command is:

```bash
cd frontend
npm install
```

## Environment Variables

Backend variables belong in `backend/.env` or the server's environment. Use safe local/deployment values; do not copy secrets into this README or commit them to Git.

```dotenv
FLASK_ENV=development
SECRET_KEY=your_flask_secret_here
JWT_SECRET_KEY=your_jwt_secret_here
DATABASE_URL=sqlite:///../instance/socioneed.db
CORS_ORIGINS=http://localhost:5173,http://127.0.0.1:5173
GEMINI_API_KEY=your_gemini_api_key_here
GEMINI_MODEL=your_gemini_model_name
AI_CACHE_TTL=300
AI_MAX_OUTPUT_TOKENS=2048
```

The frontend supports the optional variable below. If it is not set, the auth store defaults to `http://127.0.0.1:5000/api`:

```dotenv
VITE_API_BASE_URL=http://127.0.0.1:5000/api
```

Keep all secrets local or use deployment/server secret management. Do not expose `GEMINI_API_KEY` through a `VITE_*` variable or frontend source code.

## Running the Application

Run the backend from one terminal:

```bash
cd backend
python run.py
```

The backend runs on `http://127.0.0.1:5000` and provides a health check at:

```text
http://127.0.0.1:5000/health
```

Run the frontend from a second terminal at the repository root:

```bash
npm run dev
```

Vite normally serves the application at:

```text
http://localhost:5173/
```

If the port is already in use, Vite may select another local port. Start the backend before using data-backed portal pages or AI features.

The backend seeds local development data and default role accounts. Use the credentials supplied through your team's secure local development process; do not publish passwords in documentation.

## API Documentation

The backend API is rooted at `/api`. Main endpoint groups include:

```text
/api/auth
/api/users
/api/societies
/api/units
/api/occupancies
/api/tenants
/api/family-members
/api/maintenance-bills
/api/notices
/api/events
/api/complaints
/api/service-categories
/api/providers
/api/slots
/api/bookings
/api/reviews
/api/visitors
/api/patrol-logs
/api/emergency-alerts
/api/incident-reports
/api/analytics
/api/reports
/api/ai
```

### SocioNeed AI Assistant endpoint

#### `POST /api/ai/chat`

- Requires a valid JWT bearer token.
- Accepts a non-empty `message` string.
- Sends the message to the backend Gemini service with SocioNeed-focused guidance.

Request body:

```json
{
	"message": "What is SocioNeed?"
}
```

Successful response:

```json
{
	"success": true,
	"message": "Chat response generated",
	"data": {
		"reply": "AI-generated response"
	}
}
```

The endpoint returns a validation error for a missing or empty message, a configuration error when `GEMINI_API_KEY` is unavailable, and an AI error when the Gemini request fails. The Gemini key is never returned to the client.

## Authentication and Security

- Login and registration are handled by the Flask auth API.
- Successful login returns a JWT access token with role and society claims.
- Flask-JWT-Extended protects authenticated routes.
- `roles_required` enforces backend role permissions for restricted operations.
- The frontend stores the active session token through the Pinia auth store and sends it as a Bearer token for API requests.
- The chatbot is authenticated with `@jwt_required()` and is available to logged-in users; it does not create bookings or modify society records.
- Passwords are hashed by the backend with Werkzeug utilities.
- Gemini credentials and other secrets must remain server-side and must not be committed.
- CORS is configured for approved local frontend origins through `CORS_ORIGINS`.

## Testing

Backend tests are located in `backend/tests/` and use pytest. The AI coverage includes:

- AI status and feature listing
- Chatbot success response with mocked Gemini output
- Missing chatbot message validation
- Unauthenticated chatbot access rejection
- Additional AI endpoint success, validation, authorization, provider-error, and configuration-error cases

Run the backend tests from the repository root with:

```bash
npm run backend:test
```

Or directly from `backend`:

```bash
python -m pytest -q
```

The frontend package does not define a dedicated lint or type-check script. Build the frontend with:

```bash
npm run build
```

## Production Build

Create the frontend production build with:

```bash
npm run build
```

The generated frontend artifacts are written to `frontend/dist`.

## Root Convenience Scripts

| Command | Purpose |
|---|---|
| `npm run dev` | Start the frontend Vite development server |
| `npm run build` | Build the frontend for production |
| `npm run frontend:install` | Install frontend dependencies |
| `npm run backend:dev` | Start the Flask backend from the root |
| `npm run backend:test` | Run the backend pytest suite |

For troubleshooting and additional environment notes, see [SETUP_AND_RUN_GUIDE.md](SETUP_AND_RUN_GUIDE.md).

## Development and Contribution

Keep frontend work under `frontend/` and backend work under `backend/`. Before opening a change:

1. Keep API and role behavior consistent with the existing route guards and backend authorization decorators.
2. Do not commit `.env`, API keys, passwords, JWT secrets, database credentials, or other local secrets.
3. Run the relevant backend tests and the frontend production build.
4. Update documentation when a user-facing feature or endpoint changes.
5. Avoid changing unrelated portal functionality while working on a focused feature.

## License

This project is developed for educational purposes as part of a Software Engineering course.