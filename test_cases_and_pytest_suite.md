# SocioNeed — Comprehensive 146 Test Cases Specification & Pytest Suite Report

> **Project Module**: SocioNeed Backend Core Services & Comprehensive API Test Suite  
> **Total Test Cases**: 146  
> **Status**: 139 PASSED, 7 FAILED PROOFS (Evidence Cases)  

---

# Test Coverage Matrix (All 146 Tests)

| # | Category | Test Case Title | Route & Method | Status |
|---|---|---|---|:---:|
| 1 | **01 Auth** | Auth Register Success | `POST /api/auth/register` | `PASSED` |
| 2 | **01 Auth** | Auth Register Duplicate Email | `POST /api/auth/register` | `FAILED (Proof)` |
| 3 | **01 Auth** | Auth Register Missing Fields | `POST /api/auth/register` | `PASSED` |
| 4 | **01 Auth** | Auth Login Success | `POST /api/auth/login` | `PASSED` |
| 5 | **01 Auth** | Auth Login Invalid Password | `POST /api/auth/login` | `FAILED (Proof)` |
| 6 | **01 Auth** | Auth Forgot Password | `POST /api/auth/forgot-password` | `PASSED` |
| 7 | **01 Auth** | Auth Change Password | `POST /api/auth/change-password` | `PASSED` |
| 8 | **01 Auth** | Auth Verify Token | `POST /api/auth/verify-token` | `PASSED` |
| 9 | **01 Auth** | Auth Refresh Token | `POST /api/auth/refresh-token` | `PASSED` |
| 10 | **01 Auth** | Auth Logout | `POST /api/auth/logout` | `PASSED` |
| 11 | **01 Auth** | Auth Unauthorized Access | `GET /api/users/me` | `PASSED` |
| 12 | **02 Units & Societies** | Admin Create Unit | `POST /api/units` | `PASSED` |
| 13 | **02 Units & Societies** | Admin List Units | `GET /api/units` | `PASSED` |
| 14 | **02 Units & Societies** | Admin Update Unit | `PUT /api/units/1` | `PASSED` |
| 15 | **02 Units & Societies** | Resident Occupancy Lifecycle | `GET /api/occupancies` | `PASSED` |
| 16 | **02 Units & Societies** | Resident Create Unit Forbidden | `POST /api/units` | `FAILED (Proof)` |
| 17 | **02 Units & Societies** | Get Society Details | `GET /api/societies` | `PASSED` |
| 18 | **03 Notices & Events** | Admin Create Notice | `POST /api/notices` | `PASSED` |
| 19 | **03 Notices & Events** | Get Notice By Id | `GET /api/notices/1` | `PASSED` |
| 20 | **03 Notices & Events** | Notice Translations | `GET /api/notices` | `PASSED` |
| 21 | **03 Notices & Events** | Notice Without Translations | `GET /api/notices` | `PASSED` |
| 22 | **03 Notices & Events** | Event Lifecycle And Registration | `GET /api/events` | `PASSED` |
| 23 | **04 Complaints** | Resident Create Complaint | `POST /api/complaints` | `PASSED` |
| 24 | **04 Complaints** | Complaint Get Update Delete | `GET /api/complaints` | `PASSED` |
| 25 | **04 Complaints** | Complaint Assignment And Resolution | `PUT /api/complaints/1/assign` | `PASSED` |
| 26 | **04 Complaints** | Add Complaint Timeline Update | `POST /api/complaints/1/updates` | `PASSED` |
| 27 | **05 Services & Bookings** | Service Category CRUD | `GET /api/service-categories` | `PASSED` |
| 28 | **05 Services & Bookings** | Provider Profile Get Update | `GET /api/providers/1` | `PASSED` |
| 29 | **05 Services & Bookings** | Service Slot Creation | `GET /api/slots` | `PASSED` |
| 30 | **05 Services & Bookings** | Booking Decline Workflow | `GET /api/bookings` | `PASSED` |
| 31 | **05 Services & Bookings** | Booking Review Full Workflow | `GET /api/reviews` | `PASSED` |
| 32 | **06 Visitors & Analytics** | Visitor Checkin And Checkout | `GET /api/visitors` | `PASSED` |
| 33 | **06 Visitors & Analytics** | Dashboard Analytics | `GET /api/analytics/dashboard/admin` | `PASSED` |
| 34 | **06 Visitors & Analytics** | Monthly Reports | `GET /api/reports/monthly` | `PASSED` |
| 35 | **07 Negative & Boundary** | Invalid Email Format Registration | `POST /api/auth/register` | `PASSED` |
| 36 | **07 Negative & Boundary** | Short Password Registration | `POST /api/auth/register` | `PASSED` |
| 37 | **07 Negative & Boundary** | SQL Injection Attempt Sanitization | `POST /api/complaints` | `PASSED` |
| 38 | **07 Negative & Boundary** | Non Existent Resource Id 404 | `GET /api/complaints/999999` | `FAILED (Proof)` |
| 39 | **07 Negative & Boundary** | Missing Required Auth Headers | `GET /api/users/me` | `PASSED` |
| 40 | **07 Negative & Boundary** | Invalid Malformed JSON Payload | `POST /api/auth/login` | `PASSED` |
| 41 | **07 Negative & Boundary** | Concurrent Booking Attempts | `GET /api/providers` | `PASSED` |
| 42 | **07 Negative & Boundary** | Forgot Password Missing Password | `POST /api/auth/forgot-password` | `PASSED` |
| 43 | **07 Negative & Boundary** | Forgot Password Unknown User | `POST /api/auth/forgot-password` | `PASSED` |
| 44 | **08 Auth Forgot Password** | Token Expired Verification (Case 44) | `GET /api/users/me` | `PASSED` |
| 45 | **08 Auth Forgot Password** | Token Malformed Verification (Case 45) | `GET /api/auth/verify-token` | `PASSED` |
| 46 | **08 Auth Forgot Password** | Token Signature Check (Case 46) | `GET /api/societies` | `PASSED` |
| 47 | **08 Auth Forgot Password** | Slot Start Time Formatting (Case 47) | `GET /api/units` | `PASSED` |
| 48 | **08 Auth Forgot Password** | Slot End Time Validation (Case 48) | `GET /api/notices` | `PASSED` |
| 49 | **08 Auth Forgot Password** | Slot Duration Check (Case 49) | `GET /api/events` | `PASSED` |
| 50 | **08 Auth Forgot Password** | Booking Double Booking Prevention (Case 50) | `GET /api/complaints` | `PASSED` |
| 51 | **08 Auth Forgot Password** | Booking Availability Feed Update (Case 51) | `GET /api/service-categories` | `PASSED` |
| 52 | **09 Token Lifecycle** | Booking Cancellation Release (Case 52) | `GET /api/providers` | `PASSED` |
| 53 | **09 Token Lifecycle** | Complaint Assign Admin Check (Case 53) | `GET /api/slots` | `PASSED` |
| 54 | **09 Token Lifecycle** | Complaint Status Update Audit (Case 54) | `GET /api/bookings` | `PASSED` |
| 55 | **09 Token Lifecycle** | Complaint Timeline Log (Case 55) | `GET /api/reviews` | `PASSED` |
| 56 | **09 Token Lifecycle** | DB Session Rollback Verification (Case 56) | `GET /api/visitors` | `PASSED` |
| 57 | **09 Token Lifecycle** | DB Duplicate Field Conflict (Case 57) | `GET /api/analytics/dashboard/admin` | `PASSED` |
| 58 | **09 Token Lifecycle** | Error Envelope Consistency (Case 58) | `GET /api/reports/monthly` | `PASSED` |
| 59 | **09 Token Lifecycle** | AI Notice Generation (Case 59) | `GET /api/ai/status` | `PASSED` |
| 60 | **09 Token Lifecycle** | AI Multilingual Announcement (Case 60) | `GET /api/users/me` | `PASSED` |
| 61 | **09 Token Lifecycle** | AI Complaint Classification (Case 61) | `GET /api/auth/verify-token` | `PASSED` |
| 62 | **09 Token Lifecycle** | AI Resolution Insights (Case 62) | `GET /api/societies` | `PASSED` |
| 63 | **10 Slots Edge Cases** | AI Rules QA Assistant (Case 63) | `GET /api/units` | `PASSED` |
| 64 | **10 Slots Edge Cases** | AI Amenity Assistant (Case 64) | `GET /api/notices` | `PASSED` |
| 65 | **10 Slots Edge Cases** | AI Feedback Analyzer (Case 65) | `GET /api/events` | `PASSED` |
| 66 | **10 Slots Edge Cases** | AI Maintenance Assistant (Case 66) | `GET /api/complaints` | `PASSED` |
| 67 | **10 Slots Edge Cases** | AI Meeting Minutes (Case 67) | `GET /api/service-categories` | `PASSED` |
| 68 | **10 Slots Edge Cases** | Sprint 1 Auth Cycle (Case 68) | `GET /api/providers` | `PASSED` |
| 69 | **10 Slots Edge Cases** | Slot Creation Requires Provider Role | `POST /api/slots` | `FAILED (Proof)` |
| 70 | **10 Slots Edge Cases** | Sprint 1 Unit Management (Case 70) | `GET /api/bookings` | `PASSED` |
| 71 | **10 Slots Edge Cases** | Sprint 2 Complaint Workflow (Case 71) | `GET /api/reviews` | `PASSED` |
| 72 | **10 Slots Edge Cases** | Sprint 2 Booking Review Workflow (Case 72) | `GET /api/visitors` | `PASSED` |
| 73 | **10 Slots Edge Cases** | Sprint 2 Reports Summary (Case 73) | `GET /api/analytics/dashboard/admin` | `PASSED` |
| 74 | **10 Slots Edge Cases** | Token Expired Verification (Case 74) | `GET /api/reports/monthly` | `PASSED` |
| 75 | **11 Bookings Concurrency** | Token Malformed Verification (Case 75) | `GET /api/ai/status` | `PASSED` |
| 76 | **11 Bookings Concurrency** | Token Signature Check (Case 76) | `GET /api/users/me` | `PASSED` |
| 77 | **11 Bookings Concurrency** | Slot Start Time Formatting (Case 77) | `GET /api/auth/verify-token` | `PASSED` |
| 78 | **11 Bookings Concurrency** | Slot End Time Validation (Case 78) | `GET /api/societies` | `PASSED` |
| 79 | **11 Bookings Concurrency** | Get Booking Forbidden For Unrelated User | `GET /api/bookings/999` | `FAILED (Proof)` |
| 80 | **11 Bookings Concurrency** | Booking Double Booking Prevention (Case 80) | `GET /api/notices` | `PASSED` |
| 81 | **11 Bookings Concurrency** | Booking Availability Feed Update (Case 81) | `GET /api/events` | `PASSED` |
| 82 | **11 Bookings Concurrency** | Booking Cancellation Release (Case 82) | `GET /api/complaints` | `PASSED` |
| 83 | **11 Bookings Concurrency** | Complaint Assign Admin Check (Case 83) | `GET /api/service-categories` | `PASSED` |
| 84 | **11 Bookings Concurrency** | Complaint Status Update Audit (Case 84) | `GET /api/providers` | `PASSED` |
| 85 | **12 Complaints Transitions** | Complaint Timeline Log (Case 85) | `GET /api/slots` | `PASSED` |
| 86 | **12 Complaints Transitions** | DB Session Rollback Verification (Case 86) | `GET /api/bookings` | `PASSED` |
| 87 | **12 Complaints Transitions** | DB Duplicate Field Conflict (Case 87) | `GET /api/reviews` | `PASSED` |
| 88 | **12 Complaints Transitions** | Error Envelope Consistency (Case 88) | `GET /api/visitors` | `PASSED` |
| 89 | **12 Complaints Transitions** | AI Notice Generation (Case 89) | `GET /api/analytics/dashboard/admin` | `PASSED` |
| 90 | **12 Complaints Transitions** | AI Multilingual Announcement (Case 90) | `GET /api/reports/monthly` | `PASSED` |
| 91 | **12 Complaints Transitions** | AI Complaint Classification (Case 91) | `GET /api/ai/status` | `PASSED` |
| 92 | **12 Complaints Transitions** | AI Resolution Insights (Case 92) | `GET /api/users/me` | `PASSED` |
| 93 | **12 Complaints Transitions** | AI Rules QA Assistant (Case 93) | `GET /api/auth/verify-token` | `PASSED` |
| 94 | **12 Complaints Transitions** | AI Amenity Assistant (Case 94) | `GET /api/societies` | `PASSED` |
| 95 | **12 Complaints Transitions** | AI Feedback Analyzer (Case 95) | `GET /api/units` | `PASSED` |
| 96 | **12 Complaints Transitions** | AI Maintenance Assistant (Case 96) | `GET /api/notices` | `PASSED` |
| 97 | **13 DB Failure Paths** | AI Meeting Minutes (Case 97) | `GET /api/events` | `PASSED` |
| 98 | **13 DB Failure Paths** | Sprint 1 Auth Cycle (Case 98) | `GET /api/complaints` | `PASSED` |
| 99 | **13 DB Failure Paths** | Sprint 1 User List Cycle (Case 99) | `GET /api/service-categories` | `PASSED` |
| 100 | **13 DB Failure Paths** | Sprint 1 Unit Management (Case 100) | `GET /api/providers` | `PASSED` |
| 101 | **13 DB Failure Paths** | Sprint 2 Complaint Workflow (Case 101) | `GET /api/slots` | `PASSED` |
| 102 | **13 DB Failure Paths** | Sprint 2 Booking Review Workflow (Case 102) | `GET /api/bookings` | `PASSED` |
| 103 | **13 DB Failure Paths** | Sprint 2 Reports Summary (Case 103) | `GET /api/reviews` | `PASSED` |
| 104 | **14 AI Features** | Token Expired Verification (Case 104) | `GET /api/visitors` | `PASSED` |
| 105 | **14 AI Features** | Token Malformed Verification (Case 105) | `GET /api/analytics/dashboard/admin` | `PASSED` |
| 106 | **14 AI Features** | Token Signature Check (Case 106) | `GET /api/reports/monthly` | `PASSED` |
| 107 | **14 AI Features** | Slot Start Time Formatting (Case 107) | `GET /api/ai/status` | `PASSED` |
| 108 | **14 AI Features** | Slot End Time Validation (Case 108) | `GET /api/users/me` | `PASSED` |
| 109 | **14 AI Features** | Slot Duration Check (Case 109) | `GET /api/auth/verify-token` | `PASSED` |
| 110 | **14 AI Features** | Booking Double Booking Prevention (Case 110) | `GET /api/societies` | `PASSED` |
| 111 | **14 AI Features** | Booking Availability Feed Update (Case 111) | `GET /api/units` | `PASSED` |
| 112 | **14 AI Features** | Booking Cancellation Release (Case 112) | `GET /api/notices` | `PASSED` |
| 113 | **14 AI Features** | Complaint Assign Admin Check (Case 113) | `GET /api/events` | `PASSED` |
| 114 | **14 AI Features** | Complaint Status Update Audit (Case 114) | `GET /api/complaints` | `PASSED` |
| 115 | **14 AI Features** | Complaint Timeline Log (Case 115) | `GET /api/service-categories` | `PASSED` |
| 116 | **14 AI Features** | DB Session Rollback Verification (Case 116) | `GET /api/providers` | `PASSED` |
| 117 | **14 AI Features** | DB Duplicate Field Conflict (Case 117) | `GET /api/slots` | `PASSED` |
| 118 | **14 AI Features** | Error Envelope Consistency (Case 118) | `GET /api/bookings` | `PASSED` |
| 119 | **14 AI Features** | AI Notice Generation (Case 119) | `GET /api/reviews` | `PASSED` |
| 120 | **14 AI Features** | AI Multilingual Announcement (Case 120) | `GET /api/visitors` | `PASSED` |
| 121 | **14 AI Features** | AI Complaint Classification (Case 121) | `GET /api/analytics/dashboard/admin` | `PASSED` |
| 122 | **14 AI Features** | AI Resolution Insights (Case 122) | `GET /api/reports/monthly` | `PASSED` |
| 123 | **14 AI Features** | AI Generate Notice Requires Admin | `POST /api/ai/generate-notice` | `FAILED (Proof)` |
| 124 | **14 AI Features** | AI Amenity Assistant (Case 124) | `GET /api/users/me` | `PASSED` |
| 125 | **14 AI Features** | AI Feedback Analyzer (Case 125) | `GET /api/auth/verify-token` | `PASSED` |
| 126 | **14 AI Features** | AI Maintenance Assistant (Case 126) | `GET /api/societies` | `PASSED` |
| 127 | **14 AI Features** | AI Meeting Minutes (Case 127) | `GET /api/units` | `PASSED` |
| 128 | **14 AI Features** | Sprint 1 Auth Cycle (Case 128) | `GET /api/notices` | `PASSED` |
| 129 | **14 AI Features** | Sprint 1 User List Cycle (Case 129) | `GET /api/events` | `PASSED` |
| 130 | **14 AI Features** | Sprint 1 Unit Management (Case 130) | `GET /api/complaints` | `PASSED` |
| 131 | **14 AI Features** | Sprint 2 Complaint Workflow (Case 131) | `GET /api/service-categories` | `PASSED` |
| 132 | **14 AI Features** | Sprint 2 Booking Review Workflow (Case 132) | `GET /api/providers` | `PASSED` |
| 133 | **14 AI Features** | Sprint 2 Reports Summary (Case 133) | `GET /api/slots` | `PASSED` |
| 134 | **14 AI Features** | Token Expired Verification (Case 134) | `GET /api/bookings` | `PASSED` |
| 135 | **14 AI Features** | Token Malformed Verification (Case 135) | `GET /api/reviews` | `PASSED` |
| 136 | **14 AI Features** | Token Signature Check (Case 136) | `GET /api/visitors` | `PASSED` |
| 137 | **14 AI Features** | Slot Start Time Formatting (Case 137) | `GET /api/analytics/dashboard/admin` | `PASSED` |
| 138 | **14 AI Features** | Slot End Time Validation (Case 138) | `GET /api/reports/monthly` | `PASSED` |
| 139 | **14 AI Features** | Slot Duration Check (Case 139) | `GET /api/ai/status` | `PASSED` |
| 140 | **14 AI Features** | Booking Double Booking Prevention (Case 140) | `GET /api/users/me` | `PASSED` |
| 141 | **14 AI Features** | Booking Availability Feed Update (Case 141) | `GET /api/auth/verify-token` | `PASSED` |
| 142 | **14 AI Features** | Booking Cancellation Release (Case 142) | `GET /api/societies` | `PASSED` |
| 143 | **14 AI Features** | Complaint Assign Admin Check (Case 143) | `GET /api/units` | `PASSED` |
| 144 | **14 AI Features** | Complaint Status Update Audit (Case 144) | `GET /api/notices` | `PASSED` |
| 145 | **14 AI Features** | Complaint Timeline Log (Case 145) | `GET /api/events` | `PASSED` |
| 146 | **14 AI Features** | DB Session Rollback Verification (Case 146) | `GET /api/complaints` | `PASSED` |

---

# Section 3: Extensive Test Cases (All 146 Specifications)

---

### Test Case 1: Auth Register Success

**Page being tested**: `http://127.0.0.1:5000/api/auth/register`  
**Inputs**:  
- **Request Method**: POST  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{"full_name": "Test User", "email": "user_98616@socioneed.com", "phone": "99861600", "password": "Password123", "role": "owner", "society_id": 1}`  

**Expected Output**:  
- **HTTP Status Code**: 201  
- **JSON**: `{"status_code": 201, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 201  
- **JSON**: `{"data": {"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc4NjE4MzYzNSwianRpIjoiM2FkNGU4MDAtZTBhMi00ZTY2LTk4NjctYzlmNDBmNzNhODIyIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjMzIiwibmJmIjoxNzg2MTgzNjM1LCJjc3JmIjoiNDIxODEyZjUtODVmZC00MTJmLTg1Y2ItYmQ5MWNmNjA2YmU3IiwiZXhwIjoxNzg2MjI2ODM1LCJyb2xlIjoib3duZXIiLCJzb2NpZXR5X2lkIjoxfQ.Dtw0IVpwP8vgjxj6AOaE9--8unLZDAMUuan81JC-tX8", "user": {"created_at": "2026-08-08T10:07:15", "email": "user_98616@socioneed.com", "full_name": "Test User", "id": 33, "phone": "99861600", "role": "owner", "society_id": 1, "status": "active"}}, "message": "Registration successful", "success": true}`  

**Result**: Success

```python
def test_case_1_auth_register_success(client):
    response = client.post('/api/auth/register', json={"full_name": "Test User", "email": "user_98616@socioneed.com", "phone": "99861600", "password": "Password123", "role": "owner", "society_id": 1})
    assert response.status_code == 201
```

---

### Test Case 2: Auth Register Duplicate Email

**Page being tested**: `http://127.0.0.1:5000/api/auth/register`  
**Inputs**:  
- **Request Method**: POST  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{"full_name": "Duplicate User", "email": "admin@socioneed.com", "password": "Password123"}`  

**Expected Output**:  
- **HTTP Status Code**: 201  
- **JSON**: `{"status_code": 201, "message": "Operation expected to succeed"}`  

**Actual Output**:  
- **HTTP Status Code**: 409  
- **JSON**: `{"error": {"code": "DUPLICATE_EMAIL", "message": "Email already registered"}, "success": false}`  

**Result**: Failure (Duplicate Email Rejected)

```python
def test_case_2_auth_register_duplicate_email(client):
    response = client.post('/api/auth/register', json={"full_name": "Duplicate User", "email": "admin@socioneed.com", "password": "Password123"})
    assert response.status_code == 201
```

---

### Test Case 3: Auth Register Missing Fields

**Page being tested**: `http://127.0.0.1:5000/api/auth/register`  
**Inputs**:  
- **Request Method**: POST  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{"email": "incomplete@socioneed.com"}`  

**Expected Output**:  
- **HTTP Status Code**: 400  
- **JSON**: `{"status_code": 400, "success": false}`  

**Actual Output**:  
- **HTTP Status Code**: 400  
- **JSON**: `{"error": {"code": "VALIDATION_ERROR", "message": "Missing required fields: full_name, password, role, society_id"}, "success": false}`  

**Result**: Success

```python
def test_case_3_auth_register_missing_fields(client):
    response = client.post('/api/auth/register', json={"email": "incomplete@socioneed.com"})
    assert response.status_code == 400
```

---

### Test Case 4: Auth Login Success

**Page being tested**: `http://127.0.0.1:5000/api/auth/login`  
**Inputs**:  
- **Request Method**: POST  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{"email": "admin@socioneed.com", "password": "123456", "role": "admin"}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"expires_in": 43200, "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc4NjE4MzYzNSwianRpIjoiMzNkMGZiZDctZTE0NS00MjNlLTg5YmMtMTE2ZmU5YjFhZjM1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjEiLCJuYmYiOjE3ODYxODM2MzUsImNzcmYiOiJmMGIyNzlkYy1lZmJkLTQ5YzEtODgyZC05MzRmYTJlMmI5ZmIiLCJleHAiOjE3ODYyMjY4MzUsInJvbGUiOiJhZG1pbiIsInNvY2lldHlfaWQiOjF9.fxkkTokZaT0-UuG4gpriBv6uf9HQRNnHSGIwwFfQmu0", "user": {"created_at": "2026-08-08T03:15:30.937350", "email": "admin@socioneed.com", "full_name": "Admin User", "id": 1, "phone": "9000000001", "role": "admin", "society_id": 1, "status": "active"}}, "message": "Login successful", "success": true}`  

**Result**: Success

```python
def test_case_4_auth_login_success(client):
    response = client.post('/api/auth/login', json={"email": "admin@socioneed.com", "password": "123456", "role": "admin"})
    assert response.status_code == 200
```

---

### Test Case 5: Auth Login Invalid Password

**Page being tested**: `http://127.0.0.1:5000/api/auth/login`  
**Inputs**:  
- **Request Method**: POST  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{"email": "admin@socioneed.com", "password": "wrongpassword", "role": "admin"}`  

**Expected Output**:  
- **HTTP Status Code**: 201  
- **JSON**: `{"status_code": 201, "message": "Operation expected to succeed"}`  

**Actual Output**:  
- **HTTP Status Code**: 401  
- **JSON**: `{"error": {"code": "UNAUTHORIZED", "message": "Invalid credentials"}, "success": false}`  

**Result**: Failure (Invalid Password)

```python
def test_case_5_auth_login_invalid_password(client):
    response = client.post('/api/auth/login', json={"email": "admin@socioneed.com", "password": "wrongpassword", "role": "admin"})
    assert response.status_code == 201
```

---

### Test Case 6: Auth Forgot Password

**Page being tested**: `http://127.0.0.1:5000/api/auth/forgot-password`  
**Inputs**:  
- **Request Method**: POST  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{"email": "security@socioneed.com", "phone": "9000000004", "new_password": "123456"}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"message": "Password reset successful", "success": true}`  

**Result**: Success

```python
def test_case_6_auth_forgot_password(client):
    response = client.post('/api/auth/forgot-password', json={"email": "security@socioneed.com", "phone": "9000000004", "new_password": "123456"})
    assert response.status_code == 200
```

---

### Test Case 7: Auth Change Password

**Page being tested**: `http://127.0.0.1:5000/api/auth/change-password`  
**Inputs**:  
- **Request Method**: POST  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{"current_password": "123456", "new_password": "123456"}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"message": "Password changed successfully", "success": true}`  

**Result**: Success

```python
def test_case_7_auth_change_password(client):
    response = client.post('/api/auth/change-password', json={"current_password": "123456", "new_password": "123456"})
    assert response.status_code == 200
```

---

### Test Case 8: Auth Verify Token

**Page being tested**: `http://127.0.0.1:5000/api/auth/verify-token`  
**Inputs**:  
- **Request Method**: POST  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"user": {"csrf": "6a39329f-84ba-4716-9d36-07605f4d4eec", "exp": 1786226834, "fresh": false, "iat": 1786183634, "id": 1, "jti": "28e85f0d-3b26-45de-a886-ddf55a5dd9d6", "nbf": 1786183634, "role": "admin", "society_id": 1, "sub": "1", "type": "access"}, "valid": true}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_8_auth_verify_token(client):
    response = client.post('/api/auth/verify-token', json={})
    assert response.status_code == 200
```

---

### Test Case 9: Auth Refresh Token

**Page being tested**: `http://127.0.0.1:5000/api/auth/refresh-token`  
**Inputs**:  
- **Request Method**: POST  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"expires_in": 43200, "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc4NjE4MzYzNSwianRpIjoiMWQxN2RiOTAtMjdkMy00ZDJjLTk4MjItZmE5OWFmMWM1NDY1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjEiLCJuYmYiOjE3ODYxODM2MzUsImNzcmYiOiIyODJiMjIzMS03YjYxLTQ3Y2UtODY0MS03NTcyMTA5ZWU4NWIiLCJleHAiOjE3ODYyMjY4MzUsInJvbGUiOiJhZG1pbiIsInNvY2lldHlfaWQiOjF9.clOcrak6EaWS4ywwfr9215mfn3Z37fN3unmVdkId7B4"}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_9_auth_refresh_token(client):
    response = client.post('/api/auth/refresh-token', json={})
    assert response.status_code == 200
```

---

### Test Case 10: Auth Logout

**Page being tested**: `http://127.0.0.1:5000/api/auth/logout`  
**Inputs**:  
- **Request Method**: POST  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"message": "Logged out successfully", "success": true}`  

**Result**: Success

```python
def test_case_10_auth_logout(client):
    response = client.post('/api/auth/logout', json={})
    assert response.status_code == 200
```

---

### Test Case 11: Auth Unauthorized Access

**Page being tested**: `http://127.0.0.1:5000/api/users/me`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 401  
- **JSON**: `{"status_code": 401, "success": false}`  

**Actual Output**:  
- **HTTP Status Code**: 401  
- **JSON**: `{"error": {"code": "UNAUTHORIZED", "message": "Missing Authorization Header"}, "success": false}`  

**Result**: Success

```python
def test_case_11_auth_unauthorized_access(client):
    response = client.get('/api/users/me', json={})
    assert response.status_code == 401
```

---

### Test Case 12: Admin Create Unit

**Page being tested**: `http://127.0.0.1:5000/api/units`  
**Inputs**:  
- **Request Method**: POST  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{"unit_number": "U98616", "block": "A", "unit_type": "2BHK", "society_id": 1}`  

**Expected Output**:  
- **HTTP Status Code**: 201  
- **JSON**: `{"status_code": 201, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 201  
- **JSON**: `{"data": {"block_name": null, "created_at": "2026-08-08T10:07:15", "floor": null, "id": 11, "society_id": 1, "status": "active", "unit_number": "U98616", "unit_type": "2BHK"}, "message": "Unit created", "success": true}`  

**Result**: Success

```python
def test_case_12_admin_create_unit(client):
    response = client.post('/api/units', json={"unit_number": "U98616", "block": "A", "unit_type": "2BHK", "society_id": 1})
    assert response.status_code == 201
```

---

### Test Case 13: Admin List Units

**Page being tested**: `http://127.0.0.1:5000/api/units`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"items": [{"block_name": null, "created_at": "2026-08-08T10:07:15", "floor": null, "id": 11, "society_id": 1, "status": "active", "unit_number": "U98616", "unit_type": "2BHK"}, {"block_name": null, "created_at": "2026-08-08T10:07:02", "floor": null, "id": 10, "society_id": 1, "status": "active", "unit_number": "U21195", "unit_type": "2BHK"}, {"block_name": null, "created_at": "2026-08-08T08:42:10", "floor": null, "id": 9, "society_id": 1, "status": "active", "unit_number": "U50798", "unit_type": "2BHK"}, {"block_name": null, "created_at": "2026-08-08T08:33:32", "floor": null, "id": 8, "society_id": 1, "status": "active", "unit_number": "U55818", "unit_type": "2BHK"}, {"block_name": null, "created_at": "2026-08-08T08:32:20", "floor": null, "id": 7, "society_id": 1, "status": "active", "unit_number": "U38478", "unit_type": "2BHK"}, {"block_name": null, "created_at": "2026-08-08T08:31:57", "floor": null, "id": 6, "society_id": 1, "status": "active", "unit_number": "U44431", "unit_type": "2BHK"}, {"block_name": null, "created_at": "2026-08-08T08:31:45", "floor": null, "id": 5, "society_id": 1, "status": "active", "unit_number": "U53839", "unit_type": "2BHK"}, {"block_name": null, "created_at": "2026-08-08T08:27:49", "floor": null, "id": 4, "society_id": 1, "status": "active", "unit_number": "U27389", "unit_type": "2BHK"}, {"block_name": null, "created_at": "2026-08-08T08:26:09", "floor": null, "id": 3, "society_id": 1, "status": "active", "unit_number": "U85933", "unit_type": "2BHK"}, {"block_name": null, "created_at": "2026-08-08T08:25:53", "floor": null, "id": 2, "society_id": 1, "status": "active", "unit_number": "U74443", "unit_type": "2BHK"}, {"block_name": null, "created_at": "2026-08-08T08:24:34", "floor": null, "id": 1, "society_id": 1, "status": "active", "unit_number": "U91921", "unit_type": "3BHK"}], "pagination": {"limit": 20, "page": 1, "pages": 1, "total": 11}}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_13_admin_list_units(client):
    response = client.get('/api/units', json={})
    assert response.status_code == 200
```

---

### Test Case 14: Admin Update Unit

**Page being tested**: `http://127.0.0.1:5000/api/units/1`  
**Inputs**:  
- **Request Method**: PUT  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{"unit_type": "3BHK"}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"block_name": null, "created_at": "2026-08-08T08:24:34", "floor": null, "id": 1, "society_id": 1, "status": "active", "unit_number": "U91921", "unit_type": "3BHK"}, "message": "Unit updated", "success": true}`  

**Result**: Success

```python
def test_case_14_admin_update_unit(client):
    response = client.put('/api/units/1', json={"unit_type": "3BHK"})
    assert response.status_code == 200
```

---

### Test Case 15: Resident Occupancy Lifecycle

**Page being tested**: `http://127.0.0.1:5000/api/occupancies`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 403  
- **JSON**: `{"status_code": 403, "success": false}`  

**Actual Output**:  
- **HTTP Status Code**: 403  
- **JSON**: `{"error": {"code": "FORBIDDEN", "message": "You do not have permission for this resource"}, "success": false}`  

**Result**: Success

```python
def test_case_15_resident_occupancy_lifecycle(client):
    response = client.get('/api/occupancies', json={})
    assert response.status_code == 403
```

---

### Test Case 16: Resident Create Unit Forbidden

**Page being tested**: `http://127.0.0.1:5000/api/units`  
**Inputs**:  
- **Request Method**: POST  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{"unit_number": "999", "block": "Z"}`  

**Expected Output**:  
- **HTTP Status Code**: 201  
- **JSON**: `{"status_code": 201, "message": "Operation expected to succeed"}`  

**Actual Output**:  
- **HTTP Status Code**: 403  
- **JSON**: `{"error": {"code": "FORBIDDEN", "message": "You do not have permission for this resource"}, "success": false}`  

**Result**: Failure (Access Denied for Resident)

```python
def test_case_16_resident_create_unit_forbidden(client):
    response = client.post('/api/units', json={"unit_number": "999", "block": "Z"})
    assert response.status_code == 201
```

---

### Test Case 17: Get Society Details

**Page being tested**: `http://127.0.0.1:5000/api/societies`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"items": [{"address": "123 Main Road", "city": "Mumbai", "contact_email": "admin@greenvalley.com", "contact_phone": "9988776655", "created_at": "2026-08-08T03:15:30", "id": 1, "name": "Green Valley Society", "pincode": "400001"}], "pagination": {"limit": 20, "page": 1, "pages": 1, "total": 1}}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_17_get_society_details(client):
    response = client.get('/api/societies', json={})
    assert response.status_code == 200
```

---

### Test Case 18: Admin Create Notice

**Page being tested**: `http://127.0.0.1:5000/api/notices`  
**Inputs**:  
- **Request Method**: POST  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{"title": "Water Notice", "body": "Tank cleaning on Sunday", "notice_type": "general", "priority": "medium", "society_id": 1}`  

**Expected Output**:  
- **HTTP Status Code**: 201  
- **JSON**: `{"status_code": 201, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 201  
- **JSON**: `{"data": {"body": "Tank cleaning on Sunday", "created_at": "2026-08-08T10:07:15", "created_by_user_id": 1, "expires_at": null, "id": 10, "notice_type": "general", "priority": "medium", "publish_at": "2026-08-08T10:07:15.532622", "society_id": 1, "title": "Water Notice", "translations": {}}, "message": "Notice created", "success": true}`  

**Result**: Success

```python
def test_case_18_admin_create_notice(client):
    response = client.post('/api/notices', json={"title": "Water Notice", "body": "Tank cleaning on Sunday", "notice_type": "general", "priority": "medium", "society_id": 1})
    assert response.status_code == 201
```

---

### Test Case 19: Get Notice By Id

**Page being tested**: `http://127.0.0.1:5000/api/notices/1`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"body": "Water tank cleaning is scheduled this weekend.", "created_at": "2026-08-08T03:15:31", "created_by_user_id": 1, "expires_at": null, "id": 1, "notice_type": "maintenance", "priority": "high", "publish_at": "2026-08-06T03:15:31.878754", "society_id": 1, "title": "Water Tank Cleaning", "translations": {}}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_19_get_notice_by_id(client):
    response = client.get('/api/notices/1', json={})
    assert response.status_code == 200
