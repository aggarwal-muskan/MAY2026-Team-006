# SocioNeed - Society Management System

SocioNeed is a full-stack society management application with role-based portals for Residents, Admins, Service Providers, and Security Staff.

---

# 📌 Project Overview

SocioNeed provides a centralized platform for managing society operations, including:

- 🏠 Resident Management
- 📢 Notices & Announcements
- 🛠 Complaint Management
- 🏢 Amenity Booking
- 👨‍🔧 Service Provider Management
- 👮 Security Portal
- 💳 Maintenance Billing
- 📊 Admin Dashboard

---

# Tech Stack

- Vue 3 (Composition API)
- Vite
- Vue Router
- Pinia
- Flask
- SQLAlchemy
- JWT
- SQLite
# Project Structure
---

SE_CSP_PROJECT/
├── backend/
│   ├── app/
│   ├── tests/
│   ├── requirements.txt
│   └── run.py
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── vite.config.js
├── docs/
├── src/            (legacy frontend artifacts)
├── public/         (legacy frontend artifacts)
└── README.md

- Dashboard
- My Complaints
- Notices
# Installation

Clone the repository:
- Family Members

---
cd SE_CSP_PROJECT

## 🛡 Admin Portal
Install frontend dependencies (from frontend folder):
- Dashboard
- User Management
cd frontend
npm install
- Notice Management
- Service Provider Management
Install backend dependencies (from backend folder):

---
cd ../backend
python -m pip install -r requirements.txt
## 👨‍🔧 Service Provider Portal

---

# Running Locally

Start backend:

```bash
cd backend
python run.py
```

Start frontend:

```bash
cd frontend
npm run dev
```

Important:
- Do not run npm commands from SE_CSP_PROJECT root.
- `package.json` is located in `frontend/package.json`.
- Running `npm install` or `npm run dev` from project root causes ENOENT package.json errors.

Health checks:

- Assigned Services
# backend
http://127.0.0.1:5000/health

# frontend
http://127.0.0.1:5173/
- Work History
- Profile

---
# Production Build
## 👮 Security Portal

cd frontend
- Dashboard
- Visitor Entry
- Visitor Exit
- Emergency Alerts

---

# 🔑 Demo Login Credentials

| Role             |       Email            | Password |
|------------------|------------------------|---------|
| Resident         | resident@socioneed.com | 123456 |
| Admin            | admin@socioneed.com    | 123456 |
| Service Provider | provider@socioneed.com | 123456 |
| Security         | security@socioneed.com | 123456 |

---

# 📁 Project Structure

```text
socioneed/
│
├── public/
│
├── src/
│   ├── assets/
│   ├── components/
│   ├── data/
│   ├── layouts/
│   ├── router/
│   ├── stores/
│   ├── views/
│   │   ├── auth/
│   │   ├── public/
│   │   ├── resident/
│   │   ├── admin/
│   │   ├── provider/
│   │   └── security/
│   │
│   ├── App.vue
│   ├── main.js
│   └── style.css
│
├── package.json
├── vite.config.js
└── README.md
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone <repository-url>
```

Move into the project folder

```bash
cd socioneed
```

Install dependencies

```bash
npm install
```

Start the development server

```bash
npm run dev
```

---

# 📦 Production Build

```bash
npm run build
```

---

# 🎨 Frontend Status

- ✅ Public Website Completed
- ✅ Authentication Completed
- ✅ Resident Portal Completed
- ✅ Admin Portal Completed
- ✅ Service Provider Portal Completed
- ✅ Security Portal Completed
- ✅ Responsive Layout
- ✅ Mock Authentication
- ✅ Role-based Navigation
- ✅ Ready for Backend Integration

---

For complete full-stack setup, troubleshooting, and environment configuration, see:
- SETUP_AND_RUN_GUIDE.md

---

# 🤝 Team Workflow

### Frontend

- UI/UX Design
- Vue Components
- Routing
- State Management
- Mock Authentication

### Backend

- REST APIs
- Database Schema
- Authentication
- Business Logic
- Data Validation

---

# 📋 Notes for Developers

- The project currently uses **mock data**.
- No backend integration has been implemented yet.
- Authentication is simulated using mock user credentials.
- The frontend architecture is prepared for seamless API integration.
- Please avoid modifying the frontend structure without discussion to maintain consistency.

---

# 📌 Future Enhancements

- JWT Authentication
- Real Database Integration
- Push Notifications
- Payment Gateway
- Real-time Chat
- Visitor QR Pass
- Mobile Application
- Analytics Dashboard

---

# 👨‍💻 Developed For

**Software Engineering Course Project**

**Project Name:** SocioNeed – Society Management System

---

## 📄 License

This project is developed for educational purposes as part of the Software Engineering course.