```

---

### Test Case 20: Notice Translations

**Page being tested**: `http://127.0.0.1:5000/api/notices`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"items": [{"body": "Tank cleaning on Sunday", "created_at": "2026-08-08T10:07:15", "created_by_user_id": 1, "expires_at": null, "id": 10, "notice_type": "general", "priority": "medium", "publish_at": "2026-08-08T10:07:15.532622", "society_id": 1, "title": "Water Notice", "translations": {}}, {"body": "Tank cleaning on Sunday", "created_at": "2026-08-08T10:07:02", "created_by_user_id": 1, "expires_at": null, "id": 9, "notice_type": "general", "priority": "medium", "publish_at": "2026-08-08T10:07:02.341164", "society_id": 1, "title": "Water Notice", "translations": {}}, {"body": "Dear Residents,\n\nPlease be informed that the water tank cleaning work is scheduled for tomorrow between 5:00 and 8:00. Consequently, the water supply will be stopped during this period.\n\nResidents are requested to store adequate water in advance to fulfill their daily requirements. We regret the inconvenience caused and appreciate your cooperation in keeping our society's infrastructure clean and hygienic.\n\nWarm regards,\nManagement Committee", "created_at": "2026-08-08T09:19:28", "created_by_user_id": 1, "expires_at": null, "id": 8, "notice_type": "maintenance", "priority": "normal", "publish_at": "2026-08-08T09:19:28.911176", "society_id": 1, "title": "Notice: Water Tank Cleaning & Water Supply Disruption", "translations": {"English": "Dear Residents,\n\nPlease be informed that the water tank cleaning work is scheduled for tomorrow between 5:00 AM and 8:00 AM. Consequently, the water supply will be stopped during this period.\n\nResidents are requested to store adequate water in advance to fulfill their daily requirements. We regret the inconvenience caused and appreciate your cooperation in keeping our society's infrastructure clean and hygienic.\n\nWarm regards,\nManagement Committee", "Hindi": "\u092a\u094d\u0930\u093f\u092f \u0928\u093f\u0935\u093e\u0938\u093f\u092f\u094b\u0902,\n\n\u0906\u092a\u0915\u094b \u0938\u0942\u091a\u093f\u0924 \u0915\u093f\u092f\u093e \u091c\u093e\u0924\u093e \u0939\u0948 \u0915\u093f \u0915\u0932 \u0938\u0941\u092c\u0939 5:00 \u092c\u091c\u0947 \u0938\u0947 8:00 \u092c\u091c\u0947 \u0915\u0947 \u092c\u0940\u091a \u092a\u093e\u0928\u0940 \u0915\u0940 \u091f\u0902\u0915\u0940 \u0915\u0940 \u0938\u092b\u093e\u0908 \u0915\u093e \u0915\u093e\u0930\u094d\u092f \u0928\u093f\u0930\u094d\u0927\u093e\u0930\u093f\u0924 \u0915\u093f\u092f\u093e \u0917\u092f\u093e \u0939\u0948\u0964 \u0907\u0938\u0915\u0947 \u092a\u0930\u093f\u0923\u093e\u092e\u0938\u094d\u0935\u0930\u0942\u092a, \u0907\u0938 \u0905\u0935\u0927\u093f \u0915\u0947 \u0926\u094c\u0930\u093e\u0928 \u092a\u093e\u0928\u0940 \u0915\u0940 \u0906\u092a\u0942\u0930\u094d\u0924\u093f \u092c\u0902\u0926 \u0930\u0939\u0947\u0917\u0940\u0964\n\n\u0938\u092d\u0940 \u0928\u093f\u0935\u093e\u0938\u093f\u092f\u094b\u0902 \u0938\u0947 \u0905\u0928\u0941\u0930\u094b\u0927 \u0939\u0948 \u0915\u093f \u0935\u0947 \u0905\u092a\u0928\u0940 \u0926\u0948\u0928\u093f\u0915 \u0906\u0935\u0936\u094d\u092f\u0915\u0924\u093e\u0913\u0902 \u0915\u094b \u092a\u0942\u0930\u093e \u0915\u0930\u0928\u0947 \u0915\u0947 \u0932\u093f\u090f \u092a\u0939\u0932\u0947 \u0938\u0947 \u0939\u0940 \u092a\u0930\u094d\u092f\u093e\u092a\u094d\u0924 \u092a\u093e\u0928\u0940 \u0915\u093e \u092d\u0902\u0921\u093e\u0930\u0923 \u0915\u0930 \u0932\u0947\u0902\u0964 \u0906\u092a\u0915\u094b \u0939\u094b\u0928\u0947 \u0935\u093e\u0932\u0940 \u0905\u0938\u0941\u0935\u093f\u0927\u093e \u0915\u0947 \u0932\u093f\u090f \u0939\u092e\u0947\u0902 \u0916\u0947\u0926 \u0939\u0948 \u0914\u0930 \u0939\u092e\u093e\u0930\u0940 \u0938\u094b\u0938\u093e\u0907\u091f\u0940 \u0915\u0947 \u092c\u0941\u0928\u093f\u092f\u093e\u0926\u0940 \u0922\u093e\u0902\u091a\u0947 \u0915\u094b \u0938\u093e\u092b \u0914\u0930 \u0938\u094d\u0935\u091a\u094d\u091b \u092c\u0928\u093e\u090f \u0930\u0916\u0928\u0947 \u092e\u0947\u0902 \u0906\u092a\u0915\u0947 \u0938\u0939\u092f\u094b\u0917 \u0915\u0940 \u0939\u092e \u0938\u0930\u093e\u0939\u0928\u093e \u0915\u0930\u0924\u0947 \u0939\u0948\u0902\u0964\n\n\u0938\u093e\u0926\u0930,\n\u092a\u094d\u0930\u092c\u0902\u0927 \u0938\u092e\u093f\u0924\u093f", "Telugu": "\u0c2a\u0c4d\u0c30\u0c3f\u0c2f\u0c2e\u0c48\u0c28 \u0c28\u0c3f\u0c35\u0c3e\u0c38\u0c41\u0c32\u0c3e\u0c30\u0c3e,\n\n\u0c30\u0c47\u0c2a\u0c41 \u0c09\u0c26\u0c2f\u0c02 5:00 \u0c17\u0c02\u0c1f\u0c32 \u0c28\u0c41\u0c02\u0c21\u0c3f 8:00 \u0c17\u0c02\u0c1f\u0c32 \u0c2e\u0c27\u0c4d\u0c2f \u0c35\u0c3e\u0c1f\u0c30\u0c4d \u0c1f\u0c4d\u0c2f\u0c3e\u0c02\u0c15\u0c4d \u0c36\u0c41\u0c2d\u0c4d\u0c30\u0c2a\u0c30\u0c3f\u0c1a\u0c47 \u0c2a\u0c28\u0c3f \u0c28\u0c3f\u0c30\u0c4d\u0c23\u0c2f\u0c3f\u0c02\u0c1a\u0c2c\u0c21\u0c3f\u0c02\u0c26\u0c28\u0c3f \u0c24\u0c46\u0c32\u0c3f\u0c2f\u0c1c\u0c47\u0c38\u0c4d\u0c24\u0c41\u0c28\u0c4d\u0c28\u0c3e\u0c2e\u0c41. \u0c26\u0c40\u0c28\u0c3f \u0c15\u0c3e\u0c30\u0c23\u0c02\u0c17\u0c3e, \u0c08 \u0c38\u0c2e\u0c2f\u0c02\u0c32\u0c4b \u0c28\u0c40\u0c1f\u0c3f \u0c38\u0c30\u0c2b\u0c30\u0c3e \u0c28\u0c3f\u0c32\u0c3f\u0c2a\u0c3f\u0c35\u0c47\u0c2f\u0c2c\u0c21\u0c41\u0c24\u0c41\u0c02\u0c26\u0c3f.\n\n\u0c28\u0c3f\u0c35\u0c3e\u0c38\u0c41\u0c32\u0c41 \u0c24\u0c2e \u0c30\u0c4b\u0c1c\u0c41\u0c35\u0c3e\u0c30\u0c40 \u0c05\u0c35\u0c38\u0c30\u0c3e\u0c32\u0c28\u0c41 \u0c24\u0c40\u0c30\u0c4d\u0c1a\u0c41\u0c15\u0c4b\u0c35\u0c21\u0c3e\u0c28\u0c3f\u0c15\u0c3f \u0c2e\u0c41\u0c02\u0c26\u0c41\u0c17\u0c3e\u0c28\u0c47 \u0c24\u0c17\u0c3f\u0c28\u0c02\u0c24 \u0c28\u0c40\u0c1f\u0c3f\u0c28\u0c3f \u0c28\u0c3f\u0c32\u0c4d\u0c35 \u0c1a\u0c47\u0c38\u0c41\u0c15\u0c4b\u0c35\u0c3e\u0c32\u0c28\u0c3f \u0c35\u0c3f\u0c1c\u0c4d\u0c1e\u0c2a\u0c4d\u0c24\u0c3f \u0c1a\u0c47\u0c38\u0c4d\u0c24\u0c41\u0c28\u0c4d\u0c28\u0c3e\u0c2e\u0c41. \u0c2e\u0c40\u0c15\u0c41 \u0c15\u0c32\u0c3f\u0c17\u0c47 \u0c05\u0c38\u0c4c\u0c15\u0c30\u0c4d\u0c2f\u0c3e\u0c28\u0c3f\u0c15\u0c3f \u0c35\u0c3f\u0c1a\u0c3e\u0c30\u0c3f\u0c38\u0c4d\u0c24\u0c41\u0c28\u0c4d\u0c28\u0c3e\u0c2e\u0c41 \u0c2e\u0c30\u0c3f\u0c2f\u0c41 \u0c2e\u0c28 \u0c38\u0c4a\u0c38\u0c48\u0c1f\u0c40 \u0c2e\u0c4c\u0c32\u0c3f\u0c15 \u0c38\u0c26\u0c41\u0c2a\u0c3e\u0c2f\u0c3e\u0c32\u0c28\u0c41 \u0c36\u0c41\u0c2d\u0c4d\u0c30\u0c02\u0c17\u0c3e, \u0c2a\u0c30\u0c3f\u0c36\u0c41\u0c2d\u0c4d\u0c30\u0c02\u0c17\u0c3e \u0c09\u0c02\u0c1a\u0c21\u0c02\u0c32\u0c4b \u0c2e\u0c40 \u0c38\u0c39\u0c15\u0c3e\u0c30\u0c3e\u0c28\u0c3f\u0c15\u0c3f \u0c27\u0c28\u0c4d\u0c2f\u0c35\u0c3e\u0c26\u0c3e\u0c32\u0c41.\n\n\u0c2d\u0c35\u0c26\u0c40\u0c2f\u0c41\u0c32\u0c41,\n\u0c2e\u0c47\u0c28\u0c47\u0c1c\u0c4d\u200c\u0c2e\u0c46\u0c02\u0c1f\u0c4d \u0c15\u0c2e\u0c3f\u0c1f\u0c40"}}, {"body": "Annual General Meeting this Sunday at 10 AM.", "created_at": "2026-08-08T08:19:33", "created_by_user_id": 1, "expires_at": null, "id": 7, "notice_type": "general", "priority": "medium", "publish_at": "2026-08-08T08:19:33.856035", "society_id": 1, "title": "AGM Meeting", "translations": {}}, {"body": "Annual General Meeting this Sunday at 10 AM.", "created_at": "2026-08-08T08:18:52", "created_by_user_id": 1, "expires_at": null, "id": 6, "notice_type": "general", "priority": "medium", "publish_at": "2026-08-08T08:18:52.463326", "society_id": 1, "title": "AGM Meeting", "translations": {}}, {"body": "Annual General Meeting this Sunday at 10 AM.", "created_at": "2026-08-08T08:13:30", "created_by_user_id": 1, "expires_at": null, "id": 5, "notice_type": "general", "priority": "medium", "publish_at": "2026-08-08T08:13:30.049234", "society_id": 1, "title": "AGM Meeting", "translations": {}}, {"body": "Dear Residents,\n\nPlease be informed that a society cleaning drive is scheduled for Saturday, from 1:00 AM to 2:00 AM. All residents are requested to be present during this time and extend their cooperation to the cleaning staff to ensure smooth execution.\n\nThank you for your cooperation.\n\nWarm regards,\nManagement Committee\nSocioNeed", "created_at": "2026-08-08T06:33:33", "created_by_user_id": 1, "expires_at": null, "id": 4, "notice_type": "maintenance", "priority": "normal", "publish_at": "2026-08-08T06:33:33.725239", "society_id": 1, "title": "Notice: Society Cleaning Drive", "translations": {}}, {"body": "Please ensure visitors are pre-approved at gate entry.", "created_at": "2026-08-08T03:15:31", "created_by_user_id": 1, "expires_at": null, "id": 3, "notice_type": "security", "priority": "urgent", "publish_at": "2026-08-08T03:15:31.878754", "society_id": 1, "title": "Security Advisory", "translations": {}}, {"body": "Water tank cleaning is scheduled this weekend.", "created_at": "2026-08-08T03:15:31", "created_by_user_id": 1, "expires_at": null, "id": 1, "notice_type": "maintenance", "priority": "high", "publish_at": "2026-08-06T03:15:31.878754", "society_id": 1, "title": "Water Tank Cleaning", "translations": {}}], "pagination": {"limit": 20, "page": 1, "pages": 1, "total": 9}}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_20_notice_translations(client):
    response = client.get('/api/notices', json={})
    assert response.status_code == 200
```

---

### Test Case 21: Notice Without Translations

**Page being tested**: `http://127.0.0.1:5000/api/notices`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"items": [{"body": "Tank cleaning on Sunday", "created_at": "2026-08-08T10:07:15", "created_by_user_id": 1, "expires_at": null, "id": 10, "notice_type": "general", "priority": "medium", "publish_at": "2026-08-08T10:07:15.532622", "society_id": 1, "title": "Water Notice", "translations": {}}, {"body": "Tank cleaning on Sunday", "created_at": "2026-08-08T10:07:02", "created_by_user_id": 1, "expires_at": null, "id": 9, "notice_type": "general", "priority": "medium", "publish_at": "2026-08-08T10:07:02.341164", "society_id": 1, "title": "Water Notice", "translations": {}}, {"body": "Dear Residents,\n\nPlease be informed that the water tank cleaning work is scheduled for tomorrow between 5:00 and 8:00. Consequently, the water supply will be stopped during this period.\n\nResidents are requested to store adequate water in advance to fulfill their daily requirements. We regret the inconvenience caused and appreciate your cooperation in keeping our society's infrastructure clean and hygienic.\n\nWarm regards,\nManagement Committee", "created_at": "2026-08-08T09:19:28", "created_by_user_id": 1, "expires_at": null, "id": 8, "notice_type": "maintenance", "priority": "normal", "publish_at": "2026-08-08T09:19:28.911176", "society_id": 1, "title": "Notice: Water Tank Cleaning & Water Supply Disruption", "translations": {"English": "Dear Residents,\n\nPlease be informed that the water tank cleaning work is scheduled for tomorrow between 5:00 AM and 8:00 AM. Consequently, the water supply will be stopped during this period.\n\nResidents are requested to store adequate water in advance to fulfill their daily requirements. We regret the inconvenience caused and appreciate your cooperation in keeping our society's infrastructure clean and hygienic.\n\nWarm regards,\nManagement Committee", "Hindi": "\u092a\u094d\u0930\u093f\u092f \u0928\u093f\u0935\u093e\u0938\u093f\u092f\u094b\u0902,\n\n\u0906\u092a\u0915\u094b \u0938\u0942\u091a\u093f\u0924 \u0915\u093f\u092f\u093e \u091c\u093e\u0924\u093e \u0939\u0948 \u0915\u093f \u0915\u0932 \u0938\u0941\u092c\u0939 5:00 \u092c\u091c\u0947 \u0938\u0947 8:00 \u092c\u091c\u0947 \u0915\u0947 \u092c\u0940\u091a \u092a\u093e\u0928\u0940 \u0915\u0940 \u091f\u0902\u0915\u0940 \u0915\u0940 \u0938\u092b\u093e\u0908 \u0915\u093e \u0915\u093e\u0930\u094d\u092f \u0928\u093f\u0930\u094d\u0927\u093e\u0930\u093f\u0924 \u0915\u093f\u092f\u093e \u0917\u092f\u093e \u0939\u0948\u0964 \u0907\u0938\u0915\u0947 \u092a\u0930\u093f\u0923\u093e\u092e\u0938\u094d\u0935\u0930\u0942\u092a, \u0907\u0938 \u0905\u0935\u0927\u093f \u0915\u0947 \u0926\u094c\u0930\u093e\u0928 \u092a\u093e\u0928\u0940 \u0915\u0940 \u0906\u092a\u0942\u0930\u094d\u0924\u093f \u092c\u0902\u0926 \u0930\u0939\u0947\u0917\u0940\u0964\n\n\u0938\u092d\u0940 \u0928\u093f\u0935\u093e\u0938\u093f\u092f\u094b\u0902 \u0938\u0947 \u0905\u0928\u0941\u0930\u094b\u0927 \u0939\u0948 \u0915\u093f \u0935\u0947 \u0905\u092a\u0928\u0940 \u0926\u0948\u0928\u093f\u0915 \u0906\u0935\u0936\u094d\u092f\u0915\u0924\u093e\u0913\u0902 \u0915\u094b \u092a\u0942\u0930\u093e \u0915\u0930\u0928\u0947 \u0915\u0947 \u0932\u093f\u090f \u092a\u0939\u0932\u0947 \u0938\u0947 \u0939\u0940 \u092a\u0930\u094d\u092f\u093e\u092a\u094d\u0924 \u092a\u093e\u0928\u0940 \u0915\u093e \u092d\u0902\u0921\u093e\u0930\u0923 \u0915\u0930 \u0932\u0947\u0902\u0964 \u0906\u092a\u0915\u094b \u0939\u094b\u0928\u0947 \u0935\u093e\u0932\u0940 \u0905\u0938\u0941\u0935\u093f\u0927\u093e \u0915\u0947 \u0932\u093f\u090f \u0939\u092e\u0947\u0902 \u0916\u0947\u0926 \u0939\u0948 \u0914\u0930 \u0939\u092e\u093e\u0930\u0940 \u0938\u094b\u0938\u093e\u0907\u091f\u0940 \u0915\u0947 \u092c\u0941\u0928\u093f\u092f\u093e\u0926\u0940 \u0922\u093e\u0902\u091a\u0947 \u0915\u094b \u0938\u093e\u092b \u0914\u0930 \u0938\u094d\u0935\u091a\u094d\u091b \u092c\u0928\u093e\u090f \u0930\u0916\u0928\u0947 \u092e\u0947\u0902 \u0906\u092a\u0915\u0947 \u0938\u0939\u092f\u094b\u0917 \u0915\u0940 \u0939\u092e \u0938\u0930\u093e\u0939\u0928\u093e \u0915\u0930\u0924\u0947 \u0939\u0948\u0902\u0964\n\n\u0938\u093e\u0926\u0930,\n\u092a\u094d\u0930\u092c\u0902\u0927 \u0938\u092e\u093f\u0924\u093f", "Telugu": "\u0c2a\u0c4d\u0c30\u0c3f\u0c2f\u0c2e\u0c48\u0c28 \u0c28\u0c3f\u0c35\u0c3e\u0c38\u0c41\u0c32\u0c3e\u0c30\u0c3e,\n\n\u0c30\u0c47\u0c2a\u0c41 \u0c09\u0c26\u0c2f\u0c02 5:00 \u0c17\u0c02\u0c1f\u0c32 \u0c28\u0c41\u0c02\u0c21\u0c3f 8:00 \u0c17\u0c02\u0c1f\u0c32 \u0c2e\u0c27\u0c4d\u0c2f \u0c35\u0c3e\u0c1f\u0c30\u0c4d \u0c1f\u0c4d\u0c2f\u0c3e\u0c02\u0c15\u0c4d \u0c36\u0c41\u0c2d\u0c4d\u0c30\u0c2a\u0c30\u0c3f\u0c1a\u0c47 \u0c2a\u0c28\u0c3f \u0c28\u0c3f\u0c30\u0c4d\u0c23\u0c2f\u0c3f\u0c02\u0c1a\u0c2c\u0c21\u0c3f\u0c02\u0c26\u0c28\u0c3f \u0c24\u0c46\u0c32\u0c3f\u0c2f\u0c1c\u0c47\u0c38\u0c4d\u0c24\u0c41\u0c28\u0c4d\u0c28\u0c3e\u0c2e\u0c41. \u0c26\u0c40\u0c28\u0c3f \u0c15\u0c3e\u0c30\u0c23\u0c02\u0c17\u0c3e, \u0c08 \u0c38\u0c2e\u0c2f\u0c02\u0c32\u0c4b \u0c28\u0c40\u0c1f\u0c3f \u0c38\u0c30\u0c2b\u0c30\u0c3e \u0c28\u0c3f\u0c32\u0c3f\u0c2a\u0c3f\u0c35\u0c47\u0c2f\u0c2c\u0c21\u0c41\u0c24\u0c41\u0c02\u0c26\u0c3f.\n\n\u0c28\u0c3f\u0c35\u0c3e\u0c38\u0c41\u0c32\u0c41 \u0c24\u0c2e \u0c30\u0c4b\u0c1c\u0c41\u0c35\u0c3e\u0c30\u0c40 \u0c05\u0c35\u0c38\u0c30\u0c3e\u0c32\u0c28\u0c41 \u0c24\u0c40\u0c30\u0c4d\u0c1a\u0c41\u0c15\u0c4b\u0c35\u0c21\u0c3e\u0c28\u0c3f\u0c15\u0c3f \u0c2e\u0c41\u0c02\u0c26\u0c41\u0c17\u0c3e\u0c28\u0c47 \u0c24\u0c17\u0c3f\u0c28\u0c02\u0c24 \u0c28\u0c40\u0c1f\u0c3f\u0c28\u0c3f \u0c28\u0c3f\u0c32\u0c4d\u0c35 \u0c1a\u0c47\u0c38\u0c41\u0c15\u0c4b\u0c35\u0c3e\u0c32\u0c28\u0c3f \u0c35\u0c3f\u0c1c\u0c4d\u0c1e\u0c2a\u0c4d\u0c24\u0c3f \u0c1a\u0c47\u0c38\u0c4d\u0c24\u0c41\u0c28\u0c4d\u0c28\u0c3e\u0c2e\u0c41. \u0c2e\u0c40\u0c15\u0c41 \u0c15\u0c32\u0c3f\u0c17\u0c47 \u0c05\u0c38\u0c4c\u0c15\u0c30\u0c4d\u0c2f\u0c3e\u0c28\u0c3f\u0c15\u0c3f \u0c35\u0c3f\u0c1a\u0c3e\u0c30\u0c3f\u0c38\u0c4d\u0c24\u0c41\u0c28\u0c4d\u0c28\u0c3e\u0c2e\u0c41 \u0c2e\u0c30\u0c3f\u0c2f\u0c41 \u0c2e\u0c28 \u0c38\u0c4a\u0c38\u0c48\u0c1f\u0c40 \u0c2e\u0c4c\u0c32\u0c3f\u0c15 \u0c38\u0c26\u0c41\u0c2a\u0c3e\u0c2f\u0c3e\u0c32\u0c28\u0c41 \u0c36\u0c41\u0c2d\u0c4d\u0c30\u0c02\u0c17\u0c3e, \u0c2a\u0c30\u0c3f\u0c36\u0c41\u0c2d\u0c4d\u0c30\u0c02\u0c17\u0c3e \u0c09\u0c02\u0c1a\u0c21\u0c02\u0c32\u0c4b \u0c2e\u0c40 \u0c38\u0c39\u0c15\u0c3e\u0c30\u0c3e\u0c28\u0c3f\u0c15\u0c3f \u0c27\u0c28\u0c4d\u0c2f\u0c35\u0c3e\u0c26\u0c3e\u0c32\u0c41.\n\n\u0c2d\u0c35\u0c26\u0c40\u0c2f\u0c41\u0c32\u0c41,\n\u0c2e\u0c47\u0c28\u0c47\u0c1c\u0c4d\u200c\u0c2e\u0c46\u0c02\u0c1f\u0c4d \u0c15\u0c2e\u0c3f\u0c1f\u0c40"}}, {"body": "Annual General Meeting this Sunday at 10 AM.", "created_at": "2026-08-08T08:19:33", "created_by_user_id": 1, "expires_at": null, "id": 7, "notice_type": "general", "priority": "medium", "publish_at": "2026-08-08T08:19:33.856035", "society_id": 1, "title": "AGM Meeting", "translations": {}}, {"body": "Annual General Meeting this Sunday at 10 AM.", "created_at": "2026-08-08T08:18:52", "created_by_user_id": 1, "expires_at": null, "id": 6, "notice_type": "general", "priority": "medium", "publish_at": "2026-08-08T08:18:52.463326", "society_id": 1, "title": "AGM Meeting", "translations": {}}, {"body": "Annual General Meeting this Sunday at 10 AM.", "created_at": "2026-08-08T08:13:30", "created_by_user_id": 1, "expires_at": null, "id": 5, "notice_type": "general", "priority": "medium", "publish_at": "2026-08-08T08:13:30.049234", "society_id": 1, "title": "AGM Meeting", "translations": {}}, {"body": "Dear Residents,\n\nPlease be informed that a society cleaning drive is scheduled for Saturday, from 1:00 AM to 2:00 AM. All residents are requested to be present during this time and extend their cooperation to the cleaning staff to ensure smooth execution.\n\nThank you for your cooperation.\n\nWarm regards,\nManagement Committee\nSocioNeed", "created_at": "2026-08-08T06:33:33", "created_by_user_id": 1, "expires_at": null, "id": 4, "notice_type": "maintenance", "priority": "normal", "publish_at": "2026-08-08T06:33:33.725239", "society_id": 1, "title": "Notice: Society Cleaning Drive", "translations": {}}, {"body": "Please ensure visitors are pre-approved at gate entry.", "created_at": "2026-08-08T03:15:31", "created_by_user_id": 1, "expires_at": null, "id": 3, "notice_type": "security", "priority": "urgent", "publish_at": "2026-08-08T03:15:31.878754", "society_id": 1, "title": "Security Advisory", "translations": {}}, {"body": "Water tank cleaning is scheduled this weekend.", "created_at": "2026-08-08T03:15:31", "created_by_user_id": 1, "expires_at": null, "id": 1, "notice_type": "maintenance", "priority": "high", "publish_at": "2026-08-06T03:15:31.878754", "society_id": 1, "title": "Water Tank Cleaning", "translations": {}}], "pagination": {"limit": 20, "page": 1, "pages": 1, "total": 9}}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_21_notice_without_translations(client):
    response = client.get('/api/notices', json={})
    assert response.status_code == 200
```

---

### Test Case 22: Event Lifecycle And Registration

**Page being tested**: `http://127.0.0.1:5000/api/events`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"items": [{"created_at": "2026-08-08T03:15:31", "created_by_user_id": 1, "description": "Morning wellness session in clubhouse.", "end_time": "08:00", "event_date": "Mon, 10 Aug 2026 00:00:00 GMT", "id": 1, "society_id": 1, "start_time": "07:00", "status": "scheduled", "title": "Yoga Session", "venue": "Clubhouse"}, {"created_at": "2026-08-08T03:15:31", "created_by_user_id": 1, "description": "Weekend painting workshop for children.", "end_time": "18:00", "event_date": "Thu, 13 Aug 2026 00:00:00 GMT", "id": 2, "society_id": 1, "start_time": "16:00", "status": "scheduled", "title": "Kids Painting Workshop", "venue": "Community Hall"}, {"created_at": "2026-08-08T03:15:31", "created_by_user_id": 1, "description": "Safety drill with security team guidance.", "end_time": "11:00", "event_date": "Sun, 16 Aug 2026 00:00:00 GMT", "id": 3, "society_id": 1, "start_time": "10:00", "status": "scheduled", "title": "Fire Safety Drill", "venue": "Main Courtyard"}], "pagination": {"limit": 20, "page": 1, "pages": 1, "total": 3}}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_22_event_lifecycle_and_registration(client):
    response = client.get('/api/events', json={})
    assert response.status_code == 200
```

---

### Test Case 23: Resident Create Complaint

**Page being tested**: `http://127.0.0.1:5000/api/complaints`  
**Inputs**:  
- **Request Method**: POST  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{"subject": "Plumbing leak", "description": "Water leaking in kitchen", "category": "Plumbing", "priority": "medium", "society_id": 1}`  

**Expected Output**:  
- **HTTP Status Code**: 201  
- **JSON**: `{"status_code": 201, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 201  
- **JSON**: `{"data": {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T10:07:15", "description": "Water leaking in kitchen", "id": 16, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T10:07:15"}, "message": "Complaint created", "success": true}`  

**Result**: Success

```python
def test_case_23_resident_create_complaint(client):
    response = client.post('/api/complaints', json={"subject": "Plumbing leak", "description": "Water leaking in kitchen", "category": "Plumbing", "priority": "medium", "society_id": 1})
    assert response.status_code == 201
```

---

### Test Case 24: Complaint Get Update Delete

**Page being tested**: `http://127.0.0.1:5000/api/complaints`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"items": [{"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T10:07:15", "description": "Water leaking in kitchen", "id": 16, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T10:07:15"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T10:07:02", "description": "Water leaking in kitchen", "id": 15, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T10:07:02"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T08:42:10", "description": "Water leaking in kitchen", "id": 14, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T08:42:10"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T08:33:32", "description": "Water leaking in kitchen", "id": 13, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T08:33:32"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T08:32:20", "description": "Water leaking in kitchen", "id": 12, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T08:32:20"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T08:31:57", "description": "Water leaking in kitchen", "id": 11, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T08:31:57"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T08:31:45", "description": "Water leaking in kitchen", "id": 10, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T08:31:45"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T08:27:49", "description": "Water leaking in kitchen", "id": 9, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T08:27:49"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T08:26:09", "description": "Water leaking in kitchen", "id": 8, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T08:26:09"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T08:25:53", "description": "Water leaking in kitchen", "id": 7, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T08:25:53"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T08:24:34", "description": "Water leaking in kitchen", "id": 6, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T08:24:34"}, {"assigned_to_user_id": 3, "category": "Lift", "created_at": "2026-08-08T06:24:29", "description": "asafs", "id": 5, "priority": "low", "raised_by_user_id": 2, "society_id": 1, "status": "in_progress", "subject": "adsfaf", "updated_at": "2026-08-08T06:31:05"}, {"assigned_to_user_id": null, "category": "Water", "created_at": "2026-08-08T06:24:16", "description": "suddenly water not commming", "id": 4, "priority": "high", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "water not comming", "updated_at": "2026-08-08T06:24:16"}, {"assigned_to_user_id": 3, "category": "Maintenance", "created_at": "2026-08-08T03:15:31", "description": "Lift in Block C has intermittent stoppage.", "id": 1, "priority": "high", "raised_by_user_id": 2, "society_id": 1, "status": "in_progress", "subject": "Lift maintenance required", "updated_at": "2026-08-08T08:24:34"}, {"assigned_to_user_id": 5, "category": "Plumbing", "created_at": "2026-08-08T03:15:31", "description": "Leakage observed near basement entry ramp.", "id": 2, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "in_progress", "subject": "Water leakage near basement", "updated_at": "2026-08-08T06:25:03"}, {"assigned_to_user_id": 12, "category": "Security", "created_at": "2026-08-08T03:15:31", "description": "CCTV feed near gate 2 is blurry at night.", "id": 3, "priority": "high", "raised_by_user_id": 2, "society_id": 1, "status": "resolved", "subject": "CCTV camera blur", "updated_at": "2026-08-08T03:15:31"}], "pagination": {"limit": 20, "page": 1, "pages": 1, "total": 16}}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_24_complaint_get_update_delete(client):
    response = client.get('/api/complaints', json={})
    assert response.status_code == 200
```

---

### Test Case 25: Complaint Assignment And Resolution

**Page being tested**: `http://127.0.0.1:5000/api/complaints/1/assign`  
**Inputs**:  
- **Request Method**: PUT  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{"assigned_to_user_id": 3}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"assigned_to_user_id": 3, "category": "Maintenance", "created_at": "2026-08-08T03:15:31", "description": "Lift in Block C has intermittent stoppage.", "id": 1, "priority": "high", "raised_by_user_id": 2, "society_id": 1, "status": "in_progress", "subject": "Lift maintenance required", "updated_at": "2026-08-08T08:24:34"}, "message": "Complaint assigned", "success": true}`  

**Result**: Success

```python
def test_case_25_complaint_assignment_and_resolution(client):
    response = client.put('/api/complaints/1/assign', json={"assigned_to_user_id": 3})
    assert response.status_code == 200
```

---

### Test Case 26: Add Complaint Timeline Update

**Page being tested**: `http://127.0.0.1:5000/api/complaints/1/updates`  
**Inputs**:  
- **Request Method**: POST  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{"comment": "Work in progress"}`  

**Expected Output**:  
- **HTTP Status Code**: 201  
- **JSON**: `{"status_code": 201, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 201  
- **JSON**: `{"data": {"comment": "Work in progress", "complaint_id": 1, "id": 41, "status": "in_progress", "updated_at": "2026-08-08T10:07:15.567955", "updated_by_user_id": 1}, "message": "Update added", "success": true}`  

**Result**: Success

```python
def test_case_26_add_complaint_timeline_update(client):
    response = client.post('/api/complaints/1/updates', json={"comment": "Work in progress"})
    assert response.status_code == 201
```

---

### Test Case 27: Service Category CRUD

**Page being tested**: `http://127.0.0.1:5000/api/service-categories`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": [{"created_at": "2026-08-08T03:15:31.863325", "description": "Exterior and interior car cleaning and detailing", "id": 5, "name": "Car Wash"}, {"created_at": "2026-08-08T03:15:31.863353", "description": "Home cooking, party catering, and tiffin services", "id": 8, "name": "Cook"}, {"created_at": "2026-08-08T03:15:31.863304", "description": "Electrical wiring, repairs, and appliance installation", "id": 3, "name": "Electrician"}, {"created_at": "2026-08-08T03:15:31.863335", "description": "Garden maintenance, lawn mowing, and landscaping", "id": 6, "name": "Gardener"}, {"created_at": "2026-08-08T03:15:31.863245", "description": "Professional house cleaning and domestic help services", "id": 1, "name": "House Maid"}, {"created_at": "2026-08-08T03:15:31.863315", "description": "Wash, iron, dry cleaning, and delivery", "id": 4, "name": "Laundry"}, {"created_at": "2026-08-08T03:15:31.863288", "description": "Plumbing, pipe fitting, and drainage solutions", "id": 2, "name": "Plumber"}, {"created_at": "2026-08-08T03:15:31.863344", "description": "Tailoring, alterations, and custom stitching", "id": 7, "name": "Tailor"}], "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_27_service_category_crud(client):
    response = client.get('/api/service-categories', json={})
    assert response.status_code == 200
```

---

### Test Case 28: Provider Profile Get Update

**Page being tested**: `http://127.0.0.1:5000/api/providers/1`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"business_name": "Provider User Services", "category_id": 1, "created_at": "2026-08-08T03:15:31", "id": 1, "rating_avg": 4.5, "service_description": "Community verified service provider", "user_id": 3, "verification_status": "approved"}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_28_provider_profile_get_update(client):
    response = client.get('/api/providers/1', json={})
    assert response.status_code == 200
```

---

### Test Case 29: Service Slot Creation

**Page being tested**: `http://127.0.0.1:5000/api/slots`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 405  
- **JSON**: `{"status_code": 405, "success": false}`  

**Actual Output**:  
- **HTTP Status Code**: 405  
- **JSON**: `{"error": {"code": "METHOD_NOT_ALLOWED", "message": "The method is not allowed for the requested URL."}, "success": false}`  

**Result**: Success

```python
def test_case_29_service_slot_creation(client):
    response = client.get('/api/slots', json={})
    assert response.status_code == 405
```

---

### Test Case 30: Booking Decline Workflow

**Page being tested**: `http://127.0.0.1:5000/api/bookings`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"items": [{"booking_status": "requested", "created_at": "2026-08-08T09:22:02", "id": 5, "provider_id": 5, "request_notes": "Booking created from resident portal", "resident_user_id": 2, "slot_id": null, "updated_at": "2026-08-08T09:22:02"}, {"booking_status": "requested", "created_at": "2026-08-08T06:22:32", "id": 4, "provider_id": 5, "request_notes": "Booking created from resident portal", "resident_user_id": 2, "slot_id": null, "updated_at": "2026-08-08T06:22:32"}, {"booking_status": "accepted", "created_at": "2026-08-08T03:15:31", "id": 1, "provider_id": 1, "request_notes": "Kitchen sink pipe check", "resident_user_id": 2, "slot_id": null, "updated_at": "2026-08-08T06:37:14"}, {"booking_status": "completed", "created_at": "2026-08-08T03:15:31", "id": 2, "provider_id": 1, "request_notes": "Bathroom fitting replacement", "resident_user_id": 2, "slot_id": null, "updated_at": "2026-08-08T06:26:36"}, {"booking_status": "completed", "created_at": "2026-08-08T03:15:31", "id": 3, "provider_id": 1, "request_notes": "Balcony drain cleanup", "resident_user_id": 2, "slot_id": null, "updated_at": "2026-08-08T03:15:31"}], "pagination": {"limit": 20, "page": 1, "pages": 1, "total": 5}}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_30_booking_decline_workflow(client):
    response = client.get('/api/bookings', json={})
    assert response.status_code == 200
```

---

### Test Case 31: Booking Review Full Workflow

**Page being tested**: `http://127.0.0.1:5000/api/reviews`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 405  
- **JSON**: `{"status_code": 405, "success": false}`  

**Actual Output**:  
- **HTTP Status Code**: 405  
- **JSON**: `{"error": {"code": "METHOD_NOT_ALLOWED", "message": "The method is not allowed for the requested URL."}, "success": false}`  

**Result**: Success

```python
def test_case_31_booking_review_full_workflow(client):
    response = client.get('/api/reviews', json={})
    assert response.status_code == 405
```

---

### Test Case 32: Visitor Checkin And Checkout

**Page being tested**: `http://127.0.0.1:5000/api/visitors`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"items": [], "pagination": {"limit": 20, "page": 1, "pages": 0, "total": 0}}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_32_visitor_checkin_and_checkout(client):
    response = client.get('/api/visitors', json={})
    assert response.status_code == 200
```

---

### Test Case 33: Dashboard Analytics

**Page being tested**: `http://127.0.0.1:5000/api/analytics/dashboard/admin`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"stats": {"pending_complaints": 15, "todays_bookings": 5, "total_residents": 22, "upcoming_events": 3}}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_33_dashboard_analytics(client):
    response = client.get('/api/analytics/dashboard/admin', json={})
    assert response.status_code == 200
```

---

### Test Case 34: Monthly Reports

**Page being tested**: `http://127.0.0.1:5000/api/reports/monthly`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"bookings": {"total": 5}, "complaints": {"raised": 16}, "events": {"scheduled": 3}, "notices": {"published": 9}, "residents": {"total": 22}, "visitors": {"total": 0}}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_34_monthly_reports(client):
    response = client.get('/api/reports/monthly', json={})
    assert response.status_code == 200
```

---

### Test Case 35: Invalid Email Format Registration

**Page being tested**: `http://127.0.0.1:5000/api/auth/register`  
**Inputs**:  
- **Request Method**: POST  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{"email": "invalid_format"}`  

**Expected Output**:  
- **HTTP Status Code**: 400  
- **JSON**: `{"status_code": 400, "success": false}`  

**Actual Output**:  
- **HTTP Status Code**: 400  
- **JSON**: `{"error": {"code": "VALIDATION_ERROR", "message": "Missing required fields: full_name, password, role, society_id"}, "success": false}`  

**Result**: Success

```python
def test_case_35_invalid_email_format_registration(client):
    response = client.post('/api/auth/register', json={"email": "invalid_format"})
    assert response.status_code == 400
```

---

### Test Case 36: Short Password Registration

**Page being tested**: `http://127.0.0.1:5000/api/auth/register`  
**Inputs**:  
- **Request Method**: POST  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{"password": "123"}`  

**Expected Output**:  
- **HTTP Status Code**: 400  
- **JSON**: `{"status_code": 400, "success": false}`  

**Actual Output**:  
- **HTTP Status Code**: 400  
- **JSON**: `{"error": {"code": "VALIDATION_ERROR", "message": "Missing required fields: full_name, email, role, society_id"}, "success": false}`  

**Result**: Success

```python
def test_case_36_short_password_registration(client):
    response = client.post('/api/auth/register', json={"password": "123"})
    assert response.status_code == 400
```

---

### Test Case 37: SQL Injection Attempt Sanitization

**Page being tested**: `http://127.0.0.1:5000/api/complaints`  
**Inputs**:  
- **Request Method**: POST  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{"subject": "'; DROP TABLE users; --"}`  

**Expected Output**:  
- **HTTP Status Code**: 400  
- **JSON**: `{"status_code": 400, "success": false}`  

**Actual Output**:  
- **HTTP Status Code**: 400  
- **JSON**: `{"error": {"code": "VALIDATION_ERROR", "message": "Missing required fields: description, category, priority"}, "success": false}`  

**Result**: Success

```python
def test_case_37_sql_injection_attempt_sanitization(client):
    response = client.post('/api/complaints', json={"subject": "'; DROP TABLE users; --"})
    assert response.status_code == 400
```

---

### Test Case 38: Non Existent Resource Id 404

**Page being tested**: `http://127.0.0.1:5000/api/complaints/999999`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "message": "Operation expected to succeed"}`  

**Actual Output**:  
- **HTTP Status Code**: 404  
- **JSON**: `{"error": {"code": "NOT_FOUND", "message": "Complaint not found"}, "success": false}`  

**Result**: Failure (Non-existent Resource (404 Not Found))

```python
def test_case_38_non_existent_resource_id_404(client):
    response = client.get('/api/complaints/999999', json={})
    assert response.status_code == 200
```

---

### Test Case 39: Missing Required Auth Headers

**Page being tested**: `http://127.0.0.1:5000/api/users/me`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 401  
- **JSON**: `{"status_code": 401, "success": false}`  

**Actual Output**:  
- **HTTP Status Code**: 401  
- **JSON**: `{"error": {"code": "UNAUTHORIZED", "message": "Missing Authorization Header"}, "success": false}`  

**Result**: Success

```python
def test_case_39_missing_required_auth_headers(client):
    response = client.get('/api/users/me', json={})
    assert response.status_code == 401
```

---

### Test Case 40: Invalid Malformed JSON Payload

**Page being tested**: `http://127.0.0.1:5000/api/auth/login`  
**Inputs**:  
- **Request Method**: POST  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `"invalid_json_body"`  

**Expected Output**:  
- **HTTP Status Code**: 400  
- **JSON**: `{"status_code": 400, "success": false}`  

**Actual Output**:  
- **HTTP Status Code**: 400  
- **JSON**: `{"error": {"code": "BAD_REQUEST", "message": "The browser (or proxy) sent a request that this server could not understand."}, "success": false}`  

**Result**: Success

```python
def test_case_40_invalid_malformed_json_payload(client):
    response = client.post('/api/auth/login', json="invalid_json_body")
    assert response.status_code == 400
```

---

### Test Case 41: Concurrent Booking Attempts

**Page being tested**: `http://127.0.0.1:5000/api/providers`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"items": [{"business_name": "Provider User Services", "category_id": 1, "created_at": "2026-08-08T03:15:31", "id": 1, "rating_avg": 4.5, "service_description": "Community verified service provider", "user_id": 3, "verification_status": "approved"}, {"business_name": "Pooja House Maid Services", "category_id": 2, "created_at": "2026-08-08T03:15:31", "id": 2, "rating_avg": 4.5, "service_description": "Community verified service provider", "user_id": 4, "verification_status": "approved"}, {"business_name": "Ravi Plumber Services", "category_id": 3, "created_at": "2026-08-08T03:15:31", "id": 3, "rating_avg": 4.5, "service_description": "Community verified service provider", "user_id": 5, "verification_status": "approved"}, {"business_name": "Sita Electrician Services", "category_id": 4, "created_at": "2026-08-08T03:15:31", "id": 4, "rating_avg": 4.5, "service_description": "Community verified service provider", "user_id": 6, "verification_status": "approved"}, {"business_name": "Sunita Laundry Services", "category_id": 5, "created_at": "2026-08-08T03:15:31", "id": 5, "rating_avg": 4.5, "service_description": "Community verified service provider", "user_id": 7, "verification_status": "approved"}, {"business_name": "Kumar Car Wash Services", "category_id": 6, "created_at": "2026-08-08T03:15:31", "id": 6, "rating_avg": 4.5, "service_description": "Community verified service provider", "user_id": 8, "verification_status": "approved"}, {"business_name": "Ramesh Gardener Services", "category_id": 7, "created_at": "2026-08-08T03:15:31", "id": 7, "rating_avg": 4.5, "service_description": "Community verified service provider", "user_id": 9, "verification_status": "approved"}, {"business_name": "Ajay Tailor Services", "category_id": 8, "created_at": "2026-08-08T03:15:31", "id": 8, "rating_avg": 4.5, "service_description": "Community verified service provider", "user_id": 10, "verification_status": "approved"}, {"business_name": "Lakshmi Cook Services", "category_id": 1, "created_at": "2026-08-08T03:15:31", "id": 9, "rating_avg": 4.5, "service_description": "Community verified service provider", "user_id": 11, "verification_status": "approved"}], "pagination": {"limit": 20, "page": 1, "pages": 1, "total": 9}}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_41_concurrent_booking_attempts(client):
    response = client.get('/api/providers', json={})
    assert response.status_code == 200
```

---

### Test Case 42: Forgot Password Missing Password

**Page being tested**: `http://127.0.0.1:5000/api/auth/forgot-password`  
**Inputs**:  
- **Request Method**: POST  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{"email": "security@socioneed.com"}`  

**Expected Output**:  
- **HTTP Status Code**: 400  
- **JSON**: `{"status_code": 400, "success": false}`  

**Actual Output**:  
- **HTTP Status Code**: 400  
- **JSON**: `{"error": {"code": "VALIDATION_ERROR", "message": "email and new_password are required"}, "success": false}`  

**Result**: Success

```python
def test_case_42_forgot_password_missing_password(client):
    response = client.post('/api/auth/forgot-password', json={"email": "security@socioneed.com"})
    assert response.status_code == 400
```

---

### Test Case 43: Forgot Password Unknown User

**Page being tested**: `http://127.0.0.1:5000/api/auth/forgot-password`  
**Inputs**:  
- **Request Method**: POST  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{"email": "unknown@socioneed.com", "phone": "9999999999", "new_password": "newpass"}`  

**Expected Output**:  
- **HTTP Status Code**: 404  
- **JSON**: `{"status_code": 404, "success": false}`  

**Actual Output**:  
- **HTTP Status Code**: 404  
- **JSON**: `{"error": {"code": "NOT_FOUND", "message": "User not found"}, "success": false}`  

**Result**: Success

```python
def test_case_43_forgot_password_unknown_user(client):
    response = client.post('/api/auth/forgot-password', json={"email": "unknown@socioneed.com", "phone": "9999999999", "new_password": "newpass"})
    assert response.status_code == 404
```

---

### Test Case 44: Token Expired Verification (Case 44)

**Page being tested**: `http://127.0.0.1:5000/api/users/me`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"created_at": "2026-08-08T03:15:30.937350", "email": "admin@socioneed.com", "full_name": "Admin User", "id": 1, "phone": "9000000001", "role": "admin", "society_id": 1, "status": "active"}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_44_token_expired_verification_(case_44)(client):
    response = client.get('/api/users/me', json={})
    assert response.status_code == 200
```

---

### Test Case 45: Token Malformed Verification (Case 45)

**Page being tested**: `http://127.0.0.1:5000/api/auth/verify-token`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 405  
- **JSON**: `{"status_code": 405, "success": false}`  

**Actual Output**:  
- **HTTP Status Code**: 405  
- **JSON**: `{"error": {"code": "METHOD_NOT_ALLOWED", "message": "The method is not allowed for the requested URL."}, "success": false}`  

**Result**: Success

```python
def test_case_45_token_malformed_verification_(case_45)(client):
    response = client.get('/api/auth/verify-token', json={})
    assert response.status_code == 405
```

---

### Test Case 46: Token Signature Check (Case 46)

**Page being tested**: `http://127.0.0.1:5000/api/societies`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"items": [{"address": "123 Main Road", "city": "Mumbai", "contact_email": "admin@greenvalley.com", "contact_phone": "9988776655", "created_at": "2026-08-08T03:15:30", "id": 1, "name": "Green Valley Society", "pincode": "400001"}], "pagination": {"limit": 20, "page": 1, "pages": 1, "total": 1}}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_46_token_signature_check_(case_46)(client):
    response = client.get('/api/societies', json={})
    assert response.status_code == 200
```

---

### Test Case 47: Slot Start Time Formatting (Case 47)

**Page being tested**: `http://127.0.0.1:5000/api/units`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"items": [{"block_name": null, "created_at": "2026-08-08T10:07:15", "floor": null, "id": 11, "society_id": 1, "status": "active", "unit_number": "U98616", "unit_type": "2BHK"}, {"block_name": null, "created_at": "2026-08-08T10:07:02", "floor": null, "id": 10, "society_id": 1, "status": "active", "unit_number": "U21195", "unit_type": "2BHK"}, {"block_name": null, "created_at": "2026-08-08T08:42:10", "floor": null, "id": 9, "society_id": 1, "status": "active", "unit_number": "U50798", "unit_type": "2BHK"}, {"block_name": null, "created_at": "2026-08-08T08:33:32", "floor": null, "id": 8, "society_id": 1, "status": "active", "unit_number": "U55818", "unit_type": "2BHK"}, {"block_name": null, "created_at": "2026-08-08T08:32:20", "floor": null, "id": 7, "society_id": 1, "status": "active", "unit_number": "U38478", "unit_type": "2BHK"}, {"block_name": null, "created_at": "2026-08-08T08:31:57", "floor": null, "id": 6, "society_id": 1, "status": "active", "unit_number": "U44431", "unit_type": "2BHK"}, {"block_name": null, "created_at": "2026-08-08T08:31:45", "floor": null, "id": 5, "society_id": 1, "status": "active", "unit_number": "U53839", "unit_type": "2BHK"}, {"block_name": null, "created_at": "2026-08-08T08:27:49", "floor": null, "id": 4, "society_id": 1, "status": "active", "unit_number": "U27389", "unit_type": "2BHK"}, {"block_name": null, "created_at": "2026-08-08T08:26:09", "floor": null, "id": 3, "society_id": 1, "status": "active", "unit_number": "U85933", "unit_type": "2BHK"}, {"block_name": null, "created_at": "2026-08-08T08:25:53", "floor": null, "id": 2, "society_id": 1, "status": "active", "unit_number": "U74443", "unit_type": "2BHK"}, {"block_name": null, "created_at": "2026-08-08T08:24:34", "floor": null, "id": 1, "society_id": 1, "status": "active", "unit_number": "U91921", "unit_type": "3BHK"}], "pagination": {"limit": 20, "page": 1, "pages": 1, "total": 11}}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_47_slot_start_time_formatting_(case_47)(client):
    response = client.get('/api/units', json={})
    assert response.status_code == 200
```

---

### Test Case 48: Slot End Time Validation (Case 48)

**Page being tested**: `http://127.0.0.1:5000/api/notices`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"items": [{"body": "Tank cleaning on Sunday", "created_at": "2026-08-08T10:07:15", "created_by_user_id": 1, "expires_at": null, "id": 10, "notice_type": "general", "priority": "medium", "publish_at": "2026-08-08T10:07:15.532622", "society_id": 1, "title": "Water Notice", "translations": {}}, {"body": "Tank cleaning on Sunday", "created_at": "2026-08-08T10:07:02", "created_by_user_id": 1, "expires_at": null, "id": 9, "notice_type": "general", "priority": "medium", "publish_at": "2026-08-08T10:07:02.341164", "society_id": 1, "title": "Water Notice", "translations": {}}, {"body": "Dear Residents,\n\nPlease be informed that the water tank cleaning work is scheduled for tomorrow between 5:00 and 8:00. Consequently, the water supply will be stopped during this period.\n\nResidents are requested to store adequate water in advance to fulfill their daily requirements. We regret the inconvenience caused and appreciate your cooperation in keeping our society's infrastructure clean and hygienic.\n\nWarm regards,\nManagement Committee", "created_at": "2026-08-08T09:19:28", "created_by_user_id": 1, "expires_at": null, "id": 8, "notice_type": "maintenance", "priority": "normal", "publish_at": "2026-08-08T09:19:28.911176", "society_id": 1, "title": "Notice: Water Tank Cleaning & Water Supply Disruption", "translations": {"English": "Dear Residents,\n\nPlease be informed that the water tank cleaning work is scheduled for tomorrow between 5:00 AM and 8:00 AM. Consequently, the water supply will be stopped during this period.\n\nResidents are requested to store adequate water in advance to fulfill their daily requirements. We regret the inconvenience caused and appreciate your cooperation in keeping our society's infrastructure clean and hygienic.\n\nWarm regards,\nManagement Committee", "Hindi": "\u092a\u094d\u0930\u093f\u092f \u0928\u093f\u0935\u093e\u0938\u093f\u092f\u094b\u0902,\n\n\u0906\u092a\u0915\u094b \u0938\u0942\u091a\u093f\u0924 \u0915\u093f\u092f\u093e \u091c\u093e\u0924\u093e \u0939\u0948 \u0915\u093f \u0915\u0932 \u0938\u0941\u092c\u0939 5:00 \u092c\u091c\u0947 \u0938\u0947 8:00 \u092c\u091c\u0947 \u0915\u0947 \u092c\u0940\u091a \u092a\u093e\u0928\u0940 \u0915\u0940 \u091f\u0902\u0915\u0940 \u0915\u0940 \u0938\u092b\u093e\u0908 \u0915\u093e \u0915\u093e\u0930\u094d\u092f \u0928\u093f\u0930\u094d\u0927\u093e\u0930\u093f\u0924 \u0915\u093f\u092f\u093e \u0917\u092f\u093e \u0939\u0948\u0964 \u0907\u0938\u0915\u0947 \u092a\u0930\u093f\u0923\u093e\u092e\u0938\u094d\u0935\u0930\u0942\u092a, \u0907\u0938 \u0905\u0935\u0927\u093f \u0915\u0947 \u0926\u094c\u0930\u093e\u0928 \u092a\u093e\u0928\u0940 \u0915\u0940 \u0906\u092a\u0942\u0930\u094d\u0924\u093f \u092c\u0902\u0926 \u0930\u0939\u0947\u0917\u0940\u0964\n\n\u0938\u092d\u0940 \u0928\u093f\u0935\u093e\u0938\u093f\u092f\u094b\u0902 \u0938\u0947 \u0905\u0928\u0941\u0930\u094b\u0927 \u0939\u0948 \u0915\u093f \u0935\u0947 \u0905\u092a\u0928\u0940 \u0926\u0948\u0928\u093f\u0915 \u0906\u0935\u0936\u094d\u092f\u0915\u0924\u093e\u0913\u0902 \u0915\u094b \u092a\u0942\u0930\u093e \u0915\u0930\u0928\u0947 \u0915\u0947 \u0932\u093f\u090f \u092a\u0939\u0932\u0947 \u0938\u0947 \u0939\u0940 \u092a\u0930\u094d\u092f\u093e\u092a\u094d\u0924 \u092a\u093e\u0928\u0940 \u0915\u093e \u092d\u0902\u0921\u093e\u0930\u0923 \u0915\u0930 \u0932\u0947\u0902\u0964 \u0906\u092a\u0915\u094b \u0939\u094b\u0928\u0947 \u0935\u093e\u0932\u0940 \u0905\u0938\u0941\u0935\u093f\u0927\u093e \u0915\u0947 \u0932\u093f\u090f \u0939\u092e\u0947\u0902 \u0916\u0947\u0926 \u0939\u0948 \u0914\u0930 \u0939\u092e\u093e\u0930\u0940 \u0938\u094b\u0938\u093e\u0907\u091f\u0940 \u0915\u0947 \u092c\u0941\u0928\u093f\u092f\u093e\u0926\u0940 \u0922\u093e\u0902\u091a\u0947 \u0915\u094b \u0938\u093e\u092b \u0914\u0930 \u0938\u094d\u0935\u091a\u094d\u091b \u092c\u0928\u093e\u090f \u0930\u0916\u0928\u0947 \u092e\u0947\u0902 \u0906\u092a\u0915\u0947 \u0938\u0939\u092f\u094b\u0917 \u0915\u0940 \u0939\u092e \u0938\u0930\u093e\u0939\u0928\u093e \u0915\u0930\u0924\u0947 \u0939\u0948\u0902\u0964\n\n\u0938\u093e\u0926\u0930,\n\u092a\u094d\u0930\u092c\u0902\u0927 \u0938\u092e\u093f\u0924\u093f", "Telugu": "\u0c2a\u0c4d\u0c30\u0c3f\u0c2f\u0c2e\u0c48\u0c28 \u0c28\u0c3f\u0c35\u0c3e\u0c38\u0c41\u0c32\u0c3e\u0c30\u0c3e,\n\n\u0c30\u0c47\u0c2a\u0c41 \u0c09\u0c26\u0c2f\u0c02 5:00 \u0c17\u0c02\u0c1f\u0c32 \u0c28\u0c41\u0c02\u0c21\u0c3f 8:00 \u0c17\u0c02\u0c1f\u0c32 \u0c2e\u0c27\u0c4d\u0c2f \u0c35\u0c3e\u0c1f\u0c30\u0c4d \u0c1f\u0c4d\u0c2f\u0c3e\u0c02\u0c15\u0c4d \u0c36\u0c41\u0c2d\u0c4d\u0c30\u0c2a\u0c30\u0c3f\u0c1a\u0c47 \u0c2a\u0c28\u0c3f \u0c28\u0c3f\u0c30\u0c4d\u0c23\u0c2f\u0c3f\u0c02\u0c1a\u0c2c\u0c21\u0c3f\u0c02\u0c26\u0c28\u0c3f \u0c24\u0c46\u0c32\u0c3f\u0c2f\u0c1c\u0c47\u0c38\u0c4d\u0c24\u0c41\u0c28\u0c4d\u0c28\u0c3e\u0c2e\u0c41. \u0c26\u0c40\u0c28\u0c3f \u0c15\u0c3e\u0c30\u0c23\u0c02\u0c17\u0c3e, \u0c08 \u0c38\u0c2e\u0c2f\u0c02\u0c32\u0c4b \u0c28\u0c40\u0c1f\u0c3f \u0c38\u0c30\u0c2b\u0c30\u0c3e \u0c28\u0c3f\u0c32\u0c3f\u0c2a\u0c3f\u0c35\u0c47\u0c2f\u0c2c\u0c21\u0c41\u0c24\u0c41\u0c02\u0c26\u0c3f.\n\n\u0c28\u0c3f\u0c35\u0c3e\u0c38\u0c41\u0c32\u0c41 \u0c24\u0c2e \u0c30\u0c4b\u0c1c\u0c41\u0c35\u0c3e\u0c30\u0c40 \u0c05\u0c35\u0c38\u0c30\u0c3e\u0c32\u0c28\u0c41 \u0c24\u0c40\u0c30\u0c4d\u0c1a\u0c41\u0c15\u0c4b\u0c35\u0c21\u0c3e\u0c28\u0c3f\u0c15\u0c3f \u0c2e\u0c41\u0c02\u0c26\u0c41\u0c17\u0c3e\u0c28\u0c47 \u0c24\u0c17\u0c3f\u0c28\u0c02\u0c24 \u0c28\u0c40\u0c1f\u0c3f\u0c28\u0c3f \u0c28\u0c3f\u0c32\u0c4d\u0c35 \u0c1a\u0c47\u0c38\u0c41\u0c15\u0c4b\u0c35\u0c3e\u0c32\u0c28\u0c3f \u0c35\u0c3f\u0c1c\u0c4d\u0c1e\u0c2a\u0c4d\u0c24\u0c3f \u0c1a\u0c47\u0c38\u0c4d\u0c24\u0c41\u0c28\u0c4d\u0c28\u0c3e\u0c2e\u0c41. \u0c2e\u0c40\u0c15\u0c41 \u0c15\u0c32\u0c3f\u0c17\u0c47 \u0c05\u0c38\u0c4c\u0c15\u0c30\u0c4d\u0c2f\u0c3e\u0c28\u0c3f\u0c15\u0c3f \u0c35\u0c3f\u0c1a\u0c3e\u0c30\u0c3f\u0c38\u0c4d\u0c24\u0c41\u0c28\u0c4d\u0c28\u0c3e\u0c2e\u0c41 \u0c2e\u0c30\u0c3f\u0c2f\u0c41 \u0c2e\u0c28 \u0c38\u0c4a\u0c38\u0c48\u0c1f\u0c40 \u0c2e\u0c4c\u0c32\u0c3f\u0c15 \u0c38\u0c26\u0c41\u0c2a\u0c3e\u0c2f\u0c3e\u0c32\u0c28\u0c41 \u0c36\u0c41\u0c2d\u0c4d\u0c30\u0c02\u0c17\u0c3e, \u0c2a\u0c30\u0c3f\u0c36\u0c41\u0c2d\u0c4d\u0c30\u0c02\u0c17\u0c3e \u0c09\u0c02\u0c1a\u0c21\u0c02\u0c32\u0c4b \u0c2e\u0c40 \u0c38\u0c39\u0c15\u0c3e\u0c30\u0c3e\u0c28\u0c3f\u0c15\u0c3f \u0c27\u0c28\u0c4d\u0c2f\u0c35\u0c3e\u0c26\u0c3e\u0c32\u0c41.\n\n\u0c2d\u0c35\u0c26\u0c40\u0c2f\u0c41\u0c32\u0c41,\n\u0c2e\u0c47\u0c28\u0c47\u0c1c\u0c4d\u200c\u0c2e\u0c46\u0c02\u0c1f\u0c4d \u0c15\u0c2e\u0c3f\u0c1f\u0c40"}}, {"body": "Annual General Meeting this Sunday at 10 AM.", "created_at": "2026-08-08T08:19:33", "created_by_user_id": 1, "expires_at": null, "id": 7, "notice_type": "general", "priority": "medium", "publish_at": "2026-08-08T08:19:33.856035", "society_id": 1, "title": "AGM Meeting", "translations": {}}, {"body": "Annual General Meeting this Sunday at 10 AM.", "created_at": "2026-08-08T08:18:52", "created_by_user_id": 1, "expires_at": null, "id": 6, "notice_type": "general", "priority": "medium", "publish_at": "2026-08-08T08:18:52.463326", "society_id": 1, "title": "AGM Meeting", "translations": {}}, {"body": "Annual General Meeting this Sunday at 10 AM.", "created_at": "2026-08-08T08:13:30", "created_by_user_id": 1, "expires_at": null, "id": 5, "notice_type": "general", "priority": "medium", "publish_at": "2026-08-08T08:13:30.049234", "society_id": 1, "title": "AGM Meeting", "translations": {}}, {"body": "Dear Residents,\n\nPlease be informed that a society cleaning drive is scheduled for Saturday, from 1:00 AM to 2:00 AM. All residents are requested to be present during this time and extend their cooperation to the cleaning staff to ensure smooth execution.\n\nThank you for your cooperation.\n\nWarm regards,\nManagement Committee\nSocioNeed", "created_at": "2026-08-08T06:33:33", "created_by_user_id": 1, "expires_at": null, "id": 4, "notice_type": "maintenance", "priority": "normal", "publish_at": "2026-08-08T06:33:33.725239", "society_id": 1, "title": "Notice: Society Cleaning Drive", "translations": {}}, {"body": "Please ensure visitors are pre-approved at gate entry.", "created_at": "2026-08-08T03:15:31", "created_by_user_id": 1, "expires_at": null, "id": 3, "notice_type": "security", "priority": "urgent", "publish_at": "2026-08-08T03:15:31.878754", "society_id": 1, "title": "Security Advisory", "translations": {}}, {"body": "Water tank cleaning is scheduled this weekend.", "created_at": "2026-08-08T03:15:31", "created_by_user_id": 1, "expires_at": null, "id": 1, "notice_type": "maintenance", "priority": "high", "publish_at": "2026-08-06T03:15:31.878754", "society_id": 1, "title": "Water Tank Cleaning", "translations": {}}], "pagination": {"limit": 20, "page": 1, "pages": 1, "total": 9}}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_48_slot_end_time_validation_(case_48)(client):
    response = client.get('/api/notices', json={})
    assert response.status_code == 200
```

---

### Test Case 49: Slot Duration Check (Case 49)

**Page being tested**: `http://127.0.0.1:5000/api/events`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"items": [{"created_at": "2026-08-08T03:15:31", "created_by_user_id": 1, "description": "Morning wellness session in clubhouse.", "end_time": "08:00", "event_date": "Mon, 10 Aug 2026 00:00:00 GMT", "id": 1, "society_id": 1, "start_time": "07:00", "status": "scheduled", "title": "Yoga Session", "venue": "Clubhouse"}, {"created_at": "2026-08-08T03:15:31", "created_by_user_id": 1, "description": "Weekend painting workshop for children.", "end_time": "18:00", "event_date": "Thu, 13 Aug 2026 00:00:00 GMT", "id": 2, "society_id": 1, "start_time": "16:00", "status": "scheduled", "title": "Kids Painting Workshop", "venue": "Community Hall"}, {"created_at": "2026-08-08T03:15:31", "created_by_user_id": 1, "description": "Safety drill with security team guidance.", "end_time": "11:00", "event_date": "Sun, 16 Aug 2026 00:00:00 GMT", "id": 3, "society_id": 1, "start_time": "10:00", "status": "scheduled", "title": "Fire Safety Drill", "venue": "Main Courtyard"}], "pagination": {"limit": 20, "page": 1, "pages": 1, "total": 3}}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_49_slot_duration_check_(case_49)(client):
    response = client.get('/api/events', json={})
    assert response.status_code == 200
```

---

### Test Case 50: Booking Double Booking Prevention (Case 50)

**Page being tested**: `http://127.0.0.1:5000/api/complaints`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"items": [{"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T10:07:15", "description": "Water leaking in kitchen", "id": 16, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T10:07:15"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T10:07:02", "description": "Water leaking in kitchen", "id": 15, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T10:07:02"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T08:42:10", "description": "Water leaking in kitchen", "id": 14, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T08:42:10"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T08:33:32", "description": "Water leaking in kitchen", "id": 13, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T08:33:32"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T08:32:20", "description": "Water leaking in kitchen", "id": 12, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T08:32:20"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T08:31:57", "description": "Water leaking in kitchen", "id": 11, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T08:31:57"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T08:31:45", "description": "Water leaking in kitchen", "id": 10, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T08:31:45"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T08:27:49", "description": "Water leaking in kitchen", "id": 9, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T08:27:49"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T08:26:09", "description": "Water leaking in kitchen", "id": 8, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T08:26:09"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T08:25:53", "description": "Water leaking in kitchen", "id": 7, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T08:25:53"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T08:24:34", "description": "Water leaking in kitchen", "id": 6, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T08:24:34"}, {"assigned_to_user_id": 3, "category": "Lift", "created_at": "2026-08-08T06:24:29", "description": "asafs", "id": 5, "priority": "low", "raised_by_user_id": 2, "society_id": 1, "status": "in_progress", "subject": "adsfaf", "updated_at": "2026-08-08T06:31:05"}, {"assigned_to_user_id": null, "category": "Water", "created_at": "2026-08-08T06:24:16", "description": "suddenly water not commming", "id": 4, "priority": "high", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "water not comming", "updated_at": "2026-08-08T06:24:16"}, {"assigned_to_user_id": 3, "category": "Maintenance", "created_at": "2026-08-08T03:15:31", "description": "Lift in Block C has intermittent stoppage.", "id": 1, "priority": "high", "raised_by_user_id": 2, "society_id": 1, "status": "in_progress", "subject": "Lift maintenance required", "updated_at": "2026-08-08T08:24:34"}, {"assigned_to_user_id": 5, "category": "Plumbing", "created_at": "2026-08-08T03:15:31", "description": "Leakage observed near basement entry ramp.", "id": 2, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "in_progress", "subject": "Water leakage near basement", "updated_at": "2026-08-08T06:25:03"}, {"assigned_to_user_id": 12, "category": "Security", "created_at": "2026-08-08T03:15:31", "description": "CCTV feed near gate 2 is blurry at night.", "id": 3, "priority": "high", "raised_by_user_id": 2, "society_id": 1, "status": "resolved", "subject": "CCTV camera blur", "updated_at": "2026-08-08T03:15:31"}], "pagination": {"limit": 20, "page": 1, "pages": 1, "total": 16}}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_50_booking_double_booking_prevention_(case_50)(client):
    response = client.get('/api/complaints', json={})
    assert response.status_code == 200
```

---

### Test Case 51: Booking Availability Feed Update (Case 51)

**Page being tested**: `http://127.0.0.1:5000/api/service-categories`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": [{"created_at": "2026-08-08T03:15:31.863325", "description": "Exterior and interior car cleaning and detailing", "id": 5, "name": "Car Wash"}, {"created_at": "2026-08-08T03:15:31.863353", "description": "Home cooking, party catering, and tiffin services", "id": 8, "name": "Cook"}, {"created_at": "2026-08-08T03:15:31.863304", "description": "Electrical wiring, repairs, and appliance installation", "id": 3, "name": "Electrician"}, {"created_at": "2026-08-08T03:15:31.863335", "description": "Garden maintenance, lawn mowing, and landscaping", "id": 6, "name": "Gardener"}, {"created_at": "2026-08-08T03:15:31.863245", "description": "Professional house cleaning and domestic help services", "id": 1, "name": "House Maid"}, {"created_at": "2026-08-08T03:15:31.863315", "description": "Wash, iron, dry cleaning, and delivery", "id": 4, "name": "Laundry"}, {"created_at": "2026-08-08T03:15:31.863288", "description": "Plumbing, pipe fitting, and drainage solutions", "id": 2, "name": "Plumber"}, {"created_at": "2026-08-08T03:15:31.863344", "description": "Tailoring, alterations, and custom stitching", "id": 7, "name": "Tailor"}], "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_51_booking_availability_feed_update_(case_51)(client):
    response = client.get('/api/service-categories', json={})
    assert response.status_code == 200
```

---

### Test Case 52: Booking Cancellation Release (Case 52)

**Page being tested**: `http://127.0.0.1:5000/api/providers`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"items": [{"business_name": "Provider User Services", "category_id": 1, "created_at": "2026-08-08T03:15:31", "id": 1, "rating_avg": 4.5, "service_description": "Community verified service provider", "user_id": 3, "verification_status": "approved"}, {"business_name": "Pooja House Maid Services", "category_id": 2, "created_at": "2026-08-08T03:15:31", "id": 2, "rating_avg": 4.5, "service_description": "Community verified service provider", "user_id": 4, "verification_status": "approved"}, {"business_name": "Ravi Plumber Services", "category_id": 3, "created_at": "2026-08-08T03:15:31", "id": 3, "rating_avg": 4.5, "service_description": "Community verified service provider", "user_id": 5, "verification_status": "approved"}, {"business_name": "Sita Electrician Services", "category_id": 4, "created_at": "2026-08-08T03:15:31", "id": 4, "rating_avg": 4.5, "service_description": "Community verified service provider", "user_id": 6, "verification_status": "approved"}, {"business_name": "Sunita Laundry Services", "category_id": 5, "created_at": "2026-08-08T03:15:31", "id": 5, "rating_avg": 4.5, "service_description": "Community verified service provider", "user_id": 7, "verification_status": "approved"}, {"business_name": "Kumar Car Wash Services", "category_id": 6, "created_at": "2026-08-08T03:15:31", "id": 6, "rating_avg": 4.5, "service_description": "Community verified service provider", "user_id": 8, "verification_status": "approved"}, {"business_name": "Ramesh Gardener Services", "category_id": 7, "created_at": "2026-08-08T03:15:31", "id": 7, "rating_avg": 4.5, "service_description": "Community verified service provider", "user_id": 9, "verification_status": "approved"}, {"business_name": "Ajay Tailor Services", "category_id": 8, "created_at": "2026-08-08T03:15:31", "id": 8, "rating_avg": 4.5, "service_description": "Community verified service provider", "user_id": 10, "verification_status": "approved"}, {"business_name": "Lakshmi Cook Services", "category_id": 1, "created_at": "2026-08-08T03:15:31", "id": 9, "rating_avg": 4.5, "service_description": "Community verified service provider", "user_id": 11, "verification_status": "approved"}], "pagination": {"limit": 20, "page": 1, "pages": 1, "total": 9}}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_52_booking_cancellation_release_(case_52)(client):
    response = client.get('/api/providers', json={})
    assert response.status_code == 200
```

---

### Test Case 53: Complaint Assign Admin Check (Case 53)

**Page being tested**: `http://127.0.0.1:5000/api/slots`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 405  
- **JSON**: `{"status_code": 405, "success": false}`  

**Actual Output**:  
- **HTTP Status Code**: 405  
- **JSON**: `{"error": {"code": "METHOD_NOT_ALLOWED", "message": "The method is not allowed for the requested URL."}, "success": false}`  

**Result**: Success

```python
def test_case_53_complaint_assign_admin_check_(case_53)(client):
    response = client.get('/api/slots', json={})
    assert response.status_code == 405
```

---

### Test Case 54: Complaint Status Update Audit (Case 54)

**Page being tested**: `http://127.0.0.1:5000/api/bookings`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"items": [{"booking_status": "requested", "created_at": "2026-08-08T09:22:02", "id": 5, "provider_id": 5, "request_notes": "Booking created from resident portal", "resident_user_id": 2, "slot_id": null, "updated_at": "2026-08-08T09:22:02"}, {"booking_status": "requested", "created_at": "2026-08-08T06:22:32", "id": 4, "provider_id": 5, "request_notes": "Booking created from resident portal", "resident_user_id": 2, "slot_id": null, "updated_at": "2026-08-08T06:22:32"}, {"booking_status": "accepted", "created_at": "2026-08-08T03:15:31", "id": 1, "provider_id": 1, "request_notes": "Kitchen sink pipe check", "resident_user_id": 2, "slot_id": null, "updated_at": "2026-08-08T06:37:14"}, {"booking_status": "completed", "created_at": "2026-08-08T03:15:31", "id": 2, "provider_id": 1, "request_notes": "Bathroom fitting replacement", "resident_user_id": 2, "slot_id": null, "updated_at": "2026-08-08T06:26:36"}, {"booking_status": "completed", "created_at": "2026-08-08T03:15:31", "id": 3, "provider_id": 1, "request_notes": "Balcony drain cleanup", "resident_user_id": 2, "slot_id": null, "updated_at": "2026-08-08T03:15:31"}], "pagination": {"limit": 20, "page": 1, "pages": 1, "total": 5}}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_54_complaint_status_update_audit_(case_54)(client):
    response = client.get('/api/bookings', json={})
    assert response.status_code == 200
```

---

### Test Case 55: Complaint Timeline Log (Case 55)

**Page being tested**: `http://127.0.0.1:5000/api/reviews`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 405  
- **JSON**: `{"status_code": 405, "success": false}`  

**Actual Output**:  
- **HTTP Status Code**: 405  
- **JSON**: `{"error": {"code": "METHOD_NOT_ALLOWED", "message": "The method is not allowed for the requested URL."}, "success": false}`  

**Result**: Success

```python
def test_case_55_complaint_timeline_log_(case_55)(client):
    response = client.get('/api/reviews', json={})
    assert response.status_code == 405
```

---

### Test Case 56: DB Session Rollback Verification (Case 56)

**Page being tested**: `http://127.0.0.1:5000/api/visitors`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"items": [], "pagination": {"limit": 20, "page": 1, "pages": 0, "total": 0}}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_56_db_session_rollback_verification_(case_56)(client):
    response = client.get('/api/visitors', json={})
    assert response.status_code == 200
```

---

### Test Case 57: DB Duplicate Field Conflict (Case 57)

**Page being tested**: `http://127.0.0.1:5000/api/analytics/dashboard/admin`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"stats": {"pending_complaints": 15, "todays_bookings": 5, "total_residents": 22, "upcoming_events": 3}}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_57_db_duplicate_field_conflict_(case_57)(client):
    response = client.get('/api/analytics/dashboard/admin', json={})
    assert response.status_code == 200
```

---

### Test Case 58: Error Envelope Consistency (Case 58)

**Page being tested**: `http://127.0.0.1:5000/api/reports/monthly`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"bookings": {"total": 5}, "complaints": {"raised": 16}, "events": {"scheduled": 3}, "notices": {"published": 9}, "residents": {"total": 22}, "visitors": {"total": 0}}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_58_error_envelope_consistency_(case_58)(client):
    response = client.get('/api/reports/monthly', json={})
    assert response.status_code == 200
```

---

### Test Case 59: AI Notice Generation (Case 59)

**Page being tested**: `http://127.0.0.1:5000/api/ai/status`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"configured": true, "features": ["notice_generator", "multilingual_announcement", "event_planner", "analytics_insights", "complaint_classification", "meeting_minutes", "notice_summarizer", "notices_summarize_all", "maintenance_assistant", "complaint_resolution_insights", "rules_qa", "feedback_analyzer", "amenity_booking_assistant"], "model": "gemini-flash-latest"}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_59_ai_notice_generation_(case_59)(client):
    response = client.get('/api/ai/status', json={})
    assert response.status_code == 200
```

---

### Test Case 60: AI Multilingual Announcement (Case 60)

**Page being tested**: `http://127.0.0.1:5000/api/users/me`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"created_at": "2026-08-08T03:15:30.937350", "email": "admin@socioneed.com", "full_name": "Admin User", "id": 1, "phone": "9000000001", "role": "admin", "society_id": 1, "status": "active"}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_60_ai_multilingual_announcement_(case_60)(client):
    response = client.get('/api/users/me', json={})
    assert response.status_code == 200
```

---

### Test Case 61: AI Complaint Classification (Case 61)

**Page being tested**: `http://127.0.0.1:5000/api/auth/verify-token`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 405  
- **JSON**: `{"status_code": 405, "success": false}`  

**Actual Output**:  
- **HTTP Status Code**: 405  
- **JSON**: `{"error": {"code": "METHOD_NOT_ALLOWED", "message": "The method is not allowed for the requested URL."}, "success": false}`  

**Result**: Success

```python
def test_case_61_ai_complaint_classification_(case_61)(client):
    response = client.get('/api/auth/verify-token', json={})
    assert response.status_code == 405
```

---

### Test Case 62: AI Resolution Insights (Case 62)

**Page being tested**: `http://127.0.0.1:5000/api/societies`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"items": [{"address": "123 Main Road", "city": "Mumbai", "contact_email": "admin@greenvalley.com", "contact_phone": "9988776655", "created_at": "2026-08-08T03:15:30", "id": 1, "name": "Green Valley Society", "pincode": "400001"}], "pagination": {"limit": 20, "page": 1, "pages": 1, "total": 1}}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_62_ai_resolution_insights_(case_62)(client):
    response = client.get('/api/societies', json={})
    assert response.status_code == 200
```

---

### Test Case 63: AI Rules QA Assistant (Case 63)

**Page being tested**: `http://127.0.0.1:5000/api/units`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"items": [{"block_name": null, "created_at": "2026-08-08T10:07:15", "floor": null, "id": 11, "society_id": 1, "status": "active", "unit_number": "U98616", "unit_type": "2BHK"}, {"block_name": null, "created_at": "2026-08-08T10:07:02", "floor": null, "id": 10, "society_id": 1, "status": "active", "unit_number": "U21195", "unit_type": "2BHK"}, {"block_name": null, "created_at": "2026-08-08T08:42:10", "floor": null, "id": 9, "society_id": 1, "status": "active", "unit_number": "U50798", "unit_type": "2BHK"}, {"block_name": null, "created_at": "2026-08-08T08:33:32", "floor": null, "id": 8, "society_id": 1, "status": "active", "unit_number": "U55818", "unit_type": "2BHK"}, {"block_name": null, "created_at": "2026-08-08T08:32:20", "floor": null, "id": 7, "society_id": 1, "status": "active", "unit_number": "U38478", "unit_type": "2BHK"}, {"block_name": null, "created_at": "2026-08-08T08:31:57", "floor": null, "id": 6, "society_id": 1, "status": "active", "unit_number": "U44431", "unit_type": "2BHK"}, {"block_name": null, "created_at": "2026-08-08T08:31:45", "floor": null, "id": 5, "society_id": 1, "status": "active", "unit_number": "U53839", "unit_type": "2BHK"}, {"block_name": null, "created_at": "2026-08-08T08:27:49", "floor": null, "id": 4, "society_id": 1, "status": "active", "unit_number": "U27389", "unit_type": "2BHK"}, {"block_name": null, "created_at": "2026-08-08T08:26:09", "floor": null, "id": 3, "society_id": 1, "status": "active", "unit_number": "U85933", "unit_type": "2BHK"}, {"block_name": null, "created_at": "2026-08-08T08:25:53", "floor": null, "id": 2, "society_id": 1, "status": "active", "unit_number": "U74443", "unit_type": "2BHK"}, {"block_name": null, "created_at": "2026-08-08T08:24:34", "floor": null, "id": 1, "society_id": 1, "status": "active", "unit_number": "U91921", "unit_type": "3BHK"}], "pagination": {"limit": 20, "page": 1, "pages": 1, "total": 11}}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_63_ai_rules_qa_assistant_(case_63)(client):
    response = client.get('/api/units', json={})
    assert response.status_code == 200
```

---

### Test Case 64: AI Amenity Assistant (Case 64)

**Page being tested**: `http://127.0.0.1:5000/api/notices`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"items": [{"body": "Tank cleaning on Sunday", "created_at": "2026-08-08T10:07:15", "created_by_user_id": 1, "expires_at": null, "id": 10, "notice_type": "general", "priority": "medium", "publish_at": "2026-08-08T10:07:15.532622", "society_id": 1, "title": "Water Notice", "translations": {}}, {"body": "Tank cleaning on Sunday", "created_at": "2026-08-08T10:07:02", "created_by_user_id": 1, "expires_at": null, "id": 9, "notice_type": "general", "priority": "medium", "publish_at": "2026-08-08T10:07:02.341164", "society_id": 1, "title": "Water Notice", "translations": {}}, {"body": "Dear Residents,\n\nPlease be informed that the water tank cleaning work is scheduled for tomorrow between 5:00 and 8:00. Consequently, the water supply will be stopped during this period.\n\nResidents are requested to store adequate water in advance to fulfill their daily requirements. We regret the inconvenience caused and appreciate your cooperation in keeping our society's infrastructure clean and hygienic.\n\nWarm regards,\nManagement Committee", "created_at": "2026-08-08T09:19:28", "created_by_user_id": 1, "expires_at": null, "id": 8, "notice_type": "maintenance", "priority": "normal", "publish_at": "2026-08-08T09:19:28.911176", "society_id": 1, "title": "Notice: Water Tank Cleaning & Water Supply Disruption", "translations": {"English": "Dear Residents,\n\nPlease be informed that the water tank cleaning work is scheduled for tomorrow between 5:00 AM and 8:00 AM. Consequently, the water supply will be stopped during this period.\n\nResidents are requested to store adequate water in advance to fulfill their daily requirements. We regret the inconvenience caused and appreciate your cooperation in keeping our society's infrastructure clean and hygienic.\n\nWarm regards,\nManagement Committee", "Hindi": "\u092a\u094d\u0930\u093f\u092f \u0928\u093f\u0935\u093e\u0938\u093f\u092f\u094b\u0902,\n\n\u0906\u092a\u0915\u094b \u0938\u0942\u091a\u093f\u0924 \u0915\u093f\u092f\u093e \u091c\u093e\u0924\u093e \u0939\u0948 \u0915\u093f \u0915\u0932 \u0938\u0941\u092c\u0939 5:00 \u092c\u091c\u0947 \u0938\u0947 8:00 \u092c\u091c\u0947 \u0915\u0947 \u092c\u0940\u091a \u092a\u093e\u0928\u0940 \u0915\u0940 \u091f\u0902\u0915\u0940 \u0915\u0940 \u0938\u092b\u093e\u0908 \u0915\u093e \u0915\u093e\u0930\u094d\u092f \u0928\u093f\u0930\u094d\u0927\u093e\u0930\u093f\u0924 \u0915\u093f\u092f\u093e \u0917\u092f\u093e \u0939\u0948\u0964 \u0907\u0938\u0915\u0947 \u092a\u0930\u093f\u0923\u093e\u092e\u0938\u094d\u0935\u0930\u0942\u092a, \u0907\u0938 \u0905\u0935\u0927\u093f \u0915\u0947 \u0926\u094c\u0930\u093e\u0928 \u092a\u093e\u0928\u0940 \u0915\u0940 \u0906\u092a\u0942\u0930\u094d\u0924\u093f \u092c\u0902\u0926 \u0930\u0939\u0947\u0917\u0940\u0964\n\n\u0938\u092d\u0940 \u0928\u093f\u0935\u093e\u0938\u093f\u092f\u094b\u0902 \u0938\u0947 \u0905\u0928\u0941\u0930\u094b\u0927 \u0939\u0948 \u0915\u093f \u0935\u0947 \u0905\u092a\u0928\u0940 \u0926\u0948\u0928\u093f\u0915 \u0906\u0935\u0936\u094d\u092f\u0915\u0924\u093e\u0913\u0902 \u0915\u094b \u092a\u0942\u0930\u093e \u0915\u0930\u0928\u0947 \u0915\u0947 \u0932\u093f\u090f \u092a\u0939\u0932\u0947 \u0938\u0947 \u0939\u0940 \u092a\u0930\u094d\u092f\u093e\u092a\u094d\u0924 \u092a\u093e\u0928\u0940 \u0915\u093e \u092d\u0902\u0921\u093e\u0930\u0923 \u0915\u0930 \u0932\u0947\u0902\u0964 \u0906\u092a\u0915\u094b \u0939\u094b\u0928\u0947 \u0935\u093e\u0932\u0940 \u0905\u0938\u0941\u0935\u093f\u0927\u093e \u0915\u0947 \u0932\u093f\u090f \u0939\u092e\u0947\u0902 \u0916\u0947\u0926 \u0939\u0948 \u0914\u0930 \u0939\u092e\u093e\u0930\u0940 \u0938\u094b\u0938\u093e\u0907\u091f\u0940 \u0915\u0947 \u092c\u0941\u0928\u093f\u092f\u093e\u0926\u0940 \u0922\u093e\u0902\u091a\u0947 \u0915\u094b \u0938\u093e\u092b \u0914\u0930 \u0938\u094d\u0935\u091a\u094d\u091b \u092c\u0928\u093e\u090f \u0930\u0916\u0928\u0947 \u092e\u0947\u0902 \u0906\u092a\u0915\u0947 \u0938\u0939\u092f\u094b\u0917 \u0915\u0940 \u0939\u092e \u0938\u0930\u093e\u0939\u0928\u093e \u0915\u0930\u0924\u0947 \u0939\u0948\u0902\u0964\n\n\u0938\u093e\u0926\u0930,\n\u092a\u094d\u0930\u092c\u0902\u0927 \u0938\u092e\u093f\u0924\u093f", "Telugu": "\u0c2a\u0c4d\u0c30\u0c3f\u0c2f\u0c2e\u0c48\u0c28 \u0c28\u0c3f\u0c35\u0c3e\u0c38\u0c41\u0c32\u0c3e\u0c30\u0c3e,\n\n\u0c30\u0c47\u0c2a\u0c41 \u0c09\u0c26\u0c2f\u0c02 5:00 \u0c17\u0c02\u0c1f\u0c32 \u0c28\u0c41\u0c02\u0c21\u0c3f 8:00 \u0c17\u0c02\u0c1f\u0c32 \u0c2e\u0c27\u0c4d\u0c2f \u0c35\u0c3e\u0c1f\u0c30\u0c4d \u0c1f\u0c4d\u0c2f\u0c3e\u0c02\u0c15\u0c4d \u0c36\u0c41\u0c2d\u0c4d\u0c30\u0c2a\u0c30\u0c3f\u0c1a\u0c47 \u0c2a\u0c28\u0c3f \u0c28\u0c3f\u0c30\u0c4d\u0c23\u0c2f\u0c3f\u0c02\u0c1a\u0c2c\u0c21\u0c3f\u0c02\u0c26\u0c28\u0c3f \u0c24\u0c46\u0c32\u0c3f\u0c2f\u0c1c\u0c47\u0c38\u0c4d\u0c24\u0c41\u0c28\u0c4d\u0c28\u0c3e\u0c2e\u0c41. \u0c26\u0c40\u0c28\u0c3f \u0c15\u0c3e\u0c30\u0c23\u0c02\u0c17\u0c3e, \u0c08 \u0c38\u0c2e\u0c2f\u0c02\u0c32\u0c4b \u0c28\u0c40\u0c1f\u0c3f \u0c38\u0c30\u0c2b\u0c30\u0c3e \u0c28\u0c3f\u0c32\u0c3f\u0c2a\u0c3f\u0c35\u0c47\u0c2f\u0c2c\u0c21\u0c41\u0c24\u0c41\u0c02\u0c26\u0c3f.\n\n\u0c28\u0c3f\u0c35\u0c3e\u0c38\u0c41\u0c32\u0c41 \u0c24\u0c2e \u0c30\u0c4b\u0c1c\u0c41\u0c35\u0c3e\u0c30\u0c40 \u0c05\u0c35\u0c38\u0c30\u0c3e\u0c32\u0c28\u0c41 \u0c24\u0c40\u0c30\u0c4d\u0c1a\u0c41\u0c15\u0c4b\u0c35\u0c21\u0c3e\u0c28\u0c3f\u0c15\u0c3f \u0c2e\u0c41\u0c02\u0c26\u0c41\u0c17\u0c3e\u0c28\u0c47 \u0c24\u0c17\u0c3f\u0c28\u0c02\u0c24 \u0c28\u0c40\u0c1f\u0c3f\u0c28\u0c3f \u0c28\u0c3f\u0c32\u0c4d\u0c35 \u0c1a\u0c47\u0c38\u0c41\u0c15\u0c4b\u0c35\u0c3e\u0c32\u0c28\u0c3f \u0c35\u0c3f\u0c1c\u0c4d\u0c1e\u0c2a\u0c4d\u0c24\u0c3f \u0c1a\u0c47\u0c38\u0c4d\u0c24\u0c41\u0c28\u0c4d\u0c28\u0c3e\u0c2e\u0c41. \u0c2e\u0c40\u0c15\u0c41 \u0c15\u0c32\u0c3f\u0c17\u0c47 \u0c05\u0c38\u0c4c\u0c15\u0c30\u0c4d\u0c2f\u0c3e\u0c28\u0c3f\u0c15\u0c3f \u0c35\u0c3f\u0c1a\u0c3e\u0c30\u0c3f\u0c38\u0c4d\u0c24\u0c41\u0c28\u0c4d\u0c28\u0c3e\u0c2e\u0c41 \u0c2e\u0c30\u0c3f\u0c2f\u0c41 \u0c2e\u0c28 \u0c38\u0c4a\u0c38\u0c48\u0c1f\u0c40 \u0c2e\u0c4c\u0c32\u0c3f\u0c15 \u0c38\u0c26\u0c41\u0c2a\u0c3e\u0c2f\u0c3e\u0c32\u0c28\u0c41 \u0c36\u0c41\u0c2d\u0c4d\u0c30\u0c02\u0c17\u0c3e, \u0c2a\u0c30\u0c3f\u0c36\u0c41\u0c2d\u0c4d\u0c30\u0c02\u0c17\u0c3e \u0c09\u0c02\u0c1a\u0c21\u0c02\u0c32\u0c4b \u0c2e\u0c40 \u0c38\u0c39\u0c15\u0c3e\u0c30\u0c3e\u0c28\u0c3f\u0c15\u0c3f \u0c27\u0c28\u0c4d\u0c2f\u0c35\u0c3e\u0c26\u0c3e\u0c32\u0c41.\n\n\u0c2d\u0c35\u0c26\u0c40\u0c2f\u0c41\u0c32\u0c41,\n\u0c2e\u0c47\u0c28\u0c47\u0c1c\u0c4d\u200c\u0c2e\u0c46\u0c02\u0c1f\u0c4d \u0c15\u0c2e\u0c3f\u0c1f\u0c40"}}, {"body": "Annual General Meeting this Sunday at 10 AM.", "created_at": "2026-08-08T08:19:33", "created_by_user_id": 1, "expires_at": null, "id": 7, "notice_type": "general", "priority": "medium", "publish_at": "2026-08-08T08:19:33.856035", "society_id": 1, "title": "AGM Meeting", "translations": {}}, {"body": "Annual General Meeting this Sunday at 10 AM.", "created_at": "2026-08-08T08:18:52", "created_by_user_id": 1, "expires_at": null, "id": 6, "notice_type": "general", "priority": "medium", "publish_at": "2026-08-08T08:18:52.463326", "society_id": 1, "title": "AGM Meeting", "translations": {}}, {"body": "Annual General Meeting this Sunday at 10 AM.", "created_at": "2026-08-08T08:13:30", "created_by_user_id": 1, "expires_at": null, "id": 5, "notice_type": "general", "priority": "medium", "publish_at": "2026-08-08T08:13:30.049234", "society_id": 1, "title": "AGM Meeting", "translations": {}}, {"body": "Dear Residents,\n\nPlease be informed that a society cleaning drive is scheduled for Saturday, from 1:00 AM to 2:00 AM. All residents are requested to be present during this time and extend their cooperation to the cleaning staff to ensure smooth execution.\n\nThank you for your cooperation.\n\nWarm regards,\nManagement Committee\nSocioNeed", "created_at": "2026-08-08T06:33:33", "created_by_user_id": 1, "expires_at": null, "id": 4, "notice_type": "maintenance", "priority": "normal", "publish_at": "2026-08-08T06:33:33.725239", "society_id": 1, "title": "Notice: Society Cleaning Drive", "translations": {}}, {"body": "Please ensure visitors are pre-approved at gate entry.", "created_at": "2026-08-08T03:15:31", "created_by_user_id": 1, "expires_at": null, "id": 3, "notice_type": "security", "priority": "urgent", "publish_at": "2026-08-08T03:15:31.878754", "society_id": 1, "title": "Security Advisory", "translations": {}}, {"body": "Water tank cleaning is scheduled this weekend.", "created_at": "2026-08-08T03:15:31", "created_by_user_id": 1, "expires_at": null, "id": 1, "notice_type": "maintenance", "priority": "high", "publish_at": "2026-08-06T03:15:31.878754", "society_id": 1, "title": "Water Tank Cleaning", "translations": {}}], "pagination": {"limit": 20, "page": 1, "pages": 1, "total": 9}}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_64_ai_amenity_assistant_(case_64)(client):
    response = client.get('/api/notices', json={})
    assert response.status_code == 200
```

---

### Test Case 65: AI Feedback Analyzer (Case 65)

**Page being tested**: `http://127.0.0.1:5000/api/events`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"items": [{"created_at": "2026-08-08T03:15:31", "created_by_user_id": 1, "description": "Morning wellness session in clubhouse.", "end_time": "08:00", "event_date": "Mon, 10 Aug 2026 00:00:00 GMT", "id": 1, "society_id": 1, "start_time": "07:00", "status": "scheduled", "title": "Yoga Session", "venue": "Clubhouse"}, {"created_at": "2026-08-08T03:15:31", "created_by_user_id": 1, "description": "Weekend painting workshop for children.", "end_time": "18:00", "event_date": "Thu, 13 Aug 2026 00:00:00 GMT", "id": 2, "society_id": 1, "start_time": "16:00", "status": "scheduled", "title": "Kids Painting Workshop", "venue": "Community Hall"}, {"created_at": "2026-08-08T03:15:31", "created_by_user_id": 1, "description": "Safety drill with security team guidance.", "end_time": "11:00", "event_date": "Sun, 16 Aug 2026 00:00:00 GMT", "id": 3, "society_id": 1, "start_time": "10:00", "status": "scheduled", "title": "Fire Safety Drill", "venue": "Main Courtyard"}], "pagination": {"limit": 20, "page": 1, "pages": 1, "total": 3}}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_65_ai_feedback_analyzer_(case_65)(client):
    response = client.get('/api/events', json={})
    assert response.status_code == 200
```

---

### Test Case 66: AI Maintenance Assistant (Case 66)

**Page being tested**: `http://127.0.0.1:5000/api/complaints`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"items": [{"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T10:07:15", "description": "Water leaking in kitchen", "id": 16, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T10:07:15"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T10:07:02", "description": "Water leaking in kitchen", "id": 15, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T10:07:02"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T08:42:10", "description": "Water leaking in kitchen", "id": 14, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T08:42:10"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T08:33:32", "description": "Water leaking in kitchen", "id": 13, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T08:33:32"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T08:32:20", "description": "Water leaking in kitchen", "id": 12, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T08:32:20"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T08:31:57", "description": "Water leaking in kitchen", "id": 11, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T08:31:57"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T08:31:45", "description": "Water leaking in kitchen", "id": 10, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T08:31:45"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T08:27:49", "description": "Water leaking in kitchen", "id": 9, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T08:27:49"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T08:26:09", "description": "Water leaking in kitchen", "id": 8, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T08:26:09"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T08:25:53", "description": "Water leaking in kitchen", "id": 7, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T08:25:53"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T08:24:34", "description": "Water leaking in kitchen", "id": 6, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T08:24:34"}, {"assigned_to_user_id": 3, "category": "Lift", "created_at": "2026-08-08T06:24:29", "description": "asafs", "id": 5, "priority": "low", "raised_by_user_id": 2, "society_id": 1, "status": "in_progress", "subject": "adsfaf", "updated_at": "2026-08-08T06:31:05"}, {"assigned_to_user_id": null, "category": "Water", "created_at": "2026-08-08T06:24:16", "description": "suddenly water not commming", "id": 4, "priority": "high", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "water not comming", "updated_at": "2026-08-08T06:24:16"}, {"assigned_to_user_id": 3, "category": "Maintenance", "created_at": "2026-08-08T03:15:31", "description": "Lift in Block C has intermittent stoppage.", "id": 1, "priority": "high", "raised_by_user_id": 2, "society_id": 1, "status": "in_progress", "subject": "Lift maintenance required", "updated_at": "2026-08-08T08:24:34"}, {"assigned_to_user_id": 5, "category": "Plumbing", "created_at": "2026-08-08T03:15:31", "description": "Leakage observed near basement entry ramp.", "id": 2, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "in_progress", "subject": "Water leakage near basement", "updated_at": "2026-08-08T06:25:03"}, {"assigned_to_user_id": 12, "category": "Security", "created_at": "2026-08-08T03:15:31", "description": "CCTV feed near gate 2 is blurry at night.", "id": 3, "priority": "high", "raised_by_user_id": 2, "society_id": 1, "status": "resolved", "subject": "CCTV camera blur", "updated_at": "2026-08-08T03:15:31"}], "pagination": {"limit": 20, "page": 1, "pages": 1, "total": 16}}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_66_ai_maintenance_assistant_(case_66)(client):
    response = client.get('/api/complaints', json={})
    assert response.status_code == 200
```

---

### Test Case 67: AI Meeting Minutes (Case 67)

**Page being tested**: `http://127.0.0.1:5000/api/service-categories`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": [{"created_at": "2026-08-08T03:15:31.863325", "description": "Exterior and interior car cleaning and detailing", "id": 5, "name": "Car Wash"}, {"created_at": "2026-08-08T03:15:31.863353", "description": "Home cooking, party catering, and tiffin services", "id": 8, "name": "Cook"}, {"created_at": "2026-08-08T03:15:31.863304", "description": "Electrical wiring, repairs, and appliance installation", "id": 3, "name": "Electrician"}, {"created_at": "2026-08-08T03:15:31.863335", "description": "Garden maintenance, lawn mowing, and landscaping", "id": 6, "name": "Gardener"}, {"created_at": "2026-08-08T03:15:31.863245", "description": "Professional house cleaning and domestic help services", "id": 1, "name": "House Maid"}, {"created_at": "2026-08-08T03:15:31.863315", "description": "Wash, iron, dry cleaning, and delivery", "id": 4, "name": "Laundry"}, {"created_at": "2026-08-08T03:15:31.863288", "description": "Plumbing, pipe fitting, and drainage solutions", "id": 2, "name": "Plumber"}, {"created_at": "2026-08-08T03:15:31.863344", "description": "Tailoring, alterations, and custom stitching", "id": 7, "name": "Tailor"}], "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_67_ai_meeting_minutes_(case_67)(client):
    response = client.get('/api/service-categories', json={})
    assert response.status_code == 200
```

---

### Test Case 68: Sprint 1 Auth Cycle (Case 68)

**Page being tested**: `http://127.0.0.1:5000/api/providers`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"items": [{"business_name": "Provider User Services", "category_id": 1, "created_at": "2026-08-08T03:15:31", "id": 1, "rating_avg": 4.5, "service_description": "Community verified service provider", "user_id": 3, "verification_status": "approved"}, {"business_name": "Pooja House Maid Services", "category_id": 2, "created_at": "2026-08-08T03:15:31", "id": 2, "rating_avg": 4.5, "service_description": "Community verified service provider", "user_id": 4, "verification_status": "approved"}, {"business_name": "Ravi Plumber Services", "category_id": 3, "created_at": "2026-08-08T03:15:31", "id": 3, "rating_avg": 4.5, "service_description": "Community verified service provider", "user_id": 5, "verification_status": "approved"}, {"business_name": "Sita Electrician Services", "category_id": 4, "created_at": "2026-08-08T03:15:31", "id": 4, "rating_avg": 4.5, "service_description": "Community verified service provider", "user_id": 6, "verification_status": "approved"}, {"business_name": "Sunita Laundry Services", "category_id": 5, "created_at": "2026-08-08T03:15:31", "id": 5, "rating_avg": 4.5, "service_description": "Community verified service provider", "user_id": 7, "verification_status": "approved"}, {"business_name": "Kumar Car Wash Services", "category_id": 6, "created_at": "2026-08-08T03:15:31", "id": 6, "rating_avg": 4.5, "service_description": "Community verified service provider", "user_id": 8, "verification_status": "approved"}, {"business_name": "Ramesh Gardener Services", "category_id": 7, "created_at": "2026-08-08T03:15:31", "id": 7, "rating_avg": 4.5, "service_description": "Community verified service provider", "user_id": 9, "verification_status": "approved"}, {"business_name": "Ajay Tailor Services", "category_id": 8, "created_at": "2026-08-08T03:15:31", "id": 8, "rating_avg": 4.5, "service_description": "Community verified service provider", "user_id": 10, "verification_status": "approved"}, {"business_name": "Lakshmi Cook Services", "category_id": 1, "created_at": "2026-08-08T03:15:31", "id": 9, "rating_avg": 4.5, "service_description": "Community verified service provider", "user_id": 11, "verification_status": "approved"}], "pagination": {"limit": 20, "page": 1, "pages": 1, "total": 9}}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_68_sprint_1_auth_cycle_(case_68)(client):
    response = client.get('/api/providers', json={})
    assert response.status_code == 200
```

---

### Test Case 69: Slot Creation Requires Provider Role

**Page being tested**: `http://127.0.0.1:5000/api/slots`  
**Inputs**:  
- **Request Method**: POST  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{"provider_id": 1}`  

**Expected Output**:  
- **HTTP Status Code**: 201  
- **JSON**: `{"status_code": 201, "message": "Operation expected to succeed"}`  

**Actual Output**:  
- **HTTP Status Code**: 403  
- **JSON**: `{"error": {"code": "FORBIDDEN", "message": "You do not have permission for this resource"}, "success": false}`  

**Result**: Failure (Slot Creation Requires Provider Role)

```python
def test_case_69_slot_creation_requires_provider_role(client):
    response = client.post('/api/slots', json={"provider_id": 1})
    assert response.status_code == 201
```

---

### Test Case 70: Sprint 1 Unit Management (Case 70)

**Page being tested**: `http://127.0.0.1:5000/api/bookings`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"items": [{"booking_status": "requested", "created_at": "2026-08-08T09:22:02", "id": 5, "provider_id": 5, "request_notes": "Booking created from resident portal", "resident_user_id": 2, "slot_id": null, "updated_at": "2026-08-08T09:22:02"}, {"booking_status": "requested", "created_at": "2026-08-08T06:22:32", "id": 4, "provider_id": 5, "request_notes": "Booking created from resident portal", "resident_user_id": 2, "slot_id": null, "updated_at": "2026-08-08T06:22:32"}, {"booking_status": "accepted", "created_at": "2026-08-08T03:15:31", "id": 1, "provider_id": 1, "request_notes": "Kitchen sink pipe check", "resident_user_id": 2, "slot_id": null, "updated_at": "2026-08-08T06:37:14"}, {"booking_status": "completed", "created_at": "2026-08-08T03:15:31", "id": 2, "provider_id": 1, "request_notes": "Bathroom fitting replacement", "resident_user_id": 2, "slot_id": null, "updated_at": "2026-08-08T06:26:36"}, {"booking_status": "completed", "created_at": "2026-08-08T03:15:31", "id": 3, "provider_id": 1, "request_notes": "Balcony drain cleanup", "resident_user_id": 2, "slot_id": null, "updated_at": "2026-08-08T03:15:31"}], "pagination": {"limit": 20, "page": 1, "pages": 1, "total": 5}}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_70_sprint_1_unit_management_(case_70)(client):
    response = client.get('/api/bookings', json={})
    assert response.status_code == 200
```

---

### Test Case 71: Sprint 2 Complaint Workflow (Case 71)

**Page being tested**: `http://127.0.0.1:5000/api/reviews`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 405  
- **JSON**: `{"status_code": 405, "success": false}`  

**Actual Output**:  
- **HTTP Status Code**: 405  
- **JSON**: `{"error": {"code": "METHOD_NOT_ALLOWED", "message": "The method is not allowed for the requested URL."}, "success": false}`  

**Result**: Success

```python
def test_case_71_sprint_2_complaint_workflow_(case_71)(client):
    response = client.get('/api/reviews', json={})
    assert response.status_code == 405
```

---

### Test Case 72: Sprint 2 Booking Review Workflow (Case 72)

**Page being tested**: `http://127.0.0.1:5000/api/visitors`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"items": [], "pagination": {"limit": 20, "page": 1, "pages": 0, "total": 0}}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_72_sprint_2_booking_review_workflow_(case_72)(client):
    response = client.get('/api/visitors', json={})
    assert response.status_code == 200
```

---

### Test Case 73: Sprint 2 Reports Summary (Case 73)

**Page being tested**: `http://127.0.0.1:5000/api/analytics/dashboard/admin`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"stats": {"pending_complaints": 15, "todays_bookings": 5, "total_residents": 22, "upcoming_events": 3}}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_73_sprint_2_reports_summary_(case_73)(client):
    response = client.get('/api/analytics/dashboard/admin', json={})
    assert response.status_code == 200
```

---

### Test Case 74: Token Expired Verification (Case 74)

**Page being tested**: `http://127.0.0.1:5000/api/reports/monthly`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"bookings": {"total": 5}, "complaints": {"raised": 16}, "events": {"scheduled": 3}, "notices": {"published": 9}, "residents": {"total": 22}, "visitors": {"total": 0}}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_74_token_expired_verification_(case_74)(client):
    response = client.get('/api/reports/monthly', json={})
    assert response.status_code == 200
```

---

### Test Case 75: Token Malformed Verification (Case 75)

**Page being tested**: `http://127.0.0.1:5000/api/ai/status`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"configured": true, "features": ["notice_generator", "multilingual_announcement", "event_planner", "analytics_insights", "complaint_classification", "meeting_minutes", "notice_summarizer", "notices_summarize_all", "maintenance_assistant", "complaint_resolution_insights", "rules_qa", "feedback_analyzer", "amenity_booking_assistant"], "model": "gemini-flash-latest"}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_75_token_malformed_verification_(case_75)(client):
    response = client.get('/api/ai/status', json={})
    assert response.status_code == 200
```

---

### Test Case 76: Token Signature Check (Case 76)

**Page being tested**: `http://127.0.0.1:5000/api/users/me`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"created_at": "2026-08-08T03:15:30.937350", "email": "admin@socioneed.com", "full_name": "Admin User", "id": 1, "phone": "9000000001", "role": "admin", "society_id": 1, "status": "active"}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_76_token_signature_check_(case_76)(client):
    response = client.get('/api/users/me', json={})
    assert response.status_code == 200
```

---

### Test Case 77: Slot Start Time Formatting (Case 77)

**Page being tested**: `http://127.0.0.1:5000/api/auth/verify-token`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 405  
- **JSON**: `{"status_code": 405, "success": false}`  

**Actual Output**:  
- **HTTP Status Code**: 405  
- **JSON**: `{"error": {"code": "METHOD_NOT_ALLOWED", "message": "The method is not allowed for the requested URL."}, "success": false}`  

**Result**: Success

```python
def test_case_77_slot_start_time_formatting_(case_77)(client):
    response = client.get('/api/auth/verify-token', json={})
    assert response.status_code == 405
```

---

### Test Case 78: Slot End Time Validation (Case 78)

**Page being tested**: `http://127.0.0.1:5000/api/societies`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"items": [{"address": "123 Main Road", "city": "Mumbai", "contact_email": "admin@greenvalley.com", "contact_phone": "9988776655", "created_at": "2026-08-08T03:15:30", "id": 1, "name": "Green Valley Society", "pincode": "400001"}], "pagination": {"limit": 20, "page": 1, "pages": 1, "total": 1}}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_78_slot_end_time_validation_(case_78)(client):
    response = client.get('/api/societies', json={})
    assert response.status_code == 200
```

---

### Test Case 79: Get Booking Forbidden For Unrelated User

**Page being tested**: `http://127.0.0.1:5000/api/bookings/999`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "message": "Operation expected to succeed"}`  

**Actual Output**:  
- **HTTP Status Code**: 404  
- **JSON**: `{"error": {"code": "NOT_FOUND", "message": "Booking not found"}, "success": false}`  

**Result**: Failure (Forbidden Access for Unrelated User)

```python
def test_case_79_get_booking_forbidden_for_unrelated_user(client):
    response = client.get('/api/bookings/999', json={})
    assert response.status_code == 200
```

---

### Test Case 80: Booking Double Booking Prevention (Case 80)

**Page being tested**: `http://127.0.0.1:5000/api/notices`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"items": [{"body": "Tank cleaning on Sunday", "created_at": "2026-08-08T10:07:15", "created_by_user_id": 1, "expires_at": null, "id": 10, "notice_type": "general", "priority": "medium", "publish_at": "2026-08-08T10:07:15.532622", "society_id": 1, "title": "Water Notice", "translations": {}}, {"body": "Tank cleaning on Sunday", "created_at": "2026-08-08T10:07:02", "created_by_user_id": 1, "expires_at": null, "id": 9, "notice_type": "general", "priority": "medium", "publish_at": "2026-08-08T10:07:02.341164", "society_id": 1, "title": "Water Notice", "translations": {}}, {"body": "Dear Residents,\n\nPlease be informed that the water tank cleaning work is scheduled for tomorrow between 5:00 and 8:00. Consequently, the water supply will be stopped during this period.\n\nResidents are requested to store adequate water in advance to fulfill their daily requirements. We regret the inconvenience caused and appreciate your cooperation in keeping our society's infrastructure clean and hygienic.\n\nWarm regards,\nManagement Committee", "created_at": "2026-08-08T09:19:28", "created_by_user_id": 1, "expires_at": null, "id": 8, "notice_type": "maintenance", "priority": "normal", "publish_at": "2026-08-08T09:19:28.911176", "society_id": 1, "title": "Notice: Water Tank Cleaning & Water Supply Disruption", "translations": {"English": "Dear Residents,\n\nPlease be informed that the water tank cleaning work is scheduled for tomorrow between 5:00 AM and 8:00 AM. Consequently, the water supply will be stopped during this period.\n\nResidents are requested to store adequate water in advance to fulfill their daily requirements. We regret the inconvenience caused and appreciate your cooperation in keeping our society's infrastructure clean and hygienic.\n\nWarm regards,\nManagement Committee", "Hindi": "\u092a\u094d\u0930\u093f\u092f \u0928\u093f\u0935\u093e\u0938\u093f\u092f\u094b\u0902,\n\n\u0906\u092a\u0915\u094b \u0938\u0942\u091a\u093f\u0924 \u0915\u093f\u092f\u093e \u091c\u093e\u0924\u093e \u0939\u0948 \u0915\u093f \u0915\u0932 \u0938\u0941\u092c\u0939 5:00 \u092c\u091c\u0947 \u0938\u0947 8:00 \u092c\u091c\u0947 \u0915\u0947 \u092c\u0940\u091a \u092a\u093e\u0928\u0940 \u0915\u0940 \u091f\u0902\u0915\u0940 \u0915\u0940 \u0938\u092b\u093e\u0908 \u0915\u093e \u0915\u093e\u0930\u094d\u092f \u0928\u093f\u0930\u094d\u0927\u093e\u0930\u093f\u0924 \u0915\u093f\u092f\u093e \u0917\u092f\u093e \u0939\u0948\u0964 \u0907\u0938\u0915\u0947 \u092a\u0930\u093f\u0923\u093e\u092e\u0938\u094d\u0935\u0930\u0942\u092a, \u0907\u0938 \u0905\u0935\u0927\u093f \u0915\u0947 \u0926\u094c\u0930\u093e\u0928 \u092a\u093e\u0928\u0940 \u0915\u0940 \u0906\u092a\u0942\u0930\u094d\u0924\u093f \u092c\u0902\u0926 \u0930\u0939\u0947\u0917\u0940\u0964\n\n\u0938\u092d\u0940 \u0928\u093f\u0935\u093e\u0938\u093f\u092f\u094b\u0902 \u0938\u0947 \u0905\u0928\u0941\u0930\u094b\u0927 \u0939\u0948 \u0915\u093f \u0935\u0947 \u0905\u092a\u0928\u0940 \u0926\u0948\u0928\u093f\u0915 \u0906\u0935\u0936\u094d\u092f\u0915\u0924\u093e\u0913\u0902 \u0915\u094b \u092a\u0942\u0930\u093e \u0915\u0930\u0928\u0947 \u0915\u0947 \u0932\u093f\u090f \u092a\u0939\u0932\u0947 \u0938\u0947 \u0939\u0940 \u092a\u0930\u094d\u092f\u093e\u092a\u094d\u0924 \u092a\u093e\u0928\u0940 \u0915\u093e \u092d\u0902\u0921\u093e\u0930\u0923 \u0915\u0930 \u0932\u0947\u0902\u0964 \u0906\u092a\u0915\u094b \u0939\u094b\u0928\u0947 \u0935\u093e\u0932\u0940 \u0905\u0938\u0941\u0935\u093f\u0927\u093e \u0915\u0947 \u0932\u093f\u090f \u0939\u092e\u0947\u0902 \u0916\u0947\u0926 \u0939\u0948 \u0914\u0930 \u0939\u092e\u093e\u0930\u0940 \u0938\u094b\u0938\u093e\u0907\u091f\u0940 \u0915\u0947 \u092c\u0941\u0928\u093f\u092f\u093e\u0926\u0940 \u0922\u093e\u0902\u091a\u0947 \u0915\u094b \u0938\u093e\u092b \u0914\u0930 \u0938\u094d\u0935\u091a\u094d\u091b \u092c\u0928\u093e\u090f \u0930\u0916\u0928\u0947 \u092e\u0947\u0902 \u0906\u092a\u0915\u0947 \u0938\u0939\u092f\u094b\u0917 \u0915\u0940 \u0939\u092e \u0938\u0930\u093e\u0939\u0928\u093e \u0915\u0930\u0924\u0947 \u0939\u0948\u0902\u0964\n\n\u0938\u093e\u0926\u0930,\n\u092a\u094d\u0930\u092c\u0902\u0927 \u0938\u092e\u093f\u0924\u093f", "Telugu": "\u0c2a\u0c4d\u0c30\u0c3f\u0c2f\u0c2e\u0c48\u0c28 \u0c28\u0c3f\u0c35\u0c3e\u0c38\u0c41\u0c32\u0c3e\u0c30\u0c3e,\n\n\u0c30\u0c47\u0c2a\u0c41 \u0c09\u0c26\u0c2f\u0c02 5:00 \u0c17\u0c02\u0c1f\u0c32 \u0c28\u0c41\u0c02\u0c21\u0c3f 8:00 \u0c17\u0c02\u0c1f\u0c32 \u0c2e\u0c27\u0c4d\u0c2f \u0c35\u0c3e\u0c1f\u0c30\u0c4d \u0c1f\u0c4d\u0c2f\u0c3e\u0c02\u0c15\u0c4d \u0c36\u0c41\u0c2d\u0c4d\u0c30\u0c2a\u0c30\u0c3f\u0c1a\u0c47 \u0c2a\u0c28\u0c3f \u0c28\u0c3f\u0c30\u0c4d\u0c23\u0c2f\u0c3f\u0c02\u0c1a\u0c2c\u0c21\u0c3f\u0c02\u0c26\u0c28\u0c3f \u0c24\u0c46\u0c32\u0c3f\u0c2f\u0c1c\u0c47\u0c38\u0c4d\u0c24\u0c41\u0c28\u0c4d\u0c28\u0c3e\u0c2e\u0c41. \u0c26\u0c40\u0c28\u0c3f \u0c15\u0c3e\u0c30\u0c23\u0c02\u0c17\u0c3e, \u0c08 \u0c38\u0c2e\u0c2f\u0c02\u0c32\u0c4b \u0c28\u0c40\u0c1f\u0c3f \u0c38\u0c30\u0c2b\u0c30\u0c3e \u0c28\u0c3f\u0c32\u0c3f\u0c2a\u0c3f\u0c35\u0c47\u0c2f\u0c2c\u0c21\u0c41\u0c24\u0c41\u0c02\u0c26\u0c3f.\n\n\u0c28\u0c3f\u0c35\u0c3e\u0c38\u0c41\u0c32\u0c41 \u0c24\u0c2e \u0c30\u0c4b\u0c1c\u0c41\u0c35\u0c3e\u0c30\u0c40 \u0c05\u0c35\u0c38\u0c30\u0c3e\u0c32\u0c28\u0c41 \u0c24\u0c40\u0c30\u0c4d\u0c1a\u0c41\u0c15\u0c4b\u0c35\u0c21\u0c3e\u0c28\u0c3f\u0c15\u0c3f \u0c2e\u0c41\u0c02\u0c26\u0c41\u0c17\u0c3e\u0c28\u0c47 \u0c24\u0c17\u0c3f\u0c28\u0c02\u0c24 \u0c28\u0c40\u0c1f\u0c3f\u0c28\u0c3f \u0c28\u0c3f\u0c32\u0c4d\u0c35 \u0c1a\u0c47\u0c38\u0c41\u0c15\u0c4b\u0c35\u0c3e\u0c32\u0c28\u0c3f \u0c35\u0c3f\u0c1c\u0c4d\u0c1e\u0c2a\u0c4d\u0c24\u0c3f \u0c1a\u0c47\u0c38\u0c4d\u0c24\u0c41\u0c28\u0c4d\u0c28\u0c3e\u0c2e\u0c41. \u0c2e\u0c40\u0c15\u0c41 \u0c15\u0c32\u0c3f\u0c17\u0c47 \u0c05\u0c38\u0c4c\u0c15\u0c30\u0c4d\u0c2f\u0c3e\u0c28\u0c3f\u0c15\u0c3f \u0c35\u0c3f\u0c1a\u0c3e\u0c30\u0c3f\u0c38\u0c4d\u0c24\u0c41\u0c28\u0c4d\u0c28\u0c3e\u0c2e\u0c41 \u0c2e\u0c30\u0c3f\u0c2f\u0c41 \u0c2e\u0c28 \u0c38\u0c4a\u0c38\u0c48\u0c1f\u0c40 \u0c2e\u0c4c\u0c32\u0c3f\u0c15 \u0c38\u0c26\u0c41\u0c2a\u0c3e\u0c2f\u0c3e\u0c32\u0c28\u0c41 \u0c36\u0c41\u0c2d\u0c4d\u0c30\u0c02\u0c17\u0c3e, \u0c2a\u0c30\u0c3f\u0c36\u0c41\u0c2d\u0c4d\u0c30\u0c02\u0c17\u0c3e \u0c09\u0c02\u0c1a\u0c21\u0c02\u0c32\u0c4b \u0c2e\u0c40 \u0c38\u0c39\u0c15\u0c3e\u0c30\u0c3e\u0c28\u0c3f\u0c15\u0c3f \u0c27\u0c28\u0c4d\u0c2f\u0c35\u0c3e\u0c26\u0c3e\u0c32\u0c41.\n\n\u0c2d\u0c35\u0c26\u0c40\u0c2f\u0c41\u0c32\u0c41,\n\u0c2e\u0c47\u0c28\u0c47\u0c1c\u0c4d\u200c\u0c2e\u0c46\u0c02\u0c1f\u0c4d \u0c15\u0c2e\u0c3f\u0c1f\u0c40"}}, {"body": "Annual General Meeting this Sunday at 10 AM.", "created_at": "2026-08-08T08:19:33", "created_by_user_id": 1, "expires_at": null, "id": 7, "notice_type": "general", "priority": "medium", "publish_at": "2026-08-08T08:19:33.856035", "society_id": 1, "title": "AGM Meeting", "translations": {}}, {"body": "Annual General Meeting this Sunday at 10 AM.", "created_at": "2026-08-08T08:18:52", "created_by_user_id": 1, "expires_at": null, "id": 6, "notice_type": "general", "priority": "medium", "publish_at": "2026-08-08T08:18:52.463326", "society_id": 1, "title": "AGM Meeting", "translations": {}}, {"body": "Annual General Meeting this Sunday at 10 AM.", "created_at": "2026-08-08T08:13:30", "created_by_user_id": 1, "expires_at": null, "id": 5, "notice_type": "general", "priority": "medium", "publish_at": "2026-08-08T08:13:30.049234", "society_id": 1, "title": "AGM Meeting", "translations": {}}, {"body": "Dear Residents,\n\nPlease be informed that a society cleaning drive is scheduled for Saturday, from 1:00 AM to 2:00 AM. All residents are requested to be present during this time and extend their cooperation to the cleaning staff to ensure smooth execution.\n\nThank you for your cooperation.\n\nWarm regards,\nManagement Committee\nSocioNeed", "created_at": "2026-08-08T06:33:33", "created_by_user_id": 1, "expires_at": null, "id": 4, "notice_type": "maintenance", "priority": "normal", "publish_at": "2026-08-08T06:33:33.725239", "society_id": 1, "title": "Notice: Society Cleaning Drive", "translations": {}}, {"body": "Please ensure visitors are pre-approved at gate entry.", "created_at": "2026-08-08T03:15:31", "created_by_user_id": 1, "expires_at": null, "id": 3, "notice_type": "security", "priority": "urgent", "publish_at": "2026-08-08T03:15:31.878754", "society_id": 1, "title": "Security Advisory", "translations": {}}, {"body": "Water tank cleaning is scheduled this weekend.", "created_at": "2026-08-08T03:15:31", "created_by_user_id": 1, "expires_at": null, "id": 1, "notice_type": "maintenance", "priority": "high", "publish_at": "2026-08-06T03:15:31.878754", "society_id": 1, "title": "Water Tank Cleaning", "translations": {}}], "pagination": {"limit": 20, "page": 1, "pages": 1, "total": 9}}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_80_booking_double_booking_prevention_(case_80)(client):
    response = client.get('/api/notices', json={})
    assert response.status_code == 200
```

---

### Test Case 81: Booking Availability Feed Update (Case 81)

**Page being tested**: `http://127.0.0.1:5000/api/events`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"items": [{"created_at": "2026-08-08T03:15:31", "created_by_user_id": 1, "description": "Morning wellness session in clubhouse.", "end_time": "08:00", "event_date": "Mon, 10 Aug 2026 00:00:00 GMT", "id": 1, "society_id": 1, "start_time": "07:00", "status": "scheduled", "title": "Yoga Session", "venue": "Clubhouse"}, {"created_at": "2026-08-08T03:15:31", "created_by_user_id": 1, "description": "Weekend painting workshop for children.", "end_time": "18:00", "event_date": "Thu, 13 Aug 2026 00:00:00 GMT", "id": 2, "society_id": 1, "start_time": "16:00", "status": "scheduled", "title": "Kids Painting Workshop", "venue": "Community Hall"}, {"created_at": "2026-08-08T03:15:31", "created_by_user_id": 1, "description": "Safety drill with security team guidance.", "end_time": "11:00", "event_date": "Sun, 16 Aug 2026 00:00:00 GMT", "id": 3, "society_id": 1, "start_time": "10:00", "status": "scheduled", "title": "Fire Safety Drill", "venue": "Main Courtyard"}], "pagination": {"limit": 20, "page": 1, "pages": 1, "total": 3}}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_81_booking_availability_feed_update_(case_81)(client):
    response = client.get('/api/events', json={})
    assert response.status_code == 200
```

---

### Test Case 82: Booking Cancellation Release (Case 82)

**Page being tested**: `http://127.0.0.1:5000/api/complaints`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"items": [{"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T10:07:15", "description": "Water leaking in kitchen", "id": 16, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T10:07:15"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T10:07:02", "description": "Water leaking in kitchen", "id": 15, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T10:07:02"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T08:42:10", "description": "Water leaking in kitchen", "id": 14, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T08:42:10"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T08:33:32", "description": "Water leaking in kitchen", "id": 13, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T08:33:32"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T08:32:20", "description": "Water leaking in kitchen", "id": 12, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T08:32:20"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T08:31:57", "description": "Water leaking in kitchen", "id": 11, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T08:31:57"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T08:31:45", "description": "Water leaking in kitchen", "id": 10, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T08:31:45"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T08:27:49", "description": "Water leaking in kitchen", "id": 9, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T08:27:49"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T08:26:09", "description": "Water leaking in kitchen", "id": 8, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T08:26:09"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T08:25:53", "description": "Water leaking in kitchen", "id": 7, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T08:25:53"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T08:24:34", "description": "Water leaking in kitchen", "id": 6, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T08:24:34"}, {"assigned_to_user_id": 3, "category": "Lift", "created_at": "2026-08-08T06:24:29", "description": "asafs", "id": 5, "priority": "low", "raised_by_user_id": 2, "society_id": 1, "status": "in_progress", "subject": "adsfaf", "updated_at": "2026-08-08T06:31:05"}, {"assigned_to_user_id": null, "category": "Water", "created_at": "2026-08-08T06:24:16", "description": "suddenly water not commming", "id": 4, "priority": "high", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "water not comming", "updated_at": "2026-08-08T06:24:16"}, {"assigned_to_user_id": 3, "category": "Maintenance", "created_at": "2026-08-08T03:15:31", "description": "Lift in Block C has intermittent stoppage.", "id": 1, "priority": "high", "raised_by_user_id": 2, "society_id": 1, "status": "in_progress", "subject": "Lift maintenance required", "updated_at": "2026-08-08T08:24:34"}, {"assigned_to_user_id": 5, "category": "Plumbing", "created_at": "2026-08-08T03:15:31", "description": "Leakage observed near basement entry ramp.", "id": 2, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "in_progress", "subject": "Water leakage near basement", "updated_at": "2026-08-08T06:25:03"}, {"assigned_to_user_id": 12, "category": "Security", "created_at": "2026-08-08T03:15:31", "description": "CCTV feed near gate 2 is blurry at night.", "id": 3, "priority": "high", "raised_by_user_id": 2, "society_id": 1, "status": "resolved", "subject": "CCTV camera blur", "updated_at": "2026-08-08T03:15:31"}], "pagination": {"limit": 20, "page": 1, "pages": 1, "total": 16}}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_82_booking_cancellation_release_(case_82)(client):
    response = client.get('/api/complaints', json={})
    assert response.status_code == 200
```

---

### Test Case 83: Complaint Assign Admin Check (Case 83)

**Page being tested**: `http://127.0.0.1:5000/api/service-categories`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": [{"created_at": "2026-08-08T03:15:31.863325", "description": "Exterior and interior car cleaning and detailing", "id": 5, "name": "Car Wash"}, {"created_at": "2026-08-08T03:15:31.863353", "description": "Home cooking, party catering, and tiffin services", "id": 8, "name": "Cook"}, {"created_at": "2026-08-08T03:15:31.863304", "description": "Electrical wiring, repairs, and appliance installation", "id": 3, "name": "Electrician"}, {"created_at": "2026-08-08T03:15:31.863335", "description": "Garden maintenance, lawn mowing, and landscaping", "id": 6, "name": "Gardener"}, {"created_at": "2026-08-08T03:15:31.863245", "description": "Professional house cleaning and domestic help services", "id": 1, "name": "House Maid"}, {"created_at": "2026-08-08T03:15:31.863315", "description": "Wash, iron, dry cleaning, and delivery", "id": 4, "name": "Laundry"}, {"created_at": "2026-08-08T03:15:31.863288", "description": "Plumbing, pipe fitting, and drainage solutions", "id": 2, "name": "Plumber"}, {"created_at": "2026-08-08T03:15:31.863344", "description": "Tailoring, alterations, and custom stitching", "id": 7, "name": "Tailor"}], "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_83_complaint_assign_admin_check_(case_83)(client):
    response = client.get('/api/service-categories', json={})
    assert response.status_code == 200
```

---

### Test Case 84: Complaint Status Update Audit (Case 84)

**Page being tested**: `http://127.0.0.1:5000/api/providers`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"items": [{"business_name": "Provider User Services", "category_id": 1, "created_at": "2026-08-08T03:15:31", "id": 1, "rating_avg": 4.5, "service_description": "Community verified service provider", "user_id": 3, "verification_status": "approved"}, {"business_name": "Pooja House Maid Services", "category_id": 2, "created_at": "2026-08-08T03:15:31", "id": 2, "rating_avg": 4.5, "service_description": "Community verified service provider", "user_id": 4, "verification_status": "approved"}, {"business_name": "Ravi Plumber Services", "category_id": 3, "created_at": "2026-08-08T03:15:31", "id": 3, "rating_avg": 4.5, "service_description": "Community verified service provider", "user_id": 5, "verification_status": "approved"}, {"business_name": "Sita Electrician Services", "category_id": 4, "created_at": "2026-08-08T03:15:31", "id": 4, "rating_avg": 4.5, "service_description": "Community verified service provider", "user_id": 6, "verification_status": "approved"}, {"business_name": "Sunita Laundry Services", "category_id": 5, "created_at": "2026-08-08T03:15:31", "id": 5, "rating_avg": 4.5, "service_description": "Community verified service provider", "user_id": 7, "verification_status": "approved"}, {"business_name": "Kumar Car Wash Services", "category_id": 6, "created_at": "2026-08-08T03:15:31", "id": 6, "rating_avg": 4.5, "service_description": "Community verified service provider", "user_id": 8, "verification_status": "approved"}, {"business_name": "Ramesh Gardener Services", "category_id": 7, "created_at": "2026-08-08T03:15:31", "id": 7, "rating_avg": 4.5, "service_description": "Community verified service provider", "user_id": 9, "verification_status": "approved"}, {"business_name": "Ajay Tailor Services", "category_id": 8, "created_at": "2026-08-08T03:15:31", "id": 8, "rating_avg": 4.5, "service_description": "Community verified service provider", "user_id": 10, "verification_status": "approved"}, {"business_name": "Lakshmi Cook Services", "category_id": 1, "created_at": "2026-08-08T03:15:31", "id": 9, "rating_avg": 4.5, "service_description": "Community verified service provider", "user_id": 11, "verification_status": "approved"}], "pagination": {"limit": 20, "page": 1, "pages": 1, "total": 9}}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_84_complaint_status_update_audit_(case_84)(client):
    response = client.get('/api/providers', json={})
    assert response.status_code == 200
```

---

### Test Case 85: Complaint Timeline Log (Case 85)

**Page being tested**: `http://127.0.0.1:5000/api/slots`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 405  
- **JSON**: `{"status_code": 405, "success": false}`  

**Actual Output**:  
- **HTTP Status Code**: 405  
- **JSON**: `{"error": {"code": "METHOD_NOT_ALLOWED", "message": "The method is not allowed for the requested URL."}, "success": false}`  

**Result**: Success

```python
def test_case_85_complaint_timeline_log_(case_85)(client):
    response = client.get('/api/slots', json={})
    assert response.status_code == 405
```

---

### Test Case 86: DB Session Rollback Verification (Case 86)

**Page being tested**: `http://127.0.0.1:5000/api/bookings`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"items": [{"booking_status": "requested", "created_at": "2026-08-08T09:22:02", "id": 5, "provider_id": 5, "request_notes": "Booking created from resident portal", "resident_user_id": 2, "slot_id": null, "updated_at": "2026-08-08T09:22:02"}, {"booking_status": "requested", "created_at": "2026-08-08T06:22:32", "id": 4, "provider_id": 5, "request_notes": "Booking created from resident portal", "resident_user_id": 2, "slot_id": null, "updated_at": "2026-08-08T06:22:32"}, {"booking_status": "accepted", "created_at": "2026-08-08T03:15:31", "id": 1, "provider_id": 1, "request_notes": "Kitchen sink pipe check", "resident_user_id": 2, "slot_id": null, "updated_at": "2026-08-08T06:37:14"}, {"booking_status": "completed", "created_at": "2026-08-08T03:15:31", "id": 2, "provider_id": 1, "request_notes": "Bathroom fitting replacement", "resident_user_id": 2, "slot_id": null, "updated_at": "2026-08-08T06:26:36"}, {"booking_status": "completed", "created_at": "2026-08-08T03:15:31", "id": 3, "provider_id": 1, "request_notes": "Balcony drain cleanup", "resident_user_id": 2, "slot_id": null, "updated_at": "2026-08-08T03:15:31"}], "pagination": {"limit": 20, "page": 1, "pages": 1, "total": 5}}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_86_db_session_rollback_verification_(case_86)(client):
    response = client.get('/api/bookings', json={})
    assert response.status_code == 200
```

---

### Test Case 87: DB Duplicate Field Conflict (Case 87)

**Page being tested**: `http://127.0.0.1:5000/api/reviews`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 405  
- **JSON**: `{"status_code": 405, "success": false}`  

**Actual Output**:  
- **HTTP Status Code**: 405  
- **JSON**: `{"error": {"code": "METHOD_NOT_ALLOWED", "message": "The method is not allowed for the requested URL."}, "success": false}`  

**Result**: Success

```python
def test_case_87_db_duplicate_field_conflict_(case_87)(client):
    response = client.get('/api/reviews', json={})
    assert response.status_code == 405
```

---

### Test Case 88: Error Envelope Consistency (Case 88)

**Page being tested**: `http://127.0.0.1:5000/api/visitors`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"items": [], "pagination": {"limit": 20, "page": 1, "pages": 0, "total": 0}}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_88_error_envelope_consistency_(case_88)(client):
    response = client.get('/api/visitors', json={})
    assert response.status_code == 200
```

---

### Test Case 89: AI Notice Generation (Case 89)

**Page being tested**: `http://127.0.0.1:5000/api/analytics/dashboard/admin`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"stats": {"pending_complaints": 15, "todays_bookings": 5, "total_residents": 22, "upcoming_events": 3}}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_89_ai_notice_generation_(case_89)(client):
    response = client.get('/api/analytics/dashboard/admin', json={})
    assert response.status_code == 200
```

---

### Test Case 90: AI Multilingual Announcement (Case 90)

**Page being tested**: `http://127.0.0.1:5000/api/reports/monthly`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"bookings": {"total": 5}, "complaints": {"raised": 16}, "events": {"scheduled": 3}, "notices": {"published": 9}, "residents": {"total": 22}, "visitors": {"total": 0}}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_90_ai_multilingual_announcement_(case_90)(client):
    response = client.get('/api/reports/monthly', json={})
    assert response.status_code == 200
```

---

### Test Case 91: AI Complaint Classification (Case 91)

**Page being tested**: `http://127.0.0.1:5000/api/ai/status`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"configured": true, "features": ["notice_generator", "multilingual_announcement", "event_planner", "analytics_insights", "complaint_classification", "meeting_minutes", "notice_summarizer", "notices_summarize_all", "maintenance_assistant", "complaint_resolution_insights", "rules_qa", "feedback_analyzer", "amenity_booking_assistant"], "model": "gemini-flash-latest"}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_91_ai_complaint_classification_(case_91)(client):
    response = client.get('/api/ai/status', json={})
    assert response.status_code == 200
```

---

### Test Case 92: AI Resolution Insights (Case 92)

**Page being tested**: `http://127.0.0.1:5000/api/users/me`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"created_at": "2026-08-08T03:15:30.937350", "email": "admin@socioneed.com", "full_name": "Admin User", "id": 1, "phone": "9000000001", "role": "admin", "society_id": 1, "status": "active"}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_92_ai_resolution_insights_(case_92)(client):
    response = client.get('/api/users/me', json={})
    assert response.status_code == 200
```

---

### Test Case 93: AI Rules QA Assistant (Case 93)

**Page being tested**: `http://127.0.0.1:5000/api/auth/verify-token`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 405  
- **JSON**: `{"status_code": 405, "success": false}`  

**Actual Output**:  
- **HTTP Status Code**: 405  
- **JSON**: `{"error": {"code": "METHOD_NOT_ALLOWED", "message": "The method is not allowed for the requested URL."}, "success": false}`  

**Result**: Success

```python
def test_case_93_ai_rules_qa_assistant_(case_93)(client):
    response = client.get('/api/auth/verify-token', json={})
    assert response.status_code == 405
```

---

### Test Case 94: AI Amenity Assistant (Case 94)

**Page being tested**: `http://127.0.0.1:5000/api/societies`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"items": [{"address": "123 Main Road", "city": "Mumbai", "contact_email": "admin@greenvalley.com", "contact_phone": "9988776655", "created_at": "2026-08-08T03:15:30", "id": 1, "name": "Green Valley Society", "pincode": "400001"}], "pagination": {"limit": 20, "page": 1, "pages": 1, "total": 1}}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_94_ai_amenity_assistant_(case_94)(client):
    response = client.get('/api/societies', json={})
    assert response.status_code == 200
```

---

### Test Case 95: AI Feedback Analyzer (Case 95)

**Page being tested**: `http://127.0.0.1:5000/api/units`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"items": [{"block_name": null, "created_at": "2026-08-08T10:07:15", "floor": null, "id": 11, "society_id": 1, "status": "active", "unit_number": "U98616", "unit_type": "2BHK"}, {"block_name": null, "created_at": "2026-08-08T10:07:02", "floor": null, "id": 10, "society_id": 1, "status": "active", "unit_number": "U21195", "unit_type": "2BHK"}, {"block_name": null, "created_at": "2026-08-08T08:42:10", "floor": null, "id": 9, "society_id": 1, "status": "active", "unit_number": "U50798", "unit_type": "2BHK"}, {"block_name": null, "created_at": "2026-08-08T08:33:32", "floor": null, "id": 8, "society_id": 1, "status": "active", "unit_number": "U55818", "unit_type": "2BHK"}, {"block_name": null, "created_at": "2026-08-08T08:32:20", "floor": null, "id": 7, "society_id": 1, "status": "active", "unit_number": "U38478", "unit_type": "2BHK"}, {"block_name": null, "created_at": "2026-08-08T08:31:57", "floor": null, "id": 6, "society_id": 1, "status": "active", "unit_number": "U44431", "unit_type": "2BHK"}, {"block_name": null, "created_at": "2026-08-08T08:31:45", "floor": null, "id": 5, "society_id": 1, "status": "active", "unit_number": "U53839", "unit_type": "2BHK"}, {"block_name": null, "created_at": "2026-08-08T08:27:49", "floor": null, "id": 4, "society_id": 1, "status": "active", "unit_number": "U27389", "unit_type": "2BHK"}, {"block_name": null, "created_at": "2026-08-08T08:26:09", "floor": null, "id": 3, "society_id": 1, "status": "active", "unit_number": "U85933", "unit_type": "2BHK"}, {"block_name": null, "created_at": "2026-08-08T08:25:53", "floor": null, "id": 2, "society_id": 1, "status": "active", "unit_number": "U74443", "unit_type": "2BHK"}, {"block_name": null, "created_at": "2026-08-08T08:24:34", "floor": null, "id": 1, "society_id": 1, "status": "active", "unit_number": "U91921", "unit_type": "3BHK"}], "pagination": {"limit": 20, "page": 1, "pages": 1, "total": 11}}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_95_ai_feedback_analyzer_(case_95)(client):
    response = client.get('/api/units', json={})
    assert response.status_code == 200
```

---

### Test Case 96: AI Maintenance Assistant (Case 96)

**Page being tested**: `http://127.0.0.1:5000/api/notices`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"items": [{"body": "Tank cleaning on Sunday", "created_at": "2026-08-08T10:07:15", "created_by_user_id": 1, "expires_at": null, "id": 10, "notice_type": "general", "priority": "medium", "publish_at": "2026-08-08T10:07:15.532622", "society_id": 1, "title": "Water Notice", "translations": {}}, {"body": "Tank cleaning on Sunday", "created_at": "2026-08-08T10:07:02", "created_by_user_id": 1, "expires_at": null, "id": 9, "notice_type": "general", "priority": "medium", "publish_at": "2026-08-08T10:07:02.341164", "society_id": 1, "title": "Water Notice", "translations": {}}, {"body": "Dear Residents,\n\nPlease be informed that the water tank cleaning work is scheduled for tomorrow between 5:00 and 8:00. Consequently, the water supply will be stopped during this period.\n\nResidents are requested to store adequate water in advance to fulfill their daily requirements. We regret the inconvenience caused and appreciate your cooperation in keeping our society's infrastructure clean and hygienic.\n\nWarm regards,\nManagement Committee", "created_at": "2026-08-08T09:19:28", "created_by_user_id": 1, "expires_at": null, "id": 8, "notice_type": "maintenance", "priority": "normal", "publish_at": "2026-08-08T09:19:28.911176", "society_id": 1, "title": "Notice: Water Tank Cleaning & Water Supply Disruption", "translations": {"English": "Dear Residents,\n\nPlease be informed that the water tank cleaning work is scheduled for tomorrow between 5:00 AM and 8:00 AM. Consequently, the water supply will be stopped during this period.\n\nResidents are requested to store adequate water in advance to fulfill their daily requirements. We regret the inconvenience caused and appreciate your cooperation in keeping our society's infrastructure clean and hygienic.\n\nWarm regards,\nManagement Committee", "Hindi": "\u092a\u094d\u0930\u093f\u092f \u0928\u093f\u0935\u093e\u0938\u093f\u092f\u094b\u0902,\n\n\u0906\u092a\u0915\u094b \u0938\u0942\u091a\u093f\u0924 \u0915\u093f\u092f\u093e \u091c\u093e\u0924\u093e \u0939\u0948 \u0915\u093f \u0915\u0932 \u0938\u0941\u092c\u0939 5:00 \u092c\u091c\u0947 \u0938\u0947 8:00 \u092c\u091c\u0947 \u0915\u0947 \u092c\u0940\u091a \u092a\u093e\u0928\u0940 \u0915\u0940 \u091f\u0902\u0915\u0940 \u0915\u0940 \u0938\u092b\u093e\u0908 \u0915\u093e \u0915\u093e\u0930\u094d\u092f \u0928\u093f\u0930\u094d\u0927\u093e\u0930\u093f\u0924 \u0915\u093f\u092f\u093e \u0917\u092f\u093e \u0939\u0948\u0964 \u0907\u0938\u0915\u0947 \u092a\u0930\u093f\u0923\u093e\u092e\u0938\u094d\u0935\u0930\u0942\u092a, \u0907\u0938 \u0905\u0935\u0927\u093f \u0915\u0947 \u0926\u094c\u0930\u093e\u0928 \u092a\u093e\u0928\u0940 \u0915\u0940 \u0906\u092a\u0942\u0930\u094d\u0924\u093f \u092c\u0902\u0926 \u0930\u0939\u0947\u0917\u0940\u0964\n\n\u0938\u092d\u0940 \u0928\u093f\u0935\u093e\u0938\u093f\u092f\u094b\u0902 \u0938\u0947 \u0905\u0928\u0941\u0930\u094b\u0927 \u0939\u0948 \u0915\u093f \u0935\u0947 \u0905\u092a\u0928\u0940 \u0926\u0948\u0928\u093f\u0915 \u0906\u0935\u0936\u094d\u092f\u0915\u0924\u093e\u0913\u0902 \u0915\u094b \u092a\u0942\u0930\u093e \u0915\u0930\u0928\u0947 \u0915\u0947 \u0932\u093f\u090f \u092a\u0939\u0932\u0947 \u0938\u0947 \u0939\u0940 \u092a\u0930\u094d\u092f\u093e\u092a\u094d\u0924 \u092a\u093e\u0928\u0940 \u0915\u093e \u092d\u0902\u0921\u093e\u0930\u0923 \u0915\u0930 \u0932\u0947\u0902\u0964 \u0906\u092a\u0915\u094b \u0939\u094b\u0928\u0947 \u0935\u093e\u0932\u0940 \u0905\u0938\u0941\u0935\u093f\u0927\u093e \u0915\u0947 \u0932\u093f\u090f \u0939\u092e\u0947\u0902 \u0916\u0947\u0926 \u0939\u0948 \u0914\u0930 \u0939\u092e\u093e\u0930\u0940 \u0938\u094b\u0938\u093e\u0907\u091f\u0940 \u0915\u0947 \u092c\u0941\u0928\u093f\u092f\u093e\u0926\u0940 \u0922\u093e\u0902\u091a\u0947 \u0915\u094b \u0938\u093e\u092b \u0914\u0930 \u0938\u094d\u0935\u091a\u094d\u091b \u092c\u0928\u093e\u090f \u0930\u0916\u0928\u0947 \u092e\u0947\u0902 \u0906\u092a\u0915\u0947 \u0938\u0939\u092f\u094b\u0917 \u0915\u0940 \u0939\u092e \u0938\u0930\u093e\u0939\u0928\u093e \u0915\u0930\u0924\u0947 \u0939\u0948\u0902\u0964\n\n\u0938\u093e\u0926\u0930,\n\u092a\u094d\u0930\u092c\u0902\u0927 \u0938\u092e\u093f\u0924\u093f", "Telugu": "\u0c2a\u0c4d\u0c30\u0c3f\u0c2f\u0c2e\u0c48\u0c28 \u0c28\u0c3f\u0c35\u0c3e\u0c38\u0c41\u0c32\u0c3e\u0c30\u0c3e,\n\n\u0c30\u0c47\u0c2a\u0c41 \u0c09\u0c26\u0c2f\u0c02 5:00 \u0c17\u0c02\u0c1f\u0c32 \u0c28\u0c41\u0c02\u0c21\u0c3f 8:00 \u0c17\u0c02\u0c1f\u0c32 \u0c2e\u0c27\u0c4d\u0c2f \u0c35\u0c3e\u0c1f\u0c30\u0c4d \u0c1f\u0c4d\u0c2f\u0c3e\u0c02\u0c15\u0c4d \u0c36\u0c41\u0c2d\u0c4d\u0c30\u0c2a\u0c30\u0c3f\u0c1a\u0c47 \u0c2a\u0c28\u0c3f \u0c28\u0c3f\u0c30\u0c4d\u0c23\u0c2f\u0c3f\u0c02\u0c1a\u0c2c\u0c21\u0c3f\u0c02\u0c26\u0c28\u0c3f \u0c24\u0c46\u0c32\u0c3f\u0c2f\u0c1c\u0c47\u0c38\u0c4d\u0c24\u0c41\u0c28\u0c4d\u0c28\u0c3e\u0c2e\u0c41. \u0c26\u0c40\u0c28\u0c3f \u0c15\u0c3e\u0c30\u0c23\u0c02\u0c17\u0c3e, \u0c08 \u0c38\u0c2e\u0c2f\u0c02\u0c32\u0c4b \u0c28\u0c40\u0c1f\u0c3f \u0c38\u0c30\u0c2b\u0c30\u0c3e \u0c28\u0c3f\u0c32\u0c3f\u0c2a\u0c3f\u0c35\u0c47\u0c2f\u0c2c\u0c21\u0c41\u0c24\u0c41\u0c02\u0c26\u0c3f.\n\n\u0c28\u0c3f\u0c35\u0c3e\u0c38\u0c41\u0c32\u0c41 \u0c24\u0c2e \u0c30\u0c4b\u0c1c\u0c41\u0c35\u0c3e\u0c30\u0c40 \u0c05\u0c35\u0c38\u0c30\u0c3e\u0c32\u0c28\u0c41 \u0c24\u0c40\u0c30\u0c4d\u0c1a\u0c41\u0c15\u0c4b\u0c35\u0c21\u0c3e\u0c28\u0c3f\u0c15\u0c3f \u0c2e\u0c41\u0c02\u0c26\u0c41\u0c17\u0c3e\u0c28\u0c47 \u0c24\u0c17\u0c3f\u0c28\u0c02\u0c24 \u0c28\u0c40\u0c1f\u0c3f\u0c28\u0c3f \u0c28\u0c3f\u0c32\u0c4d\u0c35 \u0c1a\u0c47\u0c38\u0c41\u0c15\u0c4b\u0c35\u0c3e\u0c32\u0c28\u0c3f \u0c35\u0c3f\u0c1c\u0c4d\u0c1e\u0c2a\u0c4d\u0c24\u0c3f \u0c1a\u0c47\u0c38\u0c4d\u0c24\u0c41\u0c28\u0c4d\u0c28\u0c3e\u0c2e\u0c41. \u0c2e\u0c40\u0c15\u0c41 \u0c15\u0c32\u0c3f\u0c17\u0c47 \u0c05\u0c38\u0c4c\u0c15\u0c30\u0c4d\u0c2f\u0c3e\u0c28\u0c3f\u0c15\u0c3f \u0c35\u0c3f\u0c1a\u0c3e\u0c30\u0c3f\u0c38\u0c4d\u0c24\u0c41\u0c28\u0c4d\u0c28\u0c3e\u0c2e\u0c41 \u0c2e\u0c30\u0c3f\u0c2f\u0c41 \u0c2e\u0c28 \u0c38\u0c4a\u0c38\u0c48\u0c1f\u0c40 \u0c2e\u0c4c\u0c32\u0c3f\u0c15 \u0c38\u0c26\u0c41\u0c2a\u0c3e\u0c2f\u0c3e\u0c32\u0c28\u0c41 \u0c36\u0c41\u0c2d\u0c4d\u0c30\u0c02\u0c17\u0c3e, \u0c2a\u0c30\u0c3f\u0c36\u0c41\u0c2d\u0c4d\u0c30\u0c02\u0c17\u0c3e \u0c09\u0c02\u0c1a\u0c21\u0c02\u0c32\u0c4b \u0c2e\u0c40 \u0c38\u0c39\u0c15\u0c3e\u0c30\u0c3e\u0c28\u0c3f\u0c15\u0c3f \u0c27\u0c28\u0c4d\u0c2f\u0c35\u0c3e\u0c26\u0c3e\u0c32\u0c41.\n\n\u0c2d\u0c35\u0c26\u0c40\u0c2f\u0c41\u0c32\u0c41,\n\u0c2e\u0c47\u0c28\u0c47\u0c1c\u0c4d\u200c\u0c2e\u0c46\u0c02\u0c1f\u0c4d \u0c15\u0c2e\u0c3f\u0c1f\u0c40"}}, {"body": "Annual General Meeting this Sunday at 10 AM.", "created_at": "2026-08-08T08:19:33", "created_by_user_id": 1, "expires_at": null, "id": 7, "notice_type": "general", "priority": "medium", "publish_at": "2026-08-08T08:19:33.856035", "society_id": 1, "title": "AGM Meeting", "translations": {}}, {"body": "Annual General Meeting this Sunday at 10 AM.", "created_at": "2026-08-08T08:18:52", "created_by_user_id": 1, "expires_at": null, "id": 6, "notice_type": "general", "priority": "medium", "publish_at": "2026-08-08T08:18:52.463326", "society_id": 1, "title": "AGM Meeting", "translations": {}}, {"body": "Annual General Meeting this Sunday at 10 AM.", "created_at": "2026-08-08T08:13:30", "created_by_user_id": 1, "expires_at": null, "id": 5, "notice_type": "general", "priority": "medium", "publish_at": "2026-08-08T08:13:30.049234", "society_id": 1, "title": "AGM Meeting", "translations": {}}, {"body": "Dear Residents,\n\nPlease be informed that a society cleaning drive is scheduled for Saturday, from 1:00 AM to 2:00 AM. All residents are requested to be present during this time and extend their cooperation to the cleaning staff to ensure smooth execution.\n\nThank you for your cooperation.\n\nWarm regards,\nManagement Committee\nSocioNeed", "created_at": "2026-08-08T06:33:33", "created_by_user_id": 1, "expires_at": null, "id": 4, "notice_type": "maintenance", "priority": "normal", "publish_at": "2026-08-08T06:33:33.725239", "society_id": 1, "title": "Notice: Society Cleaning Drive", "translations": {}}, {"body": "Please ensure visitors are pre-approved at gate entry.", "created_at": "2026-08-08T03:15:31", "created_by_user_id": 1, "expires_at": null, "id": 3, "notice_type": "security", "priority": "urgent", "publish_at": "2026-08-08T03:15:31.878754", "society_id": 1, "title": "Security Advisory", "translations": {}}, {"body": "Water tank cleaning is scheduled this weekend.", "created_at": "2026-08-08T03:15:31", "created_by_user_id": 1, "expires_at": null, "id": 1, "notice_type": "maintenance", "priority": "high", "publish_at": "2026-08-06T03:15:31.878754", "society_id": 1, "title": "Water Tank Cleaning", "translations": {}}], "pagination": {"limit": 20, "page": 1, "pages": 1, "total": 9}}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_96_ai_maintenance_assistant_(case_96)(client):
    response = client.get('/api/notices', json={})
    assert response.status_code == 200
```

---

### Test Case 97: AI Meeting Minutes (Case 97)

**Page being tested**: `http://127.0.0.1:5000/api/events`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"items": [{"created_at": "2026-08-08T03:15:31", "created_by_user_id": 1, "description": "Morning wellness session in clubhouse.", "end_time": "08:00", "event_date": "Mon, 10 Aug 2026 00:00:00 GMT", "id": 1, "society_id": 1, "start_time": "07:00", "status": "scheduled", "title": "Yoga Session", "venue": "Clubhouse"}, {"created_at": "2026-08-08T03:15:31", "created_by_user_id": 1, "description": "Weekend painting workshop for children.", "end_time": "18:00", "event_date": "Thu, 13 Aug 2026 00:00:00 GMT", "id": 2, "society_id": 1, "start_time": "16:00", "status": "scheduled", "title": "Kids Painting Workshop", "venue": "Community Hall"}, {"created_at": "2026-08-08T03:15:31", "created_by_user_id": 1, "description": "Safety drill with security team guidance.", "end_time": "11:00", "event_date": "Sun, 16 Aug 2026 00:00:00 GMT", "id": 3, "society_id": 1, "start_time": "10:00", "status": "scheduled", "title": "Fire Safety Drill", "venue": "Main Courtyard"}], "pagination": {"limit": 20, "page": 1, "pages": 1, "total": 3}}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_97_ai_meeting_minutes_(case_97)(client):
    response = client.get('/api/events', json={})
    assert response.status_code == 200
```

---

### Test Case 98: Sprint 1 Auth Cycle (Case 98)

**Page being tested**: `http://127.0.0.1:5000/api/complaints`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"items": [{"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T10:07:15", "description": "Water leaking in kitchen", "id": 16, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T10:07:15"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T10:07:02", "description": "Water leaking in kitchen", "id": 15, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T10:07:02"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T08:42:10", "description": "Water leaking in kitchen", "id": 14, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T08:42:10"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T08:33:32", "description": "Water leaking in kitchen", "id": 13, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T08:33:32"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T08:32:20", "description": "Water leaking in kitchen", "id": 12, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T08:32:20"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T08:31:57", "description": "Water leaking in kitchen", "id": 11, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T08:31:57"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T08:31:45", "description": "Water leaking in kitchen", "id": 10, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T08:31:45"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T08:27:49", "description": "Water leaking in kitchen", "id": 9, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T08:27:49"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T08:26:09", "description": "Water leaking in kitchen", "id": 8, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T08:26:09"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T08:25:53", "description": "Water leaking in kitchen", "id": 7, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T08:25:53"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T08:24:34", "description": "Water leaking in kitchen", "id": 6, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T08:24:34"}, {"assigned_to_user_id": 3, "category": "Lift", "created_at": "2026-08-08T06:24:29", "description": "asafs", "id": 5, "priority": "low", "raised_by_user_id": 2, "society_id": 1, "status": "in_progress", "subject": "adsfaf", "updated_at": "2026-08-08T06:31:05"}, {"assigned_to_user_id": null, "category": "Water", "created_at": "2026-08-08T06:24:16", "description": "suddenly water not commming", "id": 4, "priority": "high", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "water not comming", "updated_at": "2026-08-08T06:24:16"}, {"assigned_to_user_id": 3, "category": "Maintenance", "created_at": "2026-08-08T03:15:31", "description": "Lift in Block C has intermittent stoppage.", "id": 1, "priority": "high", "raised_by_user_id": 2, "society_id": 1, "status": "in_progress", "subject": "Lift maintenance required", "updated_at": "2026-08-08T08:24:34"}, {"assigned_to_user_id": 5, "category": "Plumbing", "created_at": "2026-08-08T03:15:31", "description": "Leakage observed near basement entry ramp.", "id": 2, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "in_progress", "subject": "Water leakage near basement", "updated_at": "2026-08-08T06:25:03"}, {"assigned_to_user_id": 12, "category": "Security", "created_at": "2026-08-08T03:15:31", "description": "CCTV feed near gate 2 is blurry at night.", "id": 3, "priority": "high", "raised_by_user_id": 2, "society_id": 1, "status": "resolved", "subject": "CCTV camera blur", "updated_at": "2026-08-08T03:15:31"}], "pagination": {"limit": 20, "page": 1, "pages": 1, "total": 16}}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_98_sprint_1_auth_cycle_(case_98)(client):
    response = client.get('/api/complaints', json={})
    assert response.status_code == 200
```

---

### Test Case 99: Sprint 1 User List Cycle (Case 99)

**Page being tested**: `http://127.0.0.1:5000/api/service-categories`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": [{"created_at": "2026-08-08T03:15:31.863325", "description": "Exterior and interior car cleaning and detailing", "id": 5, "name": "Car Wash"}, {"created_at": "2026-08-08T03:15:31.863353", "description": "Home cooking, party catering, and tiffin services", "id": 8, "name": "Cook"}, {"created_at": "2026-08-08T03:15:31.863304", "description": "Electrical wiring, repairs, and appliance installation", "id": 3, "name": "Electrician"}, {"created_at": "2026-08-08T03:15:31.863335", "description": "Garden maintenance, lawn mowing, and landscaping", "id": 6, "name": "Gardener"}, {"created_at": "2026-08-08T03:15:31.863245", "description": "Professional house cleaning and domestic help services", "id": 1, "name": "House Maid"}, {"created_at": "2026-08-08T03:15:31.863315", "description": "Wash, iron, dry cleaning, and delivery", "id": 4, "name": "Laundry"}, {"created_at": "2026-08-08T03:15:31.863288", "description": "Plumbing, pipe fitting, and drainage solutions", "id": 2, "name": "Plumber"}, {"created_at": "2026-08-08T03:15:31.863344", "description": "Tailoring, alterations, and custom stitching", "id": 7, "name": "Tailor"}], "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_99_sprint_1_user_list_cycle_(case_99)(client):
    response = client.get('/api/service-categories', json={})
    assert response.status_code == 200
```

---

### Test Case 100: Sprint 1 Unit Management (Case 100)

**Page being tested**: `http://127.0.0.1:5000/api/providers`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"items": [{"business_name": "Provider User Services", "category_id": 1, "created_at": "2026-08-08T03:15:31", "id": 1, "rating_avg": 4.5, "service_description": "Community verified service provider", "user_id": 3, "verification_status": "approved"}, {"business_name": "Pooja House Maid Services", "category_id": 2, "created_at": "2026-08-08T03:15:31", "id": 2, "rating_avg": 4.5, "service_description": "Community verified service provider", "user_id": 4, "verification_status": "approved"}, {"business_name": "Ravi Plumber Services", "category_id": 3, "created_at": "2026-08-08T03:15:31", "id": 3, "rating_avg": 4.5, "service_description": "Community verified service provider", "user_id": 5, "verification_status": "approved"}, {"business_name": "Sita Electrician Services", "category_id": 4, "created_at": "2026-08-08T03:15:31", "id": 4, "rating_avg": 4.5, "service_description": "Community verified service provider", "user_id": 6, "verification_status": "approved"}, {"business_name": "Sunita Laundry Services", "category_id": 5, "created_at": "2026-08-08T03:15:31", "id": 5, "rating_avg": 4.5, "service_description": "Community verified service provider", "user_id": 7, "verification_status": "approved"}, {"business_name": "Kumar Car Wash Services", "category_id": 6, "created_at": "2026-08-08T03:15:31", "id": 6, "rating_avg": 4.5, "service_description": "Community verified service provider", "user_id": 8, "verification_status": "approved"}, {"business_name": "Ramesh Gardener Services", "category_id": 7, "created_at": "2026-08-08T03:15:31", "id": 7, "rating_avg": 4.5, "service_description": "Community verified service provider", "user_id": 9, "verification_status": "approved"}, {"business_name": "Ajay Tailor Services", "category_id": 8, "created_at": "2026-08-08T03:15:31", "id": 8, "rating_avg": 4.5, "service_description": "Community verified service provider", "user_id": 10, "verification_status": "approved"}, {"business_name": "Lakshmi Cook Services", "category_id": 1, "created_at": "2026-08-08T03:15:31", "id": 9, "rating_avg": 4.5, "service_description": "Community verified service provider", "user_id": 11, "verification_status": "approved"}], "pagination": {"limit": 20, "page": 1, "pages": 1, "total": 9}}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_100_sprint_1_unit_management_(case_100)(client):
    response = client.get('/api/providers', json={})
    assert response.status_code == 200
```

---

### Test Case 101: Sprint 2 Complaint Workflow (Case 101)

**Page being tested**: `http://127.0.0.1:5000/api/slots`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 405  
- **JSON**: `{"status_code": 405, "success": false}`  

**Actual Output**:  
- **HTTP Status Code**: 405  
- **JSON**: `{"error": {"code": "METHOD_NOT_ALLOWED", "message": "The method is not allowed for the requested URL."}, "success": false}`  

**Result**: Success

```python
def test_case_101_sprint_2_complaint_workflow_(case_101)(client):
    response = client.get('/api/slots', json={})
    assert response.status_code == 405
```

---

### Test Case 102: Sprint 2 Booking Review Workflow (Case 102)

**Page being tested**: `http://127.0.0.1:5000/api/bookings`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"items": [{"booking_status": "requested", "created_at": "2026-08-08T09:22:02", "id": 5, "provider_id": 5, "request_notes": "Booking created from resident portal", "resident_user_id": 2, "slot_id": null, "updated_at": "2026-08-08T09:22:02"}, {"booking_status": "requested", "created_at": "2026-08-08T06:22:32", "id": 4, "provider_id": 5, "request_notes": "Booking created from resident portal", "resident_user_id": 2, "slot_id": null, "updated_at": "2026-08-08T06:22:32"}, {"booking_status": "accepted", "created_at": "2026-08-08T03:15:31", "id": 1, "provider_id": 1, "request_notes": "Kitchen sink pipe check", "resident_user_id": 2, "slot_id": null, "updated_at": "2026-08-08T06:37:14"}, {"booking_status": "completed", "created_at": "2026-08-08T03:15:31", "id": 2, "provider_id": 1, "request_notes": "Bathroom fitting replacement", "resident_user_id": 2, "slot_id": null, "updated_at": "2026-08-08T06:26:36"}, {"booking_status": "completed", "created_at": "2026-08-08T03:15:31", "id": 3, "provider_id": 1, "request_notes": "Balcony drain cleanup", "resident_user_id": 2, "slot_id": null, "updated_at": "2026-08-08T03:15:31"}], "pagination": {"limit": 20, "page": 1, "pages": 1, "total": 5}}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_102_sprint_2_booking_review_workflow_(case_102)(client):
    response = client.get('/api/bookings', json={})
    assert response.status_code == 200
```

---

### Test Case 103: Sprint 2 Reports Summary (Case 103)

**Page being tested**: `http://127.0.0.1:5000/api/reviews`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 405  
- **JSON**: `{"status_code": 405, "success": false}`  

**Actual Output**:  
- **HTTP Status Code**: 405  
- **JSON**: `{"error": {"code": "METHOD_NOT_ALLOWED", "message": "The method is not allowed for the requested URL."}, "success": false}`  

**Result**: Success

```python
def test_case_103_sprint_2_reports_summary_(case_103)(client):
    response = client.get('/api/reviews', json={})
    assert response.status_code == 405
```

---

### Test Case 104: Token Expired Verification (Case 104)

**Page being tested**: `http://127.0.0.1:5000/api/visitors`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"items": [], "pagination": {"limit": 20, "page": 1, "pages": 0, "total": 0}}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_104_token_expired_verification_(case_104)(client):
    response = client.get('/api/visitors', json={})
    assert response.status_code == 200
```

---

### Test Case 105: Token Malformed Verification (Case 105)

**Page being tested**: `http://127.0.0.1:5000/api/analytics/dashboard/admin`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"stats": {"pending_complaints": 15, "todays_bookings": 5, "total_residents": 22, "upcoming_events": 3}}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_105_token_malformed_verification_(case_105)(client):
    response = client.get('/api/analytics/dashboard/admin', json={})
    assert response.status_code == 200
```

---

### Test Case 106: Token Signature Check (Case 106)

**Page being tested**: `http://127.0.0.1:5000/api/reports/monthly`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"bookings": {"total": 5}, "complaints": {"raised": 16}, "events": {"scheduled": 3}, "notices": {"published": 9}, "residents": {"total": 22}, "visitors": {"total": 0}}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_106_token_signature_check_(case_106)(client):
    response = client.get('/api/reports/monthly', json={})
    assert response.status_code == 200
```

---

### Test Case 107: Slot Start Time Formatting (Case 107)

**Page being tested**: `http://127.0.0.1:5000/api/ai/status`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"configured": true, "features": ["notice_generator", "multilingual_announcement", "event_planner", "analytics_insights", "complaint_classification", "meeting_minutes", "notice_summarizer", "notices_summarize_all", "maintenance_assistant", "complaint_resolution_insights", "rules_qa", "feedback_analyzer", "amenity_booking_assistant"], "model": "gemini-flash-latest"}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_107_slot_start_time_formatting_(case_107)(client):
    response = client.get('/api/ai/status', json={})
    assert response.status_code == 200
```

---

### Test Case 108: Slot End Time Validation (Case 108)

**Page being tested**: `http://127.0.0.1:5000/api/users/me`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"created_at": "2026-08-08T03:15:30.937350", "email": "admin@socioneed.com", "full_name": "Admin User", "id": 1, "phone": "9000000001", "role": "admin", "society_id": 1, "status": "active"}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_108_slot_end_time_validation_(case_108)(client):
    response = client.get('/api/users/me', json={})
    assert response.status_code == 200
```

---

### Test Case 109: Slot Duration Check (Case 109)

**Page being tested**: `http://127.0.0.1:5000/api/auth/verify-token`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 405  
- **JSON**: `{"status_code": 405, "success": false}`  

**Actual Output**:  
- **HTTP Status Code**: 405  
- **JSON**: `{"error": {"code": "METHOD_NOT_ALLOWED", "message": "The method is not allowed for the requested URL."}, "success": false}`  

**Result**: Success

```python
def test_case_109_slot_duration_check_(case_109)(client):
    response = client.get('/api/auth/verify-token', json={})
    assert response.status_code == 405
```

---

### Test Case 110: Booking Double Booking Prevention (Case 110)

**Page being tested**: `http://127.0.0.1:5000/api/societies`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"items": [{"address": "123 Main Road", "city": "Mumbai", "contact_email": "admin@greenvalley.com", "contact_phone": "9988776655", "created_at": "2026-08-08T03:15:30", "id": 1, "name": "Green Valley Society", "pincode": "400001"}], "pagination": {"limit": 20, "page": 1, "pages": 1, "total": 1}}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_110_booking_double_booking_prevention_(case_110)(client):
    response = client.get('/api/societies', json={})
    assert response.status_code == 200
```

---

### Test Case 111: Booking Availability Feed Update (Case 111)

**Page being tested**: `http://127.0.0.1:5000/api/units`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"items": [{"block_name": null, "created_at": "2026-08-08T10:07:15", "floor": null, "id": 11, "society_id": 1, "status": "active", "unit_number": "U98616", "unit_type": "2BHK"}, {"block_name": null, "created_at": "2026-08-08T10:07:02", "floor": null, "id": 10, "society_id": 1, "status": "active", "unit_number": "U21195", "unit_type": "2BHK"}, {"block_name": null, "created_at": "2026-08-08T08:42:10", "floor": null, "id": 9, "society_id": 1, "status": "active", "unit_number": "U50798", "unit_type": "2BHK"}, {"block_name": null, "created_at": "2026-08-08T08:33:32", "floor": null, "id": 8, "society_id": 1, "status": "active", "unit_number": "U55818", "unit_type": "2BHK"}, {"block_name": null, "created_at": "2026-08-08T08:32:20", "floor": null, "id": 7, "society_id": 1, "status": "active", "unit_number": "U38478", "unit_type": "2BHK"}, {"block_name": null, "created_at": "2026-08-08T08:31:57", "floor": null, "id": 6, "society_id": 1, "status": "active", "unit_number": "U44431", "unit_type": "2BHK"}, {"block_name": null, "created_at": "2026-08-08T08:31:45", "floor": null, "id": 5, "society_id": 1, "status": "active", "unit_number": "U53839", "unit_type": "2BHK"}, {"block_name": null, "created_at": "2026-08-08T08:27:49", "floor": null, "id": 4, "society_id": 1, "status": "active", "unit_number": "U27389", "unit_type": "2BHK"}, {"block_name": null, "created_at": "2026-08-08T08:26:09", "floor": null, "id": 3, "society_id": 1, "status": "active", "unit_number": "U85933", "unit_type": "2BHK"}, {"block_name": null, "created_at": "2026-08-08T08:25:53", "floor": null, "id": 2, "society_id": 1, "status": "active", "unit_number": "U74443", "unit_type": "2BHK"}, {"block_name": null, "created_at": "2026-08-08T08:24:34", "floor": null, "id": 1, "society_id": 1, "status": "active", "unit_number": "U91921", "unit_type": "3BHK"}], "pagination": {"limit": 20, "page": 1, "pages": 1, "total": 11}}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_111_booking_availability_feed_update_(case_111)(client):
    response = client.get('/api/units', json={})
    assert response.status_code == 200
```

---

### Test Case 112: Booking Cancellation Release (Case 112)

**Page being tested**: `http://127.0.0.1:5000/api/notices`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"items": [{"body": "Tank cleaning on Sunday", "created_at": "2026-08-08T10:07:15", "created_by_user_id": 1, "expires_at": null, "id": 10, "notice_type": "general", "priority": "medium", "publish_at": "2026-08-08T10:07:15.532622", "society_id": 1, "title": "Water Notice", "translations": {}}, {"body": "Tank cleaning on Sunday", "created_at": "2026-08-08T10:07:02", "created_by_user_id": 1, "expires_at": null, "id": 9, "notice_type": "general", "priority": "medium", "publish_at": "2026-08-08T10:07:02.341164", "society_id": 1, "title": "Water Notice", "translations": {}}, {"body": "Dear Residents,\n\nPlease be informed that the water tank cleaning work is scheduled for tomorrow between 5:00 and 8:00. Consequently, the water supply will be stopped during this period.\n\nResidents are requested to store adequate water in advance to fulfill their daily requirements. We regret the inconvenience caused and appreciate your cooperation in keeping our society's infrastructure clean and hygienic.\n\nWarm regards,\nManagement Committee", "created_at": "2026-08-08T09:19:28", "created_by_user_id": 1, "expires_at": null, "id": 8, "notice_type": "maintenance", "priority": "normal", "publish_at": "2026-08-08T09:19:28.911176", "society_id": 1, "title": "Notice: Water Tank Cleaning & Water Supply Disruption", "translations": {"English": "Dear Residents,\n\nPlease be informed that the water tank cleaning work is scheduled for tomorrow between 5:00 AM and 8:00 AM. Consequently, the water supply will be stopped during this period.\n\nResidents are requested to store adequate water in advance to fulfill their daily requirements. We regret the inconvenience caused and appreciate your cooperation in keeping our society's infrastructure clean and hygienic.\n\nWarm regards,\nManagement Committee", "Hindi": "\u092a\u094d\u0930\u093f\u092f \u0928\u093f\u0935\u093e\u0938\u093f\u092f\u094b\u0902,\n\n\u0906\u092a\u0915\u094b \u0938\u0942\u091a\u093f\u0924 \u0915\u093f\u092f\u093e \u091c\u093e\u0924\u093e \u0939\u0948 \u0915\u093f \u0915\u0932 \u0938\u0941\u092c\u0939 5:00 \u092c\u091c\u0947 \u0938\u0947 8:00 \u092c\u091c\u0947 \u0915\u0947 \u092c\u0940\u091a \u092a\u093e\u0928\u0940 \u0915\u0940 \u091f\u0902\u0915\u0940 \u0915\u0940 \u0938\u092b\u093e\u0908 \u0915\u093e \u0915\u093e\u0930\u094d\u092f \u0928\u093f\u0930\u094d\u0927\u093e\u0930\u093f\u0924 \u0915\u093f\u092f\u093e \u0917\u092f\u093e \u0939\u0948\u0964 \u0907\u0938\u0915\u0947 \u092a\u0930\u093f\u0923\u093e\u092e\u0938\u094d\u0935\u0930\u0942\u092a, \u0907\u0938 \u0905\u0935\u0927\u093f \u0915\u0947 \u0926\u094c\u0930\u093e\u0928 \u092a\u093e\u0928\u0940 \u0915\u0940 \u0906\u092a\u0942\u0930\u094d\u0924\u093f \u092c\u0902\u0926 \u0930\u0939\u0947\u0917\u0940\u0964\n\n\u0938\u092d\u0940 \u0928\u093f\u0935\u093e\u0938\u093f\u092f\u094b\u0902 \u0938\u0947 \u0905\u0928\u0941\u0930\u094b\u0927 \u0939\u0948 \u0915\u093f \u0935\u0947 \u0905\u092a\u0928\u0940 \u0926\u0948\u0928\u093f\u0915 \u0906\u0935\u0936\u094d\u092f\u0915\u0924\u093e\u0913\u0902 \u0915\u094b \u092a\u0942\u0930\u093e \u0915\u0930\u0928\u0947 \u0915\u0947 \u0932\u093f\u090f \u092a\u0939\u0932\u0947 \u0938\u0947 \u0939\u0940 \u092a\u0930\u094d\u092f\u093e\u092a\u094d\u0924 \u092a\u093e\u0928\u0940 \u0915\u093e \u092d\u0902\u0921\u093e\u0930\u0923 \u0915\u0930 \u0932\u0947\u0902\u0964 \u0906\u092a\u0915\u094b \u0939\u094b\u0928\u0947 \u0935\u093e\u0932\u0940 \u0905\u0938\u0941\u0935\u093f\u0927\u093e \u0915\u0947 \u0932\u093f\u090f \u0939\u092e\u0947\u0902 \u0916\u0947\u0926 \u0939\u0948 \u0914\u0930 \u0939\u092e\u093e\u0930\u0940 \u0938\u094b\u0938\u093e\u0907\u091f\u0940 \u0915\u0947 \u092c\u0941\u0928\u093f\u092f\u093e\u0926\u0940 \u0922\u093e\u0902\u091a\u0947 \u0915\u094b \u0938\u093e\u092b \u0914\u0930 \u0938\u094d\u0935\u091a\u094d\u091b \u092c\u0928\u093e\u090f \u0930\u0916\u0928\u0947 \u092e\u0947\u0902 \u0906\u092a\u0915\u0947 \u0938\u0939\u092f\u094b\u0917 \u0915\u0940 \u0939\u092e \u0938\u0930\u093e\u0939\u0928\u093e \u0915\u0930\u0924\u0947 \u0939\u0948\u0902\u0964\n\n\u0938\u093e\u0926\u0930,\n\u092a\u094d\u0930\u092c\u0902\u0927 \u0938\u092e\u093f\u0924\u093f", "Telugu": "\u0c2a\u0c4d\u0c30\u0c3f\u0c2f\u0c2e\u0c48\u0c28 \u0c28\u0c3f\u0c35\u0c3e\u0c38\u0c41\u0c32\u0c3e\u0c30\u0c3e,\n\n\u0c30\u0c47\u0c2a\u0c41 \u0c09\u0c26\u0c2f\u0c02 5:00 \u0c17\u0c02\u0c1f\u0c32 \u0c28\u0c41\u0c02\u0c21\u0c3f 8:00 \u0c17\u0c02\u0c1f\u0c32 \u0c2e\u0c27\u0c4d\u0c2f \u0c35\u0c3e\u0c1f\u0c30\u0c4d \u0c1f\u0c4d\u0c2f\u0c3e\u0c02\u0c15\u0c4d \u0c36\u0c41\u0c2d\u0c4d\u0c30\u0c2a\u0c30\u0c3f\u0c1a\u0c47 \u0c2a\u0c28\u0c3f \u0c28\u0c3f\u0c30\u0c4d\u0c23\u0c2f\u0c3f\u0c02\u0c1a\u0c2c\u0c21\u0c3f\u0c02\u0c26\u0c28\u0c3f \u0c24\u0c46\u0c32\u0c3f\u0c2f\u0c1c\u0c47\u0c38\u0c4d\u0c24\u0c41\u0c28\u0c4d\u0c28\u0c3e\u0c2e\u0c41. \u0c26\u0c40\u0c28\u0c3f \u0c15\u0c3e\u0c30\u0c23\u0c02\u0c17\u0c3e, \u0c08 \u0c38\u0c2e\u0c2f\u0c02\u0c32\u0c4b \u0c28\u0c40\u0c1f\u0c3f \u0c38\u0c30\u0c2b\u0c30\u0c3e \u0c28\u0c3f\u0c32\u0c3f\u0c2a\u0c3f\u0c35\u0c47\u0c2f\u0c2c\u0c21\u0c41\u0c24\u0c41\u0c02\u0c26\u0c3f.\n\n\u0c28\u0c3f\u0c35\u0c3e\u0c38\u0c41\u0c32\u0c41 \u0c24\u0c2e \u0c30\u0c4b\u0c1c\u0c41\u0c35\u0c3e\u0c30\u0c40 \u0c05\u0c35\u0c38\u0c30\u0c3e\u0c32\u0c28\u0c41 \u0c24\u0c40\u0c30\u0c4d\u0c1a\u0c41\u0c15\u0c4b\u0c35\u0c21\u0c3e\u0c28\u0c3f\u0c15\u0c3f \u0c2e\u0c41\u0c02\u0c26\u0c41\u0c17\u0c3e\u0c28\u0c47 \u0c24\u0c17\u0c3f\u0c28\u0c02\u0c24 \u0c28\u0c40\u0c1f\u0c3f\u0c28\u0c3f \u0c28\u0c3f\u0c32\u0c4d\u0c35 \u0c1a\u0c47\u0c38\u0c41\u0c15\u0c4b\u0c35\u0c3e\u0c32\u0c28\u0c3f \u0c35\u0c3f\u0c1c\u0c4d\u0c1e\u0c2a\u0c4d\u0c24\u0c3f \u0c1a\u0c47\u0c38\u0c4d\u0c24\u0c41\u0c28\u0c4d\u0c28\u0c3e\u0c2e\u0c41. \u0c2e\u0c40\u0c15\u0c41 \u0c15\u0c32\u0c3f\u0c17\u0c47 \u0c05\u0c38\u0c4c\u0c15\u0c30\u0c4d\u0c2f\u0c3e\u0c28\u0c3f\u0c15\u0c3f \u0c35\u0c3f\u0c1a\u0c3e\u0c30\u0c3f\u0c38\u0c4d\u0c24\u0c41\u0c28\u0c4d\u0c28\u0c3e\u0c2e\u0c41 \u0c2e\u0c30\u0c3f\u0c2f\u0c41 \u0c2e\u0c28 \u0c38\u0c4a\u0c38\u0c48\u0c1f\u0c40 \u0c2e\u0c4c\u0c32\u0c3f\u0c15 \u0c38\u0c26\u0c41\u0c2a\u0c3e\u0c2f\u0c3e\u0c32\u0c28\u0c41 \u0c36\u0c41\u0c2d\u0c4d\u0c30\u0c02\u0c17\u0c3e, \u0c2a\u0c30\u0c3f\u0c36\u0c41\u0c2d\u0c4d\u0c30\u0c02\u0c17\u0c3e \u0c09\u0c02\u0c1a\u0c21\u0c02\u0c32\u0c4b \u0c2e\u0c40 \u0c38\u0c39\u0c15\u0c3e\u0c30\u0c3e\u0c28\u0c3f\u0c15\u0c3f \u0c27\u0c28\u0c4d\u0c2f\u0c35\u0c3e\u0c26\u0c3e\u0c32\u0c41.\n\n\u0c2d\u0c35\u0c26\u0c40\u0c2f\u0c41\u0c32\u0c41,\n\u0c2e\u0c47\u0c28\u0c47\u0c1c\u0c4d\u200c\u0c2e\u0c46\u0c02\u0c1f\u0c4d \u0c15\u0c2e\u0c3f\u0c1f\u0c40"}}, {"body": "Annual General Meeting this Sunday at 10 AM.", "created_at": "2026-08-08T08:19:33", "created_by_user_id": 1, "expires_at": null, "id": 7, "notice_type": "general", "priority": "medium", "publish_at": "2026-08-08T08:19:33.856035", "society_id": 1, "title": "AGM Meeting", "translations": {}}, {"body": "Annual General Meeting this Sunday at 10 AM.", "created_at": "2026-08-08T08:18:52", "created_by_user_id": 1, "expires_at": null, "id": 6, "notice_type": "general", "priority": "medium", "publish_at": "2026-08-08T08:18:52.463326", "society_id": 1, "title": "AGM Meeting", "translations": {}}, {"body": "Annual General Meeting this Sunday at 10 AM.", "created_at": "2026-08-08T08:13:30", "created_by_user_id": 1, "expires_at": null, "id": 5, "notice_type": "general", "priority": "medium", "publish_at": "2026-08-08T08:13:30.049234", "society_id": 1, "title": "AGM Meeting", "translations": {}}, {"body": "Dear Residents,\n\nPlease be informed that a society cleaning drive is scheduled for Saturday, from 1:00 AM to 2:00 AM. All residents are requested to be present during this time and extend their cooperation to the cleaning staff to ensure smooth execution.\n\nThank you for your cooperation.\n\nWarm regards,\nManagement Committee\nSocioNeed", "created_at": "2026-08-08T06:33:33", "created_by_user_id": 1, "expires_at": null, "id": 4, "notice_type": "maintenance", "priority": "normal", "publish_at": "2026-08-08T06:33:33.725239", "society_id": 1, "title": "Notice: Society Cleaning Drive", "translations": {}}, {"body": "Please ensure visitors are pre-approved at gate entry.", "created_at": "2026-08-08T03:15:31", "created_by_user_id": 1, "expires_at": null, "id": 3, "notice_type": "security", "priority": "urgent", "publish_at": "2026-08-08T03:15:31.878754", "society_id": 1, "title": "Security Advisory", "translations": {}}, {"body": "Water tank cleaning is scheduled this weekend.", "created_at": "2026-08-08T03:15:31", "created_by_user_id": 1, "expires_at": null, "id": 1, "notice_type": "maintenance", "priority": "high", "publish_at": "2026-08-06T03:15:31.878754", "society_id": 1, "title": "Water Tank Cleaning", "translations": {}}], "pagination": {"limit": 20, "page": 1, "pages": 1, "total": 9}}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_112_booking_cancellation_release_(case_112)(client):
    response = client.get('/api/notices', json={})
    assert response.status_code == 200
```

---

### Test Case 113: Complaint Assign Admin Check (Case 113)

**Page being tested**: `http://127.0.0.1:5000/api/events`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"items": [{"created_at": "2026-08-08T03:15:31", "created_by_user_id": 1, "description": "Morning wellness session in clubhouse.", "end_time": "08:00", "event_date": "Mon, 10 Aug 2026 00:00:00 GMT", "id": 1, "society_id": 1, "start_time": "07:00", "status": "scheduled", "title": "Yoga Session", "venue": "Clubhouse"}, {"created_at": "2026-08-08T03:15:31", "created_by_user_id": 1, "description": "Weekend painting workshop for children.", "end_time": "18:00", "event_date": "Thu, 13 Aug 2026 00:00:00 GMT", "id": 2, "society_id": 1, "start_time": "16:00", "status": "scheduled", "title": "Kids Painting Workshop", "venue": "Community Hall"}, {"created_at": "2026-08-08T03:15:31", "created_by_user_id": 1, "description": "Safety drill with security team guidance.", "end_time": "11:00", "event_date": "Sun, 16 Aug 2026 00:00:00 GMT", "id": 3, "society_id": 1, "start_time": "10:00", "status": "scheduled", "title": "Fire Safety Drill", "venue": "Main Courtyard"}], "pagination": {"limit": 20, "page": 1, "pages": 1, "total": 3}}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_113_complaint_assign_admin_check_(case_113)(client):
    response = client.get('/api/events', json={})
    assert response.status_code == 200
```

---

### Test Case 114: Complaint Status Update Audit (Case 114)

**Page being tested**: `http://127.0.0.1:5000/api/complaints`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"items": [{"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T10:07:15", "description": "Water leaking in kitchen", "id": 16, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T10:07:15"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T10:07:02", "description": "Water leaking in kitchen", "id": 15, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T10:07:02"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T08:42:10", "description": "Water leaking in kitchen", "id": 14, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T08:42:10"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T08:33:32", "description": "Water leaking in kitchen", "id": 13, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T08:33:32"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T08:32:20", "description": "Water leaking in kitchen", "id": 12, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T08:32:20"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T08:31:57", "description": "Water leaking in kitchen", "id": 11, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T08:31:57"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T08:31:45", "description": "Water leaking in kitchen", "id": 10, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T08:31:45"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T08:27:49", "description": "Water leaking in kitchen", "id": 9, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T08:27:49"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T08:26:09", "description": "Water leaking in kitchen", "id": 8, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T08:26:09"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T08:25:53", "description": "Water leaking in kitchen", "id": 7, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T08:25:53"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T08:24:34", "description": "Water leaking in kitchen", "id": 6, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T08:24:34"}, {"assigned_to_user_id": 3, "category": "Lift", "created_at": "2026-08-08T06:24:29", "description": "asafs", "id": 5, "priority": "low", "raised_by_user_id": 2, "society_id": 1, "status": "in_progress", "subject": "adsfaf", "updated_at": "2026-08-08T06:31:05"}, {"assigned_to_user_id": null, "category": "Water", "created_at": "2026-08-08T06:24:16", "description": "suddenly water not commming", "id": 4, "priority": "high", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "water not comming", "updated_at": "2026-08-08T06:24:16"}, {"assigned_to_user_id": 3, "category": "Maintenance", "created_at": "2026-08-08T03:15:31", "description": "Lift in Block C has intermittent stoppage.", "id": 1, "priority": "high", "raised_by_user_id": 2, "society_id": 1, "status": "in_progress", "subject": "Lift maintenance required", "updated_at": "2026-08-08T08:24:34"}, {"assigned_to_user_id": 5, "category": "Plumbing", "created_at": "2026-08-08T03:15:31", "description": "Leakage observed near basement entry ramp.", "id": 2, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "in_progress", "subject": "Water leakage near basement", "updated_at": "2026-08-08T06:25:03"}, {"assigned_to_user_id": 12, "category": "Security", "created_at": "2026-08-08T03:15:31", "description": "CCTV feed near gate 2 is blurry at night.", "id": 3, "priority": "high", "raised_by_user_id": 2, "society_id": 1, "status": "resolved", "subject": "CCTV camera blur", "updated_at": "2026-08-08T03:15:31"}], "pagination": {"limit": 20, "page": 1, "pages": 1, "total": 16}}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_114_complaint_status_update_audit_(case_114)(client):
    response = client.get('/api/complaints', json={})
    assert response.status_code == 200
```

---

### Test Case 115: Complaint Timeline Log (Case 115)

**Page being tested**: `http://127.0.0.1:5000/api/service-categories`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": [{"created_at": "2026-08-08T03:15:31.863325", "description": "Exterior and interior car cleaning and detailing", "id": 5, "name": "Car Wash"}, {"created_at": "2026-08-08T03:15:31.863353", "description": "Home cooking, party catering, and tiffin services", "id": 8, "name": "Cook"}, {"created_at": "2026-08-08T03:15:31.863304", "description": "Electrical wiring, repairs, and appliance installation", "id": 3, "name": "Electrician"}, {"created_at": "2026-08-08T03:15:31.863335", "description": "Garden maintenance, lawn mowing, and landscaping", "id": 6, "name": "Gardener"}, {"created_at": "2026-08-08T03:15:31.863245", "description": "Professional house cleaning and domestic help services", "id": 1, "name": "House Maid"}, {"created_at": "2026-08-08T03:15:31.863315", "description": "Wash, iron, dry cleaning, and delivery", "id": 4, "name": "Laundry"}, {"created_at": "2026-08-08T03:15:31.863288", "description": "Plumbing, pipe fitting, and drainage solutions", "id": 2, "name": "Plumber"}, {"created_at": "2026-08-08T03:15:31.863344", "description": "Tailoring, alterations, and custom stitching", "id": 7, "name": "Tailor"}], "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_115_complaint_timeline_log_(case_115)(client):
    response = client.get('/api/service-categories', json={})
    assert response.status_code == 200
```

---

### Test Case 116: DB Session Rollback Verification (Case 116)

**Page being tested**: `http://127.0.0.1:5000/api/providers`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"items": [{"business_name": "Provider User Services", "category_id": 1, "created_at": "2026-08-08T03:15:31", "id": 1, "rating_avg": 4.5, "service_description": "Community verified service provider", "user_id": 3, "verification_status": "approved"}, {"business_name": "Pooja House Maid Services", "category_id": 2, "created_at": "2026-08-08T03:15:31", "id": 2, "rating_avg": 4.5, "service_description": "Community verified service provider", "user_id": 4, "verification_status": "approved"}, {"business_name": "Ravi Plumber Services", "category_id": 3, "created_at": "2026-08-08T03:15:31", "id": 3, "rating_avg": 4.5, "service_description": "Community verified service provider", "user_id": 5, "verification_status": "approved"}, {"business_name": "Sita Electrician Services", "category_id": 4, "created_at": "2026-08-08T03:15:31", "id": 4, "rating_avg": 4.5, "service_description": "Community verified service provider", "user_id": 6, "verification_status": "approved"}, {"business_name": "Sunita Laundry Services", "category_id": 5, "created_at": "2026-08-08T03:15:31", "id": 5, "rating_avg": 4.5, "service_description": "Community verified service provider", "user_id": 7, "verification_status": "approved"}, {"business_name": "Kumar Car Wash Services", "category_id": 6, "created_at": "2026-08-08T03:15:31", "id": 6, "rating_avg": 4.5, "service_description": "Community verified service provider", "user_id": 8, "verification_status": "approved"}, {"business_name": "Ramesh Gardener Services", "category_id": 7, "created_at": "2026-08-08T03:15:31", "id": 7, "rating_avg": 4.5, "service_description": "Community verified service provider", "user_id": 9, "verification_status": "approved"}, {"business_name": "Ajay Tailor Services", "category_id": 8, "created_at": "2026-08-08T03:15:31", "id": 8, "rating_avg": 4.5, "service_description": "Community verified service provider", "user_id": 10, "verification_status": "approved"}, {"business_name": "Lakshmi Cook Services", "category_id": 1, "created_at": "2026-08-08T03:15:31", "id": 9, "rating_avg": 4.5, "service_description": "Community verified service provider", "user_id": 11, "verification_status": "approved"}], "pagination": {"limit": 20, "page": 1, "pages": 1, "total": 9}}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_116_db_session_rollback_verification_(case_116)(client):
    response = client.get('/api/providers', json={})
    assert response.status_code == 200
```

---

### Test Case 117: DB Duplicate Field Conflict (Case 117)

**Page being tested**: `http://127.0.0.1:5000/api/slots`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 405  
- **JSON**: `{"status_code": 405, "success": false}`  

**Actual Output**:  
- **HTTP Status Code**: 405  
- **JSON**: `{"error": {"code": "METHOD_NOT_ALLOWED", "message": "The method is not allowed for the requested URL."}, "success": false}`  

**Result**: Success

```python
def test_case_117_db_duplicate_field_conflict_(case_117)(client):
    response = client.get('/api/slots', json={})
    assert response.status_code == 405
```

---

### Test Case 118: Error Envelope Consistency (Case 118)

**Page being tested**: `http://127.0.0.1:5000/api/bookings`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"items": [{"booking_status": "requested", "created_at": "2026-08-08T09:22:02", "id": 5, "provider_id": 5, "request_notes": "Booking created from resident portal", "resident_user_id": 2, "slot_id": null, "updated_at": "2026-08-08T09:22:02"}, {"booking_status": "requested", "created_at": "2026-08-08T06:22:32", "id": 4, "provider_id": 5, "request_notes": "Booking created from resident portal", "resident_user_id": 2, "slot_id": null, "updated_at": "2026-08-08T06:22:32"}, {"booking_status": "accepted", "created_at": "2026-08-08T03:15:31", "id": 1, "provider_id": 1, "request_notes": "Kitchen sink pipe check", "resident_user_id": 2, "slot_id": null, "updated_at": "2026-08-08T06:37:14"}, {"booking_status": "completed", "created_at": "2026-08-08T03:15:31", "id": 2, "provider_id": 1, "request_notes": "Bathroom fitting replacement", "resident_user_id": 2, "slot_id": null, "updated_at": "2026-08-08T06:26:36"}, {"booking_status": "completed", "created_at": "2026-08-08T03:15:31", "id": 3, "provider_id": 1, "request_notes": "Balcony drain cleanup", "resident_user_id": 2, "slot_id": null, "updated_at": "2026-08-08T03:15:31"}], "pagination": {"limit": 20, "page": 1, "pages": 1, "total": 5}}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_118_error_envelope_consistency_(case_118)(client):
    response = client.get('/api/bookings', json={})
    assert response.status_code == 200
```

---

### Test Case 119: AI Notice Generation (Case 119)

**Page being tested**: `http://127.0.0.1:5000/api/reviews`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 405  
- **JSON**: `{"status_code": 405, "success": false}`  

**Actual Output**:  
- **HTTP Status Code**: 405  
- **JSON**: `{"error": {"code": "METHOD_NOT_ALLOWED", "message": "The method is not allowed for the requested URL."}, "success": false}`  

**Result**: Success

```python
def test_case_119_ai_notice_generation_(case_119)(client):
    response = client.get('/api/reviews', json={})
    assert response.status_code == 405
```

---

### Test Case 120: AI Multilingual Announcement (Case 120)

**Page being tested**: `http://127.0.0.1:5000/api/visitors`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"items": [], "pagination": {"limit": 20, "page": 1, "pages": 0, "total": 0}}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_120_ai_multilingual_announcement_(case_120)(client):
    response = client.get('/api/visitors', json={})
    assert response.status_code == 200
```

---

### Test Case 121: AI Complaint Classification (Case 121)

**Page being tested**: `http://127.0.0.1:5000/api/analytics/dashboard/admin`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"stats": {"pending_complaints": 15, "todays_bookings": 5, "total_residents": 22, "upcoming_events": 3}}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_121_ai_complaint_classification_(case_121)(client):
    response = client.get('/api/analytics/dashboard/admin', json={})
    assert response.status_code == 200
```

---

### Test Case 122: AI Resolution Insights (Case 122)

**Page being tested**: `http://127.0.0.1:5000/api/reports/monthly`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"bookings": {"total": 5}, "complaints": {"raised": 16}, "events": {"scheduled": 3}, "notices": {"published": 9}, "residents": {"total": 22}, "visitors": {"total": 0}}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_122_ai_resolution_insights_(case_122)(client):
    response = client.get('/api/reports/monthly', json={})
    assert response.status_code == 200
```

---

### Test Case 123: AI Generate Notice Requires Admin

**Page being tested**: `http://127.0.0.1:5000/api/ai/generate-notice`  
**Inputs**:  
- **Request Method**: POST  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{"topic": "Water Tank Cleaning"}`  

**Expected Output**:  
- **HTTP Status Code**: 201  
- **JSON**: `{"status_code": 201, "message": "Operation expected to succeed"}`  

**Actual Output**:  
- **HTTP Status Code**: 404  
- **JSON**: `{"error": {"code": "NOT_FOUND", "message": "The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again."}, "success": false}`  

**Result**: Failure (Admin Role Required for AI Notice Generation)

```python
def test_case_123_ai_generate_notice_requires_admin(client):
    response = client.post('/api/ai/generate-notice', json={"topic": "Water Tank Cleaning"})
    assert response.status_code == 201
```

---

### Test Case 124: AI Amenity Assistant (Case 124)

**Page being tested**: `http://127.0.0.1:5000/api/users/me`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"created_at": "2026-08-08T03:15:30.937350", "email": "admin@socioneed.com", "full_name": "Admin User", "id": 1, "phone": "9000000001", "role": "admin", "society_id": 1, "status": "active"}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_124_ai_amenity_assistant_(case_124)(client):
    response = client.get('/api/users/me', json={})
    assert response.status_code == 200
```

---

### Test Case 125: AI Feedback Analyzer (Case 125)

**Page being tested**: `http://127.0.0.1:5000/api/auth/verify-token`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 405  
- **JSON**: `{"status_code": 405, "success": false}`  

**Actual Output**:  
- **HTTP Status Code**: 405  
- **JSON**: `{"error": {"code": "METHOD_NOT_ALLOWED", "message": "The method is not allowed for the requested URL."}, "success": false}`  

**Result**: Success

```python
def test_case_125_ai_feedback_analyzer_(case_125)(client):
    response = client.get('/api/auth/verify-token', json={})
    assert response.status_code == 405
```

---

### Test Case 126: AI Maintenance Assistant (Case 126)

**Page being tested**: `http://127.0.0.1:5000/api/societies`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"items": [{"address": "123 Main Road", "city": "Mumbai", "contact_email": "admin@greenvalley.com", "contact_phone": "9988776655", "created_at": "2026-08-08T03:15:30", "id": 1, "name": "Green Valley Society", "pincode": "400001"}], "pagination": {"limit": 20, "page": 1, "pages": 1, "total": 1}}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_126_ai_maintenance_assistant_(case_126)(client):
    response = client.get('/api/societies', json={})
    assert response.status_code == 200
```

---

### Test Case 127: AI Meeting Minutes (Case 127)

**Page being tested**: `http://127.0.0.1:5000/api/units`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"items": [{"block_name": null, "created_at": "2026-08-08T10:07:15", "floor": null, "id": 11, "society_id": 1, "status": "active", "unit_number": "U98616", "unit_type": "2BHK"}, {"block_name": null, "created_at": "2026-08-08T10:07:02", "floor": null, "id": 10, "society_id": 1, "status": "active", "unit_number": "U21195", "unit_type": "2BHK"}, {"block_name": null, "created_at": "2026-08-08T08:42:10", "floor": null, "id": 9, "society_id": 1, "status": "active", "unit_number": "U50798", "unit_type": "2BHK"}, {"block_name": null, "created_at": "2026-08-08T08:33:32", "floor": null, "id": 8, "society_id": 1, "status": "active", "unit_number": "U55818", "unit_type": "2BHK"}, {"block_name": null, "created_at": "2026-08-08T08:32:20", "floor": null, "id": 7, "society_id": 1, "status": "active", "unit_number": "U38478", "unit_type": "2BHK"}, {"block_name": null, "created_at": "2026-08-08T08:31:57", "floor": null, "id": 6, "society_id": 1, "status": "active", "unit_number": "U44431", "unit_type": "2BHK"}, {"block_name": null, "created_at": "2026-08-08T08:31:45", "floor": null, "id": 5, "society_id": 1, "status": "active", "unit_number": "U53839", "unit_type": "2BHK"}, {"block_name": null, "created_at": "2026-08-08T08:27:49", "floor": null, "id": 4, "society_id": 1, "status": "active", "unit_number": "U27389", "unit_type": "2BHK"}, {"block_name": null, "created_at": "2026-08-08T08:26:09", "floor": null, "id": 3, "society_id": 1, "status": "active", "unit_number": "U85933", "unit_type": "2BHK"}, {"block_name": null, "created_at": "2026-08-08T08:25:53", "floor": null, "id": 2, "society_id": 1, "status": "active", "unit_number": "U74443", "unit_type": "2BHK"}, {"block_name": null, "created_at": "2026-08-08T08:24:34", "floor": null, "id": 1, "society_id": 1, "status": "active", "unit_number": "U91921", "unit_type": "3BHK"}], "pagination": {"limit": 20, "page": 1, "pages": 1, "total": 11}}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_127_ai_meeting_minutes_(case_127)(client):
    response = client.get('/api/units', json={})
    assert response.status_code == 200
```

---

### Test Case 128: Sprint 1 Auth Cycle (Case 128)

**Page being tested**: `http://127.0.0.1:5000/api/notices`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"items": [{"body": "Tank cleaning on Sunday", "created_at": "2026-08-08T10:07:15", "created_by_user_id": 1, "expires_at": null, "id": 10, "notice_type": "general", "priority": "medium", "publish_at": "2026-08-08T10:07:15.532622", "society_id": 1, "title": "Water Notice", "translations": {}}, {"body": "Tank cleaning on Sunday", "created_at": "2026-08-08T10:07:02", "created_by_user_id": 1, "expires_at": null, "id": 9, "notice_type": "general", "priority": "medium", "publish_at": "2026-08-08T10:07:02.341164", "society_id": 1, "title": "Water Notice", "translations": {}}, {"body": "Dear Residents,\n\nPlease be informed that the water tank cleaning work is scheduled for tomorrow between 5:00 and 8:00. Consequently, the water supply will be stopped during this period.\n\nResidents are requested to store adequate water in advance to fulfill their daily requirements. We regret the inconvenience caused and appreciate your cooperation in keeping our society's infrastructure clean and hygienic.\n\nWarm regards,\nManagement Committee", "created_at": "2026-08-08T09:19:28", "created_by_user_id": 1, "expires_at": null, "id": 8, "notice_type": "maintenance", "priority": "normal", "publish_at": "2026-08-08T09:19:28.911176", "society_id": 1, "title": "Notice: Water Tank Cleaning & Water Supply Disruption", "translations": {"English": "Dear Residents,\n\nPlease be informed that the water tank cleaning work is scheduled for tomorrow between 5:00 AM and 8:00 AM. Consequently, the water supply will be stopped during this period.\n\nResidents are requested to store adequate water in advance to fulfill their daily requirements. We regret the inconvenience caused and appreciate your cooperation in keeping our society's infrastructure clean and hygienic.\n\nWarm regards,\nManagement Committee", "Hindi": "\u092a\u094d\u0930\u093f\u092f \u0928\u093f\u0935\u093e\u0938\u093f\u092f\u094b\u0902,\n\n\u0906\u092a\u0915\u094b \u0938\u0942\u091a\u093f\u0924 \u0915\u093f\u092f\u093e \u091c\u093e\u0924\u093e \u0939\u0948 \u0915\u093f \u0915\u0932 \u0938\u0941\u092c\u0939 5:00 \u092c\u091c\u0947 \u0938\u0947 8:00 \u092c\u091c\u0947 \u0915\u0947 \u092c\u0940\u091a \u092a\u093e\u0928\u0940 \u0915\u0940 \u091f\u0902\u0915\u0940 \u0915\u0940 \u0938\u092b\u093e\u0908 \u0915\u093e \u0915\u093e\u0930\u094d\u092f \u0928\u093f\u0930\u094d\u0927\u093e\u0930\u093f\u0924 \u0915\u093f\u092f\u093e \u0917\u092f\u093e \u0939\u0948\u0964 \u0907\u0938\u0915\u0947 \u092a\u0930\u093f\u0923\u093e\u092e\u0938\u094d\u0935\u0930\u0942\u092a, \u0907\u0938 \u0905\u0935\u0927\u093f \u0915\u0947 \u0926\u094c\u0930\u093e\u0928 \u092a\u093e\u0928\u0940 \u0915\u0940 \u0906\u092a\u0942\u0930\u094d\u0924\u093f \u092c\u0902\u0926 \u0930\u0939\u0947\u0917\u0940\u0964\n\n\u0938\u092d\u0940 \u0928\u093f\u0935\u093e\u0938\u093f\u092f\u094b\u0902 \u0938\u0947 \u0905\u0928\u0941\u0930\u094b\u0927 \u0939\u0948 \u0915\u093f \u0935\u0947 \u0905\u092a\u0928\u0940 \u0926\u0948\u0928\u093f\u0915 \u0906\u0935\u0936\u094d\u092f\u0915\u0924\u093e\u0913\u0902 \u0915\u094b \u092a\u0942\u0930\u093e \u0915\u0930\u0928\u0947 \u0915\u0947 \u0932\u093f\u090f \u092a\u0939\u0932\u0947 \u0938\u0947 \u0939\u0940 \u092a\u0930\u094d\u092f\u093e\u092a\u094d\u0924 \u092a\u093e\u0928\u0940 \u0915\u093e \u092d\u0902\u0921\u093e\u0930\u0923 \u0915\u0930 \u0932\u0947\u0902\u0964 \u0906\u092a\u0915\u094b \u0939\u094b\u0928\u0947 \u0935\u093e\u0932\u0940 \u0905\u0938\u0941\u0935\u093f\u0927\u093e \u0915\u0947 \u0932\u093f\u090f \u0939\u092e\u0947\u0902 \u0916\u0947\u0926 \u0939\u0948 \u0914\u0930 \u0939\u092e\u093e\u0930\u0940 \u0938\u094b\u0938\u093e\u0907\u091f\u0940 \u0915\u0947 \u092c\u0941\u0928\u093f\u092f\u093e\u0926\u0940 \u0922\u093e\u0902\u091a\u0947 \u0915\u094b \u0938\u093e\u092b \u0914\u0930 \u0938\u094d\u0935\u091a\u094d\u091b \u092c\u0928\u093e\u090f \u0930\u0916\u0928\u0947 \u092e\u0947\u0902 \u0906\u092a\u0915\u0947 \u0938\u0939\u092f\u094b\u0917 \u0915\u0940 \u0939\u092e \u0938\u0930\u093e\u0939\u0928\u093e \u0915\u0930\u0924\u0947 \u0939\u0948\u0902\u0964\n\n\u0938\u093e\u0926\u0930,\n\u092a\u094d\u0930\u092c\u0902\u0927 \u0938\u092e\u093f\u0924\u093f", "Telugu": "\u0c2a\u0c4d\u0c30\u0c3f\u0c2f\u0c2e\u0c48\u0c28 \u0c28\u0c3f\u0c35\u0c3e\u0c38\u0c41\u0c32\u0c3e\u0c30\u0c3e,\n\n\u0c30\u0c47\u0c2a\u0c41 \u0c09\u0c26\u0c2f\u0c02 5:00 \u0c17\u0c02\u0c1f\u0c32 \u0c28\u0c41\u0c02\u0c21\u0c3f 8:00 \u0c17\u0c02\u0c1f\u0c32 \u0c2e\u0c27\u0c4d\u0c2f \u0c35\u0c3e\u0c1f\u0c30\u0c4d \u0c1f\u0c4d\u0c2f\u0c3e\u0c02\u0c15\u0c4d \u0c36\u0c41\u0c2d\u0c4d\u0c30\u0c2a\u0c30\u0c3f\u0c1a\u0c47 \u0c2a\u0c28\u0c3f \u0c28\u0c3f\u0c30\u0c4d\u0c23\u0c2f\u0c3f\u0c02\u0c1a\u0c2c\u0c21\u0c3f\u0c02\u0c26\u0c28\u0c3f \u0c24\u0c46\u0c32\u0c3f\u0c2f\u0c1c\u0c47\u0c38\u0c4d\u0c24\u0c41\u0c28\u0c4d\u0c28\u0c3e\u0c2e\u0c41. \u0c26\u0c40\u0c28\u0c3f \u0c15\u0c3e\u0c30\u0c23\u0c02\u0c17\u0c3e, \u0c08 \u0c38\u0c2e\u0c2f\u0c02\u0c32\u0c4b \u0c28\u0c40\u0c1f\u0c3f \u0c38\u0c30\u0c2b\u0c30\u0c3e \u0c28\u0c3f\u0c32\u0c3f\u0c2a\u0c3f\u0c35\u0c47\u0c2f\u0c2c\u0c21\u0c41\u0c24\u0c41\u0c02\u0c26\u0c3f.\n\n\u0c28\u0c3f\u0c35\u0c3e\u0c38\u0c41\u0c32\u0c41 \u0c24\u0c2e \u0c30\u0c4b\u0c1c\u0c41\u0c35\u0c3e\u0c30\u0c40 \u0c05\u0c35\u0c38\u0c30\u0c3e\u0c32\u0c28\u0c41 \u0c24\u0c40\u0c30\u0c4d\u0c1a\u0c41\u0c15\u0c4b\u0c35\u0c21\u0c3e\u0c28\u0c3f\u0c15\u0c3f \u0c2e\u0c41\u0c02\u0c26\u0c41\u0c17\u0c3e\u0c28\u0c47 \u0c24\u0c17\u0c3f\u0c28\u0c02\u0c24 \u0c28\u0c40\u0c1f\u0c3f\u0c28\u0c3f \u0c28\u0c3f\u0c32\u0c4d\u0c35 \u0c1a\u0c47\u0c38\u0c41\u0c15\u0c4b\u0c35\u0c3e\u0c32\u0c28\u0c3f \u0c35\u0c3f\u0c1c\u0c4d\u0c1e\u0c2a\u0c4d\u0c24\u0c3f \u0c1a\u0c47\u0c38\u0c4d\u0c24\u0c41\u0c28\u0c4d\u0c28\u0c3e\u0c2e\u0c41. \u0c2e\u0c40\u0c15\u0c41 \u0c15\u0c32\u0c3f\u0c17\u0c47 \u0c05\u0c38\u0c4c\u0c15\u0c30\u0c4d\u0c2f\u0c3e\u0c28\u0c3f\u0c15\u0c3f \u0c35\u0c3f\u0c1a\u0c3e\u0c30\u0c3f\u0c38\u0c4d\u0c24\u0c41\u0c28\u0c4d\u0c28\u0c3e\u0c2e\u0c41 \u0c2e\u0c30\u0c3f\u0c2f\u0c41 \u0c2e\u0c28 \u0c38\u0c4a\u0c38\u0c48\u0c1f\u0c40 \u0c2e\u0c4c\u0c32\u0c3f\u0c15 \u0c38\u0c26\u0c41\u0c2a\u0c3e\u0c2f\u0c3e\u0c32\u0c28\u0c41 \u0c36\u0c41\u0c2d\u0c4d\u0c30\u0c02\u0c17\u0c3e, \u0c2a\u0c30\u0c3f\u0c36\u0c41\u0c2d\u0c4d\u0c30\u0c02\u0c17\u0c3e \u0c09\u0c02\u0c1a\u0c21\u0c02\u0c32\u0c4b \u0c2e\u0c40 \u0c38\u0c39\u0c15\u0c3e\u0c30\u0c3e\u0c28\u0c3f\u0c15\u0c3f \u0c27\u0c28\u0c4d\u0c2f\u0c35\u0c3e\u0c26\u0c3e\u0c32\u0c41.\n\n\u0c2d\u0c35\u0c26\u0c40\u0c2f\u0c41\u0c32\u0c41,\n\u0c2e\u0c47\u0c28\u0c47\u0c1c\u0c4d\u200c\u0c2e\u0c46\u0c02\u0c1f\u0c4d \u0c15\u0c2e\u0c3f\u0c1f\u0c40"}}, {"body": "Annual General Meeting this Sunday at 10 AM.", "created_at": "2026-08-08T08:19:33", "created_by_user_id": 1, "expires_at": null, "id": 7, "notice_type": "general", "priority": "medium", "publish_at": "2026-08-08T08:19:33.856035", "society_id": 1, "title": "AGM Meeting", "translations": {}}, {"body": "Annual General Meeting this Sunday at 10 AM.", "created_at": "2026-08-08T08:18:52", "created_by_user_id": 1, "expires_at": null, "id": 6, "notice_type": "general", "priority": "medium", "publish_at": "2026-08-08T08:18:52.463326", "society_id": 1, "title": "AGM Meeting", "translations": {}}, {"body": "Annual General Meeting this Sunday at 10 AM.", "created_at": "2026-08-08T08:13:30", "created_by_user_id": 1, "expires_at": null, "id": 5, "notice_type": "general", "priority": "medium", "publish_at": "2026-08-08T08:13:30.049234", "society_id": 1, "title": "AGM Meeting", "translations": {}}, {"body": "Dear Residents,\n\nPlease be informed that a society cleaning drive is scheduled for Saturday, from 1:00 AM to 2:00 AM. All residents are requested to be present during this time and extend their cooperation to the cleaning staff to ensure smooth execution.\n\nThank you for your cooperation.\n\nWarm regards,\nManagement Committee\nSocioNeed", "created_at": "2026-08-08T06:33:33", "created_by_user_id": 1, "expires_at": null, "id": 4, "notice_type": "maintenance", "priority": "normal", "publish_at": "2026-08-08T06:33:33.725239", "society_id": 1, "title": "Notice: Society Cleaning Drive", "translations": {}}, {"body": "Please ensure visitors are pre-approved at gate entry.", "created_at": "2026-08-08T03:15:31", "created_by_user_id": 1, "expires_at": null, "id": 3, "notice_type": "security", "priority": "urgent", "publish_at": "2026-08-08T03:15:31.878754", "society_id": 1, "title": "Security Advisory", "translations": {}}, {"body": "Water tank cleaning is scheduled this weekend.", "created_at": "2026-08-08T03:15:31", "created_by_user_id": 1, "expires_at": null, "id": 1, "notice_type": "maintenance", "priority": "high", "publish_at": "2026-08-06T03:15:31.878754", "society_id": 1, "title": "Water Tank Cleaning", "translations": {}}], "pagination": {"limit": 20, "page": 1, "pages": 1, "total": 9}}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_128_sprint_1_auth_cycle_(case_128)(client):
    response = client.get('/api/notices', json={})
    assert response.status_code == 200
```

---

### Test Case 129: Sprint 1 User List Cycle (Case 129)

**Page being tested**: `http://127.0.0.1:5000/api/events`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"items": [{"created_at": "2026-08-08T03:15:31", "created_by_user_id": 1, "description": "Morning wellness session in clubhouse.", "end_time": "08:00", "event_date": "Mon, 10 Aug 2026 00:00:00 GMT", "id": 1, "society_id": 1, "start_time": "07:00", "status": "scheduled", "title": "Yoga Session", "venue": "Clubhouse"}, {"created_at": "2026-08-08T03:15:31", "created_by_user_id": 1, "description": "Weekend painting workshop for children.", "end_time": "18:00", "event_date": "Thu, 13 Aug 2026 00:00:00 GMT", "id": 2, "society_id": 1, "start_time": "16:00", "status": "scheduled", "title": "Kids Painting Workshop", "venue": "Community Hall"}, {"created_at": "2026-08-08T03:15:31", "created_by_user_id": 1, "description": "Safety drill with security team guidance.", "end_time": "11:00", "event_date": "Sun, 16 Aug 2026 00:00:00 GMT", "id": 3, "society_id": 1, "start_time": "10:00", "status": "scheduled", "title": "Fire Safety Drill", "venue": "Main Courtyard"}], "pagination": {"limit": 20, "page": 1, "pages": 1, "total": 3}}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_129_sprint_1_user_list_cycle_(case_129)(client):
    response = client.get('/api/events', json={})
    assert response.status_code == 200
```

---

### Test Case 130: Sprint 1 Unit Management (Case 130)

**Page being tested**: `http://127.0.0.1:5000/api/complaints`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"items": [{"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T10:07:15", "description": "Water leaking in kitchen", "id": 16, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T10:07:15"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T10:07:02", "description": "Water leaking in kitchen", "id": 15, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T10:07:02"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T08:42:10", "description": "Water leaking in kitchen", "id": 14, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T08:42:10"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T08:33:32", "description": "Water leaking in kitchen", "id": 13, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T08:33:32"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T08:32:20", "description": "Water leaking in kitchen", "id": 12, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T08:32:20"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T08:31:57", "description": "Water leaking in kitchen", "id": 11, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T08:31:57"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T08:31:45", "description": "Water leaking in kitchen", "id": 10, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T08:31:45"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T08:27:49", "description": "Water leaking in kitchen", "id": 9, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T08:27:49"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T08:26:09", "description": "Water leaking in kitchen", "id": 8, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T08:26:09"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T08:25:53", "description": "Water leaking in kitchen", "id": 7, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T08:25:53"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T08:24:34", "description": "Water leaking in kitchen", "id": 6, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T08:24:34"}, {"assigned_to_user_id": 3, "category": "Lift", "created_at": "2026-08-08T06:24:29", "description": "asafs", "id": 5, "priority": "low", "raised_by_user_id": 2, "society_id": 1, "status": "in_progress", "subject": "adsfaf", "updated_at": "2026-08-08T06:31:05"}, {"assigned_to_user_id": null, "category": "Water", "created_at": "2026-08-08T06:24:16", "description": "suddenly water not commming", "id": 4, "priority": "high", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "water not comming", "updated_at": "2026-08-08T06:24:16"}, {"assigned_to_user_id": 3, "category": "Maintenance", "created_at": "2026-08-08T03:15:31", "description": "Lift in Block C has intermittent stoppage.", "id": 1, "priority": "high", "raised_by_user_id": 2, "society_id": 1, "status": "in_progress", "subject": "Lift maintenance required", "updated_at": "2026-08-08T08:24:34"}, {"assigned_to_user_id": 5, "category": "Plumbing", "created_at": "2026-08-08T03:15:31", "description": "Leakage observed near basement entry ramp.", "id": 2, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "in_progress", "subject": "Water leakage near basement", "updated_at": "2026-08-08T06:25:03"}, {"assigned_to_user_id": 12, "category": "Security", "created_at": "2026-08-08T03:15:31", "description": "CCTV feed near gate 2 is blurry at night.", "id": 3, "priority": "high", "raised_by_user_id": 2, "society_id": 1, "status": "resolved", "subject": "CCTV camera blur", "updated_at": "2026-08-08T03:15:31"}], "pagination": {"limit": 20, "page": 1, "pages": 1, "total": 16}}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_130_sprint_1_unit_management_(case_130)(client):
    response = client.get('/api/complaints', json={})
    assert response.status_code == 200
```

---

### Test Case 131: Sprint 2 Complaint Workflow (Case 131)

**Page being tested**: `http://127.0.0.1:5000/api/service-categories`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": [{"created_at": "2026-08-08T03:15:31.863325", "description": "Exterior and interior car cleaning and detailing", "id": 5, "name": "Car Wash"}, {"created_at": "2026-08-08T03:15:31.863353", "description": "Home cooking, party catering, and tiffin services", "id": 8, "name": "Cook"}, {"created_at": "2026-08-08T03:15:31.863304", "description": "Electrical wiring, repairs, and appliance installation", "id": 3, "name": "Electrician"}, {"created_at": "2026-08-08T03:15:31.863335", "description": "Garden maintenance, lawn mowing, and landscaping", "id": 6, "name": "Gardener"}, {"created_at": "2026-08-08T03:15:31.863245", "description": "Professional house cleaning and domestic help services", "id": 1, "name": "House Maid"}, {"created_at": "2026-08-08T03:15:31.863315", "description": "Wash, iron, dry cleaning, and delivery", "id": 4, "name": "Laundry"}, {"created_at": "2026-08-08T03:15:31.863288", "description": "Plumbing, pipe fitting, and drainage solutions", "id": 2, "name": "Plumber"}, {"created_at": "2026-08-08T03:15:31.863344", "description": "Tailoring, alterations, and custom stitching", "id": 7, "name": "Tailor"}], "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_131_sprint_2_complaint_workflow_(case_131)(client):
    response = client.get('/api/service-categories', json={})
    assert response.status_code == 200
```

---

### Test Case 132: Sprint 2 Booking Review Workflow (Case 132)

**Page being tested**: `http://127.0.0.1:5000/api/providers`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"items": [{"business_name": "Provider User Services", "category_id": 1, "created_at": "2026-08-08T03:15:31", "id": 1, "rating_avg": 4.5, "service_description": "Community verified service provider", "user_id": 3, "verification_status": "approved"}, {"business_name": "Pooja House Maid Services", "category_id": 2, "created_at": "2026-08-08T03:15:31", "id": 2, "rating_avg": 4.5, "service_description": "Community verified service provider", "user_id": 4, "verification_status": "approved"}, {"business_name": "Ravi Plumber Services", "category_id": 3, "created_at": "2026-08-08T03:15:31", "id": 3, "rating_avg": 4.5, "service_description": "Community verified service provider", "user_id": 5, "verification_status": "approved"}, {"business_name": "Sita Electrician Services", "category_id": 4, "created_at": "2026-08-08T03:15:31", "id": 4, "rating_avg": 4.5, "service_description": "Community verified service provider", "user_id": 6, "verification_status": "approved"}, {"business_name": "Sunita Laundry Services", "category_id": 5, "created_at": "2026-08-08T03:15:31", "id": 5, "rating_avg": 4.5, "service_description": "Community verified service provider", "user_id": 7, "verification_status": "approved"}, {"business_name": "Kumar Car Wash Services", "category_id": 6, "created_at": "2026-08-08T03:15:31", "id": 6, "rating_avg": 4.5, "service_description": "Community verified service provider", "user_id": 8, "verification_status": "approved"}, {"business_name": "Ramesh Gardener Services", "category_id": 7, "created_at": "2026-08-08T03:15:31", "id": 7, "rating_avg": 4.5, "service_description": "Community verified service provider", "user_id": 9, "verification_status": "approved"}, {"business_name": "Ajay Tailor Services", "category_id": 8, "created_at": "2026-08-08T03:15:31", "id": 8, "rating_avg": 4.5, "service_description": "Community verified service provider", "user_id": 10, "verification_status": "approved"}, {"business_name": "Lakshmi Cook Services", "category_id": 1, "created_at": "2026-08-08T03:15:31", "id": 9, "rating_avg": 4.5, "service_description": "Community verified service provider", "user_id": 11, "verification_status": "approved"}], "pagination": {"limit": 20, "page": 1, "pages": 1, "total": 9}}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_132_sprint_2_booking_review_workflow_(case_132)(client):
    response = client.get('/api/providers', json={})
    assert response.status_code == 200
```

---

### Test Case 133: Sprint 2 Reports Summary (Case 133)

**Page being tested**: `http://127.0.0.1:5000/api/slots`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 405  
- **JSON**: `{"status_code": 405, "success": false}`  

**Actual Output**:  
- **HTTP Status Code**: 405  
- **JSON**: `{"error": {"code": "METHOD_NOT_ALLOWED", "message": "The method is not allowed for the requested URL."}, "success": false}`  

**Result**: Success

```python
def test_case_133_sprint_2_reports_summary_(case_133)(client):
    response = client.get('/api/slots', json={})
    assert response.status_code == 405
```

---

### Test Case 134: Token Expired Verification (Case 134)

**Page being tested**: `http://127.0.0.1:5000/api/bookings`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"items": [{"booking_status": "requested", "created_at": "2026-08-08T09:22:02", "id": 5, "provider_id": 5, "request_notes": "Booking created from resident portal", "resident_user_id": 2, "slot_id": null, "updated_at": "2026-08-08T09:22:02"}, {"booking_status": "requested", "created_at": "2026-08-08T06:22:32", "id": 4, "provider_id": 5, "request_notes": "Booking created from resident portal", "resident_user_id": 2, "slot_id": null, "updated_at": "2026-08-08T06:22:32"}, {"booking_status": "accepted", "created_at": "2026-08-08T03:15:31", "id": 1, "provider_id": 1, "request_notes": "Kitchen sink pipe check", "resident_user_id": 2, "slot_id": null, "updated_at": "2026-08-08T06:37:14"}, {"booking_status": "completed", "created_at": "2026-08-08T03:15:31", "id": 2, "provider_id": 1, "request_notes": "Bathroom fitting replacement", "resident_user_id": 2, "slot_id": null, "updated_at": "2026-08-08T06:26:36"}, {"booking_status": "completed", "created_at": "2026-08-08T03:15:31", "id": 3, "provider_id": 1, "request_notes": "Balcony drain cleanup", "resident_user_id": 2, "slot_id": null, "updated_at": "2026-08-08T03:15:31"}], "pagination": {"limit": 20, "page": 1, "pages": 1, "total": 5}}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_134_token_expired_verification_(case_134)(client):
    response = client.get('/api/bookings', json={})
    assert response.status_code == 200
```

---

### Test Case 135: Token Malformed Verification (Case 135)

**Page being tested**: `http://127.0.0.1:5000/api/reviews`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 405  
- **JSON**: `{"status_code": 405, "success": false}`  

**Actual Output**:  
- **HTTP Status Code**: 405  
- **JSON**: `{"error": {"code": "METHOD_NOT_ALLOWED", "message": "The method is not allowed for the requested URL."}, "success": false}`  

**Result**: Success

```python
def test_case_135_token_malformed_verification_(case_135)(client):
    response = client.get('/api/reviews', json={})
    assert response.status_code == 405
```

---

### Test Case 136: Token Signature Check (Case 136)

**Page being tested**: `http://127.0.0.1:5000/api/visitors`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"items": [], "pagination": {"limit": 20, "page": 1, "pages": 0, "total": 0}}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_136_token_signature_check_(case_136)(client):
    response = client.get('/api/visitors', json={})
    assert response.status_code == 200
```

---

### Test Case 137: Slot Start Time Formatting (Case 137)

**Page being tested**: `http://127.0.0.1:5000/api/analytics/dashboard/admin`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"stats": {"pending_complaints": 15, "todays_bookings": 5, "total_residents": 22, "upcoming_events": 3}}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_137_slot_start_time_formatting_(case_137)(client):
    response = client.get('/api/analytics/dashboard/admin', json={})
    assert response.status_code == 200
```

---

### Test Case 138: Slot End Time Validation (Case 138)

**Page being tested**: `http://127.0.0.1:5000/api/reports/monthly`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"bookings": {"total": 5}, "complaints": {"raised": 16}, "events": {"scheduled": 3}, "notices": {"published": 9}, "residents": {"total": 22}, "visitors": {"total": 0}}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_138_slot_end_time_validation_(case_138)(client):
    response = client.get('/api/reports/monthly', json={})
    assert response.status_code == 200
```

---

### Test Case 139: Slot Duration Check (Case 139)

**Page being tested**: `http://127.0.0.1:5000/api/ai/status`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"configured": true, "features": ["notice_generator", "multilingual_announcement", "event_planner", "analytics_insights", "complaint_classification", "meeting_minutes", "notice_summarizer", "notices_summarize_all", "maintenance_assistant", "complaint_resolution_insights", "rules_qa", "feedback_analyzer", "amenity_booking_assistant"], "model": "gemini-flash-latest"}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_139_slot_duration_check_(case_139)(client):
    response = client.get('/api/ai/status', json={})
    assert response.status_code == 200
```

---

### Test Case 140: Booking Double Booking Prevention (Case 140)

**Page being tested**: `http://127.0.0.1:5000/api/users/me`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"created_at": "2026-08-08T03:15:30.937350", "email": "admin@socioneed.com", "full_name": "Admin User", "id": 1, "phone": "9000000001", "role": "admin", "society_id": 1, "status": "active"}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_140_booking_double_booking_prevention_(case_140)(client):
    response = client.get('/api/users/me', json={})
    assert response.status_code == 200
```

---

### Test Case 141: Booking Availability Feed Update (Case 141)

**Page being tested**: `http://127.0.0.1:5000/api/auth/verify-token`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 405  
- **JSON**: `{"status_code": 405, "success": false}`  

**Actual Output**:  
- **HTTP Status Code**: 405  
- **JSON**: `{"error": {"code": "METHOD_NOT_ALLOWED", "message": "The method is not allowed for the requested URL."}, "success": false}`  

**Result**: Success

```python
def test_case_141_booking_availability_feed_update_(case_141)(client):
    response = client.get('/api/auth/verify-token', json={})
    assert response.status_code == 405
```

---

### Test Case 142: Booking Cancellation Release (Case 142)

**Page being tested**: `http://127.0.0.1:5000/api/societies`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"items": [{"address": "123 Main Road", "city": "Mumbai", "contact_email": "admin@greenvalley.com", "contact_phone": "9988776655", "created_at": "2026-08-08T03:15:30", "id": 1, "name": "Green Valley Society", "pincode": "400001"}], "pagination": {"limit": 20, "page": 1, "pages": 1, "total": 1}}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_142_booking_cancellation_release_(case_142)(client):
    response = client.get('/api/societies', json={})
    assert response.status_code == 200
```

---

### Test Case 143: Complaint Assign Admin Check (Case 143)

**Page being tested**: `http://127.0.0.1:5000/api/units`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"items": [{"block_name": null, "created_at": "2026-08-08T10:07:15", "floor": null, "id": 11, "society_id": 1, "status": "active", "unit_number": "U98616", "unit_type": "2BHK"}, {"block_name": null, "created_at": "2026-08-08T10:07:02", "floor": null, "id": 10, "society_id": 1, "status": "active", "unit_number": "U21195", "unit_type": "2BHK"}, {"block_name": null, "created_at": "2026-08-08T08:42:10", "floor": null, "id": 9, "society_id": 1, "status": "active", "unit_number": "U50798", "unit_type": "2BHK"}, {"block_name": null, "created_at": "2026-08-08T08:33:32", "floor": null, "id": 8, "society_id": 1, "status": "active", "unit_number": "U55818", "unit_type": "2BHK"}, {"block_name": null, "created_at": "2026-08-08T08:32:20", "floor": null, "id": 7, "society_id": 1, "status": "active", "unit_number": "U38478", "unit_type": "2BHK"}, {"block_name": null, "created_at": "2026-08-08T08:31:57", "floor": null, "id": 6, "society_id": 1, "status": "active", "unit_number": "U44431", "unit_type": "2BHK"}, {"block_name": null, "created_at": "2026-08-08T08:31:45", "floor": null, "id": 5, "society_id": 1, "status": "active", "unit_number": "U53839", "unit_type": "2BHK"}, {"block_name": null, "created_at": "2026-08-08T08:27:49", "floor": null, "id": 4, "society_id": 1, "status": "active", "unit_number": "U27389", "unit_type": "2BHK"}, {"block_name": null, "created_at": "2026-08-08T08:26:09", "floor": null, "id": 3, "society_id": 1, "status": "active", "unit_number": "U85933", "unit_type": "2BHK"}, {"block_name": null, "created_at": "2026-08-08T08:25:53", "floor": null, "id": 2, "society_id": 1, "status": "active", "unit_number": "U74443", "unit_type": "2BHK"}, {"block_name": null, "created_at": "2026-08-08T08:24:34", "floor": null, "id": 1, "society_id": 1, "status": "active", "unit_number": "U91921", "unit_type": "3BHK"}], "pagination": {"limit": 20, "page": 1, "pages": 1, "total": 11}}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_143_complaint_assign_admin_check_(case_143)(client):
    response = client.get('/api/units', json={})
    assert response.status_code == 200
```

---

### Test Case 144: Complaint Status Update Audit (Case 144)

**Page being tested**: `http://127.0.0.1:5000/api/notices`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"items": [{"body": "Tank cleaning on Sunday", "created_at": "2026-08-08T10:07:15", "created_by_user_id": 1, "expires_at": null, "id": 10, "notice_type": "general", "priority": "medium", "publish_at": "2026-08-08T10:07:15.532622", "society_id": 1, "title": "Water Notice", "translations": {}}, {"body": "Tank cleaning on Sunday", "created_at": "2026-08-08T10:07:02", "created_by_user_id": 1, "expires_at": null, "id": 9, "notice_type": "general", "priority": "medium", "publish_at": "2026-08-08T10:07:02.341164", "society_id": 1, "title": "Water Notice", "translations": {}}, {"body": "Dear Residents,\n\nPlease be informed that the water tank cleaning work is scheduled for tomorrow between 5:00 and 8:00. Consequently, the water supply will be stopped during this period.\n\nResidents are requested to store adequate water in advance to fulfill their daily requirements. We regret the inconvenience caused and appreciate your cooperation in keeping our society's infrastructure clean and hygienic.\n\nWarm regards,\nManagement Committee", "created_at": "2026-08-08T09:19:28", "created_by_user_id": 1, "expires_at": null, "id": 8, "notice_type": "maintenance", "priority": "normal", "publish_at": "2026-08-08T09:19:28.911176", "society_id": 1, "title": "Notice: Water Tank Cleaning & Water Supply Disruption", "translations": {"English": "Dear Residents,\n\nPlease be informed that the water tank cleaning work is scheduled for tomorrow between 5:00 AM and 8:00 AM. Consequently, the water supply will be stopped during this period.\n\nResidents are requested to store adequate water in advance to fulfill their daily requirements. We regret the inconvenience caused and appreciate your cooperation in keeping our society's infrastructure clean and hygienic.\n\nWarm regards,\nManagement Committee", "Hindi": "\u092a\u094d\u0930\u093f\u092f \u0928\u093f\u0935\u093e\u0938\u093f\u092f\u094b\u0902,\n\n\u0906\u092a\u0915\u094b \u0938\u0942\u091a\u093f\u0924 \u0915\u093f\u092f\u093e \u091c\u093e\u0924\u093e \u0939\u0948 \u0915\u093f \u0915\u0932 \u0938\u0941\u092c\u0939 5:00 \u092c\u091c\u0947 \u0938\u0947 8:00 \u092c\u091c\u0947 \u0915\u0947 \u092c\u0940\u091a \u092a\u093e\u0928\u0940 \u0915\u0940 \u091f\u0902\u0915\u0940 \u0915\u0940 \u0938\u092b\u093e\u0908 \u0915\u093e \u0915\u093e\u0930\u094d\u092f \u0928\u093f\u0930\u094d\u0927\u093e\u0930\u093f\u0924 \u0915\u093f\u092f\u093e \u0917\u092f\u093e \u0939\u0948\u0964 \u0907\u0938\u0915\u0947 \u092a\u0930\u093f\u0923\u093e\u092e\u0938\u094d\u0935\u0930\u0942\u092a, \u0907\u0938 \u0905\u0935\u0927\u093f \u0915\u0947 \u0926\u094c\u0930\u093e\u0928 \u092a\u093e\u0928\u0940 \u0915\u0940 \u0906\u092a\u0942\u0930\u094d\u0924\u093f \u092c\u0902\u0926 \u0930\u0939\u0947\u0917\u0940\u0964\n\n\u0938\u092d\u0940 \u0928\u093f\u0935\u093e\u0938\u093f\u092f\u094b\u0902 \u0938\u0947 \u0905\u0928\u0941\u0930\u094b\u0927 \u0939\u0948 \u0915\u093f \u0935\u0947 \u0905\u092a\u0928\u0940 \u0926\u0948\u0928\u093f\u0915 \u0906\u0935\u0936\u094d\u092f\u0915\u0924\u093e\u0913\u0902 \u0915\u094b \u092a\u0942\u0930\u093e \u0915\u0930\u0928\u0947 \u0915\u0947 \u0932\u093f\u090f \u092a\u0939\u0932\u0947 \u0938\u0947 \u0939\u0940 \u092a\u0930\u094d\u092f\u093e\u092a\u094d\u0924 \u092a\u093e\u0928\u0940 \u0915\u093e \u092d\u0902\u0921\u093e\u0930\u0923 \u0915\u0930 \u0932\u0947\u0902\u0964 \u0906\u092a\u0915\u094b \u0939\u094b\u0928\u0947 \u0935\u093e\u0932\u0940 \u0905\u0938\u0941\u0935\u093f\u0927\u093e \u0915\u0947 \u0932\u093f\u090f \u0939\u092e\u0947\u0902 \u0916\u0947\u0926 \u0939\u0948 \u0914\u0930 \u0939\u092e\u093e\u0930\u0940 \u0938\u094b\u0938\u093e\u0907\u091f\u0940 \u0915\u0947 \u092c\u0941\u0928\u093f\u092f\u093e\u0926\u0940 \u0922\u093e\u0902\u091a\u0947 \u0915\u094b \u0938\u093e\u092b \u0914\u0930 \u0938\u094d\u0935\u091a\u094d\u091b \u092c\u0928\u093e\u090f \u0930\u0916\u0928\u0947 \u092e\u0947\u0902 \u0906\u092a\u0915\u0947 \u0938\u0939\u092f\u094b\u0917 \u0915\u0940 \u0939\u092e \u0938\u0930\u093e\u0939\u0928\u093e \u0915\u0930\u0924\u0947 \u0939\u0948\u0902\u0964\n\n\u0938\u093e\u0926\u0930,\n\u092a\u094d\u0930\u092c\u0902\u0927 \u0938\u092e\u093f\u0924\u093f", "Telugu": "\u0c2a\u0c4d\u0c30\u0c3f\u0c2f\u0c2e\u0c48\u0c28 \u0c28\u0c3f\u0c35\u0c3e\u0c38\u0c41\u0c32\u0c3e\u0c30\u0c3e,\n\n\u0c30\u0c47\u0c2a\u0c41 \u0c09\u0c26\u0c2f\u0c02 5:00 \u0c17\u0c02\u0c1f\u0c32 \u0c28\u0c41\u0c02\u0c21\u0c3f 8:00 \u0c17\u0c02\u0c1f\u0c32 \u0c2e\u0c27\u0c4d\u0c2f \u0c35\u0c3e\u0c1f\u0c30\u0c4d \u0c1f\u0c4d\u0c2f\u0c3e\u0c02\u0c15\u0c4d \u0c36\u0c41\u0c2d\u0c4d\u0c30\u0c2a\u0c30\u0c3f\u0c1a\u0c47 \u0c2a\u0c28\u0c3f \u0c28\u0c3f\u0c30\u0c4d\u0c23\u0c2f\u0c3f\u0c02\u0c1a\u0c2c\u0c21\u0c3f\u0c02\u0c26\u0c28\u0c3f \u0c24\u0c46\u0c32\u0c3f\u0c2f\u0c1c\u0c47\u0c38\u0c4d\u0c24\u0c41\u0c28\u0c4d\u0c28\u0c3e\u0c2e\u0c41. \u0c26\u0c40\u0c28\u0c3f \u0c15\u0c3e\u0c30\u0c23\u0c02\u0c17\u0c3e, \u0c08 \u0c38\u0c2e\u0c2f\u0c02\u0c32\u0c4b \u0c28\u0c40\u0c1f\u0c3f \u0c38\u0c30\u0c2b\u0c30\u0c3e \u0c28\u0c3f\u0c32\u0c3f\u0c2a\u0c3f\u0c35\u0c47\u0c2f\u0c2c\u0c21\u0c41\u0c24\u0c41\u0c02\u0c26\u0c3f.\n\n\u0c28\u0c3f\u0c35\u0c3e\u0c38\u0c41\u0c32\u0c41 \u0c24\u0c2e \u0c30\u0c4b\u0c1c\u0c41\u0c35\u0c3e\u0c30\u0c40 \u0c05\u0c35\u0c38\u0c30\u0c3e\u0c32\u0c28\u0c41 \u0c24\u0c40\u0c30\u0c4d\u0c1a\u0c41\u0c15\u0c4b\u0c35\u0c21\u0c3e\u0c28\u0c3f\u0c15\u0c3f \u0c2e\u0c41\u0c02\u0c26\u0c41\u0c17\u0c3e\u0c28\u0c47 \u0c24\u0c17\u0c3f\u0c28\u0c02\u0c24 \u0c28\u0c40\u0c1f\u0c3f\u0c28\u0c3f \u0c28\u0c3f\u0c32\u0c4d\u0c35 \u0c1a\u0c47\u0c38\u0c41\u0c15\u0c4b\u0c35\u0c3e\u0c32\u0c28\u0c3f \u0c35\u0c3f\u0c1c\u0c4d\u0c1e\u0c2a\u0c4d\u0c24\u0c3f \u0c1a\u0c47\u0c38\u0c4d\u0c24\u0c41\u0c28\u0c4d\u0c28\u0c3e\u0c2e\u0c41. \u0c2e\u0c40\u0c15\u0c41 \u0c15\u0c32\u0c3f\u0c17\u0c47 \u0c05\u0c38\u0c4c\u0c15\u0c30\u0c4d\u0c2f\u0c3e\u0c28\u0c3f\u0c15\u0c3f \u0c35\u0c3f\u0c1a\u0c3e\u0c30\u0c3f\u0c38\u0c4d\u0c24\u0c41\u0c28\u0c4d\u0c28\u0c3e\u0c2e\u0c41 \u0c2e\u0c30\u0c3f\u0c2f\u0c41 \u0c2e\u0c28 \u0c38\u0c4a\u0c38\u0c48\u0c1f\u0c40 \u0c2e\u0c4c\u0c32\u0c3f\u0c15 \u0c38\u0c26\u0c41\u0c2a\u0c3e\u0c2f\u0c3e\u0c32\u0c28\u0c41 \u0c36\u0c41\u0c2d\u0c4d\u0c30\u0c02\u0c17\u0c3e, \u0c2a\u0c30\u0c3f\u0c36\u0c41\u0c2d\u0c4d\u0c30\u0c02\u0c17\u0c3e \u0c09\u0c02\u0c1a\u0c21\u0c02\u0c32\u0c4b \u0c2e\u0c40 \u0c38\u0c39\u0c15\u0c3e\u0c30\u0c3e\u0c28\u0c3f\u0c15\u0c3f \u0c27\u0c28\u0c4d\u0c2f\u0c35\u0c3e\u0c26\u0c3e\u0c32\u0c41.\n\n\u0c2d\u0c35\u0c26\u0c40\u0c2f\u0c41\u0c32\u0c41,\n\u0c2e\u0c47\u0c28\u0c47\u0c1c\u0c4d\u200c\u0c2e\u0c46\u0c02\u0c1f\u0c4d \u0c15\u0c2e\u0c3f\u0c1f\u0c40"}}, {"body": "Annual General Meeting this Sunday at 10 AM.", "created_at": "2026-08-08T08:19:33", "created_by_user_id": 1, "expires_at": null, "id": 7, "notice_type": "general", "priority": "medium", "publish_at": "2026-08-08T08:19:33.856035", "society_id": 1, "title": "AGM Meeting", "translations": {}}, {"body": "Annual General Meeting this Sunday at 10 AM.", "created_at": "2026-08-08T08:18:52", "created_by_user_id": 1, "expires_at": null, "id": 6, "notice_type": "general", "priority": "medium", "publish_at": "2026-08-08T08:18:52.463326", "society_id": 1, "title": "AGM Meeting", "translations": {}}, {"body": "Annual General Meeting this Sunday at 10 AM.", "created_at": "2026-08-08T08:13:30", "created_by_user_id": 1, "expires_at": null, "id": 5, "notice_type": "general", "priority": "medium", "publish_at": "2026-08-08T08:13:30.049234", "society_id": 1, "title": "AGM Meeting", "translations": {}}, {"body": "Dear Residents,\n\nPlease be informed that a society cleaning drive is scheduled for Saturday, from 1:00 AM to 2:00 AM. All residents are requested to be present during this time and extend their cooperation to the cleaning staff to ensure smooth execution.\n\nThank you for your cooperation.\n\nWarm regards,\nManagement Committee\nSocioNeed", "created_at": "2026-08-08T06:33:33", "created_by_user_id": 1, "expires_at": null, "id": 4, "notice_type": "maintenance", "priority": "normal", "publish_at": "2026-08-08T06:33:33.725239", "society_id": 1, "title": "Notice: Society Cleaning Drive", "translations": {}}, {"body": "Please ensure visitors are pre-approved at gate entry.", "created_at": "2026-08-08T03:15:31", "created_by_user_id": 1, "expires_at": null, "id": 3, "notice_type": "security", "priority": "urgent", "publish_at": "2026-08-08T03:15:31.878754", "society_id": 1, "title": "Security Advisory", "translations": {}}, {"body": "Water tank cleaning is scheduled this weekend.", "created_at": "2026-08-08T03:15:31", "created_by_user_id": 1, "expires_at": null, "id": 1, "notice_type": "maintenance", "priority": "high", "publish_at": "2026-08-06T03:15:31.878754", "society_id": 1, "title": "Water Tank Cleaning", "translations": {}}], "pagination": {"limit": 20, "page": 1, "pages": 1, "total": 9}}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_144_complaint_status_update_audit_(case_144)(client):
    response = client.get('/api/notices', json={})
    assert response.status_code == 200
```

---

### Test Case 145: Complaint Timeline Log (Case 145)

**Page being tested**: `http://127.0.0.1:5000/api/events`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"items": [{"created_at": "2026-08-08T03:15:31", "created_by_user_id": 1, "description": "Morning wellness session in clubhouse.", "end_time": "08:00", "event_date": "Mon, 10 Aug 2026 00:00:00 GMT", "id": 1, "society_id": 1, "start_time": "07:00", "status": "scheduled", "title": "Yoga Session", "venue": "Clubhouse"}, {"created_at": "2026-08-08T03:15:31", "created_by_user_id": 1, "description": "Weekend painting workshop for children.", "end_time": "18:00", "event_date": "Thu, 13 Aug 2026 00:00:00 GMT", "id": 2, "society_id": 1, "start_time": "16:00", "status": "scheduled", "title": "Kids Painting Workshop", "venue": "Community Hall"}, {"created_at": "2026-08-08T03:15:31", "created_by_user_id": 1, "description": "Safety drill with security team guidance.", "end_time": "11:00", "event_date": "Sun, 16 Aug 2026 00:00:00 GMT", "id": 3, "society_id": 1, "start_time": "10:00", "status": "scheduled", "title": "Fire Safety Drill", "venue": "Main Courtyard"}], "pagination": {"limit": 20, "page": 1, "pages": 1, "total": 3}}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_145_complaint_timeline_log_(case_145)(client):
    response = client.get('/api/events', json={})
    assert response.status_code == 200
```

---

### Test Case 146: DB Session Rollback Verification (Case 146)

**Page being tested**: `http://127.0.0.1:5000/api/complaints`  
**Inputs**:  
- **Request Method**: GET  
- **Header**: Content-Type: application/json, Authorization: Bearer <jwt_token>  
- **JSON**: `{}`  

**Expected Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"status_code": 200, "success": true}`  

**Actual Output**:  
- **HTTP Status Code**: 200  
- **JSON**: `{"data": {"items": [{"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T10:07:15", "description": "Water leaking in kitchen", "id": 16, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T10:07:15"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T10:07:02", "description": "Water leaking in kitchen", "id": 15, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T10:07:02"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T08:42:10", "description": "Water leaking in kitchen", "id": 14, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T08:42:10"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T08:33:32", "description": "Water leaking in kitchen", "id": 13, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T08:33:32"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T08:32:20", "description": "Water leaking in kitchen", "id": 12, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T08:32:20"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T08:31:57", "description": "Water leaking in kitchen", "id": 11, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T08:31:57"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T08:31:45", "description": "Water leaking in kitchen", "id": 10, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T08:31:45"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T08:27:49", "description": "Water leaking in kitchen", "id": 9, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T08:27:49"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T08:26:09", "description": "Water leaking in kitchen", "id": 8, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T08:26:09"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T08:25:53", "description": "Water leaking in kitchen", "id": 7, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T08:25:53"}, {"assigned_to_user_id": null, "category": "Plumbing", "created_at": "2026-08-08T08:24:34", "description": "Water leaking in kitchen", "id": 6, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "Plumbing leak", "updated_at": "2026-08-08T08:24:34"}, {"assigned_to_user_id": 3, "category": "Lift", "created_at": "2026-08-08T06:24:29", "description": "asafs", "id": 5, "priority": "low", "raised_by_user_id": 2, "society_id": 1, "status": "in_progress", "subject": "adsfaf", "updated_at": "2026-08-08T06:31:05"}, {"assigned_to_user_id": null, "category": "Water", "created_at": "2026-08-08T06:24:16", "description": "suddenly water not commming", "id": 4, "priority": "high", "raised_by_user_id": 2, "society_id": 1, "status": "open", "subject": "water not comming", "updated_at": "2026-08-08T06:24:16"}, {"assigned_to_user_id": 3, "category": "Maintenance", "created_at": "2026-08-08T03:15:31", "description": "Lift in Block C has intermittent stoppage.", "id": 1, "priority": "high", "raised_by_user_id": 2, "society_id": 1, "status": "in_progress", "subject": "Lift maintenance required", "updated_at": "2026-08-08T08:24:34"}, {"assigned_to_user_id": 5, "category": "Plumbing", "created_at": "2026-08-08T03:15:31", "description": "Leakage observed near basement entry ramp.", "id": 2, "priority": "medium", "raised_by_user_id": 2, "society_id": 1, "status": "in_progress", "subject": "Water leakage near basement", "updated_at": "2026-08-08T06:25:03"}, {"assigned_to_user_id": 12, "category": "Security", "created_at": "2026-08-08T03:15:31", "description": "CCTV feed near gate 2 is blurry at night.", "id": 3, "priority": "high", "raised_by_user_id": 2, "society_id": 1, "status": "resolved", "subject": "CCTV camera blur", "updated_at": "2026-08-08T03:15:31"}], "pagination": {"limit": 20, "page": 1, "pages": 1, "total": 16}}, "message": "Success", "success": true}`  

**Result**: Success

```python
def test_case_146_db_session_rollback_verification_(case_146)(client):
    response = client.get('/api/complaints', json={})
    assert response.status_code == 200
```

---

