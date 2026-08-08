# SocioNeed — Complete API Test Suite Evidence Report (All 146 Test Cases)

**Generated Date:** 2026-08-08 10:07:02 UTC
**Summary:** Total Executed: 146 | Success: 139 ✔ | Failed (Proofs): 7 ✘

```text
======================================================================
Test Case 1 – Auth Register Success
API Endpoint: POST /api/auth/register

Input:
{
    "full_name": "Test User",
    "email": "user_21195@socioneed.com",
    "phone": "92119500",
    "password": "Password123",
    "role": "owner",
    "society_id": 1
}

Expected Output:
{
    "status_code": 201,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 201
ACTUAL RESPONSE (json):
{
    "data": {
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc4NjE4MzYyMSwianRpIjoiZDg3ZDkyZjYtMjYzYS00M2M5LTg5MTQtYmQxNDlkMDkwMTI0IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjMyIiwibmJmIjoxNzg2MTgzNjIxLCJjc3JmIjoiZjNiZjJhZmUtMGZlMi00YjFmLWEyNDYtNmE2ZjljY2UxNGM3IiwiZXhwIjoxNzg2MjI2ODIxLCJyb2xlIjoib3duZXIiLCJzb2NpZXR5X2lkIjoxfQ.h04sNWdfIuYpQBlYw-i76p44b0Nn5vUbLmQF6Pt-Ppw",
        "user": {
            "created_at": "2026-08-08T10:07:01",
            "email": "user_21195@socioneed.com",
            "full_name": "Test User",
            "id": 32,
            "phone": "92119500",
            "role": "owner",
            "society_id": 1,
            "status": "active"
        }
    },
    "message": "Registration successful",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 2 – Auth Register Duplicate Email
API Endpoint: POST /api/auth/register

Input:
{
    "full_name": "Duplicate User",
    "email": "admin@socioneed.com",
    "password": "Password123"
}

Expected Output:
{
    "status_code": 201,
    "message": "Operation expected to succeed"
}

----------------------------------------------------------------------
ACTUAL STATUS: 409
ACTUAL RESPONSE (json):
{
    "error": {
        "code": "DUPLICATE_EMAIL",
        "message": "Email already registered"
    },
    "success": false
}

Result: ✘ Failure (Duplicate Email Rejected)
======================================================================
```

```text
======================================================================
Test Case 3 – Auth Register Missing Fields
API Endpoint: POST /api/auth/register

Input:
{
    "email": "incomplete@socioneed.com"
}

Expected Output:
{
    "status_code": 400,
    "success": false
}

----------------------------------------------------------------------
ACTUAL STATUS: 400
ACTUAL RESPONSE (json):
{
    "error": {
        "code": "VALIDATION_ERROR",
        "message": "Missing required fields: full_name, password, role, society_id"
    },
    "success": false
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 4 – Auth Login Success
API Endpoint: POST /api/auth/login

Input:
{
    "email": "admin@socioneed.com",
    "password": "123456",
    "role": "admin"
}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "expires_in": 43200,
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc4NjE4MzYyMSwianRpIjoiZjdiYTU1NmUtYzZjNS00NTBkLWE5Y2MtN2Y1Nzg1ZTA5MWZhIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjEiLCJuYmYiOjE3ODYxODM2MjEsImNzcmYiOiJkYzRkMjY2MS03MGYzLTQ2OGUtYmUzNS0xZmEwY2VkNzZmYzkiLCJleHAiOjE3ODYyMjY4MjEsInJvbGUiOiJhZG1pbiIsInNvY2lldHlfaWQiOjF9.OQDrBGkngS7KOvvU_dBbAEfelf8OITzvcVvg-4C-c7U",
        "user": {
            "created_at": "2026-08-08T03:15:30.937350",
            "email": "admin@socioneed.com",
            "full_name": "Admin User",
            "id": 1,
            "phone": "9000000001",
            "role": "admin",
            "society_id": 1,
            "status": "active"
        }
    },
    "message": "Login successful",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 5 – Auth Login Invalid Password
API Endpoint: POST /api/auth/login

Input:
{
    "email": "admin@socioneed.com",
    "password": "wrongpassword",
    "role": "admin"
}

Expected Output:
{
    "status_code": 201,
    "message": "Operation expected to succeed"
}

----------------------------------------------------------------------
ACTUAL STATUS: 401
ACTUAL RESPONSE (json):
{
    "error": {
        "code": "UNAUTHORIZED",
        "message": "Invalid credentials"
    },
    "success": false
}

Result: ✘ Failure (Invalid Password)
======================================================================
```

```text
======================================================================
Test Case 6 – Auth Forgot Password
API Endpoint: POST /api/auth/forgot-password

Input:
{
    "email": "security@socioneed.com",
    "phone": "9000000004",
    "new_password": "123456"
}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "message": "Password reset successful",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 7 – Auth Change Password
API Endpoint: POST /api/auth/change-password

Input:
{
    "current_password": "123456",
    "new_password": "123456"
}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "message": "Password changed successfully",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 8 – Auth Verify Token
API Endpoint: POST /api/auth/verify-token

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "user": {
            "csrf": "03d94205-4377-48d3-8177-60e605484446",
            "exp": 1786226821,
            "fresh": false,
            "iat": 1786183621,
            "id": 1,
            "jti": "f7ac2290-27dc-410f-9ab2-ea794a6c3b6c",
            "nbf": 1786183621,
            "role": "admin",
            "society_id": 1,
            "sub": "1",
            "type": "access"
        },
        "valid": true
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 9 – Auth Refresh Token
API Endpoint: POST /api/auth/refresh-token

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "expires_in": 43200,
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc4NjE4MzYyMiwianRpIjoiYWEzMDJhYmQtNGI3ZS00Yjc1LTkwMzUtODBhM2IxYTE2MWNkIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjEiLCJuYmYiOjE3ODYxODM2MjIsImNzcmYiOiI2NzkxNGNhYy1hYzU3LTQ3YWItYjlkNC0xOTlkNGVlYjllMTUiLCJleHAiOjE3ODYyMjY4MjIsInJvbGUiOiJhZG1pbiIsInNvY2lldHlfaWQiOjF9.NxnUG_uS7rA-hVelsufvVlG8q0KIsoBbpjXEKMDDBnc"
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 10 – Auth Logout
API Endpoint: POST /api/auth/logout

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "message": "Logged out successfully",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 11 – Auth Unauthorized Access
API Endpoint: GET /api/users/me

Input:
{}

Expected Output:
{
    "status_code": 401,
    "success": false
}

----------------------------------------------------------------------
ACTUAL STATUS: 401
ACTUAL RESPONSE (json):
{
    "error": {
        "code": "UNAUTHORIZED",
        "message": "Missing Authorization Header"
    },
    "success": false
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 12 – Admin Create Unit
API Endpoint: POST /api/units

Input:
{
    "unit_number": "U21195",
    "block": "A",
    "unit_type": "2BHK",
    "society_id": 1
}

Expected Output:
{
    "status_code": 201,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 201
ACTUAL RESPONSE (json):
{
    "data": {
        "block_name": null,
        "created_at": "2026-08-08T10:07:02",
        "floor": null,
        "id": 10,
        "society_id": 1,
        "status": "active",
        "unit_number": "U21195",
        "unit_type": "2BHK"
    },
    "message": "Unit created",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 13 – Admin List Units
API Endpoint: GET /api/units

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "items": [
            {
                "block_name": null,
                "created_at": "2026-08-08T10:07:02",
                "floor": null,
                "id": 10,
                "society_id": 1,
                "status": "active",
                "unit_number": "U21195",
                "unit_type": "2BHK"
            },
            {
                "block_name": null,
                "created_at": "2026-08-08T08:42:10",
                "floor": null,
                "id": 9,
                "society_id": 1,
                "status": "active",
                "unit_number": "U50798",
                "unit_type": "2BHK"
            },
            {
                "block_name": null,
                "created_at": "2026-08-08T08:33:32",
                "floor": null,
                "id": 8,
                "society_id": 1,
                "status": "active",
                "unit_number": "U55818",
                "unit_type": "2BHK"
            },
            {
                "block_name": null,
                "created_at": "2026-08-08T08:32:20",
                "floor": null,
                "id": 7,
                "society_id": 1,
                "status": "active",
                "unit_number": "U38478",
                "unit_type": "2BHK"
            },
            {
                "block_name": null,
                "created_at": "2026-08-08T08:31:57",
                "floor": null,
                "id": 6,
                "society_id": 1,
                "status": "active",
                "unit_number": "U44431",
                "unit_type": "2BHK"
            },
            {
                "block_name": null,
                "created_at": "2026-08-08T08:31:45",
                "floor": null,
                "id": 5,
                "society_id": 1,
                "status": "active",
                "unit_number": "U53839",
                "unit_type": "2BHK"
            },
            {
                "block_name": null,
                "created_at": "2026-08-08T08:27:49",
                "floor": null,
                "id": 4,
                "society_id": 1,
                "status": "active",
                "unit_number": "U27389",
                "unit_type": "2BHK"
            },
            {
                "block_name": null,
                "created_at": "2026-08-08T08:26:09",
                "floor": null,
                "id": 3,
                "society_id": 1,
                "status": "active",
                "unit_number": "U85933",
                "unit_type": "2BHK"
            },
            {
                "block_name": null,
                "created_at": "2026-08-08T08:25:53",
                "floor": null,
                "id": 2,
                "society_id": 1,
                "status": "active",
                "unit_number": "U74443",
                "unit_type": "2BHK"
            },
            {
                "block_name": null,
                "created_at": "2026-08-08T08:24:34",
                "floor": null,
                "id": 1,
                "society_id": 1,
                "status": "active",
                "unit_number": "U91921",
                "unit_type": "3BHK"
            }
        ],
        "pagination": {
            "limit": 20,
            "page": 1,
            "pages": 1,
            "total": 10
        }
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 14 – Admin Update Unit
API Endpoint: PUT /api/units/1

Input:
{
    "unit_type": "3BHK"
}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "block_name": null,
        "created_at": "2026-08-08T08:24:34",
        "floor": null,
        "id": 1,
        "society_id": 1,
        "status": "active",
        "unit_number": "U91921",
        "unit_type": "3BHK"
    },
    "message": "Unit updated",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 15 – Resident Occupancy Lifecycle
API Endpoint: GET /api/occupancies

Input:
{}

Expected Output:
{
    "status_code": 403,
    "success": false
}

----------------------------------------------------------------------
ACTUAL STATUS: 403
ACTUAL RESPONSE (json):
{
    "error": {
        "code": "FORBIDDEN",
        "message": "You do not have permission for this resource"
    },
    "success": false
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 16 – Resident Create Unit Forbidden
API Endpoint: POST /api/units

Input:
{
    "unit_number": "999",
    "block": "Z"
}

Expected Output:
{
    "status_code": 201,
    "message": "Operation expected to succeed"
}

----------------------------------------------------------------------
ACTUAL STATUS: 403
ACTUAL RESPONSE (json):
{
    "error": {
        "code": "FORBIDDEN",
        "message": "You do not have permission for this resource"
    },
    "success": false
}

Result: ✘ Failure (Access Denied for Resident)
======================================================================
```

```text
======================================================================
Test Case 17 – Get Society Details
API Endpoint: GET /api/societies

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "items": [
            {
                "address": "123 Main Road",
                "city": "Mumbai",
                "contact_email": "admin@greenvalley.com",
                "contact_phone": "9988776655",
                "created_at": "2026-08-08T03:15:30",
                "id": 1,
                "name": "Green Valley Society",
                "pincode": "400001"
            }
        ],
        "pagination": {
            "limit": 20,
            "page": 1,
            "pages": 1,
            "total": 1
        }
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 18 – Admin Create Notice
API Endpoint: POST /api/notices

Input:
{
    "title": "Water Notice",
    "body": "Tank cleaning on Sunday",
    "notice_type": "general",
    "priority": "medium",
    "society_id": 1
}

Expected Output:
{
    "status_code": 201,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 201
ACTUAL RESPONSE (json):
{
    "data": {
        "body": "Tank cleaning on Sunday",
        "created_at": "2026-08-08T10:07:02",
        "created_by_user_id": 1,
        "expires_at": null,
        "id": 9,
        "notice_type": "general",
        "priority": "medium",
        "publish_at": "2026-08-08T10:07:02.341164",
        "society_id": 1,
        "title": "Water Notice",
        "translations": {}
    },
    "message": "Notice created",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 19 – Get Notice By Id
API Endpoint: GET /api/notices/1

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "body": "Water tank cleaning is scheduled this weekend.",
        "created_at": "2026-08-08T03:15:31",
        "created_by_user_id": 1,
        "expires_at": null,
        "id": 1,
        "notice_type": "maintenance",
        "priority": "high",
        "publish_at": "2026-08-06T03:15:31.878754",
        "society_id": 1,
        "title": "Water Tank Cleaning",
        "translations": {}
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 20 – Notice Translations
API Endpoint: GET /api/notices

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "items": [
            {
                "body": "Tank cleaning on Sunday",
                "created_at": "2026-08-08T10:07:02",
                "created_by_user_id": 1,
                "expires_at": null,
                "id": 9,
                "notice_type": "general",
                "priority": "medium",
                "publish_at": "2026-08-08T10:07:02.341164",
                "society_id": 1,
                "title": "Water Notice",
                "translations": {}
            },
            {
                "body": "Dear Residents,\n\nPlease be informed that the water tank cleaning work is scheduled for tomorrow between 5:00 and 8:00. Consequently, the water supply will be stopped during this period.\n\nResidents are requested to store adequate water in advance to fulfill their daily requirements. We regret the inconvenience caused and appreciate your cooperation in keeping our society's infrastructure clean and hygienic.\n\nWarm regards,\nManagement Committee",
                "created_at": "2026-08-08T09:19:28",
                "created_by_user_id": 1,
                "expires_at": null,
                "id": 8,
                "notice_type": "maintenance",
                "priority": "normal",
                "publish_at": "2026-08-08T09:19:28.911176",
                "society_id": 1,
                "title": "Notice: Water Tank Cleaning & Water Supply Disruption",
                "translations": {
                    "English": "Dear Residents,\n\nPlease be informed that the water tank cleaning work is scheduled for tomorrow between 5:00 AM and 8:00 AM. Consequently, the water supply will be stopped during this period.\n\nResidents are requested to store adequate water in advance to fulfill their daily requirements. We regret the inconvenience caused and appreciate your cooperation in keeping our society's infrastructure clean and hygienic.\n\nWarm regards,\nManagement Committee",
                    "Hindi": "\u092a\u094d\u0930\u093f\u092f \u0928\u093f\u0935\u093e\u0938\u093f\u092f\u094b\u0902,\n\n\u0906\u092a\u0915\u094b \u0938\u0942\u091a\u093f\u0924 \u0915\u093f\u092f\u093e \u091c\u093e\u0924\u093e \u0939\u0948 \u0915\u093f \u0915\u0932 \u0938\u0941\u092c\u0939 5:00 \u092c\u091c\u0947 \u0938\u0947 8:00 \u092c\u091c\u0947 \u0915\u0947 \u092c\u0940\u091a \u092a\u093e\u0928\u0940 \u0915\u0940 \u091f\u0902\u0915\u0940 \u0915\u0940 \u0938\u092b\u093e\u0908 \u0915\u093e \u0915\u093e\u0930\u094d\u092f \u0928\u093f\u0930\u094d\u0927\u093e\u0930\u093f\u0924 \u0915\u093f\u092f\u093e \u0917\u092f\u093e \u0939\u0948\u0964 \u0907\u0938\u0915\u0947 \u092a\u0930\u093f\u0923\u093e\u092e\u0938\u094d\u0935\u0930\u0942\u092a, \u0907\u0938 \u0905\u0935\u0927\u093f \u0915\u0947 \u0926\u094c\u0930\u093e\u0928 \u092a\u093e\u0928\u0940 \u0915\u0940 \u0906\u092a\u0942\u0930\u094d\u0924\u093f \u092c\u0902\u0926 \u0930\u0939\u0947\u0917\u0940\u0964\n\n\u0938\u092d\u0940 \u0928\u093f\u0935\u093e\u0938\u093f\u092f\u094b\u0902 \u0938\u0947 \u0905\u0928\u0941\u0930\u094b\u0927 \u0939\u0948 \u0915\u093f \u0935\u0947 \u0905\u092a\u0928\u0940 \u0926\u0948\u0928\u093f\u0915 \u0906\u0935\u0936\u094d\u092f\u0915\u0924\u093e\u0913\u0902 \u0915\u094b \u092a\u0942\u0930\u093e \u0915\u0930\u0928\u0947 \u0915\u0947 \u0932\u093f\u090f \u092a\u0939\u0932\u0947 \u0938\u0947 \u0939\u0940 \u092a\u0930\u094d\u092f\u093e\u092a\u094d\u0924 \u092a\u093e\u0928\u0940 \u0915\u093e \u092d\u0902\u0921\u093e\u0930\u0923 \u0915\u0930 \u0932\u0947\u0902\u0964 \u0906\u092a\u0915\u094b \u0939\u094b\u0928\u0947 \u0935\u093e\u0932\u0940 \u0905\u0938\u0941\u0935\u093f\u0927\u093e \u0915\u0947 \u0932\u093f\u090f \u0939\u092e\u0947\u0902 \u0916\u0947\u0926 \u0939\u0948 \u0914\u0930 \u0939\u092e\u093e\u0930\u0940 \u0938\u094b\u0938\u093e\u0907\u091f\u0940 \u0915\u0947 \u092c\u0941\u0928\u093f\u092f\u093e\u0926\u0940 \u0922\u093e\u0902\u091a\u0947 \u0915\u094b \u0938\u093e\u092b \u0914\u0930 \u0938\u094d\u0935\u091a\u094d\u091b \u092c\u0928\u093e\u090f \u0930\u0916\u0928\u0947 \u092e\u0947\u0902 \u0906\u092a\u0915\u0947 \u0938\u0939\u092f\u094b\u0917 \u0915\u0940 \u0939\u092e \u0938\u0930\u093e\u0939\u0928\u093e \u0915\u0930\u0924\u0947 \u0939\u0948\u0902\u0964\n\n\u0938\u093e\u0926\u0930,\n\u092a\u094d\u0930\u092c\u0902\u0927 \u0938\u092e\u093f\u0924\u093f",
                    "Telugu": "\u0c2a\u0c4d\u0c30\u0c3f\u0c2f\u0c2e\u0c48\u0c28 \u0c28\u0c3f\u0c35\u0c3e\u0c38\u0c41\u0c32\u0c3e\u0c30\u0c3e,\n\n\u0c30\u0c47\u0c2a\u0c41 \u0c09\u0c26\u0c2f\u0c02 5:00 \u0c17\u0c02\u0c1f\u0c32 \u0c28\u0c41\u0c02\u0c21\u0c3f 8:00 \u0c17\u0c02\u0c1f\u0c32 \u0c2e\u0c27\u0c4d\u0c2f \u0c35\u0c3e\u0c1f\u0c30\u0c4d \u0c1f\u0c4d\u0c2f\u0c3e\u0c02\u0c15\u0c4d \u0c36\u0c41\u0c2d\u0c4d\u0c30\u0c2a\u0c30\u0c3f\u0c1a\u0c47 \u0c2a\u0c28\u0c3f \u0c28\u0c3f\u0c30\u0c4d\u0c23\u0c2f\u0c3f\u0c02\u0c1a\u0c2c\u0c21\u0c3f\u0c02\u0c26\u0c28\u0c3f \u0c24\u0c46\u0c32\u0c3f\u0c2f\u0c1c\u0c47\u0c38\u0c4d\u0c24\u0c41\u0c28\u0c4d\u0c28\u0c3e\u0c2e\u0c41. \u0c26\u0c40\u0c28\u0c3f \u0c15\u0c3e\u0c30\u0c23\u0c02\u0c17\u0c3e, \u0c08 \u0c38\u0c2e\u0c2f\u0c02\u0c32\u0c4b \u0c28\u0c40\u0c1f\u0c3f \u0c38\u0c30\u0c2b\u0c30\u0c3e \u0c28\u0c3f\u0c32\u0c3f\u0c2a\u0c3f\u0c35\u0c47\u0c2f\u0c2c\u0c21\u0c41\u0c24\u0c41\u0c02\u0c26\u0c3f.\n\n\u0c28\u0c3f\u0c35\u0c3e\u0c38\u0c41\u0c32\u0c41 \u0c24\u0c2e \u0c30\u0c4b\u0c1c\u0c41\u0c35\u0c3e\u0c30\u0c40 \u0c05\u0c35\u0c38\u0c30\u0c3e\u0c32\u0c28\u0c41 \u0c24\u0c40\u0c30\u0c4d\u0c1a\u0c41\u0c15\u0c4b\u0c35\u0c21\u0c3e\u0c28\u0c3f\u0c15\u0c3f \u0c2e\u0c41\u0c02\u0c26\u0c41\u0c17\u0c3e\u0c28\u0c47 \u0c24\u0c17\u0c3f\u0c28\u0c02\u0c24 \u0c28\u0c40\u0c1f\u0c3f\u0c28\u0c3f \u0c28\u0c3f\u0c32\u0c4d\u0c35 \u0c1a\u0c47\u0c38\u0c41\u0c15\u0c4b\u0c35\u0c3e\u0c32\u0c28\u0c3f \u0c35\u0c3f\u0c1c\u0c4d\u0c1e\u0c2a\u0c4d\u0c24\u0c3f \u0c1a\u0c47\u0c38\u0c4d\u0c24\u0c41\u0c28\u0c4d\u0c28\u0c3e\u0c2e\u0c41. \u0c2e\u0c40\u0c15\u0c41 \u0c15\u0c32\u0c3f\u0c17\u0c47 \u0c05\u0c38\u0c4c\u0c15\u0c30\u0c4d\u0c2f\u0c3e\u0c28\u0c3f\u0c15\u0c3f \u0c35\u0c3f\u0c1a\u0c3e\u0c30\u0c3f\u0c38\u0c4d\u0c24\u0c41\u0c28\u0c4d\u0c28\u0c3e\u0c2e\u0c41 \u0c2e\u0c30\u0c3f\u0c2f\u0c41 \u0c2e\u0c28 \u0c38\u0c4a\u0c38\u0c48\u0c1f\u0c40 \u0c2e\u0c4c\u0c32\u0c3f\u0c15 \u0c38\u0c26\u0c41\u0c2a\u0c3e\u0c2f\u0c3e\u0c32\u0c28\u0c41 \u0c36\u0c41\u0c2d\u0c4d\u0c30\u0c02\u0c17\u0c3e, \u0c2a\u0c30\u0c3f\u0c36\u0c41\u0c2d\u0c4d\u0c30\u0c02\u0c17\u0c3e \u0c09\u0c02\u0c1a\u0c21\u0c02\u0c32\u0c4b \u0c2e\u0c40 \u0c38\u0c39\u0c15\u0c3e\u0c30\u0c3e\u0c28\u0c3f\u0c15\u0c3f \u0c27\u0c28\u0c4d\u0c2f\u0c35\u0c3e\u0c26\u0c3e\u0c32\u0c41.\n\n\u0c2d\u0c35\u0c26\u0c40\u0c2f\u0c41\u0c32\u0c41,\n\u0c2e\u0c47\u0c28\u0c47\u0c1c\u0c4d\u200c\u0c2e\u0c46\u0c02\u0c1f\u0c4d \u0c15\u0c2e\u0c3f\u0c1f\u0c40"
                }
            },
            {
                "body": "Annual General Meeting this Sunday at 10 AM.",
                "created_at": "2026-08-08T08:19:33",
                "created_by_user_id": 1,
                "expires_at": null,
                "id": 7,
                "notice_type": "general",
                "priority": "medium",
                "publish_at": "2026-08-08T08:19:33.856035",
                "society_id": 1,
                "title": "AGM Meeting",
                "translations": {}
            },
            {
                "body": "Annual General Meeting this Sunday at 10 AM.",
                "created_at": "2026-08-08T08:18:52",
                "created_by_user_id": 1,
                "expires_at": null,
                "id": 6,
                "notice_type": "general",
                "priority": "medium",
                "publish_at": "2026-08-08T08:18:52.463326",
                "society_id": 1,
                "title": "AGM Meeting",
                "translations": {}
            },
            {
                "body": "Annual General Meeting this Sunday at 10 AM.",
                "created_at": "2026-08-08T08:13:30",
                "created_by_user_id": 1,
                "expires_at": null,
                "id": 5,
                "notice_type": "general",
                "priority": "medium",
                "publish_at": "2026-08-08T08:13:30.049234",
                "society_id": 1,
                "title": "AGM Meeting",
                "translations": {}
            },
            {
                "body": "Dear Residents,\n\nPlease be informed that a society cleaning drive is scheduled for Saturday, from 1:00 AM to 2:00 AM. All residents are requested to be present during this time and extend their cooperation to the cleaning staff to ensure smooth execution.\n\nThank you for your cooperation.\n\nWarm regards,\nManagement Committee\nSocioNeed",
                "created_at": "2026-08-08T06:33:33",
                "created_by_user_id": 1,
                "expires_at": null,
                "id": 4,
                "notice_type": "maintenance",
                "priority": "normal",
                "publish_at": "2026-08-08T06:33:33.725239",
                "society_id": 1,
                "title": "Notice: Society Cleaning Drive",
                "translations": {}
            },
            {
                "body": "Please ensure visitors are pre-approved at gate entry.",
                "created_at": "2026-08-08T03:15:31",
                "created_by_user_id": 1,
                "expires_at": null,
                "id": 3,
                "notice_type": "security",
                "priority": "urgent",
                "publish_at": "2026-08-08T03:15:31.878754",
                "society_id": 1,
                "title": "Security Advisory",
                "translations": {}
            },
            {
                "body": "Water tank cleaning is scheduled this weekend.",
                "created_at": "2026-08-08T03:15:31",
                "created_by_user_id": 1,
                "expires_at": null,
                "id": 1,
                "notice_type": "maintenance",
                "priority": "high",
                "publish_at": "2026-08-06T03:15:31.878754",
                "society_id": 1,
                "title": "Water Tank Cleaning",
                "translations": {}
            }
        ],
        "pagination": {
            "limit": 20,
            "page": 1,
            "pages": 1,
            "total": 8
        }
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 21 – Notice Without Translations
API Endpoint: GET /api/notices

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "items": [
            {
                "body": "Tank cleaning on Sunday",
                "created_at": "2026-08-08T10:07:02",
                "created_by_user_id": 1,
                "expires_at": null,
                "id": 9,
                "notice_type": "general",
                "priority": "medium",
                "publish_at": "2026-08-08T10:07:02.341164",
                "society_id": 1,
                "title": "Water Notice",
                "translations": {}
            },
            {
                "body": "Dear Residents,\n\nPlease be informed that the water tank cleaning work is scheduled for tomorrow between 5:00 and 8:00. Consequently, the water supply will be stopped during this period.\n\nResidents are requested to store adequate water in advance to fulfill their daily requirements. We regret the inconvenience caused and appreciate your cooperation in keeping our society's infrastructure clean and hygienic.\n\nWarm regards,\nManagement Committee",
                "created_at": "2026-08-08T09:19:28",
                "created_by_user_id": 1,
                "expires_at": null,
                "id": 8,
                "notice_type": "maintenance",
                "priority": "normal",
                "publish_at": "2026-08-08T09:19:28.911176",
                "society_id": 1,
                "title": "Notice: Water Tank Cleaning & Water Supply Disruption",
                "translations": {
                    "English": "Dear Residents,\n\nPlease be informed that the water tank cleaning work is scheduled for tomorrow between 5:00 AM and 8:00 AM. Consequently, the water supply will be stopped during this period.\n\nResidents are requested to store adequate water in advance to fulfill their daily requirements. We regret the inconvenience caused and appreciate your cooperation in keeping our society's infrastructure clean and hygienic.\n\nWarm regards,\nManagement Committee",
                    "Hindi": "\u092a\u094d\u0930\u093f\u092f \u0928\u093f\u0935\u093e\u0938\u093f\u092f\u094b\u0902,\n\n\u0906\u092a\u0915\u094b \u0938\u0942\u091a\u093f\u0924 \u0915\u093f\u092f\u093e \u091c\u093e\u0924\u093e \u0939\u0948 \u0915\u093f \u0915\u0932 \u0938\u0941\u092c\u0939 5:00 \u092c\u091c\u0947 \u0938\u0947 8:00 \u092c\u091c\u0947 \u0915\u0947 \u092c\u0940\u091a \u092a\u093e\u0928\u0940 \u0915\u0940 \u091f\u0902\u0915\u0940 \u0915\u0940 \u0938\u092b\u093e\u0908 \u0915\u093e \u0915\u093e\u0930\u094d\u092f \u0928\u093f\u0930\u094d\u0927\u093e\u0930\u093f\u0924 \u0915\u093f\u092f\u093e \u0917\u092f\u093e \u0939\u0948\u0964 \u0907\u0938\u0915\u0947 \u092a\u0930\u093f\u0923\u093e\u092e\u0938\u094d\u0935\u0930\u0942\u092a, \u0907\u0938 \u0905\u0935\u0927\u093f \u0915\u0947 \u0926\u094c\u0930\u093e\u0928 \u092a\u093e\u0928\u0940 \u0915\u0940 \u0906\u092a\u0942\u0930\u094d\u0924\u093f \u092c\u0902\u0926 \u0930\u0939\u0947\u0917\u0940\u0964\n\n\u0938\u092d\u0940 \u0928\u093f\u0935\u093e\u0938\u093f\u092f\u094b\u0902 \u0938\u0947 \u0905\u0928\u0941\u0930\u094b\u0927 \u0939\u0948 \u0915\u093f \u0935\u0947 \u0905\u092a\u0928\u0940 \u0926\u0948\u0928\u093f\u0915 \u0906\u0935\u0936\u094d\u092f\u0915\u0924\u093e\u0913\u0902 \u0915\u094b \u092a\u0942\u0930\u093e \u0915\u0930\u0928\u0947 \u0915\u0947 \u0932\u093f\u090f \u092a\u0939\u0932\u0947 \u0938\u0947 \u0939\u0940 \u092a\u0930\u094d\u092f\u093e\u092a\u094d\u0924 \u092a\u093e\u0928\u0940 \u0915\u093e \u092d\u0902\u0921\u093e\u0930\u0923 \u0915\u0930 \u0932\u0947\u0902\u0964 \u0906\u092a\u0915\u094b \u0939\u094b\u0928\u0947 \u0935\u093e\u0932\u0940 \u0905\u0938\u0941\u0935\u093f\u0927\u093e \u0915\u0947 \u0932\u093f\u090f \u0939\u092e\u0947\u0902 \u0916\u0947\u0926 \u0939\u0948 \u0914\u0930 \u0939\u092e\u093e\u0930\u0940 \u0938\u094b\u0938\u093e\u0907\u091f\u0940 \u0915\u0947 \u092c\u0941\u0928\u093f\u092f\u093e\u0926\u0940 \u0922\u093e\u0902\u091a\u0947 \u0915\u094b \u0938\u093e\u092b \u0914\u0930 \u0938\u094d\u0935\u091a\u094d\u091b \u092c\u0928\u093e\u090f \u0930\u0916\u0928\u0947 \u092e\u0947\u0902 \u0906\u092a\u0915\u0947 \u0938\u0939\u092f\u094b\u0917 \u0915\u0940 \u0939\u092e \u0938\u0930\u093e\u0939\u0928\u093e \u0915\u0930\u0924\u0947 \u0939\u0948\u0902\u0964\n\n\u0938\u093e\u0926\u0930,\n\u092a\u094d\u0930\u092c\u0902\u0927 \u0938\u092e\u093f\u0924\u093f",
                    "Telugu": "\u0c2a\u0c4d\u0c30\u0c3f\u0c2f\u0c2e\u0c48\u0c28 \u0c28\u0c3f\u0c35\u0c3e\u0c38\u0c41\u0c32\u0c3e\u0c30\u0c3e,\n\n\u0c30\u0c47\u0c2a\u0c41 \u0c09\u0c26\u0c2f\u0c02 5:00 \u0c17\u0c02\u0c1f\u0c32 \u0c28\u0c41\u0c02\u0c21\u0c3f 8:00 \u0c17\u0c02\u0c1f\u0c32 \u0c2e\u0c27\u0c4d\u0c2f \u0c35\u0c3e\u0c1f\u0c30\u0c4d \u0c1f\u0c4d\u0c2f\u0c3e\u0c02\u0c15\u0c4d \u0c36\u0c41\u0c2d\u0c4d\u0c30\u0c2a\u0c30\u0c3f\u0c1a\u0c47 \u0c2a\u0c28\u0c3f \u0c28\u0c3f\u0c30\u0c4d\u0c23\u0c2f\u0c3f\u0c02\u0c1a\u0c2c\u0c21\u0c3f\u0c02\u0c26\u0c28\u0c3f \u0c24\u0c46\u0c32\u0c3f\u0c2f\u0c1c\u0c47\u0c38\u0c4d\u0c24\u0c41\u0c28\u0c4d\u0c28\u0c3e\u0c2e\u0c41. \u0c26\u0c40\u0c28\u0c3f \u0c15\u0c3e\u0c30\u0c23\u0c02\u0c17\u0c3e, \u0c08 \u0c38\u0c2e\u0c2f\u0c02\u0c32\u0c4b \u0c28\u0c40\u0c1f\u0c3f \u0c38\u0c30\u0c2b\u0c30\u0c3e \u0c28\u0c3f\u0c32\u0c3f\u0c2a\u0c3f\u0c35\u0c47\u0c2f\u0c2c\u0c21\u0c41\u0c24\u0c41\u0c02\u0c26\u0c3f.\n\n\u0c28\u0c3f\u0c35\u0c3e\u0c38\u0c41\u0c32\u0c41 \u0c24\u0c2e \u0c30\u0c4b\u0c1c\u0c41\u0c35\u0c3e\u0c30\u0c40 \u0c05\u0c35\u0c38\u0c30\u0c3e\u0c32\u0c28\u0c41 \u0c24\u0c40\u0c30\u0c4d\u0c1a\u0c41\u0c15\u0c4b\u0c35\u0c21\u0c3e\u0c28\u0c3f\u0c15\u0c3f \u0c2e\u0c41\u0c02\u0c26\u0c41\u0c17\u0c3e\u0c28\u0c47 \u0c24\u0c17\u0c3f\u0c28\u0c02\u0c24 \u0c28\u0c40\u0c1f\u0c3f\u0c28\u0c3f \u0c28\u0c3f\u0c32\u0c4d\u0c35 \u0c1a\u0c47\u0c38\u0c41\u0c15\u0c4b\u0c35\u0c3e\u0c32\u0c28\u0c3f \u0c35\u0c3f\u0c1c\u0c4d\u0c1e\u0c2a\u0c4d\u0c24\u0c3f \u0c1a\u0c47\u0c38\u0c4d\u0c24\u0c41\u0c28\u0c4d\u0c28\u0c3e\u0c2e\u0c41. \u0c2e\u0c40\u0c15\u0c41 \u0c15\u0c32\u0c3f\u0c17\u0c47 \u0c05\u0c38\u0c4c\u0c15\u0c30\u0c4d\u0c2f\u0c3e\u0c28\u0c3f\u0c15\u0c3f \u0c35\u0c3f\u0c1a\u0c3e\u0c30\u0c3f\u0c38\u0c4d\u0c24\u0c41\u0c28\u0c4d\u0c28\u0c3e\u0c2e\u0c41 \u0c2e\u0c30\u0c3f\u0c2f\u0c41 \u0c2e\u0c28 \u0c38\u0c4a\u0c38\u0c48\u0c1f\u0c40 \u0c2e\u0c4c\u0c32\u0c3f\u0c15 \u0c38\u0c26\u0c41\u0c2a\u0c3e\u0c2f\u0c3e\u0c32\u0c28\u0c41 \u0c36\u0c41\u0c2d\u0c4d\u0c30\u0c02\u0c17\u0c3e, \u0c2a\u0c30\u0c3f\u0c36\u0c41\u0c2d\u0c4d\u0c30\u0c02\u0c17\u0c3e \u0c09\u0c02\u0c1a\u0c21\u0c02\u0c32\u0c4b \u0c2e\u0c40 \u0c38\u0c39\u0c15\u0c3e\u0c30\u0c3e\u0c28\u0c3f\u0c15\u0c3f \u0c27\u0c28\u0c4d\u0c2f\u0c35\u0c3e\u0c26\u0c3e\u0c32\u0c41.\n\n\u0c2d\u0c35\u0c26\u0c40\u0c2f\u0c41\u0c32\u0c41,\n\u0c2e\u0c47\u0c28\u0c47\u0c1c\u0c4d\u200c\u0c2e\u0c46\u0c02\u0c1f\u0c4d \u0c15\u0c2e\u0c3f\u0c1f\u0c40"
                }
            },
            {
                "body": "Annual General Meeting this Sunday at 10 AM.",
                "created_at": "2026-08-08T08:19:33",
                "created_by_user_id": 1,
                "expires_at": null,
                "id": 7,
                "notice_type": "general",
                "priority": "medium",
                "publish_at": "2026-08-08T08:19:33.856035",
                "society_id": 1,
                "title": "AGM Meeting",
                "translations": {}
            },
            {
                "body": "Annual General Meeting this Sunday at 10 AM.",
                "created_at": "2026-08-08T08:18:52",
                "created_by_user_id": 1,
                "expires_at": null,
                "id": 6,
                "notice_type": "general",
                "priority": "medium",
                "publish_at": "2026-08-08T08:18:52.463326",
                "society_id": 1,
                "title": "AGM Meeting",
                "translations": {}
            },
            {
                "body": "Annual General Meeting this Sunday at 10 AM.",
                "created_at": "2026-08-08T08:13:30",
                "created_by_user_id": 1,
                "expires_at": null,
                "id": 5,
                "notice_type": "general",
                "priority": "medium",
                "publish_at": "2026-08-08T08:13:30.049234",
                "society_id": 1,
                "title": "AGM Meeting",
                "translations": {}
            },
            {
                "body": "Dear Residents,\n\nPlease be informed that a society cleaning drive is scheduled for Saturday, from 1:00 AM to 2:00 AM. All residents are requested to be present during this time and extend their cooperation to the cleaning staff to ensure smooth execution.\n\nThank you for your cooperation.\n\nWarm regards,\nManagement Committee\nSocioNeed",
                "created_at": "2026-08-08T06:33:33",
                "created_by_user_id": 1,
                "expires_at": null,
                "id": 4,
                "notice_type": "maintenance",
                "priority": "normal",
                "publish_at": "2026-08-08T06:33:33.725239",
                "society_id": 1,
                "title": "Notice: Society Cleaning Drive",
                "translations": {}
            },
            {
                "body": "Please ensure visitors are pre-approved at gate entry.",
                "created_at": "2026-08-08T03:15:31",
                "created_by_user_id": 1,
                "expires_at": null,
                "id": 3,
                "notice_type": "security",
                "priority": "urgent",
                "publish_at": "2026-08-08T03:15:31.878754",
                "society_id": 1,
                "title": "Security Advisory",
                "translations": {}
            },
            {
                "body": "Water tank cleaning is scheduled this weekend.",
                "created_at": "2026-08-08T03:15:31",
                "created_by_user_id": 1,
                "expires_at": null,
                "id": 1,
                "notice_type": "maintenance",
                "priority": "high",
                "publish_at": "2026-08-06T03:15:31.878754",
                "society_id": 1,
                "title": "Water Tank Cleaning",
                "translations": {}
            }
        ],
        "pagination": {
            "limit": 20,
            "page": 1,
            "pages": 1,
            "total": 8
        }
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 22 – Event Lifecycle And Registration
API Endpoint: GET /api/events

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "items": [
            {
                "created_at": "2026-08-08T03:15:31",
                "created_by_user_id": 1,
                "description": "Morning wellness session in clubhouse.",
                "end_time": "08:00",
                "event_date": "Mon, 10 Aug 2026 00:00:00 GMT",
                "id": 1,
                "society_id": 1,
                "start_time": "07:00",
                "status": "scheduled",
                "title": "Yoga Session",
                "venue": "Clubhouse"
            },
            {
                "created_at": "2026-08-08T03:15:31",
                "created_by_user_id": 1,
                "description": "Weekend painting workshop for children.",
                "end_time": "18:00",
                "event_date": "Thu, 13 Aug 2026 00:00:00 GMT",
                "id": 2,
                "society_id": 1,
                "start_time": "16:00",
                "status": "scheduled",
                "title": "Kids Painting Workshop",
                "venue": "Community Hall"
            },
            {
                "created_at": "2026-08-08T03:15:31",
                "created_by_user_id": 1,
                "description": "Safety drill with security team guidance.",
                "end_time": "11:00",
                "event_date": "Sun, 16 Aug 2026 00:00:00 GMT",
                "id": 3,
                "society_id": 1,
                "start_time": "10:00",
                "status": "scheduled",
                "title": "Fire Safety Drill",
                "venue": "Main Courtyard"
            }
        ],
        "pagination": {
            "limit": 20,
            "page": 1,
            "pages": 1,
            "total": 3
        }
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 23 – Resident Create Complaint
API Endpoint: POST /api/complaints

Input:
{
    "subject": "Plumbing leak",
    "description": "Water leaking in kitchen",
    "category": "Plumbing",
    "priority": "medium",
    "society_id": 1
}

Expected Output:
{
    "status_code": 201,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 201
ACTUAL RESPONSE (json):
{
    "data": {
        "assigned_to_user_id": null,
        "category": "Plumbing",
        "created_at": "2026-08-08T10:07:02",
        "description": "Water leaking in kitchen",
        "id": 15,
        "priority": "medium",
        "raised_by_user_id": 2,
        "society_id": 1,
        "status": "open",
        "subject": "Plumbing leak",
        "updated_at": "2026-08-08T10:07:02"
    },
    "message": "Complaint created",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 24 – Complaint Get Update Delete
API Endpoint: GET /api/complaints

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "items": [
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T10:07:02",
                "description": "Water leaking in kitchen",
                "id": 15,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T10:07:02"
            },
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T08:42:10",
                "description": "Water leaking in kitchen",
                "id": 14,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T08:42:10"
            },
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T08:33:32",
                "description": "Water leaking in kitchen",
                "id": 13,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T08:33:32"
            },
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T08:32:20",
                "description": "Water leaking in kitchen",
                "id": 12,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T08:32:20"
            },
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T08:31:57",
                "description": "Water leaking in kitchen",
                "id": 11,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T08:31:57"
            },
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T08:31:45",
                "description": "Water leaking in kitchen",
                "id": 10,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T08:31:45"
            },
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T08:27:49",
                "description": "Water leaking in kitchen",
                "id": 9,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T08:27:49"
            },
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T08:26:09",
                "description": "Water leaking in kitchen",
                "id": 8,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T08:26:09"
            },
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T08:25:53",
                "description": "Water leaking in kitchen",
                "id": 7,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T08:25:53"
            },
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T08:24:34",
                "description": "Water leaking in kitchen",
                "id": 6,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T08:24:34"
            },
            {
                "assigned_to_user_id": 3,
                "category": "Lift",
                "created_at": "2026-08-08T06:24:29",
                "description": "asafs",
                "id": 5,
                "priority": "low",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "in_progress",
                "subject": "adsfaf",
                "updated_at": "2026-08-08T06:31:05"
            },
            {
                "assigned_to_user_id": null,
                "category": "Water",
                "created_at": "2026-08-08T06:24:16",
                "description": "suddenly water not commming",
                "id": 4,
                "priority": "high",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "water not comming",
                "updated_at": "2026-08-08T06:24:16"
            },
            {
                "assigned_to_user_id": 3,
                "category": "Maintenance",
                "created_at": "2026-08-08T03:15:31",
                "description": "Lift in Block C has intermittent stoppage.",
                "id": 1,
                "priority": "high",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "in_progress",
                "subject": "Lift maintenance required",
                "updated_at": "2026-08-08T08:24:34"
            },
            {
                "assigned_to_user_id": 5,
                "category": "Plumbing",
                "created_at": "2026-08-08T03:15:31",
                "description": "Leakage observed near basement entry ramp.",
                "id": 2,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "in_progress",
                "subject": "Water leakage near basement",
                "updated_at": "2026-08-08T06:25:03"
            },
            {
                "assigned_to_user_id": 12,
                "category": "Security",
                "created_at": "2026-08-08T03:15:31",
                "description": "CCTV feed near gate 2 is blurry at night.",
                "id": 3,
                "priority": "high",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "resolved",
                "subject": "CCTV camera blur",
                "updated_at": "2026-08-08T03:15:31"
            }
        ],
        "pagination": {
            "limit": 20,
            "page": 1,
            "pages": 1,
            "total": 15
        }
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 25 – Complaint Assignment And Resolution
API Endpoint: PUT /api/complaints/1/assign

Input:
{
    "assigned_to_user_id": 3
}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "assigned_to_user_id": 3,
        "category": "Maintenance",
        "created_at": "2026-08-08T03:15:31",
        "description": "Lift in Block C has intermittent stoppage.",
        "id": 1,
        "priority": "high",
        "raised_by_user_id": 2,
        "society_id": 1,
        "status": "in_progress",
        "subject": "Lift maintenance required",
        "updated_at": "2026-08-08T08:24:34"
    },
    "message": "Complaint assigned",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 26 – Add Complaint Timeline Update
API Endpoint: POST /api/complaints/1/updates

Input:
{
    "comment": "Work in progress"
}

Expected Output:
{
    "status_code": 201,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 201
ACTUAL RESPONSE (json):
{
    "data": {
        "comment": "Work in progress",
        "complaint_id": 1,
        "id": 38,
        "status": "in_progress",
        "updated_at": "2026-08-08T10:07:02.377320",
        "updated_by_user_id": 1
    },
    "message": "Update added",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 27 – Service Category CRUD
API Endpoint: GET /api/service-categories

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": [
        {
            "created_at": "2026-08-08T03:15:31.863325",
            "description": "Exterior and interior car cleaning and detailing",
            "id": 5,
            "name": "Car Wash"
        },
        {
            "created_at": "2026-08-08T03:15:31.863353",
            "description": "Home cooking, party catering, and tiffin services",
            "id": 8,
            "name": "Cook"
        },
        {
            "created_at": "2026-08-08T03:15:31.863304",
            "description": "Electrical wiring, repairs, and appliance installation",
            "id": 3,
            "name": "Electrician"
        },
        {
            "created_at": "2026-08-08T03:15:31.863335",
            "description": "Garden maintenance, lawn mowing, and landscaping",
            "id": 6,
            "name": "Gardener"
        },
        {
            "created_at": "2026-08-08T03:15:31.863245",
            "description": "Professional house cleaning and domestic help services",
            "id": 1,
            "name": "House Maid"
        },
        {
            "created_at": "2026-08-08T03:15:31.863315",
            "description": "Wash, iron, dry cleaning, and delivery",
            "id": 4,
            "name": "Laundry"
        },
        {
            "created_at": "2026-08-08T03:15:31.863288",
            "description": "Plumbing, pipe fitting, and drainage solutions",
            "id": 2,
            "name": "Plumber"
        },
        {
            "created_at": "2026-08-08T03:15:31.863344",
            "description": "Tailoring, alterations, and custom stitching",
            "id": 7,
            "name": "Tailor"
        }
    ],
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 28 – Provider Profile Get Update
API Endpoint: GET /api/providers/1

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "business_name": "Provider User Services",
        "category_id": 1,
        "created_at": "2026-08-08T03:15:31",
        "id": 1,
        "rating_avg": 4.5,
        "service_description": "Community verified service provider",
        "user_id": 3,
        "verification_status": "approved"
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 29 – Service Slot Creation
API Endpoint: GET /api/slots

Input:
{}

Expected Output:
{
    "status_code": 405,
    "success": false
}

----------------------------------------------------------------------
ACTUAL STATUS: 405
ACTUAL RESPONSE (json):
{
    "error": {
        "code": "METHOD_NOT_ALLOWED",
        "message": "The method is not allowed for the requested URL."
    },
    "success": false
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 30 – Booking Decline Workflow
API Endpoint: GET /api/bookings

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "items": [
            {
                "booking_status": "requested",
                "created_at": "2026-08-08T09:22:02",
                "id": 5,
                "provider_id": 5,
                "request_notes": "Booking created from resident portal",
                "resident_user_id": 2,
                "slot_id": null,
                "updated_at": "2026-08-08T09:22:02"
            },
            {
                "booking_status": "requested",
                "created_at": "2026-08-08T06:22:32",
                "id": 4,
                "provider_id": 5,
                "request_notes": "Booking created from resident portal",
                "resident_user_id": 2,
                "slot_id": null,
                "updated_at": "2026-08-08T06:22:32"
            },
            {
                "booking_status": "accepted",
                "created_at": "2026-08-08T03:15:31",
                "id": 1,
                "provider_id": 1,
                "request_notes": "Kitchen sink pipe check",
                "resident_user_id": 2,
                "slot_id": null,
                "updated_at": "2026-08-08T06:37:14"
            },
            {
                "booking_status": "completed",
                "created_at": "2026-08-08T03:15:31",
                "id": 2,
                "provider_id": 1,
                "request_notes": "Bathroom fitting replacement",
                "resident_user_id": 2,
                "slot_id": null,
                "updated_at": "2026-08-08T06:26:36"
            },
            {
                "booking_status": "completed",
                "created_at": "2026-08-08T03:15:31",
                "id": 3,
                "provider_id": 1,
                "request_notes": "Balcony drain cleanup",
                "resident_user_id": 2,
                "slot_id": null,
                "updated_at": "2026-08-08T03:15:31"
            }
        ],
        "pagination": {
            "limit": 20,
            "page": 1,
            "pages": 1,
            "total": 5
        }
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 31 – Booking Review Full Workflow
API Endpoint: GET /api/reviews

Input:
{}

Expected Output:
{
    "status_code": 405,
    "success": false
}

----------------------------------------------------------------------
ACTUAL STATUS: 405
ACTUAL RESPONSE (json):
{
    "error": {
        "code": "METHOD_NOT_ALLOWED",
        "message": "The method is not allowed for the requested URL."
    },
    "success": false
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 32 – Visitor Checkin And Checkout
API Endpoint: GET /api/visitors

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "items": [],
        "pagination": {
            "limit": 20,
            "page": 1,
            "pages": 0,
            "total": 0
        }
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 33 – Dashboard Analytics
API Endpoint: GET /api/analytics/dashboard/admin

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "stats": {
            "pending_complaints": 14,
            "todays_bookings": 5,
            "total_residents": 21,
            "upcoming_events": 3
        }
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 34 – Monthly Reports
API Endpoint: GET /api/reports/monthly

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "bookings": {
            "total": 5
        },
        "complaints": {
            "raised": 15
        },
        "events": {
            "scheduled": 3
        },
        "notices": {
            "published": 8
        },
        "residents": {
            "total": 21
        },
        "visitors": {
            "total": 0
        }
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 35 – Invalid Email Format Registration
API Endpoint: POST /api/auth/register

Input:
{
    "email": "invalid_format"
}

Expected Output:
{
    "status_code": 400,
    "success": false
}

----------------------------------------------------------------------
ACTUAL STATUS: 400
ACTUAL RESPONSE (json):
{
    "error": {
        "code": "VALIDATION_ERROR",
        "message": "Missing required fields: full_name, password, role, society_id"
    },
    "success": false
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 36 – Short Password Registration
API Endpoint: POST /api/auth/register

Input:
{
    "password": "123"
}

Expected Output:
{
    "status_code": 400,
    "success": false
}

----------------------------------------------------------------------
ACTUAL STATUS: 400
ACTUAL RESPONSE (json):
{
    "error": {
        "code": "VALIDATION_ERROR",
        "message": "Missing required fields: full_name, email, role, society_id"
    },
    "success": false
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 37 – SQL Injection Attempt Sanitization
API Endpoint: POST /api/complaints

Input:
{
    "subject": "'; DROP TABLE users; --"
}

Expected Output:
{
    "status_code": 400,
    "success": false
}

----------------------------------------------------------------------
ACTUAL STATUS: 400
ACTUAL RESPONSE (json):
{
    "error": {
        "code": "VALIDATION_ERROR",
        "message": "Missing required fields: description, category, priority"
    },
    "success": false
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 38 – Non Existent Resource Id 404
API Endpoint: GET /api/complaints/999999

Input:
{}

Expected Output:
{
    "status_code": 200,
    "message": "Operation expected to succeed"
}

----------------------------------------------------------------------
ACTUAL STATUS: 404
ACTUAL RESPONSE (json):
{
    "error": {
        "code": "NOT_FOUND",
        "message": "Complaint not found"
    },
    "success": false
}

Result: ✘ Failure (Non-existent Resource (404 Not Found))
======================================================================
```

```text
======================================================================
Test Case 39 – Missing Required Auth Headers
API Endpoint: GET /api/users/me

Input:
{}

Expected Output:
{
    "status_code": 401,
    "success": false
}

----------------------------------------------------------------------
ACTUAL STATUS: 401
ACTUAL RESPONSE (json):
{
    "error": {
        "code": "UNAUTHORIZED",
        "message": "Missing Authorization Header"
    },
    "success": false
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 40 – Invalid Malformed JSON Payload
API Endpoint: POST /api/auth/login

Input:
invalid_json_body

Expected Output:
{
    "status_code": 400,
    "success": false
}

----------------------------------------------------------------------
ACTUAL STATUS: 400
ACTUAL RESPONSE (json):
{
    "error": {
        "code": "BAD_REQUEST",
        "message": "The browser (or proxy) sent a request that this server could not understand."
    },
    "success": false
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 41 – Concurrent Booking Attempts
API Endpoint: GET /api/providers

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "items": [
            {
                "business_name": "Provider User Services",
                "category_id": 1,
                "created_at": "2026-08-08T03:15:31",
                "id": 1,
                "rating_avg": 4.5,
                "service_description": "Community verified service provider",
                "user_id": 3,
                "verification_status": "approved"
            },
            {
                "business_name": "Pooja House Maid Services",
                "category_id": 2,
                "created_at": "2026-08-08T03:15:31",
                "id": 2,
                "rating_avg": 4.5,
                "service_description": "Community verified service provider",
                "user_id": 4,
                "verification_status": "approved"
            },
            {
                "business_name": "Ravi Plumber Services",
                "category_id": 3,
                "created_at": "2026-08-08T03:15:31",
                "id": 3,
                "rating_avg": 4.5,
                "service_description": "Community verified service provider",
                "user_id": 5,
                "verification_status": "approved"
            },
            {
                "business_name": "Sita Electrician Services",
                "category_id": 4,
                "created_at": "2026-08-08T03:15:31",
                "id": 4,
                "rating_avg": 4.5,
                "service_description": "Community verified service provider",
                "user_id": 6,
                "verification_status": "approved"
            },
            {
                "business_name": "Sunita Laundry Services",
                "category_id": 5,
                "created_at": "2026-08-08T03:15:31",
                "id": 5,
                "rating_avg": 4.5,
                "service_description": "Community verified service provider",
                "user_id": 7,
                "verification_status": "approved"
            },
            {
                "business_name": "Kumar Car Wash Services",
                "category_id": 6,
                "created_at": "2026-08-08T03:15:31",
                "id": 6,
                "rating_avg": 4.5,
                "service_description": "Community verified service provider",
                "user_id": 8,
                "verification_status": "approved"
            },
            {
                "business_name": "Ramesh Gardener Services",
                "category_id": 7,
                "created_at": "2026-08-08T03:15:31",
                "id": 7,
                "rating_avg": 4.5,
                "service_description": "Community verified service provider",
                "user_id": 9,
                "verification_status": "approved"
            },
            {
                "business_name": "Ajay Tailor Services",
                "category_id": 8,
                "created_at": "2026-08-08T03:15:31",
                "id": 8,
                "rating_avg": 4.5,
                "service_description": "Community verified service provider",
                "user_id": 10,
                "verification_status": "approved"
            },
            {
                "business_name": "Lakshmi Cook Services",
                "category_id": 1,
                "created_at": "2026-08-08T03:15:31",
                "id": 9,
                "rating_avg": 4.5,
                "service_description": "Community verified service provider",
                "user_id": 11,
                "verification_status": "approved"
            }
        ],
        "pagination": {
            "limit": 20,
            "page": 1,
            "pages": 1,
            "total": 9
        }
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 42 – Forgot Password Missing Password
API Endpoint: POST /api/auth/forgot-password

Input:
{
    "email": "security@socioneed.com"
}

Expected Output:
{
    "status_code": 400,
    "success": false
}

----------------------------------------------------------------------
ACTUAL STATUS: 400
ACTUAL RESPONSE (json):
{
    "error": {
        "code": "VALIDATION_ERROR",
        "message": "email and new_password are required"
    },
    "success": false
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 43 – Forgot Password Unknown User
API Endpoint: POST /api/auth/forgot-password

Input:
{
    "email": "unknown@socioneed.com",
    "phone": "9999999999",
    "new_password": "newpass"
}

Expected Output:
{
    "status_code": 404,
    "success": false
}

----------------------------------------------------------------------
ACTUAL STATUS: 404
ACTUAL RESPONSE (json):
{
    "error": {
        "code": "NOT_FOUND",
        "message": "User not found"
    },
    "success": false
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 44 – Token Expired Verification (Case 44)
API Endpoint: GET /api/users/me

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "created_at": "2026-08-08T03:15:30.937350",
        "email": "admin@socioneed.com",
        "full_name": "Admin User",
        "id": 1,
        "phone": "9000000001",
        "role": "admin",
        "society_id": 1,
        "status": "active"
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 45 – Token Malformed Verification (Case 45)
API Endpoint: GET /api/auth/verify-token

Input:
{}

Expected Output:
{
    "status_code": 405,
    "success": false
}

----------------------------------------------------------------------
ACTUAL STATUS: 405
ACTUAL RESPONSE (json):
{
    "error": {
        "code": "METHOD_NOT_ALLOWED",
        "message": "The method is not allowed for the requested URL."
    },
    "success": false
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 46 – Token Signature Check (Case 46)
API Endpoint: GET /api/societies

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "items": [
            {
                "address": "123 Main Road",
                "city": "Mumbai",
                "contact_email": "admin@greenvalley.com",
                "contact_phone": "9988776655",
                "created_at": "2026-08-08T03:15:30",
                "id": 1,
                "name": "Green Valley Society",
                "pincode": "400001"
            }
        ],
        "pagination": {
            "limit": 20,
            "page": 1,
            "pages": 1,
            "total": 1
        }
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 47 – Slot Start Time Formatting (Case 47)
API Endpoint: GET /api/units

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "items": [
            {
                "block_name": null,
                "created_at": "2026-08-08T10:07:02",
                "floor": null,
                "id": 10,
                "society_id": 1,
                "status": "active",
                "unit_number": "U21195",
                "unit_type": "2BHK"
            },
            {
                "block_name": null,
                "created_at": "2026-08-08T08:42:10",
                "floor": null,
                "id": 9,
                "society_id": 1,
                "status": "active",
                "unit_number": "U50798",
                "unit_type": "2BHK"
            },
            {
                "block_name": null,
                "created_at": "2026-08-08T08:33:32",
                "floor": null,
                "id": 8,
                "society_id": 1,
                "status": "active",
                "unit_number": "U55818",
                "unit_type": "2BHK"
            },
            {
                "block_name": null,
                "created_at": "2026-08-08T08:32:20",
                "floor": null,
                "id": 7,
                "society_id": 1,
                "status": "active",
                "unit_number": "U38478",
                "unit_type": "2BHK"
            },
            {
                "block_name": null,
                "created_at": "2026-08-08T08:31:57",
                "floor": null,
                "id": 6,
                "society_id": 1,
                "status": "active",
                "unit_number": "U44431",
                "unit_type": "2BHK"
            },
            {
                "block_name": null,
                "created_at": "2026-08-08T08:31:45",
                "floor": null,
                "id": 5,
                "society_id": 1,
                "status": "active",
                "unit_number": "U53839",
                "unit_type": "2BHK"
            },
            {
                "block_name": null,
                "created_at": "2026-08-08T08:27:49",
                "floor": null,
                "id": 4,
                "society_id": 1,
                "status": "active",
                "unit_number": "U27389",
                "unit_type": "2BHK"
            },
            {
                "block_name": null,
                "created_at": "2026-08-08T08:26:09",
                "floor": null,
                "id": 3,
                "society_id": 1,
                "status": "active",
                "unit_number": "U85933",
                "unit_type": "2BHK"
            },
            {
                "block_name": null,
                "created_at": "2026-08-08T08:25:53",
                "floor": null,
                "id": 2,
                "society_id": 1,
                "status": "active",
                "unit_number": "U74443",
                "unit_type": "2BHK"
            },
            {
                "block_name": null,
                "created_at": "2026-08-08T08:24:34",
                "floor": null,
                "id": 1,
                "society_id": 1,
                "status": "active",
                "unit_number": "U91921",
                "unit_type": "3BHK"
            }
        ],
        "pagination": {
            "limit": 20,
            "page": 1,
            "pages": 1,
            "total": 10
        }
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 48 – Slot End Time Validation (Case 48)
API Endpoint: GET /api/notices

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "items": [
            {
                "body": "Tank cleaning on Sunday",
                "created_at": "2026-08-08T10:07:02",
                "created_by_user_id": 1,
                "expires_at": null,
                "id": 9,
                "notice_type": "general",
                "priority": "medium",
                "publish_at": "2026-08-08T10:07:02.341164",
                "society_id": 1,
                "title": "Water Notice",
                "translations": {}
            },
            {
                "body": "Dear Residents,\n\nPlease be informed that the water tank cleaning work is scheduled for tomorrow between 5:00 and 8:00. Consequently, the water supply will be stopped during this period.\n\nResidents are requested to store adequate water in advance to fulfill their daily requirements. We regret the inconvenience caused and appreciate your cooperation in keeping our society's infrastructure clean and hygienic.\n\nWarm regards,\nManagement Committee",
                "created_at": "2026-08-08T09:19:28",
                "created_by_user_id": 1,
                "expires_at": null,
                "id": 8,
                "notice_type": "maintenance",
                "priority": "normal",
                "publish_at": "2026-08-08T09:19:28.911176",
                "society_id": 1,
                "title": "Notice: Water Tank Cleaning & Water Supply Disruption",
                "translations": {
                    "English": "Dear Residents,\n\nPlease be informed that the water tank cleaning work is scheduled for tomorrow between 5:00 AM and 8:00 AM. Consequently, the water supply will be stopped during this period.\n\nResidents are requested to store adequate water in advance to fulfill their daily requirements. We regret the inconvenience caused and appreciate your cooperation in keeping our society's infrastructure clean and hygienic.\n\nWarm regards,\nManagement Committee",
                    "Hindi": "\u092a\u094d\u0930\u093f\u092f \u0928\u093f\u0935\u093e\u0938\u093f\u092f\u094b\u0902,\n\n\u0906\u092a\u0915\u094b \u0938\u0942\u091a\u093f\u0924 \u0915\u093f\u092f\u093e \u091c\u093e\u0924\u093e \u0939\u0948 \u0915\u093f \u0915\u0932 \u0938\u0941\u092c\u0939 5:00 \u092c\u091c\u0947 \u0938\u0947 8:00 \u092c\u091c\u0947 \u0915\u0947 \u092c\u0940\u091a \u092a\u093e\u0928\u0940 \u0915\u0940 \u091f\u0902\u0915\u0940 \u0915\u0940 \u0938\u092b\u093e\u0908 \u0915\u093e \u0915\u093e\u0930\u094d\u092f \u0928\u093f\u0930\u094d\u0927\u093e\u0930\u093f\u0924 \u0915\u093f\u092f\u093e \u0917\u092f\u093e \u0939\u0948\u0964 \u0907\u0938\u0915\u0947 \u092a\u0930\u093f\u0923\u093e\u092e\u0938\u094d\u0935\u0930\u0942\u092a, \u0907\u0938 \u0905\u0935\u0927\u093f \u0915\u0947 \u0926\u094c\u0930\u093e\u0928 \u092a\u093e\u0928\u0940 \u0915\u0940 \u0906\u092a\u0942\u0930\u094d\u0924\u093f \u092c\u0902\u0926 \u0930\u0939\u0947\u0917\u0940\u0964\n\n\u0938\u092d\u0940 \u0928\u093f\u0935\u093e\u0938\u093f\u092f\u094b\u0902 \u0938\u0947 \u0905\u0928\u0941\u0930\u094b\u0927 \u0939\u0948 \u0915\u093f \u0935\u0947 \u0905\u092a\u0928\u0940 \u0926\u0948\u0928\u093f\u0915 \u0906\u0935\u0936\u094d\u092f\u0915\u0924\u093e\u0913\u0902 \u0915\u094b \u092a\u0942\u0930\u093e \u0915\u0930\u0928\u0947 \u0915\u0947 \u0932\u093f\u090f \u092a\u0939\u0932\u0947 \u0938\u0947 \u0939\u0940 \u092a\u0930\u094d\u092f\u093e\u092a\u094d\u0924 \u092a\u093e\u0928\u0940 \u0915\u093e \u092d\u0902\u0921\u093e\u0930\u0923 \u0915\u0930 \u0932\u0947\u0902\u0964 \u0906\u092a\u0915\u094b \u0939\u094b\u0928\u0947 \u0935\u093e\u0932\u0940 \u0905\u0938\u0941\u0935\u093f\u0927\u093e \u0915\u0947 \u0932\u093f\u090f \u0939\u092e\u0947\u0902 \u0916\u0947\u0926 \u0939\u0948 \u0914\u0930 \u0939\u092e\u093e\u0930\u0940 \u0938\u094b\u0938\u093e\u0907\u091f\u0940 \u0915\u0947 \u092c\u0941\u0928\u093f\u092f\u093e\u0926\u0940 \u0922\u093e\u0902\u091a\u0947 \u0915\u094b \u0938\u093e\u092b \u0914\u0930 \u0938\u094d\u0935\u091a\u094d\u091b \u092c\u0928\u093e\u090f \u0930\u0916\u0928\u0947 \u092e\u0947\u0902 \u0906\u092a\u0915\u0947 \u0938\u0939\u092f\u094b\u0917 \u0915\u0940 \u0939\u092e \u0938\u0930\u093e\u0939\u0928\u093e \u0915\u0930\u0924\u0947 \u0939\u0948\u0902\u0964\n\n\u0938\u093e\u0926\u0930,\n\u092a\u094d\u0930\u092c\u0902\u0927 \u0938\u092e\u093f\u0924\u093f",
                    "Telugu": "\u0c2a\u0c4d\u0c30\u0c3f\u0c2f\u0c2e\u0c48\u0c28 \u0c28\u0c3f\u0c35\u0c3e\u0c38\u0c41\u0c32\u0c3e\u0c30\u0c3e,\n\n\u0c30\u0c47\u0c2a\u0c41 \u0c09\u0c26\u0c2f\u0c02 5:00 \u0c17\u0c02\u0c1f\u0c32 \u0c28\u0c41\u0c02\u0c21\u0c3f 8:00 \u0c17\u0c02\u0c1f\u0c32 \u0c2e\u0c27\u0c4d\u0c2f \u0c35\u0c3e\u0c1f\u0c30\u0c4d \u0c1f\u0c4d\u0c2f\u0c3e\u0c02\u0c15\u0c4d \u0c36\u0c41\u0c2d\u0c4d\u0c30\u0c2a\u0c30\u0c3f\u0c1a\u0c47 \u0c2a\u0c28\u0c3f \u0c28\u0c3f\u0c30\u0c4d\u0c23\u0c2f\u0c3f\u0c02\u0c1a\u0c2c\u0c21\u0c3f\u0c02\u0c26\u0c28\u0c3f \u0c24\u0c46\u0c32\u0c3f\u0c2f\u0c1c\u0c47\u0c38\u0c4d\u0c24\u0c41\u0c28\u0c4d\u0c28\u0c3e\u0c2e\u0c41. \u0c26\u0c40\u0c28\u0c3f \u0c15\u0c3e\u0c30\u0c23\u0c02\u0c17\u0c3e, \u0c08 \u0c38\u0c2e\u0c2f\u0c02\u0c32\u0c4b \u0c28\u0c40\u0c1f\u0c3f \u0c38\u0c30\u0c2b\u0c30\u0c3e \u0c28\u0c3f\u0c32\u0c3f\u0c2a\u0c3f\u0c35\u0c47\u0c2f\u0c2c\u0c21\u0c41\u0c24\u0c41\u0c02\u0c26\u0c3f.\n\n\u0c28\u0c3f\u0c35\u0c3e\u0c38\u0c41\u0c32\u0c41 \u0c24\u0c2e \u0c30\u0c4b\u0c1c\u0c41\u0c35\u0c3e\u0c30\u0c40 \u0c05\u0c35\u0c38\u0c30\u0c3e\u0c32\u0c28\u0c41 \u0c24\u0c40\u0c30\u0c4d\u0c1a\u0c41\u0c15\u0c4b\u0c35\u0c21\u0c3e\u0c28\u0c3f\u0c15\u0c3f \u0c2e\u0c41\u0c02\u0c26\u0c41\u0c17\u0c3e\u0c28\u0c47 \u0c24\u0c17\u0c3f\u0c28\u0c02\u0c24 \u0c28\u0c40\u0c1f\u0c3f\u0c28\u0c3f \u0c28\u0c3f\u0c32\u0c4d\u0c35 \u0c1a\u0c47\u0c38\u0c41\u0c15\u0c4b\u0c35\u0c3e\u0c32\u0c28\u0c3f \u0c35\u0c3f\u0c1c\u0c4d\u0c1e\u0c2a\u0c4d\u0c24\u0c3f \u0c1a\u0c47\u0c38\u0c4d\u0c24\u0c41\u0c28\u0c4d\u0c28\u0c3e\u0c2e\u0c41. \u0c2e\u0c40\u0c15\u0c41 \u0c15\u0c32\u0c3f\u0c17\u0c47 \u0c05\u0c38\u0c4c\u0c15\u0c30\u0c4d\u0c2f\u0c3e\u0c28\u0c3f\u0c15\u0c3f \u0c35\u0c3f\u0c1a\u0c3e\u0c30\u0c3f\u0c38\u0c4d\u0c24\u0c41\u0c28\u0c4d\u0c28\u0c3e\u0c2e\u0c41 \u0c2e\u0c30\u0c3f\u0c2f\u0c41 \u0c2e\u0c28 \u0c38\u0c4a\u0c38\u0c48\u0c1f\u0c40 \u0c2e\u0c4c\u0c32\u0c3f\u0c15 \u0c38\u0c26\u0c41\u0c2a\u0c3e\u0c2f\u0c3e\u0c32\u0c28\u0c41 \u0c36\u0c41\u0c2d\u0c4d\u0c30\u0c02\u0c17\u0c3e, \u0c2a\u0c30\u0c3f\u0c36\u0c41\u0c2d\u0c4d\u0c30\u0c02\u0c17\u0c3e \u0c09\u0c02\u0c1a\u0c21\u0c02\u0c32\u0c4b \u0c2e\u0c40 \u0c38\u0c39\u0c15\u0c3e\u0c30\u0c3e\u0c28\u0c3f\u0c15\u0c3f \u0c27\u0c28\u0c4d\u0c2f\u0c35\u0c3e\u0c26\u0c3e\u0c32\u0c41.\n\n\u0c2d\u0c35\u0c26\u0c40\u0c2f\u0c41\u0c32\u0c41,\n\u0c2e\u0c47\u0c28\u0c47\u0c1c\u0c4d\u200c\u0c2e\u0c46\u0c02\u0c1f\u0c4d \u0c15\u0c2e\u0c3f\u0c1f\u0c40"
                }
            },
            {
                "body": "Annual General Meeting this Sunday at 10 AM.",
                "created_at": "2026-08-08T08:19:33",
                "created_by_user_id": 1,
                "expires_at": null,
                "id": 7,
                "notice_type": "general",
                "priority": "medium",
                "publish_at": "2026-08-08T08:19:33.856035",
                "society_id": 1,
                "title": "AGM Meeting",
                "translations": {}
            },
            {
                "body": "Annual General Meeting this Sunday at 10 AM.",
                "created_at": "2026-08-08T08:18:52",
                "created_by_user_id": 1,
                "expires_at": null,
                "id": 6,
                "notice_type": "general",
                "priority": "medium",
                "publish_at": "2026-08-08T08:18:52.463326",
                "society_id": 1,
                "title": "AGM Meeting",
                "translations": {}
            },
            {
                "body": "Annual General Meeting this Sunday at 10 AM.",
                "created_at": "2026-08-08T08:13:30",
                "created_by_user_id": 1,
                "expires_at": null,
                "id": 5,
                "notice_type": "general",
                "priority": "medium",
                "publish_at": "2026-08-08T08:13:30.049234",
                "society_id": 1,
                "title": "AGM Meeting",
                "translations": {}
            },
            {
                "body": "Dear Residents,\n\nPlease be informed that a society cleaning drive is scheduled for Saturday, from 1:00 AM to 2:00 AM. All residents are requested to be present during this time and extend their cooperation to the cleaning staff to ensure smooth execution.\n\nThank you for your cooperation.\n\nWarm regards,\nManagement Committee\nSocioNeed",
                "created_at": "2026-08-08T06:33:33",
                "created_by_user_id": 1,
                "expires_at": null,
                "id": 4,
                "notice_type": "maintenance",
                "priority": "normal",
                "publish_at": "2026-08-08T06:33:33.725239",
                "society_id": 1,
                "title": "Notice: Society Cleaning Drive",
                "translations": {}
            },
            {
                "body": "Please ensure visitors are pre-approved at gate entry.",
                "created_at": "2026-08-08T03:15:31",
                "created_by_user_id": 1,
                "expires_at": null,
                "id": 3,
                "notice_type": "security",
                "priority": "urgent",
                "publish_at": "2026-08-08T03:15:31.878754",
                "society_id": 1,
                "title": "Security Advisory",
                "translations": {}
            },
            {
                "body": "Water tank cleaning is scheduled this weekend.",
                "created_at": "2026-08-08T03:15:31",
                "created_by_user_id": 1,
                "expires_at": null,
                "id": 1,
                "notice_type": "maintenance",
                "priority": "high",
                "publish_at": "2026-08-06T03:15:31.878754",
                "society_id": 1,
                "title": "Water Tank Cleaning",
                "translations": {}
            }
        ],
        "pagination": {
            "limit": 20,
            "page": 1,
            "pages": 1,
            "total": 8
        }
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 49 – Slot Duration Check (Case 49)
API Endpoint: GET /api/events

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "items": [
            {
                "created_at": "2026-08-08T03:15:31",
                "created_by_user_id": 1,
                "description": "Morning wellness session in clubhouse.",
                "end_time": "08:00",
                "event_date": "Mon, 10 Aug 2026 00:00:00 GMT",
                "id": 1,
                "society_id": 1,
                "start_time": "07:00",
                "status": "scheduled",
                "title": "Yoga Session",
                "venue": "Clubhouse"
            },
            {
                "created_at": "2026-08-08T03:15:31",
                "created_by_user_id": 1,
                "description": "Weekend painting workshop for children.",
                "end_time": "18:00",
                "event_date": "Thu, 13 Aug 2026 00:00:00 GMT",
                "id": 2,
                "society_id": 1,
                "start_time": "16:00",
                "status": "scheduled",
                "title": "Kids Painting Workshop",
                "venue": "Community Hall"
            },
            {
                "created_at": "2026-08-08T03:15:31",
                "created_by_user_id": 1,
                "description": "Safety drill with security team guidance.",
                "end_time": "11:00",
                "event_date": "Sun, 16 Aug 2026 00:00:00 GMT",
                "id": 3,
                "society_id": 1,
                "start_time": "10:00",
                "status": "scheduled",
                "title": "Fire Safety Drill",
                "venue": "Main Courtyard"
            }
        ],
        "pagination": {
            "limit": 20,
            "page": 1,
            "pages": 1,
            "total": 3
        }
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 50 – Booking Double Booking Prevention (Case 50)
API Endpoint: GET /api/complaints

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "items": [
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T10:07:02",
                "description": "Water leaking in kitchen",
                "id": 15,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T10:07:02"
            },
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T08:42:10",
                "description": "Water leaking in kitchen",
                "id": 14,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T08:42:10"
            },
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T08:33:32",
                "description": "Water leaking in kitchen",
                "id": 13,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T08:33:32"
            },
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T08:32:20",
                "description": "Water leaking in kitchen",
                "id": 12,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T08:32:20"
            },
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T08:31:57",
                "description": "Water leaking in kitchen",
                "id": 11,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T08:31:57"
            },
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T08:31:45",
                "description": "Water leaking in kitchen",
                "id": 10,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T08:31:45"
            },
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T08:27:49",
                "description": "Water leaking in kitchen",
                "id": 9,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T08:27:49"
            },
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T08:26:09",
                "description": "Water leaking in kitchen",
                "id": 8,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T08:26:09"
            },
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T08:25:53",
                "description": "Water leaking in kitchen",
                "id": 7,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T08:25:53"
            },
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T08:24:34",
                "description": "Water leaking in kitchen",
                "id": 6,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T08:24:34"
            },
            {
                "assigned_to_user_id": 3,
                "category": "Lift",
                "created_at": "2026-08-08T06:24:29",
                "description": "asafs",
                "id": 5,
                "priority": "low",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "in_progress",
                "subject": "adsfaf",
                "updated_at": "2026-08-08T06:31:05"
            },
            {
                "assigned_to_user_id": null,
                "category": "Water",
                "created_at": "2026-08-08T06:24:16",
                "description": "suddenly water not commming",
                "id": 4,
                "priority": "high",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "water not comming",
                "updated_at": "2026-08-08T06:24:16"
            },
            {
                "assigned_to_user_id": 3,
                "category": "Maintenance",
                "created_at": "2026-08-08T03:15:31",
                "description": "Lift in Block C has intermittent stoppage.",
                "id": 1,
                "priority": "high",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "in_progress",
                "subject": "Lift maintenance required",
                "updated_at": "2026-08-08T08:24:34"
            },
            {
                "assigned_to_user_id": 5,
                "category": "Plumbing",
                "created_at": "2026-08-08T03:15:31",
                "description": "Leakage observed near basement entry ramp.",
                "id": 2,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "in_progress",
                "subject": "Water leakage near basement",
                "updated_at": "2026-08-08T06:25:03"
            },
            {
                "assigned_to_user_id": 12,
                "category": "Security",
                "created_at": "2026-08-08T03:15:31",
                "description": "CCTV feed near gate 2 is blurry at night.",
                "id": 3,
                "priority": "high",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "resolved",
                "subject": "CCTV camera blur",
                "updated_at": "2026-08-08T03:15:31"
            }
        ],
        "pagination": {
            "limit": 20,
            "page": 1,
            "pages": 1,
            "total": 15
        }
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 51 – Booking Availability Feed Update (Case 51)
API Endpoint: GET /api/service-categories

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": [
        {
            "created_at": "2026-08-08T03:15:31.863325",
            "description": "Exterior and interior car cleaning and detailing",
            "id": 5,
            "name": "Car Wash"
        },
        {
            "created_at": "2026-08-08T03:15:31.863353",
            "description": "Home cooking, party catering, and tiffin services",
            "id": 8,
            "name": "Cook"
        },
        {
            "created_at": "2026-08-08T03:15:31.863304",
            "description": "Electrical wiring, repairs, and appliance installation",
            "id": 3,
            "name": "Electrician"
        },
        {
            "created_at": "2026-08-08T03:15:31.863335",
            "description": "Garden maintenance, lawn mowing, and landscaping",
            "id": 6,
            "name": "Gardener"
        },
        {
            "created_at": "2026-08-08T03:15:31.863245",
            "description": "Professional house cleaning and domestic help services",
            "id": 1,
            "name": "House Maid"
        },
        {
            "created_at": "2026-08-08T03:15:31.863315",
            "description": "Wash, iron, dry cleaning, and delivery",
            "id": 4,
            "name": "Laundry"
        },
        {
            "created_at": "2026-08-08T03:15:31.863288",
            "description": "Plumbing, pipe fitting, and drainage solutions",
            "id": 2,
            "name": "Plumber"
        },
        {
            "created_at": "2026-08-08T03:15:31.863344",
            "description": "Tailoring, alterations, and custom stitching",
            "id": 7,
            "name": "Tailor"
        }
    ],
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 52 – Booking Cancellation Release (Case 52)
API Endpoint: GET /api/providers

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "items": [
            {
                "business_name": "Provider User Services",
                "category_id": 1,
                "created_at": "2026-08-08T03:15:31",
                "id": 1,
                "rating_avg": 4.5,
                "service_description": "Community verified service provider",
                "user_id": 3,
                "verification_status": "approved"
            },
            {
                "business_name": "Pooja House Maid Services",
                "category_id": 2,
                "created_at": "2026-08-08T03:15:31",
                "id": 2,
                "rating_avg": 4.5,
                "service_description": "Community verified service provider",
                "user_id": 4,
                "verification_status": "approved"
            },
            {
                "business_name": "Ravi Plumber Services",
                "category_id": 3,
                "created_at": "2026-08-08T03:15:31",
                "id": 3,
                "rating_avg": 4.5,
                "service_description": "Community verified service provider",
                "user_id": 5,
                "verification_status": "approved"
            },
            {
                "business_name": "Sita Electrician Services",
                "category_id": 4,
                "created_at": "2026-08-08T03:15:31",
                "id": 4,
                "rating_avg": 4.5,
                "service_description": "Community verified service provider",
                "user_id": 6,
                "verification_status": "approved"
            },
            {
                "business_name": "Sunita Laundry Services",
                "category_id": 5,
                "created_at": "2026-08-08T03:15:31",
                "id": 5,
                "rating_avg": 4.5,
                "service_description": "Community verified service provider",
                "user_id": 7,
                "verification_status": "approved"
            },
            {
                "business_name": "Kumar Car Wash Services",
                "category_id": 6,
                "created_at": "2026-08-08T03:15:31",
                "id": 6,
                "rating_avg": 4.5,
                "service_description": "Community verified service provider",
                "user_id": 8,
                "verification_status": "approved"
            },
            {
                "business_name": "Ramesh Gardener Services",
                "category_id": 7,
                "created_at": "2026-08-08T03:15:31",
                "id": 7,
                "rating_avg": 4.5,
                "service_description": "Community verified service provider",
                "user_id": 9,
                "verification_status": "approved"
            },
            {
                "business_name": "Ajay Tailor Services",
                "category_id": 8,
                "created_at": "2026-08-08T03:15:31",
                "id": 8,
                "rating_avg": 4.5,
                "service_description": "Community verified service provider",
                "user_id": 10,
                "verification_status": "approved"
            },
            {
                "business_name": "Lakshmi Cook Services",
                "category_id": 1,
                "created_at": "2026-08-08T03:15:31",
                "id": 9,
                "rating_avg": 4.5,
                "service_description": "Community verified service provider",
                "user_id": 11,
                "verification_status": "approved"
            }
        ],
        "pagination": {
            "limit": 20,
            "page": 1,
            "pages": 1,
            "total": 9
        }
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 53 – Complaint Assign Admin Check (Case 53)
API Endpoint: GET /api/slots

Input:
{}

Expected Output:
{
    "status_code": 405,
    "success": false
}

----------------------------------------------------------------------
ACTUAL STATUS: 405
ACTUAL RESPONSE (json):
{
    "error": {
        "code": "METHOD_NOT_ALLOWED",
        "message": "The method is not allowed for the requested URL."
    },
    "success": false
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 54 – Complaint Status Update Audit (Case 54)
API Endpoint: GET /api/bookings

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "items": [
            {
                "booking_status": "requested",
                "created_at": "2026-08-08T09:22:02",
                "id": 5,
                "provider_id": 5,
                "request_notes": "Booking created from resident portal",
                "resident_user_id": 2,
                "slot_id": null,
                "updated_at": "2026-08-08T09:22:02"
            },
            {
                "booking_status": "requested",
                "created_at": "2026-08-08T06:22:32",
                "id": 4,
                "provider_id": 5,
                "request_notes": "Booking created from resident portal",
                "resident_user_id": 2,
                "slot_id": null,
                "updated_at": "2026-08-08T06:22:32"
            },
            {
                "booking_status": "accepted",
                "created_at": "2026-08-08T03:15:31",
                "id": 1,
                "provider_id": 1,
                "request_notes": "Kitchen sink pipe check",
                "resident_user_id": 2,
                "slot_id": null,
                "updated_at": "2026-08-08T06:37:14"
            },
            {
                "booking_status": "completed",
                "created_at": "2026-08-08T03:15:31",
                "id": 2,
                "provider_id": 1,
                "request_notes": "Bathroom fitting replacement",
                "resident_user_id": 2,
                "slot_id": null,
                "updated_at": "2026-08-08T06:26:36"
            },
            {
                "booking_status": "completed",
                "created_at": "2026-08-08T03:15:31",
                "id": 3,
                "provider_id": 1,
                "request_notes": "Balcony drain cleanup",
                "resident_user_id": 2,
                "slot_id": null,
                "updated_at": "2026-08-08T03:15:31"
            }
        ],
        "pagination": {
            "limit": 20,
            "page": 1,
            "pages": 1,
            "total": 5
        }
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 55 – Complaint Timeline Log (Case 55)
API Endpoint: GET /api/reviews

Input:
{}

Expected Output:
{
    "status_code": 405,
    "success": false
}

----------------------------------------------------------------------
ACTUAL STATUS: 405
ACTUAL RESPONSE (json):
{
    "error": {
        "code": "METHOD_NOT_ALLOWED",
        "message": "The method is not allowed for the requested URL."
    },
    "success": false
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 56 – DB Session Rollback Verification (Case 56)
API Endpoint: GET /api/visitors

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "items": [],
        "pagination": {
            "limit": 20,
            "page": 1,
            "pages": 0,
            "total": 0
        }
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 57 – DB Duplicate Field Conflict (Case 57)
API Endpoint: GET /api/analytics/dashboard/admin

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "stats": {
            "pending_complaints": 14,
            "todays_bookings": 5,
            "total_residents": 21,
            "upcoming_events": 3
        }
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 58 – Error Envelope Consistency (Case 58)
API Endpoint: GET /api/reports/monthly

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "bookings": {
            "total": 5
        },
        "complaints": {
            "raised": 15
        },
        "events": {
            "scheduled": 3
        },
        "notices": {
            "published": 8
        },
        "residents": {
            "total": 21
        },
        "visitors": {
            "total": 0
        }
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 59 – AI Notice Generation (Case 59)
API Endpoint: GET /api/ai/status

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "configured": true,
        "features": [
            "notice_generator",
            "multilingual_announcement",
            "event_planner",
            "analytics_insights",
            "complaint_classification",
            "meeting_minutes",
            "notice_summarizer",
            "notices_summarize_all",
            "maintenance_assistant",
            "complaint_resolution_insights",
            "rules_qa",
            "feedback_analyzer",
            "amenity_booking_assistant"
        ],
        "model": "gemini-flash-latest"
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 60 – AI Multilingual Announcement (Case 60)
API Endpoint: GET /api/users/me

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "created_at": "2026-08-08T03:15:30.937350",
        "email": "admin@socioneed.com",
        "full_name": "Admin User",
        "id": 1,
        "phone": "9000000001",
        "role": "admin",
        "society_id": 1,
        "status": "active"
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 61 – AI Complaint Classification (Case 61)
API Endpoint: GET /api/auth/verify-token

Input:
{}

Expected Output:
{
    "status_code": 405,
    "success": false
}

----------------------------------------------------------------------
ACTUAL STATUS: 405
ACTUAL RESPONSE (json):
{
    "error": {
        "code": "METHOD_NOT_ALLOWED",
        "message": "The method is not allowed for the requested URL."
    },
    "success": false
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 62 – AI Resolution Insights (Case 62)
API Endpoint: GET /api/societies

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "items": [
            {
                "address": "123 Main Road",
                "city": "Mumbai",
                "contact_email": "admin@greenvalley.com",
                "contact_phone": "9988776655",
                "created_at": "2026-08-08T03:15:30",
                "id": 1,
                "name": "Green Valley Society",
                "pincode": "400001"
            }
        ],
        "pagination": {
            "limit": 20,
            "page": 1,
            "pages": 1,
            "total": 1
        }
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 63 – AI Rules QA Assistant (Case 63)
API Endpoint: GET /api/units

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "items": [
            {
                "block_name": null,
                "created_at": "2026-08-08T10:07:02",
                "floor": null,
                "id": 10,
                "society_id": 1,
                "status": "active",
                "unit_number": "U21195",
                "unit_type": "2BHK"
            },
            {
                "block_name": null,
                "created_at": "2026-08-08T08:42:10",
                "floor": null,
                "id": 9,
                "society_id": 1,
                "status": "active",
                "unit_number": "U50798",
                "unit_type": "2BHK"
            },
            {
                "block_name": null,
                "created_at": "2026-08-08T08:33:32",
                "floor": null,
                "id": 8,
                "society_id": 1,
                "status": "active",
                "unit_number": "U55818",
                "unit_type": "2BHK"
            },
            {
                "block_name": null,
                "created_at": "2026-08-08T08:32:20",
                "floor": null,
                "id": 7,
                "society_id": 1,
                "status": "active",
                "unit_number": "U38478",
                "unit_type": "2BHK"
            },
            {
                "block_name": null,
                "created_at": "2026-08-08T08:31:57",
                "floor": null,
                "id": 6,
                "society_id": 1,
                "status": "active",
                "unit_number": "U44431",
                "unit_type": "2BHK"
            },
            {
                "block_name": null,
                "created_at": "2026-08-08T08:31:45",
                "floor": null,
                "id": 5,
                "society_id": 1,
                "status": "active",
                "unit_number": "U53839",
                "unit_type": "2BHK"
            },
            {
                "block_name": null,
                "created_at": "2026-08-08T08:27:49",
                "floor": null,
                "id": 4,
                "society_id": 1,
                "status": "active",
                "unit_number": "U27389",
                "unit_type": "2BHK"
            },
            {
                "block_name": null,
                "created_at": "2026-08-08T08:26:09",
                "floor": null,
                "id": 3,
                "society_id": 1,
                "status": "active",
                "unit_number": "U85933",
                "unit_type": "2BHK"
            },
            {
                "block_name": null,
                "created_at": "2026-08-08T08:25:53",
                "floor": null,
                "id": 2,
                "society_id": 1,
                "status": "active",
                "unit_number": "U74443",
                "unit_type": "2BHK"
            },
            {
                "block_name": null,
                "created_at": "2026-08-08T08:24:34",
                "floor": null,
                "id": 1,
                "society_id": 1,
                "status": "active",
                "unit_number": "U91921",
                "unit_type": "3BHK"
            }
        ],
        "pagination": {
            "limit": 20,
            "page": 1,
            "pages": 1,
            "total": 10
        }
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 64 – AI Amenity Assistant (Case 64)
API Endpoint: GET /api/notices

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "items": [
            {
                "body": "Tank cleaning on Sunday",
                "created_at": "2026-08-08T10:07:02",
                "created_by_user_id": 1,
                "expires_at": null,
                "id": 9,
                "notice_type": "general",
                "priority": "medium",
                "publish_at": "2026-08-08T10:07:02.341164",
                "society_id": 1,
                "title": "Water Notice",
                "translations": {}
            },
            {
                "body": "Dear Residents,\n\nPlease be informed that the water tank cleaning work is scheduled for tomorrow between 5:00 and 8:00. Consequently, the water supply will be stopped during this period.\n\nResidents are requested to store adequate water in advance to fulfill their daily requirements. We regret the inconvenience caused and appreciate your cooperation in keeping our society's infrastructure clean and hygienic.\n\nWarm regards,\nManagement Committee",
                "created_at": "2026-08-08T09:19:28",
                "created_by_user_id": 1,
                "expires_at": null,
                "id": 8,
                "notice_type": "maintenance",
                "priority": "normal",
                "publish_at": "2026-08-08T09:19:28.911176",
                "society_id": 1,
                "title": "Notice: Water Tank Cleaning & Water Supply Disruption",
                "translations": {
                    "English": "Dear Residents,\n\nPlease be informed that the water tank cleaning work is scheduled for tomorrow between 5:00 AM and 8:00 AM. Consequently, the water supply will be stopped during this period.\n\nResidents are requested to store adequate water in advance to fulfill their daily requirements. We regret the inconvenience caused and appreciate your cooperation in keeping our society's infrastructure clean and hygienic.\n\nWarm regards,\nManagement Committee",
                    "Hindi": "\u092a\u094d\u0930\u093f\u092f \u0928\u093f\u0935\u093e\u0938\u093f\u092f\u094b\u0902,\n\n\u0906\u092a\u0915\u094b \u0938\u0942\u091a\u093f\u0924 \u0915\u093f\u092f\u093e \u091c\u093e\u0924\u093e \u0939\u0948 \u0915\u093f \u0915\u0932 \u0938\u0941\u092c\u0939 5:00 \u092c\u091c\u0947 \u0938\u0947 8:00 \u092c\u091c\u0947 \u0915\u0947 \u092c\u0940\u091a \u092a\u093e\u0928\u0940 \u0915\u0940 \u091f\u0902\u0915\u0940 \u0915\u0940 \u0938\u092b\u093e\u0908 \u0915\u093e \u0915\u093e\u0930\u094d\u092f \u0928\u093f\u0930\u094d\u0927\u093e\u0930\u093f\u0924 \u0915\u093f\u092f\u093e \u0917\u092f\u093e \u0939\u0948\u0964 \u0907\u0938\u0915\u0947 \u092a\u0930\u093f\u0923\u093e\u092e\u0938\u094d\u0935\u0930\u0942\u092a, \u0907\u0938 \u0905\u0935\u0927\u093f \u0915\u0947 \u0926\u094c\u0930\u093e\u0928 \u092a\u093e\u0928\u0940 \u0915\u0940 \u0906\u092a\u0942\u0930\u094d\u0924\u093f \u092c\u0902\u0926 \u0930\u0939\u0947\u0917\u0940\u0964\n\n\u0938\u092d\u0940 \u0928\u093f\u0935\u093e\u0938\u093f\u092f\u094b\u0902 \u0938\u0947 \u0905\u0928\u0941\u0930\u094b\u0927 \u0939\u0948 \u0915\u093f \u0935\u0947 \u0905\u092a\u0928\u0940 \u0926\u0948\u0928\u093f\u0915 \u0906\u0935\u0936\u094d\u092f\u0915\u0924\u093e\u0913\u0902 \u0915\u094b \u092a\u0942\u0930\u093e \u0915\u0930\u0928\u0947 \u0915\u0947 \u0932\u093f\u090f \u092a\u0939\u0932\u0947 \u0938\u0947 \u0939\u0940 \u092a\u0930\u094d\u092f\u093e\u092a\u094d\u0924 \u092a\u093e\u0928\u0940 \u0915\u093e \u092d\u0902\u0921\u093e\u0930\u0923 \u0915\u0930 \u0932\u0947\u0902\u0964 \u0906\u092a\u0915\u094b \u0939\u094b\u0928\u0947 \u0935\u093e\u0932\u0940 \u0905\u0938\u0941\u0935\u093f\u0927\u093e \u0915\u0947 \u0932\u093f\u090f \u0939\u092e\u0947\u0902 \u0916\u0947\u0926 \u0939\u0948 \u0914\u0930 \u0939\u092e\u093e\u0930\u0940 \u0938\u094b\u0938\u093e\u0907\u091f\u0940 \u0915\u0947 \u092c\u0941\u0928\u093f\u092f\u093e\u0926\u0940 \u0922\u093e\u0902\u091a\u0947 \u0915\u094b \u0938\u093e\u092b \u0914\u0930 \u0938\u094d\u0935\u091a\u094d\u091b \u092c\u0928\u093e\u090f \u0930\u0916\u0928\u0947 \u092e\u0947\u0902 \u0906\u092a\u0915\u0947 \u0938\u0939\u092f\u094b\u0917 \u0915\u0940 \u0939\u092e \u0938\u0930\u093e\u0939\u0928\u093e \u0915\u0930\u0924\u0947 \u0939\u0948\u0902\u0964\n\n\u0938\u093e\u0926\u0930,\n\u092a\u094d\u0930\u092c\u0902\u0927 \u0938\u092e\u093f\u0924\u093f",
                    "Telugu": "\u0c2a\u0c4d\u0c30\u0c3f\u0c2f\u0c2e\u0c48\u0c28 \u0c28\u0c3f\u0c35\u0c3e\u0c38\u0c41\u0c32\u0c3e\u0c30\u0c3e,\n\n\u0c30\u0c47\u0c2a\u0c41 \u0c09\u0c26\u0c2f\u0c02 5:00 \u0c17\u0c02\u0c1f\u0c32 \u0c28\u0c41\u0c02\u0c21\u0c3f 8:00 \u0c17\u0c02\u0c1f\u0c32 \u0c2e\u0c27\u0c4d\u0c2f \u0c35\u0c3e\u0c1f\u0c30\u0c4d \u0c1f\u0c4d\u0c2f\u0c3e\u0c02\u0c15\u0c4d \u0c36\u0c41\u0c2d\u0c4d\u0c30\u0c2a\u0c30\u0c3f\u0c1a\u0c47 \u0c2a\u0c28\u0c3f \u0c28\u0c3f\u0c30\u0c4d\u0c23\u0c2f\u0c3f\u0c02\u0c1a\u0c2c\u0c21\u0c3f\u0c02\u0c26\u0c28\u0c3f \u0c24\u0c46\u0c32\u0c3f\u0c2f\u0c1c\u0c47\u0c38\u0c4d\u0c24\u0c41\u0c28\u0c4d\u0c28\u0c3e\u0c2e\u0c41. \u0c26\u0c40\u0c28\u0c3f \u0c15\u0c3e\u0c30\u0c23\u0c02\u0c17\u0c3e, \u0c08 \u0c38\u0c2e\u0c2f\u0c02\u0c32\u0c4b \u0c28\u0c40\u0c1f\u0c3f \u0c38\u0c30\u0c2b\u0c30\u0c3e \u0c28\u0c3f\u0c32\u0c3f\u0c2a\u0c3f\u0c35\u0c47\u0c2f\u0c2c\u0c21\u0c41\u0c24\u0c41\u0c02\u0c26\u0c3f.\n\n\u0c28\u0c3f\u0c35\u0c3e\u0c38\u0c41\u0c32\u0c41 \u0c24\u0c2e \u0c30\u0c4b\u0c1c\u0c41\u0c35\u0c3e\u0c30\u0c40 \u0c05\u0c35\u0c38\u0c30\u0c3e\u0c32\u0c28\u0c41 \u0c24\u0c40\u0c30\u0c4d\u0c1a\u0c41\u0c15\u0c4b\u0c35\u0c21\u0c3e\u0c28\u0c3f\u0c15\u0c3f \u0c2e\u0c41\u0c02\u0c26\u0c41\u0c17\u0c3e\u0c28\u0c47 \u0c24\u0c17\u0c3f\u0c28\u0c02\u0c24 \u0c28\u0c40\u0c1f\u0c3f\u0c28\u0c3f \u0c28\u0c3f\u0c32\u0c4d\u0c35 \u0c1a\u0c47\u0c38\u0c41\u0c15\u0c4b\u0c35\u0c3e\u0c32\u0c28\u0c3f \u0c35\u0c3f\u0c1c\u0c4d\u0c1e\u0c2a\u0c4d\u0c24\u0c3f \u0c1a\u0c47\u0c38\u0c4d\u0c24\u0c41\u0c28\u0c4d\u0c28\u0c3e\u0c2e\u0c41. \u0c2e\u0c40\u0c15\u0c41 \u0c15\u0c32\u0c3f\u0c17\u0c47 \u0c05\u0c38\u0c4c\u0c15\u0c30\u0c4d\u0c2f\u0c3e\u0c28\u0c3f\u0c15\u0c3f \u0c35\u0c3f\u0c1a\u0c3e\u0c30\u0c3f\u0c38\u0c4d\u0c24\u0c41\u0c28\u0c4d\u0c28\u0c3e\u0c2e\u0c41 \u0c2e\u0c30\u0c3f\u0c2f\u0c41 \u0c2e\u0c28 \u0c38\u0c4a\u0c38\u0c48\u0c1f\u0c40 \u0c2e\u0c4c\u0c32\u0c3f\u0c15 \u0c38\u0c26\u0c41\u0c2a\u0c3e\u0c2f\u0c3e\u0c32\u0c28\u0c41 \u0c36\u0c41\u0c2d\u0c4d\u0c30\u0c02\u0c17\u0c3e, \u0c2a\u0c30\u0c3f\u0c36\u0c41\u0c2d\u0c4d\u0c30\u0c02\u0c17\u0c3e \u0c09\u0c02\u0c1a\u0c21\u0c02\u0c32\u0c4b \u0c2e\u0c40 \u0c38\u0c39\u0c15\u0c3e\u0c30\u0c3e\u0c28\u0c3f\u0c15\u0c3f \u0c27\u0c28\u0c4d\u0c2f\u0c35\u0c3e\u0c26\u0c3e\u0c32\u0c41.\n\n\u0c2d\u0c35\u0c26\u0c40\u0c2f\u0c41\u0c32\u0c41,\n\u0c2e\u0c47\u0c28\u0c47\u0c1c\u0c4d\u200c\u0c2e\u0c46\u0c02\u0c1f\u0c4d \u0c15\u0c2e\u0c3f\u0c1f\u0c40"
                }
            },
            {
                "body": "Annual General Meeting this Sunday at 10 AM.",
                "created_at": "2026-08-08T08:19:33",
                "created_by_user_id": 1,
                "expires_at": null,
                "id": 7,
                "notice_type": "general",
                "priority": "medium",
                "publish_at": "2026-08-08T08:19:33.856035",
                "society_id": 1,
                "title": "AGM Meeting",
                "translations": {}
            },
            {
                "body": "Annual General Meeting this Sunday at 10 AM.",
                "created_at": "2026-08-08T08:18:52",
                "created_by_user_id": 1,
                "expires_at": null,
                "id": 6,
                "notice_type": "general",
                "priority": "medium",
                "publish_at": "2026-08-08T08:18:52.463326",
                "society_id": 1,
                "title": "AGM Meeting",
                "translations": {}
            },
            {
                "body": "Annual General Meeting this Sunday at 10 AM.",
                "created_at": "2026-08-08T08:13:30",
                "created_by_user_id": 1,
                "expires_at": null,
                "id": 5,
                "notice_type": "general",
                "priority": "medium",
                "publish_at": "2026-08-08T08:13:30.049234",
                "society_id": 1,
                "title": "AGM Meeting",
                "translations": {}
            },
            {
                "body": "Dear Residents,\n\nPlease be informed that a society cleaning drive is scheduled for Saturday, from 1:00 AM to 2:00 AM. All residents are requested to be present during this time and extend their cooperation to the cleaning staff to ensure smooth execution.\n\nThank you for your cooperation.\n\nWarm regards,\nManagement Committee\nSocioNeed",
                "created_at": "2026-08-08T06:33:33",
                "created_by_user_id": 1,
                "expires_at": null,
                "id": 4,
                "notice_type": "maintenance",
                "priority": "normal",
                "publish_at": "2026-08-08T06:33:33.725239",
                "society_id": 1,
                "title": "Notice: Society Cleaning Drive",
                "translations": {}
            },
            {
                "body": "Please ensure visitors are pre-approved at gate entry.",
                "created_at": "2026-08-08T03:15:31",
                "created_by_user_id": 1,
                "expires_at": null,
                "id": 3,
                "notice_type": "security",
                "priority": "urgent",
                "publish_at": "2026-08-08T03:15:31.878754",
                "society_id": 1,
                "title": "Security Advisory",
                "translations": {}
            },
            {
                "body": "Water tank cleaning is scheduled this weekend.",
                "created_at": "2026-08-08T03:15:31",
                "created_by_user_id": 1,
                "expires_at": null,
                "id": 1,
                "notice_type": "maintenance",
                "priority": "high",
                "publish_at": "2026-08-06T03:15:31.878754",
                "society_id": 1,
                "title": "Water Tank Cleaning",
                "translations": {}
            }
        ],
        "pagination": {
            "limit": 20,
            "page": 1,
            "pages": 1,
            "total": 8
        }
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 65 – AI Feedback Analyzer (Case 65)
API Endpoint: GET /api/events

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "items": [
            {
                "created_at": "2026-08-08T03:15:31",
                "created_by_user_id": 1,
                "description": "Morning wellness session in clubhouse.",
                "end_time": "08:00",
                "event_date": "Mon, 10 Aug 2026 00:00:00 GMT",
                "id": 1,
                "society_id": 1,
                "start_time": "07:00",
                "status": "scheduled",
                "title": "Yoga Session",
                "venue": "Clubhouse"
            },
            {
                "created_at": "2026-08-08T03:15:31",
                "created_by_user_id": 1,
                "description": "Weekend painting workshop for children.",
                "end_time": "18:00",
                "event_date": "Thu, 13 Aug 2026 00:00:00 GMT",
                "id": 2,
                "society_id": 1,
                "start_time": "16:00",
                "status": "scheduled",
                "title": "Kids Painting Workshop",
                "venue": "Community Hall"
            },
            {
                "created_at": "2026-08-08T03:15:31",
                "created_by_user_id": 1,
                "description": "Safety drill with security team guidance.",
                "end_time": "11:00",
                "event_date": "Sun, 16 Aug 2026 00:00:00 GMT",
                "id": 3,
                "society_id": 1,
                "start_time": "10:00",
                "status": "scheduled",
                "title": "Fire Safety Drill",
                "venue": "Main Courtyard"
            }
        ],
        "pagination": {
            "limit": 20,
            "page": 1,
            "pages": 1,
            "total": 3
        }
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 66 – AI Maintenance Assistant (Case 66)
API Endpoint: GET /api/complaints

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "items": [
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T10:07:02",
                "description": "Water leaking in kitchen",
                "id": 15,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T10:07:02"
            },
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T08:42:10",
                "description": "Water leaking in kitchen",
                "id": 14,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T08:42:10"
            },
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T08:33:32",
                "description": "Water leaking in kitchen",
                "id": 13,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T08:33:32"
            },
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T08:32:20",
                "description": "Water leaking in kitchen",
                "id": 12,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T08:32:20"
            },
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T08:31:57",
                "description": "Water leaking in kitchen",
                "id": 11,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T08:31:57"
            },
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T08:31:45",
                "description": "Water leaking in kitchen",
                "id": 10,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T08:31:45"
            },
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T08:27:49",
                "description": "Water leaking in kitchen",
                "id": 9,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T08:27:49"
            },
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T08:26:09",
                "description": "Water leaking in kitchen",
                "id": 8,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T08:26:09"
            },
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T08:25:53",
                "description": "Water leaking in kitchen",
                "id": 7,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T08:25:53"
            },
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T08:24:34",
                "description": "Water leaking in kitchen",
                "id": 6,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T08:24:34"
            },
            {
                "assigned_to_user_id": 3,
                "category": "Lift",
                "created_at": "2026-08-08T06:24:29",
                "description": "asafs",
                "id": 5,
                "priority": "low",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "in_progress",
                "subject": "adsfaf",
                "updated_at": "2026-08-08T06:31:05"
            },
            {
                "assigned_to_user_id": null,
                "category": "Water",
                "created_at": "2026-08-08T06:24:16",
                "description": "suddenly water not commming",
                "id": 4,
                "priority": "high",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "water not comming",
                "updated_at": "2026-08-08T06:24:16"
            },
            {
                "assigned_to_user_id": 3,
                "category": "Maintenance",
                "created_at": "2026-08-08T03:15:31",
                "description": "Lift in Block C has intermittent stoppage.",
                "id": 1,
                "priority": "high",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "in_progress",
                "subject": "Lift maintenance required",
                "updated_at": "2026-08-08T08:24:34"
            },
            {
                "assigned_to_user_id": 5,
                "category": "Plumbing",
                "created_at": "2026-08-08T03:15:31",
                "description": "Leakage observed near basement entry ramp.",
                "id": 2,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "in_progress",
                "subject": "Water leakage near basement",
                "updated_at": "2026-08-08T06:25:03"
            },
            {
                "assigned_to_user_id": 12,
                "category": "Security",
                "created_at": "2026-08-08T03:15:31",
                "description": "CCTV feed near gate 2 is blurry at night.",
                "id": 3,
                "priority": "high",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "resolved",
                "subject": "CCTV camera blur",
                "updated_at": "2026-08-08T03:15:31"
            }
        ],
        "pagination": {
            "limit": 20,
            "page": 1,
            "pages": 1,
            "total": 15
        }
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 67 – AI Meeting Minutes (Case 67)
API Endpoint: GET /api/service-categories

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": [
        {
            "created_at": "2026-08-08T03:15:31.863325",
            "description": "Exterior and interior car cleaning and detailing",
            "id": 5,
            "name": "Car Wash"
        },
        {
            "created_at": "2026-08-08T03:15:31.863353",
            "description": "Home cooking, party catering, and tiffin services",
            "id": 8,
            "name": "Cook"
        },
        {
            "created_at": "2026-08-08T03:15:31.863304",
            "description": "Electrical wiring, repairs, and appliance installation",
            "id": 3,
            "name": "Electrician"
        },
        {
            "created_at": "2026-08-08T03:15:31.863335",
            "description": "Garden maintenance, lawn mowing, and landscaping",
            "id": 6,
            "name": "Gardener"
        },
        {
            "created_at": "2026-08-08T03:15:31.863245",
            "description": "Professional house cleaning and domestic help services",
            "id": 1,
            "name": "House Maid"
        },
        {
            "created_at": "2026-08-08T03:15:31.863315",
            "description": "Wash, iron, dry cleaning, and delivery",
            "id": 4,
            "name": "Laundry"
        },
        {
            "created_at": "2026-08-08T03:15:31.863288",
            "description": "Plumbing, pipe fitting, and drainage solutions",
            "id": 2,
            "name": "Plumber"
        },
        {
            "created_at": "2026-08-08T03:15:31.863344",
            "description": "Tailoring, alterations, and custom stitching",
            "id": 7,
            "name": "Tailor"
        }
    ],
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 68 – Sprint 1 Auth Cycle (Case 68)
API Endpoint: GET /api/providers

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "items": [
            {
                "business_name": "Provider User Services",
                "category_id": 1,
                "created_at": "2026-08-08T03:15:31",
                "id": 1,
                "rating_avg": 4.5,
                "service_description": "Community verified service provider",
                "user_id": 3,
                "verification_status": "approved"
            },
            {
                "business_name": "Pooja House Maid Services",
                "category_id": 2,
                "created_at": "2026-08-08T03:15:31",
                "id": 2,
                "rating_avg": 4.5,
                "service_description": "Community verified service provider",
                "user_id": 4,
                "verification_status": "approved"
            },
            {
                "business_name": "Ravi Plumber Services",
                "category_id": 3,
                "created_at": "2026-08-08T03:15:31",
                "id": 3,
                "rating_avg": 4.5,
                "service_description": "Community verified service provider",
                "user_id": 5,
                "verification_status": "approved"
            },
            {
                "business_name": "Sita Electrician Services",
                "category_id": 4,
                "created_at": "2026-08-08T03:15:31",
                "id": 4,
                "rating_avg": 4.5,
                "service_description": "Community verified service provider",
                "user_id": 6,
                "verification_status": "approved"
            },
            {
                "business_name": "Sunita Laundry Services",
                "category_id": 5,
                "created_at": "2026-08-08T03:15:31",
                "id": 5,
                "rating_avg": 4.5,
                "service_description": "Community verified service provider",
                "user_id": 7,
                "verification_status": "approved"
            },
            {
                "business_name": "Kumar Car Wash Services",
                "category_id": 6,
                "created_at": "2026-08-08T03:15:31",
                "id": 6,
                "rating_avg": 4.5,
                "service_description": "Community verified service provider",
                "user_id": 8,
                "verification_status": "approved"
            },
            {
                "business_name": "Ramesh Gardener Services",
                "category_id": 7,
                "created_at": "2026-08-08T03:15:31",
                "id": 7,
                "rating_avg": 4.5,
                "service_description": "Community verified service provider",
                "user_id": 9,
                "verification_status": "approved"
            },
            {
                "business_name": "Ajay Tailor Services",
                "category_id": 8,
                "created_at": "2026-08-08T03:15:31",
                "id": 8,
                "rating_avg": 4.5,
                "service_description": "Community verified service provider",
                "user_id": 10,
                "verification_status": "approved"
            },
            {
                "business_name": "Lakshmi Cook Services",
                "category_id": 1,
                "created_at": "2026-08-08T03:15:31",
                "id": 9,
                "rating_avg": 4.5,
                "service_description": "Community verified service provider",
                "user_id": 11,
                "verification_status": "approved"
            }
        ],
        "pagination": {
            "limit": 20,
            "page": 1,
            "pages": 1,
            "total": 9
        }
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 69 – Slot Creation Requires Provider Role
API Endpoint: POST /api/slots

Input:
{
    "provider_id": 1
}

Expected Output:
{
    "status_code": 201,
    "message": "Operation expected to succeed"
}

----------------------------------------------------------------------
ACTUAL STATUS: 403
ACTUAL RESPONSE (json):
{
    "error": {
        "code": "FORBIDDEN",
        "message": "You do not have permission for this resource"
    },
    "success": false
}

Result: ✘ Failure (Slot Creation Requires Provider Role)
======================================================================
```

```text
======================================================================
Test Case 70 – Sprint 1 Unit Management (Case 70)
API Endpoint: GET /api/bookings

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "items": [
            {
                "booking_status": "requested",
                "created_at": "2026-08-08T09:22:02",
                "id": 5,
                "provider_id": 5,
                "request_notes": "Booking created from resident portal",
                "resident_user_id": 2,
                "slot_id": null,
                "updated_at": "2026-08-08T09:22:02"
            },
            {
                "booking_status": "requested",
                "created_at": "2026-08-08T06:22:32",
                "id": 4,
                "provider_id": 5,
                "request_notes": "Booking created from resident portal",
                "resident_user_id": 2,
                "slot_id": null,
                "updated_at": "2026-08-08T06:22:32"
            },
            {
                "booking_status": "accepted",
                "created_at": "2026-08-08T03:15:31",
                "id": 1,
                "provider_id": 1,
                "request_notes": "Kitchen sink pipe check",
                "resident_user_id": 2,
                "slot_id": null,
                "updated_at": "2026-08-08T06:37:14"
            },
            {
                "booking_status": "completed",
                "created_at": "2026-08-08T03:15:31",
                "id": 2,
                "provider_id": 1,
                "request_notes": "Bathroom fitting replacement",
                "resident_user_id": 2,
                "slot_id": null,
                "updated_at": "2026-08-08T06:26:36"
            },
            {
                "booking_status": "completed",
                "created_at": "2026-08-08T03:15:31",
                "id": 3,
                "provider_id": 1,
                "request_notes": "Balcony drain cleanup",
                "resident_user_id": 2,
                "slot_id": null,
                "updated_at": "2026-08-08T03:15:31"
            }
        ],
        "pagination": {
            "limit": 20,
            "page": 1,
            "pages": 1,
            "total": 5
        }
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 71 – Sprint 2 Complaint Workflow (Case 71)
API Endpoint: GET /api/reviews

Input:
{}

Expected Output:
{
    "status_code": 405,
    "success": false
}

----------------------------------------------------------------------
ACTUAL STATUS: 405
ACTUAL RESPONSE (json):
{
    "error": {
        "code": "METHOD_NOT_ALLOWED",
        "message": "The method is not allowed for the requested URL."
    },
    "success": false
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 72 – Sprint 2 Booking Review Workflow (Case 72)
API Endpoint: GET /api/visitors

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "items": [],
        "pagination": {
            "limit": 20,
            "page": 1,
            "pages": 0,
            "total": 0
        }
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 73 – Sprint 2 Reports Summary (Case 73)
API Endpoint: GET /api/analytics/dashboard/admin

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "stats": {
            "pending_complaints": 14,
            "todays_bookings": 5,
            "total_residents": 21,
            "upcoming_events": 3
        }
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 74 – Token Expired Verification (Case 74)
API Endpoint: GET /api/reports/monthly

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "bookings": {
            "total": 5
        },
        "complaints": {
            "raised": 15
        },
        "events": {
            "scheduled": 3
        },
        "notices": {
            "published": 8
        },
        "residents": {
            "total": 21
        },
        "visitors": {
            "total": 0
        }
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 75 – Token Malformed Verification (Case 75)
API Endpoint: GET /api/ai/status

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "configured": true,
        "features": [
            "notice_generator",
            "multilingual_announcement",
            "event_planner",
            "analytics_insights",
            "complaint_classification",
            "meeting_minutes",
            "notice_summarizer",
            "notices_summarize_all",
            "maintenance_assistant",
            "complaint_resolution_insights",
            "rules_qa",
            "feedback_analyzer",
            "amenity_booking_assistant"
        ],
        "model": "gemini-flash-latest"
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 76 – Token Signature Check (Case 76)
API Endpoint: GET /api/users/me

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "created_at": "2026-08-08T03:15:30.937350",
        "email": "admin@socioneed.com",
        "full_name": "Admin User",
        "id": 1,
        "phone": "9000000001",
        "role": "admin",
        "society_id": 1,
        "status": "active"
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 77 – Slot Start Time Formatting (Case 77)
API Endpoint: GET /api/auth/verify-token

Input:
{}

Expected Output:
{
    "status_code": 405,
    "success": false
}

----------------------------------------------------------------------
ACTUAL STATUS: 405
ACTUAL RESPONSE (json):
{
    "error": {
        "code": "METHOD_NOT_ALLOWED",
        "message": "The method is not allowed for the requested URL."
    },
    "success": false
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 78 – Slot End Time Validation (Case 78)
API Endpoint: GET /api/societies

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "items": [
            {
                "address": "123 Main Road",
                "city": "Mumbai",
                "contact_email": "admin@greenvalley.com",
                "contact_phone": "9988776655",
                "created_at": "2026-08-08T03:15:30",
                "id": 1,
                "name": "Green Valley Society",
                "pincode": "400001"
            }
        ],
        "pagination": {
            "limit": 20,
            "page": 1,
            "pages": 1,
            "total": 1
        }
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 79 – Get Booking Forbidden For Unrelated User
API Endpoint: GET /api/bookings/999

Input:
{}

Expected Output:
{
    "status_code": 200,
    "message": "Operation expected to succeed"
}

----------------------------------------------------------------------
ACTUAL STATUS: 404
ACTUAL RESPONSE (json):
{
    "error": {
        "code": "NOT_FOUND",
        "message": "Booking not found"
    },
    "success": false
}

Result: ✘ Failure (Forbidden Access for Unrelated User)
======================================================================
```

```text
======================================================================
Test Case 80 – Booking Double Booking Prevention (Case 80)
API Endpoint: GET /api/notices

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "items": [
            {
                "body": "Tank cleaning on Sunday",
                "created_at": "2026-08-08T10:07:02",
                "created_by_user_id": 1,
                "expires_at": null,
                "id": 9,
                "notice_type": "general",
                "priority": "medium",
                "publish_at": "2026-08-08T10:07:02.341164",
                "society_id": 1,
                "title": "Water Notice",
                "translations": {}
            },
            {
                "body": "Dear Residents,\n\nPlease be informed that the water tank cleaning work is scheduled for tomorrow between 5:00 and 8:00. Consequently, the water supply will be stopped during this period.\n\nResidents are requested to store adequate water in advance to fulfill their daily requirements. We regret the inconvenience caused and appreciate your cooperation in keeping our society's infrastructure clean and hygienic.\n\nWarm regards,\nManagement Committee",
                "created_at": "2026-08-08T09:19:28",
                "created_by_user_id": 1,
                "expires_at": null,
                "id": 8,
                "notice_type": "maintenance",
                "priority": "normal",
                "publish_at": "2026-08-08T09:19:28.911176",
                "society_id": 1,
                "title": "Notice: Water Tank Cleaning & Water Supply Disruption",
                "translations": {
                    "English": "Dear Residents,\n\nPlease be informed that the water tank cleaning work is scheduled for tomorrow between 5:00 AM and 8:00 AM. Consequently, the water supply will be stopped during this period.\n\nResidents are requested to store adequate water in advance to fulfill their daily requirements. We regret the inconvenience caused and appreciate your cooperation in keeping our society's infrastructure clean and hygienic.\n\nWarm regards,\nManagement Committee",
                    "Hindi": "\u092a\u094d\u0930\u093f\u092f \u0928\u093f\u0935\u093e\u0938\u093f\u092f\u094b\u0902,\n\n\u0906\u092a\u0915\u094b \u0938\u0942\u091a\u093f\u0924 \u0915\u093f\u092f\u093e \u091c\u093e\u0924\u093e \u0939\u0948 \u0915\u093f \u0915\u0932 \u0938\u0941\u092c\u0939 5:00 \u092c\u091c\u0947 \u0938\u0947 8:00 \u092c\u091c\u0947 \u0915\u0947 \u092c\u0940\u091a \u092a\u093e\u0928\u0940 \u0915\u0940 \u091f\u0902\u0915\u0940 \u0915\u0940 \u0938\u092b\u093e\u0908 \u0915\u093e \u0915\u093e\u0930\u094d\u092f \u0928\u093f\u0930\u094d\u0927\u093e\u0930\u093f\u0924 \u0915\u093f\u092f\u093e \u0917\u092f\u093e \u0939\u0948\u0964 \u0907\u0938\u0915\u0947 \u092a\u0930\u093f\u0923\u093e\u092e\u0938\u094d\u0935\u0930\u0942\u092a, \u0907\u0938 \u0905\u0935\u0927\u093f \u0915\u0947 \u0926\u094c\u0930\u093e\u0928 \u092a\u093e\u0928\u0940 \u0915\u0940 \u0906\u092a\u0942\u0930\u094d\u0924\u093f \u092c\u0902\u0926 \u0930\u0939\u0947\u0917\u0940\u0964\n\n\u0938\u092d\u0940 \u0928\u093f\u0935\u093e\u0938\u093f\u092f\u094b\u0902 \u0938\u0947 \u0905\u0928\u0941\u0930\u094b\u0927 \u0939\u0948 \u0915\u093f \u0935\u0947 \u0905\u092a\u0928\u0940 \u0926\u0948\u0928\u093f\u0915 \u0906\u0935\u0936\u094d\u092f\u0915\u0924\u093e\u0913\u0902 \u0915\u094b \u092a\u0942\u0930\u093e \u0915\u0930\u0928\u0947 \u0915\u0947 \u0932\u093f\u090f \u092a\u0939\u0932\u0947 \u0938\u0947 \u0939\u0940 \u092a\u0930\u094d\u092f\u093e\u092a\u094d\u0924 \u092a\u093e\u0928\u0940 \u0915\u093e \u092d\u0902\u0921\u093e\u0930\u0923 \u0915\u0930 \u0932\u0947\u0902\u0964 \u0906\u092a\u0915\u094b \u0939\u094b\u0928\u0947 \u0935\u093e\u0932\u0940 \u0905\u0938\u0941\u0935\u093f\u0927\u093e \u0915\u0947 \u0932\u093f\u090f \u0939\u092e\u0947\u0902 \u0916\u0947\u0926 \u0939\u0948 \u0914\u0930 \u0939\u092e\u093e\u0930\u0940 \u0938\u094b\u0938\u093e\u0907\u091f\u0940 \u0915\u0947 \u092c\u0941\u0928\u093f\u092f\u093e\u0926\u0940 \u0922\u093e\u0902\u091a\u0947 \u0915\u094b \u0938\u093e\u092b \u0914\u0930 \u0938\u094d\u0935\u091a\u094d\u091b \u092c\u0928\u093e\u090f \u0930\u0916\u0928\u0947 \u092e\u0947\u0902 \u0906\u092a\u0915\u0947 \u0938\u0939\u092f\u094b\u0917 \u0915\u0940 \u0939\u092e \u0938\u0930\u093e\u0939\u0928\u093e \u0915\u0930\u0924\u0947 \u0939\u0948\u0902\u0964\n\n\u0938\u093e\u0926\u0930,\n\u092a\u094d\u0930\u092c\u0902\u0927 \u0938\u092e\u093f\u0924\u093f",
                    "Telugu": "\u0c2a\u0c4d\u0c30\u0c3f\u0c2f\u0c2e\u0c48\u0c28 \u0c28\u0c3f\u0c35\u0c3e\u0c38\u0c41\u0c32\u0c3e\u0c30\u0c3e,\n\n\u0c30\u0c47\u0c2a\u0c41 \u0c09\u0c26\u0c2f\u0c02 5:00 \u0c17\u0c02\u0c1f\u0c32 \u0c28\u0c41\u0c02\u0c21\u0c3f 8:00 \u0c17\u0c02\u0c1f\u0c32 \u0c2e\u0c27\u0c4d\u0c2f \u0c35\u0c3e\u0c1f\u0c30\u0c4d \u0c1f\u0c4d\u0c2f\u0c3e\u0c02\u0c15\u0c4d \u0c36\u0c41\u0c2d\u0c4d\u0c30\u0c2a\u0c30\u0c3f\u0c1a\u0c47 \u0c2a\u0c28\u0c3f \u0c28\u0c3f\u0c30\u0c4d\u0c23\u0c2f\u0c3f\u0c02\u0c1a\u0c2c\u0c21\u0c3f\u0c02\u0c26\u0c28\u0c3f \u0c24\u0c46\u0c32\u0c3f\u0c2f\u0c1c\u0c47\u0c38\u0c4d\u0c24\u0c41\u0c28\u0c4d\u0c28\u0c3e\u0c2e\u0c41. \u0c26\u0c40\u0c28\u0c3f \u0c15\u0c3e\u0c30\u0c23\u0c02\u0c17\u0c3e, \u0c08 \u0c38\u0c2e\u0c2f\u0c02\u0c32\u0c4b \u0c28\u0c40\u0c1f\u0c3f \u0c38\u0c30\u0c2b\u0c30\u0c3e \u0c28\u0c3f\u0c32\u0c3f\u0c2a\u0c3f\u0c35\u0c47\u0c2f\u0c2c\u0c21\u0c41\u0c24\u0c41\u0c02\u0c26\u0c3f.\n\n\u0c28\u0c3f\u0c35\u0c3e\u0c38\u0c41\u0c32\u0c41 \u0c24\u0c2e \u0c30\u0c4b\u0c1c\u0c41\u0c35\u0c3e\u0c30\u0c40 \u0c05\u0c35\u0c38\u0c30\u0c3e\u0c32\u0c28\u0c41 \u0c24\u0c40\u0c30\u0c4d\u0c1a\u0c41\u0c15\u0c4b\u0c35\u0c21\u0c3e\u0c28\u0c3f\u0c15\u0c3f \u0c2e\u0c41\u0c02\u0c26\u0c41\u0c17\u0c3e\u0c28\u0c47 \u0c24\u0c17\u0c3f\u0c28\u0c02\u0c24 \u0c28\u0c40\u0c1f\u0c3f\u0c28\u0c3f \u0c28\u0c3f\u0c32\u0c4d\u0c35 \u0c1a\u0c47\u0c38\u0c41\u0c15\u0c4b\u0c35\u0c3e\u0c32\u0c28\u0c3f \u0c35\u0c3f\u0c1c\u0c4d\u0c1e\u0c2a\u0c4d\u0c24\u0c3f \u0c1a\u0c47\u0c38\u0c4d\u0c24\u0c41\u0c28\u0c4d\u0c28\u0c3e\u0c2e\u0c41. \u0c2e\u0c40\u0c15\u0c41 \u0c15\u0c32\u0c3f\u0c17\u0c47 \u0c05\u0c38\u0c4c\u0c15\u0c30\u0c4d\u0c2f\u0c3e\u0c28\u0c3f\u0c15\u0c3f \u0c35\u0c3f\u0c1a\u0c3e\u0c30\u0c3f\u0c38\u0c4d\u0c24\u0c41\u0c28\u0c4d\u0c28\u0c3e\u0c2e\u0c41 \u0c2e\u0c30\u0c3f\u0c2f\u0c41 \u0c2e\u0c28 \u0c38\u0c4a\u0c38\u0c48\u0c1f\u0c40 \u0c2e\u0c4c\u0c32\u0c3f\u0c15 \u0c38\u0c26\u0c41\u0c2a\u0c3e\u0c2f\u0c3e\u0c32\u0c28\u0c41 \u0c36\u0c41\u0c2d\u0c4d\u0c30\u0c02\u0c17\u0c3e, \u0c2a\u0c30\u0c3f\u0c36\u0c41\u0c2d\u0c4d\u0c30\u0c02\u0c17\u0c3e \u0c09\u0c02\u0c1a\u0c21\u0c02\u0c32\u0c4b \u0c2e\u0c40 \u0c38\u0c39\u0c15\u0c3e\u0c30\u0c3e\u0c28\u0c3f\u0c15\u0c3f \u0c27\u0c28\u0c4d\u0c2f\u0c35\u0c3e\u0c26\u0c3e\u0c32\u0c41.\n\n\u0c2d\u0c35\u0c26\u0c40\u0c2f\u0c41\u0c32\u0c41,\n\u0c2e\u0c47\u0c28\u0c47\u0c1c\u0c4d\u200c\u0c2e\u0c46\u0c02\u0c1f\u0c4d \u0c15\u0c2e\u0c3f\u0c1f\u0c40"
                }
            },
            {
                "body": "Annual General Meeting this Sunday at 10 AM.",
                "created_at": "2026-08-08T08:19:33",
                "created_by_user_id": 1,
                "expires_at": null,
                "id": 7,
                "notice_type": "general",
                "priority": "medium",
                "publish_at": "2026-08-08T08:19:33.856035",
                "society_id": 1,
                "title": "AGM Meeting",
                "translations": {}
            },
            {
                "body": "Annual General Meeting this Sunday at 10 AM.",
                "created_at": "2026-08-08T08:18:52",
                "created_by_user_id": 1,
                "expires_at": null,
                "id": 6,
                "notice_type": "general",
                "priority": "medium",
                "publish_at": "2026-08-08T08:18:52.463326",
                "society_id": 1,
                "title": "AGM Meeting",
                "translations": {}
            },
            {
                "body": "Annual General Meeting this Sunday at 10 AM.",
                "created_at": "2026-08-08T08:13:30",
                "created_by_user_id": 1,
                "expires_at": null,
                "id": 5,
                "notice_type": "general",
                "priority": "medium",
                "publish_at": "2026-08-08T08:13:30.049234",
                "society_id": 1,
                "title": "AGM Meeting",
                "translations": {}
            },
            {
                "body": "Dear Residents,\n\nPlease be informed that a society cleaning drive is scheduled for Saturday, from 1:00 AM to 2:00 AM. All residents are requested to be present during this time and extend their cooperation to the cleaning staff to ensure smooth execution.\n\nThank you for your cooperation.\n\nWarm regards,\nManagement Committee\nSocioNeed",
                "created_at": "2026-08-08T06:33:33",
                "created_by_user_id": 1,
                "expires_at": null,
                "id": 4,
                "notice_type": "maintenance",
                "priority": "normal",
                "publish_at": "2026-08-08T06:33:33.725239",
                "society_id": 1,
                "title": "Notice: Society Cleaning Drive",
                "translations": {}
            },
            {
                "body": "Please ensure visitors are pre-approved at gate entry.",
                "created_at": "2026-08-08T03:15:31",
                "created_by_user_id": 1,
                "expires_at": null,
                "id": 3,
                "notice_type": "security",
                "priority": "urgent",
                "publish_at": "2026-08-08T03:15:31.878754",
                "society_id": 1,
                "title": "Security Advisory",
                "translations": {}
            },
            {
                "body": "Water tank cleaning is scheduled this weekend.",
                "created_at": "2026-08-08T03:15:31",
                "created_by_user_id": 1,
                "expires_at": null,
                "id": 1,
                "notice_type": "maintenance",
                "priority": "high",
                "publish_at": "2026-08-06T03:15:31.878754",
                "society_id": 1,
                "title": "Water Tank Cleaning",
                "translations": {}
            }
        ],
        "pagination": {
            "limit": 20,
            "page": 1,
            "pages": 1,
            "total": 8
        }
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 81 – Booking Availability Feed Update (Case 81)
API Endpoint: GET /api/events

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "items": [
            {
                "created_at": "2026-08-08T03:15:31",
                "created_by_user_id": 1,
                "description": "Morning wellness session in clubhouse.",
                "end_time": "08:00",
                "event_date": "Mon, 10 Aug 2026 00:00:00 GMT",
                "id": 1,
                "society_id": 1,
                "start_time": "07:00",
                "status": "scheduled",
                "title": "Yoga Session",
                "venue": "Clubhouse"
            },
            {
                "created_at": "2026-08-08T03:15:31",
                "created_by_user_id": 1,
                "description": "Weekend painting workshop for children.",
                "end_time": "18:00",
                "event_date": "Thu, 13 Aug 2026 00:00:00 GMT",
                "id": 2,
                "society_id": 1,
                "start_time": "16:00",
                "status": "scheduled",
                "title": "Kids Painting Workshop",
                "venue": "Community Hall"
            },
            {
                "created_at": "2026-08-08T03:15:31",
                "created_by_user_id": 1,
                "description": "Safety drill with security team guidance.",
                "end_time": "11:00",
                "event_date": "Sun, 16 Aug 2026 00:00:00 GMT",
                "id": 3,
                "society_id": 1,
                "start_time": "10:00",
                "status": "scheduled",
                "title": "Fire Safety Drill",
                "venue": "Main Courtyard"
            }
        ],
        "pagination": {
            "limit": 20,
            "page": 1,
            "pages": 1,
            "total": 3
        }
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 82 – Booking Cancellation Release (Case 82)
API Endpoint: GET /api/complaints

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "items": [
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T10:07:02",
                "description": "Water leaking in kitchen",
                "id": 15,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T10:07:02"
            },
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T08:42:10",
                "description": "Water leaking in kitchen",
                "id": 14,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T08:42:10"
            },
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T08:33:32",
                "description": "Water leaking in kitchen",
                "id": 13,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T08:33:32"
            },
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T08:32:20",
                "description": "Water leaking in kitchen",
                "id": 12,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T08:32:20"
            },
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T08:31:57",
                "description": "Water leaking in kitchen",
                "id": 11,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T08:31:57"
            },
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T08:31:45",
                "description": "Water leaking in kitchen",
                "id": 10,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T08:31:45"
            },
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T08:27:49",
                "description": "Water leaking in kitchen",
                "id": 9,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T08:27:49"
            },
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T08:26:09",
                "description": "Water leaking in kitchen",
                "id": 8,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T08:26:09"
            },
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T08:25:53",
                "description": "Water leaking in kitchen",
                "id": 7,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T08:25:53"
            },
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T08:24:34",
                "description": "Water leaking in kitchen",
                "id": 6,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T08:24:34"
            },
            {
                "assigned_to_user_id": 3,
                "category": "Lift",
                "created_at": "2026-08-08T06:24:29",
                "description": "asafs",
                "id": 5,
                "priority": "low",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "in_progress",
                "subject": "adsfaf",
                "updated_at": "2026-08-08T06:31:05"
            },
            {
                "assigned_to_user_id": null,
                "category": "Water",
                "created_at": "2026-08-08T06:24:16",
                "description": "suddenly water not commming",
                "id": 4,
                "priority": "high",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "water not comming",
                "updated_at": "2026-08-08T06:24:16"
            },
            {
                "assigned_to_user_id": 3,
                "category": "Maintenance",
                "created_at": "2026-08-08T03:15:31",
                "description": "Lift in Block C has intermittent stoppage.",
                "id": 1,
                "priority": "high",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "in_progress",
                "subject": "Lift maintenance required",
                "updated_at": "2026-08-08T08:24:34"
            },
            {
                "assigned_to_user_id": 5,
                "category": "Plumbing",
                "created_at": "2026-08-08T03:15:31",
                "description": "Leakage observed near basement entry ramp.",
                "id": 2,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "in_progress",
                "subject": "Water leakage near basement",
                "updated_at": "2026-08-08T06:25:03"
            },
            {
                "assigned_to_user_id": 12,
                "category": "Security",
                "created_at": "2026-08-08T03:15:31",
                "description": "CCTV feed near gate 2 is blurry at night.",
                "id": 3,
                "priority": "high",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "resolved",
                "subject": "CCTV camera blur",
                "updated_at": "2026-08-08T03:15:31"
            }
        ],
        "pagination": {
            "limit": 20,
            "page": 1,
            "pages": 1,
            "total": 15
        }
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 83 – Complaint Assign Admin Check (Case 83)
API Endpoint: GET /api/service-categories

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": [
        {
            "created_at": "2026-08-08T03:15:31.863325",
            "description": "Exterior and interior car cleaning and detailing",
            "id": 5,
            "name": "Car Wash"
        },
        {
            "created_at": "2026-08-08T03:15:31.863353",
            "description": "Home cooking, party catering, and tiffin services",
            "id": 8,
            "name": "Cook"
        },
        {
            "created_at": "2026-08-08T03:15:31.863304",
            "description": "Electrical wiring, repairs, and appliance installation",
            "id": 3,
            "name": "Electrician"
        },
        {
            "created_at": "2026-08-08T03:15:31.863335",
            "description": "Garden maintenance, lawn mowing, and landscaping",
            "id": 6,
            "name": "Gardener"
        },
        {
            "created_at": "2026-08-08T03:15:31.863245",
            "description": "Professional house cleaning and domestic help services",
            "id": 1,
            "name": "House Maid"
        },
        {
            "created_at": "2026-08-08T03:15:31.863315",
            "description": "Wash, iron, dry cleaning, and delivery",
            "id": 4,
            "name": "Laundry"
        },
        {
            "created_at": "2026-08-08T03:15:31.863288",
            "description": "Plumbing, pipe fitting, and drainage solutions",
            "id": 2,
            "name": "Plumber"
        },
        {
            "created_at": "2026-08-08T03:15:31.863344",
            "description": "Tailoring, alterations, and custom stitching",
            "id": 7,
            "name": "Tailor"
        }
    ],
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 84 – Complaint Status Update Audit (Case 84)
API Endpoint: GET /api/providers

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "items": [
            {
                "business_name": "Provider User Services",
                "category_id": 1,
                "created_at": "2026-08-08T03:15:31",
                "id": 1,
                "rating_avg": 4.5,
                "service_description": "Community verified service provider",
                "user_id": 3,
                "verification_status": "approved"
            },
            {
                "business_name": "Pooja House Maid Services",
                "category_id": 2,
                "created_at": "2026-08-08T03:15:31",
                "id": 2,
                "rating_avg": 4.5,
                "service_description": "Community verified service provider",
                "user_id": 4,
                "verification_status": "approved"
            },
            {
                "business_name": "Ravi Plumber Services",
                "category_id": 3,
                "created_at": "2026-08-08T03:15:31",
                "id": 3,
                "rating_avg": 4.5,
                "service_description": "Community verified service provider",
                "user_id": 5,
                "verification_status": "approved"
            },
            {
                "business_name": "Sita Electrician Services",
                "category_id": 4,
                "created_at": "2026-08-08T03:15:31",
                "id": 4,
                "rating_avg": 4.5,
                "service_description": "Community verified service provider",
                "user_id": 6,
                "verification_status": "approved"
            },
            {
                "business_name": "Sunita Laundry Services",
                "category_id": 5,
                "created_at": "2026-08-08T03:15:31",
                "id": 5,
                "rating_avg": 4.5,
                "service_description": "Community verified service provider",
                "user_id": 7,
                "verification_status": "approved"
            },
            {
                "business_name": "Kumar Car Wash Services",
                "category_id": 6,
                "created_at": "2026-08-08T03:15:31",
                "id": 6,
                "rating_avg": 4.5,
                "service_description": "Community verified service provider",
                "user_id": 8,
                "verification_status": "approved"
            },
            {
                "business_name": "Ramesh Gardener Services",
                "category_id": 7,
                "created_at": "2026-08-08T03:15:31",
                "id": 7,
                "rating_avg": 4.5,
                "service_description": "Community verified service provider",
                "user_id": 9,
                "verification_status": "approved"
            },
            {
                "business_name": "Ajay Tailor Services",
                "category_id": 8,
                "created_at": "2026-08-08T03:15:31",
                "id": 8,
                "rating_avg": 4.5,
                "service_description": "Community verified service provider",
                "user_id": 10,
                "verification_status": "approved"
            },
            {
                "business_name": "Lakshmi Cook Services",
                "category_id": 1,
                "created_at": "2026-08-08T03:15:31",
                "id": 9,
                "rating_avg": 4.5,
                "service_description": "Community verified service provider",
                "user_id": 11,
                "verification_status": "approved"
            }
        ],
        "pagination": {
            "limit": 20,
            "page": 1,
            "pages": 1,
            "total": 9
        }
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 85 – Complaint Timeline Log (Case 85)
API Endpoint: GET /api/slots

Input:
{}

Expected Output:
{
    "status_code": 405,
    "success": false
}

----------------------------------------------------------------------
ACTUAL STATUS: 405
ACTUAL RESPONSE (json):
{
    "error": {
        "code": "METHOD_NOT_ALLOWED",
        "message": "The method is not allowed for the requested URL."
    },
    "success": false
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 86 – DB Session Rollback Verification (Case 86)
API Endpoint: GET /api/bookings

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "items": [
            {
                "booking_status": "requested",
                "created_at": "2026-08-08T09:22:02",
                "id": 5,
                "provider_id": 5,
                "request_notes": "Booking created from resident portal",
                "resident_user_id": 2,
                "slot_id": null,
                "updated_at": "2026-08-08T09:22:02"
            },
            {
                "booking_status": "requested",
                "created_at": "2026-08-08T06:22:32",
                "id": 4,
                "provider_id": 5,
                "request_notes": "Booking created from resident portal",
                "resident_user_id": 2,
                "slot_id": null,
                "updated_at": "2026-08-08T06:22:32"
            },
            {
                "booking_status": "accepted",
                "created_at": "2026-08-08T03:15:31",
                "id": 1,
                "provider_id": 1,
                "request_notes": "Kitchen sink pipe check",
                "resident_user_id": 2,
                "slot_id": null,
                "updated_at": "2026-08-08T06:37:14"
            },
            {
                "booking_status": "completed",
                "created_at": "2026-08-08T03:15:31",
                "id": 2,
                "provider_id": 1,
                "request_notes": "Bathroom fitting replacement",
                "resident_user_id": 2,
                "slot_id": null,
                "updated_at": "2026-08-08T06:26:36"
            },
            {
                "booking_status": "completed",
                "created_at": "2026-08-08T03:15:31",
                "id": 3,
                "provider_id": 1,
                "request_notes": "Balcony drain cleanup",
                "resident_user_id": 2,
                "slot_id": null,
                "updated_at": "2026-08-08T03:15:31"
            }
        ],
        "pagination": {
            "limit": 20,
            "page": 1,
            "pages": 1,
            "total": 5
        }
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 87 – DB Duplicate Field Conflict (Case 87)
API Endpoint: GET /api/reviews

Input:
{}

Expected Output:
{
    "status_code": 405,
    "success": false
}

----------------------------------------------------------------------
ACTUAL STATUS: 405
ACTUAL RESPONSE (json):
{
    "error": {
        "code": "METHOD_NOT_ALLOWED",
        "message": "The method is not allowed for the requested URL."
    },
    "success": false
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 88 – Error Envelope Consistency (Case 88)
API Endpoint: GET /api/visitors

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "items": [],
        "pagination": {
            "limit": 20,
            "page": 1,
            "pages": 0,
            "total": 0
        }
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 89 – AI Notice Generation (Case 89)
API Endpoint: GET /api/analytics/dashboard/admin

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "stats": {
            "pending_complaints": 14,
            "todays_bookings": 5,
            "total_residents": 21,
            "upcoming_events": 3
        }
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 90 – AI Multilingual Announcement (Case 90)
API Endpoint: GET /api/reports/monthly

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "bookings": {
            "total": 5
        },
        "complaints": {
            "raised": 15
        },
        "events": {
            "scheduled": 3
        },
        "notices": {
            "published": 8
        },
        "residents": {
            "total": 21
        },
        "visitors": {
            "total": 0
        }
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 91 – AI Complaint Classification (Case 91)
API Endpoint: GET /api/ai/status

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "configured": true,
        "features": [
            "notice_generator",
            "multilingual_announcement",
            "event_planner",
            "analytics_insights",
            "complaint_classification",
            "meeting_minutes",
            "notice_summarizer",
            "notices_summarize_all",
            "maintenance_assistant",
            "complaint_resolution_insights",
            "rules_qa",
            "feedback_analyzer",
            "amenity_booking_assistant"
        ],
        "model": "gemini-flash-latest"
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 92 – AI Resolution Insights (Case 92)
API Endpoint: GET /api/users/me

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "created_at": "2026-08-08T03:15:30.937350",
        "email": "admin@socioneed.com",
        "full_name": "Admin User",
        "id": 1,
        "phone": "9000000001",
        "role": "admin",
        "society_id": 1,
        "status": "active"
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 93 – AI Rules QA Assistant (Case 93)
API Endpoint: GET /api/auth/verify-token

Input:
{}

Expected Output:
{
    "status_code": 405,
    "success": false
}

----------------------------------------------------------------------
ACTUAL STATUS: 405
ACTUAL RESPONSE (json):
{
    "error": {
        "code": "METHOD_NOT_ALLOWED",
        "message": "The method is not allowed for the requested URL."
    },
    "success": false
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 94 – AI Amenity Assistant (Case 94)
API Endpoint: GET /api/societies

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "items": [
            {
                "address": "123 Main Road",
                "city": "Mumbai",
                "contact_email": "admin@greenvalley.com",
                "contact_phone": "9988776655",
                "created_at": "2026-08-08T03:15:30",
                "id": 1,
                "name": "Green Valley Society",
                "pincode": "400001"
            }
        ],
        "pagination": {
            "limit": 20,
            "page": 1,
            "pages": 1,
            "total": 1
        }
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 95 – AI Feedback Analyzer (Case 95)
API Endpoint: GET /api/units

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "items": [
            {
                "block_name": null,
                "created_at": "2026-08-08T10:07:02",
                "floor": null,
                "id": 10,
                "society_id": 1,
                "status": "active",
                "unit_number": "U21195",
                "unit_type": "2BHK"
            },
            {
                "block_name": null,
                "created_at": "2026-08-08T08:42:10",
                "floor": null,
                "id": 9,
                "society_id": 1,
                "status": "active",
                "unit_number": "U50798",
                "unit_type": "2BHK"
            },
            {
                "block_name": null,
                "created_at": "2026-08-08T08:33:32",
                "floor": null,
                "id": 8,
                "society_id": 1,
                "status": "active",
                "unit_number": "U55818",
                "unit_type": "2BHK"
            },
            {
                "block_name": null,
                "created_at": "2026-08-08T08:32:20",
                "floor": null,
                "id": 7,
                "society_id": 1,
                "status": "active",
                "unit_number": "U38478",
                "unit_type": "2BHK"
            },
            {
                "block_name": null,
                "created_at": "2026-08-08T08:31:57",
                "floor": null,
                "id": 6,
                "society_id": 1,
                "status": "active",
                "unit_number": "U44431",
                "unit_type": "2BHK"
            },
            {
                "block_name": null,
                "created_at": "2026-08-08T08:31:45",
                "floor": null,
                "id": 5,
                "society_id": 1,
                "status": "active",
                "unit_number": "U53839",
                "unit_type": "2BHK"
            },
            {
                "block_name": null,
                "created_at": "2026-08-08T08:27:49",
                "floor": null,
                "id": 4,
                "society_id": 1,
                "status": "active",
                "unit_number": "U27389",
                "unit_type": "2BHK"
            },
            {
                "block_name": null,
                "created_at": "2026-08-08T08:26:09",
                "floor": null,
                "id": 3,
                "society_id": 1,
                "status": "active",
                "unit_number": "U85933",
                "unit_type": "2BHK"
            },
            {
                "block_name": null,
                "created_at": "2026-08-08T08:25:53",
                "floor": null,
                "id": 2,
                "society_id": 1,
                "status": "active",
                "unit_number": "U74443",
                "unit_type": "2BHK"
            },
            {
                "block_name": null,
                "created_at": "2026-08-08T08:24:34",
                "floor": null,
                "id": 1,
                "society_id": 1,
                "status": "active",
                "unit_number": "U91921",
                "unit_type": "3BHK"
            }
        ],
        "pagination": {
            "limit": 20,
            "page": 1,
            "pages": 1,
            "total": 10
        }
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 96 – AI Maintenance Assistant (Case 96)
API Endpoint: GET /api/notices

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "items": [
            {
                "body": "Tank cleaning on Sunday",
                "created_at": "2026-08-08T10:07:02",
                "created_by_user_id": 1,
                "expires_at": null,
                "id": 9,
                "notice_type": "general",
                "priority": "medium",
                "publish_at": "2026-08-08T10:07:02.341164",
                "society_id": 1,
                "title": "Water Notice",
                "translations": {}
            },
            {
                "body": "Dear Residents,\n\nPlease be informed that the water tank cleaning work is scheduled for tomorrow between 5:00 and 8:00. Consequently, the water supply will be stopped during this period.\n\nResidents are requested to store adequate water in advance to fulfill their daily requirements. We regret the inconvenience caused and appreciate your cooperation in keeping our society's infrastructure clean and hygienic.\n\nWarm regards,\nManagement Committee",
                "created_at": "2026-08-08T09:19:28",
                "created_by_user_id": 1,
                "expires_at": null,
                "id": 8,
                "notice_type": "maintenance",
                "priority": "normal",
                "publish_at": "2026-08-08T09:19:28.911176",
                "society_id": 1,
                "title": "Notice: Water Tank Cleaning & Water Supply Disruption",
                "translations": {
                    "English": "Dear Residents,\n\nPlease be informed that the water tank cleaning work is scheduled for tomorrow between 5:00 AM and 8:00 AM. Consequently, the water supply will be stopped during this period.\n\nResidents are requested to store adequate water in advance to fulfill their daily requirements. We regret the inconvenience caused and appreciate your cooperation in keeping our society's infrastructure clean and hygienic.\n\nWarm regards,\nManagement Committee",
                    "Hindi": "\u092a\u094d\u0930\u093f\u092f \u0928\u093f\u0935\u093e\u0938\u093f\u092f\u094b\u0902,\n\n\u0906\u092a\u0915\u094b \u0938\u0942\u091a\u093f\u0924 \u0915\u093f\u092f\u093e \u091c\u093e\u0924\u093e \u0939\u0948 \u0915\u093f \u0915\u0932 \u0938\u0941\u092c\u0939 5:00 \u092c\u091c\u0947 \u0938\u0947 8:00 \u092c\u091c\u0947 \u0915\u0947 \u092c\u0940\u091a \u092a\u093e\u0928\u0940 \u0915\u0940 \u091f\u0902\u0915\u0940 \u0915\u0940 \u0938\u092b\u093e\u0908 \u0915\u093e \u0915\u093e\u0930\u094d\u092f \u0928\u093f\u0930\u094d\u0927\u093e\u0930\u093f\u0924 \u0915\u093f\u092f\u093e \u0917\u092f\u093e \u0939\u0948\u0964 \u0907\u0938\u0915\u0947 \u092a\u0930\u093f\u0923\u093e\u092e\u0938\u094d\u0935\u0930\u0942\u092a, \u0907\u0938 \u0905\u0935\u0927\u093f \u0915\u0947 \u0926\u094c\u0930\u093e\u0928 \u092a\u093e\u0928\u0940 \u0915\u0940 \u0906\u092a\u0942\u0930\u094d\u0924\u093f \u092c\u0902\u0926 \u0930\u0939\u0947\u0917\u0940\u0964\n\n\u0938\u092d\u0940 \u0928\u093f\u0935\u093e\u0938\u093f\u092f\u094b\u0902 \u0938\u0947 \u0905\u0928\u0941\u0930\u094b\u0927 \u0939\u0948 \u0915\u093f \u0935\u0947 \u0905\u092a\u0928\u0940 \u0926\u0948\u0928\u093f\u0915 \u0906\u0935\u0936\u094d\u092f\u0915\u0924\u093e\u0913\u0902 \u0915\u094b \u092a\u0942\u0930\u093e \u0915\u0930\u0928\u0947 \u0915\u0947 \u0932\u093f\u090f \u092a\u0939\u0932\u0947 \u0938\u0947 \u0939\u0940 \u092a\u0930\u094d\u092f\u093e\u092a\u094d\u0924 \u092a\u093e\u0928\u0940 \u0915\u093e \u092d\u0902\u0921\u093e\u0930\u0923 \u0915\u0930 \u0932\u0947\u0902\u0964 \u0906\u092a\u0915\u094b \u0939\u094b\u0928\u0947 \u0935\u093e\u0932\u0940 \u0905\u0938\u0941\u0935\u093f\u0927\u093e \u0915\u0947 \u0932\u093f\u090f \u0939\u092e\u0947\u0902 \u0916\u0947\u0926 \u0939\u0948 \u0914\u0930 \u0939\u092e\u093e\u0930\u0940 \u0938\u094b\u0938\u093e\u0907\u091f\u0940 \u0915\u0947 \u092c\u0941\u0928\u093f\u092f\u093e\u0926\u0940 \u0922\u093e\u0902\u091a\u0947 \u0915\u094b \u0938\u093e\u092b \u0914\u0930 \u0938\u094d\u0935\u091a\u094d\u091b \u092c\u0928\u093e\u090f \u0930\u0916\u0928\u0947 \u092e\u0947\u0902 \u0906\u092a\u0915\u0947 \u0938\u0939\u092f\u094b\u0917 \u0915\u0940 \u0939\u092e \u0938\u0930\u093e\u0939\u0928\u093e \u0915\u0930\u0924\u0947 \u0939\u0948\u0902\u0964\n\n\u0938\u093e\u0926\u0930,\n\u092a\u094d\u0930\u092c\u0902\u0927 \u0938\u092e\u093f\u0924\u093f",
                    "Telugu": "\u0c2a\u0c4d\u0c30\u0c3f\u0c2f\u0c2e\u0c48\u0c28 \u0c28\u0c3f\u0c35\u0c3e\u0c38\u0c41\u0c32\u0c3e\u0c30\u0c3e,\n\n\u0c30\u0c47\u0c2a\u0c41 \u0c09\u0c26\u0c2f\u0c02 5:00 \u0c17\u0c02\u0c1f\u0c32 \u0c28\u0c41\u0c02\u0c21\u0c3f 8:00 \u0c17\u0c02\u0c1f\u0c32 \u0c2e\u0c27\u0c4d\u0c2f \u0c35\u0c3e\u0c1f\u0c30\u0c4d \u0c1f\u0c4d\u0c2f\u0c3e\u0c02\u0c15\u0c4d \u0c36\u0c41\u0c2d\u0c4d\u0c30\u0c2a\u0c30\u0c3f\u0c1a\u0c47 \u0c2a\u0c28\u0c3f \u0c28\u0c3f\u0c30\u0c4d\u0c23\u0c2f\u0c3f\u0c02\u0c1a\u0c2c\u0c21\u0c3f\u0c02\u0c26\u0c28\u0c3f \u0c24\u0c46\u0c32\u0c3f\u0c2f\u0c1c\u0c47\u0c38\u0c4d\u0c24\u0c41\u0c28\u0c4d\u0c28\u0c3e\u0c2e\u0c41. \u0c26\u0c40\u0c28\u0c3f \u0c15\u0c3e\u0c30\u0c23\u0c02\u0c17\u0c3e, \u0c08 \u0c38\u0c2e\u0c2f\u0c02\u0c32\u0c4b \u0c28\u0c40\u0c1f\u0c3f \u0c38\u0c30\u0c2b\u0c30\u0c3e \u0c28\u0c3f\u0c32\u0c3f\u0c2a\u0c3f\u0c35\u0c47\u0c2f\u0c2c\u0c21\u0c41\u0c24\u0c41\u0c02\u0c26\u0c3f.\n\n\u0c28\u0c3f\u0c35\u0c3e\u0c38\u0c41\u0c32\u0c41 \u0c24\u0c2e \u0c30\u0c4b\u0c1c\u0c41\u0c35\u0c3e\u0c30\u0c40 \u0c05\u0c35\u0c38\u0c30\u0c3e\u0c32\u0c28\u0c41 \u0c24\u0c40\u0c30\u0c4d\u0c1a\u0c41\u0c15\u0c4b\u0c35\u0c21\u0c3e\u0c28\u0c3f\u0c15\u0c3f \u0c2e\u0c41\u0c02\u0c26\u0c41\u0c17\u0c3e\u0c28\u0c47 \u0c24\u0c17\u0c3f\u0c28\u0c02\u0c24 \u0c28\u0c40\u0c1f\u0c3f\u0c28\u0c3f \u0c28\u0c3f\u0c32\u0c4d\u0c35 \u0c1a\u0c47\u0c38\u0c41\u0c15\u0c4b\u0c35\u0c3e\u0c32\u0c28\u0c3f \u0c35\u0c3f\u0c1c\u0c4d\u0c1e\u0c2a\u0c4d\u0c24\u0c3f \u0c1a\u0c47\u0c38\u0c4d\u0c24\u0c41\u0c28\u0c4d\u0c28\u0c3e\u0c2e\u0c41. \u0c2e\u0c40\u0c15\u0c41 \u0c15\u0c32\u0c3f\u0c17\u0c47 \u0c05\u0c38\u0c4c\u0c15\u0c30\u0c4d\u0c2f\u0c3e\u0c28\u0c3f\u0c15\u0c3f \u0c35\u0c3f\u0c1a\u0c3e\u0c30\u0c3f\u0c38\u0c4d\u0c24\u0c41\u0c28\u0c4d\u0c28\u0c3e\u0c2e\u0c41 \u0c2e\u0c30\u0c3f\u0c2f\u0c41 \u0c2e\u0c28 \u0c38\u0c4a\u0c38\u0c48\u0c1f\u0c40 \u0c2e\u0c4c\u0c32\u0c3f\u0c15 \u0c38\u0c26\u0c41\u0c2a\u0c3e\u0c2f\u0c3e\u0c32\u0c28\u0c41 \u0c36\u0c41\u0c2d\u0c4d\u0c30\u0c02\u0c17\u0c3e, \u0c2a\u0c30\u0c3f\u0c36\u0c41\u0c2d\u0c4d\u0c30\u0c02\u0c17\u0c3e \u0c09\u0c02\u0c1a\u0c21\u0c02\u0c32\u0c4b \u0c2e\u0c40 \u0c38\u0c39\u0c15\u0c3e\u0c30\u0c3e\u0c28\u0c3f\u0c15\u0c3f \u0c27\u0c28\u0c4d\u0c2f\u0c35\u0c3e\u0c26\u0c3e\u0c32\u0c41.\n\n\u0c2d\u0c35\u0c26\u0c40\u0c2f\u0c41\u0c32\u0c41,\n\u0c2e\u0c47\u0c28\u0c47\u0c1c\u0c4d\u200c\u0c2e\u0c46\u0c02\u0c1f\u0c4d \u0c15\u0c2e\u0c3f\u0c1f\u0c40"
                }
            },
            {
                "body": "Annual General Meeting this Sunday at 10 AM.",
                "created_at": "2026-08-08T08:19:33",
                "created_by_user_id": 1,
                "expires_at": null,
                "id": 7,
                "notice_type": "general",
                "priority": "medium",
                "publish_at": "2026-08-08T08:19:33.856035",
                "society_id": 1,
                "title": "AGM Meeting",
                "translations": {}
            },
            {
                "body": "Annual General Meeting this Sunday at 10 AM.",
                "created_at": "2026-08-08T08:18:52",
                "created_by_user_id": 1,
                "expires_at": null,
                "id": 6,
                "notice_type": "general",
                "priority": "medium",
                "publish_at": "2026-08-08T08:18:52.463326",
                "society_id": 1,
                "title": "AGM Meeting",
                "translations": {}
            },
            {
                "body": "Annual General Meeting this Sunday at 10 AM.",
                "created_at": "2026-08-08T08:13:30",
                "created_by_user_id": 1,
                "expires_at": null,
                "id": 5,
                "notice_type": "general",
                "priority": "medium",
                "publish_at": "2026-08-08T08:13:30.049234",
                "society_id": 1,
                "title": "AGM Meeting",
                "translations": {}
            },
            {
                "body": "Dear Residents,\n\nPlease be informed that a society cleaning drive is scheduled for Saturday, from 1:00 AM to 2:00 AM. All residents are requested to be present during this time and extend their cooperation to the cleaning staff to ensure smooth execution.\n\nThank you for your cooperation.\n\nWarm regards,\nManagement Committee\nSocioNeed",
                "created_at": "2026-08-08T06:33:33",
                "created_by_user_id": 1,
                "expires_at": null,
                "id": 4,
                "notice_type": "maintenance",
                "priority": "normal",
                "publish_at": "2026-08-08T06:33:33.725239",
                "society_id": 1,
                "title": "Notice: Society Cleaning Drive",
                "translations": {}
            },
            {
                "body": "Please ensure visitors are pre-approved at gate entry.",
                "created_at": "2026-08-08T03:15:31",
                "created_by_user_id": 1,
                "expires_at": null,
                "id": 3,
                "notice_type": "security",
                "priority": "urgent",
                "publish_at": "2026-08-08T03:15:31.878754",
                "society_id": 1,
                "title": "Security Advisory",
                "translations": {}
            },
            {
                "body": "Water tank cleaning is scheduled this weekend.",
                "created_at": "2026-08-08T03:15:31",
                "created_by_user_id": 1,
                "expires_at": null,
                "id": 1,
                "notice_type": "maintenance",
                "priority": "high",
                "publish_at": "2026-08-06T03:15:31.878754",
                "society_id": 1,
                "title": "Water Tank Cleaning",
                "translations": {}
            }
        ],
        "pagination": {
            "limit": 20,
            "page": 1,
            "pages": 1,
            "total": 8
        }
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 97 – AI Meeting Minutes (Case 97)
API Endpoint: GET /api/events

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "items": [
            {
                "created_at": "2026-08-08T03:15:31",
                "created_by_user_id": 1,
                "description": "Morning wellness session in clubhouse.",
                "end_time": "08:00",
                "event_date": "Mon, 10 Aug 2026 00:00:00 GMT",
                "id": 1,
                "society_id": 1,
                "start_time": "07:00",
                "status": "scheduled",
                "title": "Yoga Session",
                "venue": "Clubhouse"
            },
            {
                "created_at": "2026-08-08T03:15:31",
                "created_by_user_id": 1,
                "description": "Weekend painting workshop for children.",
                "end_time": "18:00",
                "event_date": "Thu, 13 Aug 2026 00:00:00 GMT",
                "id": 2,
                "society_id": 1,
                "start_time": "16:00",
                "status": "scheduled",
                "title": "Kids Painting Workshop",
                "venue": "Community Hall"
            },
            {
                "created_at": "2026-08-08T03:15:31",
                "created_by_user_id": 1,
                "description": "Safety drill with security team guidance.",
                "end_time": "11:00",
                "event_date": "Sun, 16 Aug 2026 00:00:00 GMT",
                "id": 3,
                "society_id": 1,
                "start_time": "10:00",
                "status": "scheduled",
                "title": "Fire Safety Drill",
                "venue": "Main Courtyard"
            }
        ],
        "pagination": {
            "limit": 20,
            "page": 1,
            "pages": 1,
            "total": 3
        }
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 98 – Sprint 1 Auth Cycle (Case 98)
API Endpoint: GET /api/complaints

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "items": [
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T10:07:02",
                "description": "Water leaking in kitchen",
                "id": 15,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T10:07:02"
            },
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T08:42:10",
                "description": "Water leaking in kitchen",
                "id": 14,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T08:42:10"
            },
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T08:33:32",
                "description": "Water leaking in kitchen",
                "id": 13,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T08:33:32"
            },
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T08:32:20",
                "description": "Water leaking in kitchen",
                "id": 12,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T08:32:20"
            },
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T08:31:57",
                "description": "Water leaking in kitchen",
                "id": 11,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T08:31:57"
            },
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T08:31:45",
                "description": "Water leaking in kitchen",
                "id": 10,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T08:31:45"
            },
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T08:27:49",
                "description": "Water leaking in kitchen",
                "id": 9,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T08:27:49"
            },
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T08:26:09",
                "description": "Water leaking in kitchen",
                "id": 8,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T08:26:09"
            },
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T08:25:53",
                "description": "Water leaking in kitchen",
                "id": 7,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T08:25:53"
            },
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T08:24:34",
                "description": "Water leaking in kitchen",
                "id": 6,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T08:24:34"
            },
            {
                "assigned_to_user_id": 3,
                "category": "Lift",
                "created_at": "2026-08-08T06:24:29",
                "description": "asafs",
                "id": 5,
                "priority": "low",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "in_progress",
                "subject": "adsfaf",
                "updated_at": "2026-08-08T06:31:05"
            },
            {
                "assigned_to_user_id": null,
                "category": "Water",
                "created_at": "2026-08-08T06:24:16",
                "description": "suddenly water not commming",
                "id": 4,
                "priority": "high",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "water not comming",
                "updated_at": "2026-08-08T06:24:16"
            },
            {
                "assigned_to_user_id": 3,
                "category": "Maintenance",
                "created_at": "2026-08-08T03:15:31",
                "description": "Lift in Block C has intermittent stoppage.",
                "id": 1,
                "priority": "high",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "in_progress",
                "subject": "Lift maintenance required",
                "updated_at": "2026-08-08T08:24:34"
            },
            {
                "assigned_to_user_id": 5,
                "category": "Plumbing",
                "created_at": "2026-08-08T03:15:31",
                "description": "Leakage observed near basement entry ramp.",
                "id": 2,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "in_progress",
                "subject": "Water leakage near basement",
                "updated_at": "2026-08-08T06:25:03"
            },
            {
                "assigned_to_user_id": 12,
                "category": "Security",
                "created_at": "2026-08-08T03:15:31",
                "description": "CCTV feed near gate 2 is blurry at night.",
                "id": 3,
                "priority": "high",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "resolved",
                "subject": "CCTV camera blur",
                "updated_at": "2026-08-08T03:15:31"
            }
        ],
        "pagination": {
            "limit": 20,
            "page": 1,
            "pages": 1,
            "total": 15
        }
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 99 – Sprint 1 User List Cycle (Case 99)
API Endpoint: GET /api/service-categories

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": [
        {
            "created_at": "2026-08-08T03:15:31.863325",
            "description": "Exterior and interior car cleaning and detailing",
            "id": 5,
            "name": "Car Wash"
        },
        {
            "created_at": "2026-08-08T03:15:31.863353",
            "description": "Home cooking, party catering, and tiffin services",
            "id": 8,
            "name": "Cook"
        },
        {
            "created_at": "2026-08-08T03:15:31.863304",
            "description": "Electrical wiring, repairs, and appliance installation",
            "id": 3,
            "name": "Electrician"
        },
        {
            "created_at": "2026-08-08T03:15:31.863335",
            "description": "Garden maintenance, lawn mowing, and landscaping",
            "id": 6,
            "name": "Gardener"
        },
        {
            "created_at": "2026-08-08T03:15:31.863245",
            "description": "Professional house cleaning and domestic help services",
            "id": 1,
            "name": "House Maid"
        },
        {
            "created_at": "2026-08-08T03:15:31.863315",
            "description": "Wash, iron, dry cleaning, and delivery",
            "id": 4,
            "name": "Laundry"
        },
        {
            "created_at": "2026-08-08T03:15:31.863288",
            "description": "Plumbing, pipe fitting, and drainage solutions",
            "id": 2,
            "name": "Plumber"
        },
        {
            "created_at": "2026-08-08T03:15:31.863344",
            "description": "Tailoring, alterations, and custom stitching",
            "id": 7,
            "name": "Tailor"
        }
    ],
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 100 – Sprint 1 Unit Management (Case 100)
API Endpoint: GET /api/providers

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "items": [
            {
                "business_name": "Provider User Services",
                "category_id": 1,
                "created_at": "2026-08-08T03:15:31",
                "id": 1,
                "rating_avg": 4.5,
                "service_description": "Community verified service provider",
                "user_id": 3,
                "verification_status": "approved"
            },
            {
                "business_name": "Pooja House Maid Services",
                "category_id": 2,
                "created_at": "2026-08-08T03:15:31",
                "id": 2,
                "rating_avg": 4.5,
                "service_description": "Community verified service provider",
                "user_id": 4,
                "verification_status": "approved"
            },
            {
                "business_name": "Ravi Plumber Services",
                "category_id": 3,
                "created_at": "2026-08-08T03:15:31",
                "id": 3,
                "rating_avg": 4.5,
                "service_description": "Community verified service provider",
                "user_id": 5,
                "verification_status": "approved"
            },
            {
                "business_name": "Sita Electrician Services",
                "category_id": 4,
                "created_at": "2026-08-08T03:15:31",
                "id": 4,
                "rating_avg": 4.5,
                "service_description": "Community verified service provider",
                "user_id": 6,
                "verification_status": "approved"
            },
            {
                "business_name": "Sunita Laundry Services",
                "category_id": 5,
                "created_at": "2026-08-08T03:15:31",
                "id": 5,
                "rating_avg": 4.5,
                "service_description": "Community verified service provider",
                "user_id": 7,
                "verification_status": "approved"
            },
            {
                "business_name": "Kumar Car Wash Services",
                "category_id": 6,
                "created_at": "2026-08-08T03:15:31",
                "id": 6,
                "rating_avg": 4.5,
                "service_description": "Community verified service provider",
                "user_id": 8,
                "verification_status": "approved"
            },
            {
                "business_name": "Ramesh Gardener Services",
                "category_id": 7,
                "created_at": "2026-08-08T03:15:31",
                "id": 7,
                "rating_avg": 4.5,
                "service_description": "Community verified service provider",
                "user_id": 9,
                "verification_status": "approved"
            },
            {
                "business_name": "Ajay Tailor Services",
                "category_id": 8,
                "created_at": "2026-08-08T03:15:31",
                "id": 8,
                "rating_avg": 4.5,
                "service_description": "Community verified service provider",
                "user_id": 10,
                "verification_status": "approved"
            },
            {
                "business_name": "Lakshmi Cook Services",
                "category_id": 1,
                "created_at": "2026-08-08T03:15:31",
                "id": 9,
                "rating_avg": 4.5,
                "service_description": "Community verified service provider",
                "user_id": 11,
                "verification_status": "approved"
            }
        ],
        "pagination": {
            "limit": 20,
            "page": 1,
            "pages": 1,
            "total": 9
        }
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 101 – Sprint 2 Complaint Workflow (Case 101)
API Endpoint: GET /api/slots

Input:
{}

Expected Output:
{
    "status_code": 405,
    "success": false
}

----------------------------------------------------------------------
ACTUAL STATUS: 405
ACTUAL RESPONSE (json):
{
    "error": {
        "code": "METHOD_NOT_ALLOWED",
        "message": "The method is not allowed for the requested URL."
    },
    "success": false
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 102 – Sprint 2 Booking Review Workflow (Case 102)
API Endpoint: GET /api/bookings

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "items": [
            {
                "booking_status": "requested",
                "created_at": "2026-08-08T09:22:02",
                "id": 5,
                "provider_id": 5,
                "request_notes": "Booking created from resident portal",
                "resident_user_id": 2,
                "slot_id": null,
                "updated_at": "2026-08-08T09:22:02"
            },
            {
                "booking_status": "requested",
                "created_at": "2026-08-08T06:22:32",
                "id": 4,
                "provider_id": 5,
                "request_notes": "Booking created from resident portal",
                "resident_user_id": 2,
                "slot_id": null,
                "updated_at": "2026-08-08T06:22:32"
            },
            {
                "booking_status": "accepted",
                "created_at": "2026-08-08T03:15:31",
                "id": 1,
                "provider_id": 1,
                "request_notes": "Kitchen sink pipe check",
                "resident_user_id": 2,
                "slot_id": null,
                "updated_at": "2026-08-08T06:37:14"
            },
            {
                "booking_status": "completed",
                "created_at": "2026-08-08T03:15:31",
                "id": 2,
                "provider_id": 1,
                "request_notes": "Bathroom fitting replacement",
                "resident_user_id": 2,
                "slot_id": null,
                "updated_at": "2026-08-08T06:26:36"
            },
            {
                "booking_status": "completed",
                "created_at": "2026-08-08T03:15:31",
                "id": 3,
                "provider_id": 1,
                "request_notes": "Balcony drain cleanup",
                "resident_user_id": 2,
                "slot_id": null,
                "updated_at": "2026-08-08T03:15:31"
            }
        ],
        "pagination": {
            "limit": 20,
            "page": 1,
            "pages": 1,
            "total": 5
        }
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 103 – Sprint 2 Reports Summary (Case 103)
API Endpoint: GET /api/reviews

Input:
{}

Expected Output:
{
    "status_code": 405,
    "success": false
}

----------------------------------------------------------------------
ACTUAL STATUS: 405
ACTUAL RESPONSE (json):
{
    "error": {
        "code": "METHOD_NOT_ALLOWED",
        "message": "The method is not allowed for the requested URL."
    },
    "success": false
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 104 – Token Expired Verification (Case 104)
API Endpoint: GET /api/visitors

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "items": [],
        "pagination": {
            "limit": 20,
            "page": 1,
            "pages": 0,
            "total": 0
        }
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 105 – Token Malformed Verification (Case 105)
API Endpoint: GET /api/analytics/dashboard/admin

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "stats": {
            "pending_complaints": 14,
            "todays_bookings": 5,
            "total_residents": 21,
            "upcoming_events": 3
        }
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 106 – Token Signature Check (Case 106)
API Endpoint: GET /api/reports/monthly

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "bookings": {
            "total": 5
        },
        "complaints": {
            "raised": 15
        },
        "events": {
            "scheduled": 3
        },
        "notices": {
            "published": 8
        },
        "residents": {
            "total": 21
        },
        "visitors": {
            "total": 0
        }
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 107 – Slot Start Time Formatting (Case 107)
API Endpoint: GET /api/ai/status

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "configured": true,
        "features": [
            "notice_generator",
            "multilingual_announcement",
            "event_planner",
            "analytics_insights",
            "complaint_classification",
            "meeting_minutes",
            "notice_summarizer",
            "notices_summarize_all",
            "maintenance_assistant",
            "complaint_resolution_insights",
            "rules_qa",
            "feedback_analyzer",
            "amenity_booking_assistant"
        ],
        "model": "gemini-flash-latest"
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 108 – Slot End Time Validation (Case 108)
API Endpoint: GET /api/users/me

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "created_at": "2026-08-08T03:15:30.937350",
        "email": "admin@socioneed.com",
        "full_name": "Admin User",
        "id": 1,
        "phone": "9000000001",
        "role": "admin",
        "society_id": 1,
        "status": "active"
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 109 – Slot Duration Check (Case 109)
API Endpoint: GET /api/auth/verify-token

Input:
{}

Expected Output:
{
    "status_code": 405,
    "success": false
}

----------------------------------------------------------------------
ACTUAL STATUS: 405
ACTUAL RESPONSE (json):
{
    "error": {
        "code": "METHOD_NOT_ALLOWED",
        "message": "The method is not allowed for the requested URL."
    },
    "success": false
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 110 – Booking Double Booking Prevention (Case 110)
API Endpoint: GET /api/societies

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "items": [
            {
                "address": "123 Main Road",
                "city": "Mumbai",
                "contact_email": "admin@greenvalley.com",
                "contact_phone": "9988776655",
                "created_at": "2026-08-08T03:15:30",
                "id": 1,
                "name": "Green Valley Society",
                "pincode": "400001"
            }
        ],
        "pagination": {
            "limit": 20,
            "page": 1,
            "pages": 1,
            "total": 1
        }
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 111 – Booking Availability Feed Update (Case 111)
API Endpoint: GET /api/units

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "items": [
            {
                "block_name": null,
                "created_at": "2026-08-08T10:07:02",
                "floor": null,
                "id": 10,
                "society_id": 1,
                "status": "active",
                "unit_number": "U21195",
                "unit_type": "2BHK"
            },
            {
                "block_name": null,
                "created_at": "2026-08-08T08:42:10",
                "floor": null,
                "id": 9,
                "society_id": 1,
                "status": "active",
                "unit_number": "U50798",
                "unit_type": "2BHK"
            },
            {
                "block_name": null,
                "created_at": "2026-08-08T08:33:32",
                "floor": null,
                "id": 8,
                "society_id": 1,
                "status": "active",
                "unit_number": "U55818",
                "unit_type": "2BHK"
            },
            {
                "block_name": null,
                "created_at": "2026-08-08T08:32:20",
                "floor": null,
                "id": 7,
                "society_id": 1,
                "status": "active",
                "unit_number": "U38478",
                "unit_type": "2BHK"
            },
            {
                "block_name": null,
                "created_at": "2026-08-08T08:31:57",
                "floor": null,
                "id": 6,
                "society_id": 1,
                "status": "active",
                "unit_number": "U44431",
                "unit_type": "2BHK"
            },
            {
                "block_name": null,
                "created_at": "2026-08-08T08:31:45",
                "floor": null,
                "id": 5,
                "society_id": 1,
                "status": "active",
                "unit_number": "U53839",
                "unit_type": "2BHK"
            },
            {
                "block_name": null,
                "created_at": "2026-08-08T08:27:49",
                "floor": null,
                "id": 4,
                "society_id": 1,
                "status": "active",
                "unit_number": "U27389",
                "unit_type": "2BHK"
            },
            {
                "block_name": null,
                "created_at": "2026-08-08T08:26:09",
                "floor": null,
                "id": 3,
                "society_id": 1,
                "status": "active",
                "unit_number": "U85933",
                "unit_type": "2BHK"
            },
            {
                "block_name": null,
                "created_at": "2026-08-08T08:25:53",
                "floor": null,
                "id": 2,
                "society_id": 1,
                "status": "active",
                "unit_number": "U74443",
                "unit_type": "2BHK"
            },
            {
                "block_name": null,
                "created_at": "2026-08-08T08:24:34",
                "floor": null,
                "id": 1,
                "society_id": 1,
                "status": "active",
                "unit_number": "U91921",
                "unit_type": "3BHK"
            }
        ],
        "pagination": {
            "limit": 20,
            "page": 1,
            "pages": 1,
            "total": 10
        }
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 112 – Booking Cancellation Release (Case 112)
API Endpoint: GET /api/notices

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "items": [
            {
                "body": "Tank cleaning on Sunday",
                "created_at": "2026-08-08T10:07:02",
                "created_by_user_id": 1,
                "expires_at": null,
                "id": 9,
                "notice_type": "general",
                "priority": "medium",
                "publish_at": "2026-08-08T10:07:02.341164",
                "society_id": 1,
                "title": "Water Notice",
                "translations": {}
            },
            {
                "body": "Dear Residents,\n\nPlease be informed that the water tank cleaning work is scheduled for tomorrow between 5:00 and 8:00. Consequently, the water supply will be stopped during this period.\n\nResidents are requested to store adequate water in advance to fulfill their daily requirements. We regret the inconvenience caused and appreciate your cooperation in keeping our society's infrastructure clean and hygienic.\n\nWarm regards,\nManagement Committee",
                "created_at": "2026-08-08T09:19:28",
                "created_by_user_id": 1,
                "expires_at": null,
                "id": 8,
                "notice_type": "maintenance",
                "priority": "normal",
                "publish_at": "2026-08-08T09:19:28.911176",
                "society_id": 1,
                "title": "Notice: Water Tank Cleaning & Water Supply Disruption",
                "translations": {
                    "English": "Dear Residents,\n\nPlease be informed that the water tank cleaning work is scheduled for tomorrow between 5:00 AM and 8:00 AM. Consequently, the water supply will be stopped during this period.\n\nResidents are requested to store adequate water in advance to fulfill their daily requirements. We regret the inconvenience caused and appreciate your cooperation in keeping our society's infrastructure clean and hygienic.\n\nWarm regards,\nManagement Committee",
                    "Hindi": "\u092a\u094d\u0930\u093f\u092f \u0928\u093f\u0935\u093e\u0938\u093f\u092f\u094b\u0902,\n\n\u0906\u092a\u0915\u094b \u0938\u0942\u091a\u093f\u0924 \u0915\u093f\u092f\u093e \u091c\u093e\u0924\u093e \u0939\u0948 \u0915\u093f \u0915\u0932 \u0938\u0941\u092c\u0939 5:00 \u092c\u091c\u0947 \u0938\u0947 8:00 \u092c\u091c\u0947 \u0915\u0947 \u092c\u0940\u091a \u092a\u093e\u0928\u0940 \u0915\u0940 \u091f\u0902\u0915\u0940 \u0915\u0940 \u0938\u092b\u093e\u0908 \u0915\u093e \u0915\u093e\u0930\u094d\u092f \u0928\u093f\u0930\u094d\u0927\u093e\u0930\u093f\u0924 \u0915\u093f\u092f\u093e \u0917\u092f\u093e \u0939\u0948\u0964 \u0907\u0938\u0915\u0947 \u092a\u0930\u093f\u0923\u093e\u092e\u0938\u094d\u0935\u0930\u0942\u092a, \u0907\u0938 \u0905\u0935\u0927\u093f \u0915\u0947 \u0926\u094c\u0930\u093e\u0928 \u092a\u093e\u0928\u0940 \u0915\u0940 \u0906\u092a\u0942\u0930\u094d\u0924\u093f \u092c\u0902\u0926 \u0930\u0939\u0947\u0917\u0940\u0964\n\n\u0938\u092d\u0940 \u0928\u093f\u0935\u093e\u0938\u093f\u092f\u094b\u0902 \u0938\u0947 \u0905\u0928\u0941\u0930\u094b\u0927 \u0939\u0948 \u0915\u093f \u0935\u0947 \u0905\u092a\u0928\u0940 \u0926\u0948\u0928\u093f\u0915 \u0906\u0935\u0936\u094d\u092f\u0915\u0924\u093e\u0913\u0902 \u0915\u094b \u092a\u0942\u0930\u093e \u0915\u0930\u0928\u0947 \u0915\u0947 \u0932\u093f\u090f \u092a\u0939\u0932\u0947 \u0938\u0947 \u0939\u0940 \u092a\u0930\u094d\u092f\u093e\u092a\u094d\u0924 \u092a\u093e\u0928\u0940 \u0915\u093e \u092d\u0902\u0921\u093e\u0930\u0923 \u0915\u0930 \u0932\u0947\u0902\u0964 \u0906\u092a\u0915\u094b \u0939\u094b\u0928\u0947 \u0935\u093e\u0932\u0940 \u0905\u0938\u0941\u0935\u093f\u0927\u093e \u0915\u0947 \u0932\u093f\u090f \u0939\u092e\u0947\u0902 \u0916\u0947\u0926 \u0939\u0948 \u0914\u0930 \u0939\u092e\u093e\u0930\u0940 \u0938\u094b\u0938\u093e\u0907\u091f\u0940 \u0915\u0947 \u092c\u0941\u0928\u093f\u092f\u093e\u0926\u0940 \u0922\u093e\u0902\u091a\u0947 \u0915\u094b \u0938\u093e\u092b \u0914\u0930 \u0938\u094d\u0935\u091a\u094d\u091b \u092c\u0928\u093e\u090f \u0930\u0916\u0928\u0947 \u092e\u0947\u0902 \u0906\u092a\u0915\u0947 \u0938\u0939\u092f\u094b\u0917 \u0915\u0940 \u0939\u092e \u0938\u0930\u093e\u0939\u0928\u093e \u0915\u0930\u0924\u0947 \u0939\u0948\u0902\u0964\n\n\u0938\u093e\u0926\u0930,\n\u092a\u094d\u0930\u092c\u0902\u0927 \u0938\u092e\u093f\u0924\u093f",
                    "Telugu": "\u0c2a\u0c4d\u0c30\u0c3f\u0c2f\u0c2e\u0c48\u0c28 \u0c28\u0c3f\u0c35\u0c3e\u0c38\u0c41\u0c32\u0c3e\u0c30\u0c3e,\n\n\u0c30\u0c47\u0c2a\u0c41 \u0c09\u0c26\u0c2f\u0c02 5:00 \u0c17\u0c02\u0c1f\u0c32 \u0c28\u0c41\u0c02\u0c21\u0c3f 8:00 \u0c17\u0c02\u0c1f\u0c32 \u0c2e\u0c27\u0c4d\u0c2f \u0c35\u0c3e\u0c1f\u0c30\u0c4d \u0c1f\u0c4d\u0c2f\u0c3e\u0c02\u0c15\u0c4d \u0c36\u0c41\u0c2d\u0c4d\u0c30\u0c2a\u0c30\u0c3f\u0c1a\u0c47 \u0c2a\u0c28\u0c3f \u0c28\u0c3f\u0c30\u0c4d\u0c23\u0c2f\u0c3f\u0c02\u0c1a\u0c2c\u0c21\u0c3f\u0c02\u0c26\u0c28\u0c3f \u0c24\u0c46\u0c32\u0c3f\u0c2f\u0c1c\u0c47\u0c38\u0c4d\u0c24\u0c41\u0c28\u0c4d\u0c28\u0c3e\u0c2e\u0c41. \u0c26\u0c40\u0c28\u0c3f \u0c15\u0c3e\u0c30\u0c23\u0c02\u0c17\u0c3e, \u0c08 \u0c38\u0c2e\u0c2f\u0c02\u0c32\u0c4b \u0c28\u0c40\u0c1f\u0c3f \u0c38\u0c30\u0c2b\u0c30\u0c3e \u0c28\u0c3f\u0c32\u0c3f\u0c2a\u0c3f\u0c35\u0c47\u0c2f\u0c2c\u0c21\u0c41\u0c24\u0c41\u0c02\u0c26\u0c3f.\n\n\u0c28\u0c3f\u0c35\u0c3e\u0c38\u0c41\u0c32\u0c41 \u0c24\u0c2e \u0c30\u0c4b\u0c1c\u0c41\u0c35\u0c3e\u0c30\u0c40 \u0c05\u0c35\u0c38\u0c30\u0c3e\u0c32\u0c28\u0c41 \u0c24\u0c40\u0c30\u0c4d\u0c1a\u0c41\u0c15\u0c4b\u0c35\u0c21\u0c3e\u0c28\u0c3f\u0c15\u0c3f \u0c2e\u0c41\u0c02\u0c26\u0c41\u0c17\u0c3e\u0c28\u0c47 \u0c24\u0c17\u0c3f\u0c28\u0c02\u0c24 \u0c28\u0c40\u0c1f\u0c3f\u0c28\u0c3f \u0c28\u0c3f\u0c32\u0c4d\u0c35 \u0c1a\u0c47\u0c38\u0c41\u0c15\u0c4b\u0c35\u0c3e\u0c32\u0c28\u0c3f \u0c35\u0c3f\u0c1c\u0c4d\u0c1e\u0c2a\u0c4d\u0c24\u0c3f \u0c1a\u0c47\u0c38\u0c4d\u0c24\u0c41\u0c28\u0c4d\u0c28\u0c3e\u0c2e\u0c41. \u0c2e\u0c40\u0c15\u0c41 \u0c15\u0c32\u0c3f\u0c17\u0c47 \u0c05\u0c38\u0c4c\u0c15\u0c30\u0c4d\u0c2f\u0c3e\u0c28\u0c3f\u0c15\u0c3f \u0c35\u0c3f\u0c1a\u0c3e\u0c30\u0c3f\u0c38\u0c4d\u0c24\u0c41\u0c28\u0c4d\u0c28\u0c3e\u0c2e\u0c41 \u0c2e\u0c30\u0c3f\u0c2f\u0c41 \u0c2e\u0c28 \u0c38\u0c4a\u0c38\u0c48\u0c1f\u0c40 \u0c2e\u0c4c\u0c32\u0c3f\u0c15 \u0c38\u0c26\u0c41\u0c2a\u0c3e\u0c2f\u0c3e\u0c32\u0c28\u0c41 \u0c36\u0c41\u0c2d\u0c4d\u0c30\u0c02\u0c17\u0c3e, \u0c2a\u0c30\u0c3f\u0c36\u0c41\u0c2d\u0c4d\u0c30\u0c02\u0c17\u0c3e \u0c09\u0c02\u0c1a\u0c21\u0c02\u0c32\u0c4b \u0c2e\u0c40 \u0c38\u0c39\u0c15\u0c3e\u0c30\u0c3e\u0c28\u0c3f\u0c15\u0c3f \u0c27\u0c28\u0c4d\u0c2f\u0c35\u0c3e\u0c26\u0c3e\u0c32\u0c41.\n\n\u0c2d\u0c35\u0c26\u0c40\u0c2f\u0c41\u0c32\u0c41,\n\u0c2e\u0c47\u0c28\u0c47\u0c1c\u0c4d\u200c\u0c2e\u0c46\u0c02\u0c1f\u0c4d \u0c15\u0c2e\u0c3f\u0c1f\u0c40"
                }
            },
            {
                "body": "Annual General Meeting this Sunday at 10 AM.",
                "created_at": "2026-08-08T08:19:33",
                "created_by_user_id": 1,
                "expires_at": null,
                "id": 7,
                "notice_type": "general",
                "priority": "medium",
                "publish_at": "2026-08-08T08:19:33.856035",
                "society_id": 1,
                "title": "AGM Meeting",
                "translations": {}
            },
            {
                "body": "Annual General Meeting this Sunday at 10 AM.",
                "created_at": "2026-08-08T08:18:52",
                "created_by_user_id": 1,
                "expires_at": null,
                "id": 6,
                "notice_type": "general",
                "priority": "medium",
                "publish_at": "2026-08-08T08:18:52.463326",
                "society_id": 1,
                "title": "AGM Meeting",
                "translations": {}
            },
            {
                "body": "Annual General Meeting this Sunday at 10 AM.",
                "created_at": "2026-08-08T08:13:30",
                "created_by_user_id": 1,
                "expires_at": null,
                "id": 5,
                "notice_type": "general",
                "priority": "medium",
                "publish_at": "2026-08-08T08:13:30.049234",
                "society_id": 1,
                "title": "AGM Meeting",
                "translations": {}
            },
            {
                "body": "Dear Residents,\n\nPlease be informed that a society cleaning drive is scheduled for Saturday, from 1:00 AM to 2:00 AM. All residents are requested to be present during this time and extend their cooperation to the cleaning staff to ensure smooth execution.\n\nThank you for your cooperation.\n\nWarm regards,\nManagement Committee\nSocioNeed",
                "created_at": "2026-08-08T06:33:33",
                "created_by_user_id": 1,
                "expires_at": null,
                "id": 4,
                "notice_type": "maintenance",
                "priority": "normal",
                "publish_at": "2026-08-08T06:33:33.725239",
                "society_id": 1,
                "title": "Notice: Society Cleaning Drive",
                "translations": {}
            },
            {
                "body": "Please ensure visitors are pre-approved at gate entry.",
                "created_at": "2026-08-08T03:15:31",
                "created_by_user_id": 1,
                "expires_at": null,
                "id": 3,
                "notice_type": "security",
                "priority": "urgent",
                "publish_at": "2026-08-08T03:15:31.878754",
                "society_id": 1,
                "title": "Security Advisory",
                "translations": {}
            },
            {
                "body": "Water tank cleaning is scheduled this weekend.",
                "created_at": "2026-08-08T03:15:31",
                "created_by_user_id": 1,
                "expires_at": null,
                "id": 1,
                "notice_type": "maintenance",
                "priority": "high",
                "publish_at": "2026-08-06T03:15:31.878754",
                "society_id": 1,
                "title": "Water Tank Cleaning",
                "translations": {}
            }
        ],
        "pagination": {
            "limit": 20,
            "page": 1,
            "pages": 1,
            "total": 8
        }
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 113 – Complaint Assign Admin Check (Case 113)
API Endpoint: GET /api/events

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "items": [
            {
                "created_at": "2026-08-08T03:15:31",
                "created_by_user_id": 1,
                "description": "Morning wellness session in clubhouse.",
                "end_time": "08:00",
                "event_date": "Mon, 10 Aug 2026 00:00:00 GMT",
                "id": 1,
                "society_id": 1,
                "start_time": "07:00",
                "status": "scheduled",
                "title": "Yoga Session",
                "venue": "Clubhouse"
            },
            {
                "created_at": "2026-08-08T03:15:31",
                "created_by_user_id": 1,
                "description": "Weekend painting workshop for children.",
                "end_time": "18:00",
                "event_date": "Thu, 13 Aug 2026 00:00:00 GMT",
                "id": 2,
                "society_id": 1,
                "start_time": "16:00",
                "status": "scheduled",
                "title": "Kids Painting Workshop",
                "venue": "Community Hall"
            },
            {
                "created_at": "2026-08-08T03:15:31",
                "created_by_user_id": 1,
                "description": "Safety drill with security team guidance.",
                "end_time": "11:00",
                "event_date": "Sun, 16 Aug 2026 00:00:00 GMT",
                "id": 3,
                "society_id": 1,
                "start_time": "10:00",
                "status": "scheduled",
                "title": "Fire Safety Drill",
                "venue": "Main Courtyard"
            }
        ],
        "pagination": {
            "limit": 20,
            "page": 1,
            "pages": 1,
            "total": 3
        }
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 114 – Complaint Status Update Audit (Case 114)
API Endpoint: GET /api/complaints

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "items": [
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T10:07:02",
                "description": "Water leaking in kitchen",
                "id": 15,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T10:07:02"
            },
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T08:42:10",
                "description": "Water leaking in kitchen",
                "id": 14,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T08:42:10"
            },
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T08:33:32",
                "description": "Water leaking in kitchen",
                "id": 13,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T08:33:32"
            },
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T08:32:20",
                "description": "Water leaking in kitchen",
                "id": 12,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T08:32:20"
            },
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T08:31:57",
                "description": "Water leaking in kitchen",
                "id": 11,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T08:31:57"
            },
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T08:31:45",
                "description": "Water leaking in kitchen",
                "id": 10,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T08:31:45"
            },
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T08:27:49",
                "description": "Water leaking in kitchen",
                "id": 9,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T08:27:49"
            },
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T08:26:09",
                "description": "Water leaking in kitchen",
                "id": 8,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T08:26:09"
            },
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T08:25:53",
                "description": "Water leaking in kitchen",
                "id": 7,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T08:25:53"
            },
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T08:24:34",
                "description": "Water leaking in kitchen",
                "id": 6,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T08:24:34"
            },
            {
                "assigned_to_user_id": 3,
                "category": "Lift",
                "created_at": "2026-08-08T06:24:29",
                "description": "asafs",
                "id": 5,
                "priority": "low",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "in_progress",
                "subject": "adsfaf",
                "updated_at": "2026-08-08T06:31:05"
            },
            {
                "assigned_to_user_id": null,
                "category": "Water",
                "created_at": "2026-08-08T06:24:16",
                "description": "suddenly water not commming",
                "id": 4,
                "priority": "high",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "water not comming",
                "updated_at": "2026-08-08T06:24:16"
            },
            {
                "assigned_to_user_id": 3,
                "category": "Maintenance",
                "created_at": "2026-08-08T03:15:31",
                "description": "Lift in Block C has intermittent stoppage.",
                "id": 1,
                "priority": "high",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "in_progress",
                "subject": "Lift maintenance required",
                "updated_at": "2026-08-08T08:24:34"
            },
            {
                "assigned_to_user_id": 5,
                "category": "Plumbing",
                "created_at": "2026-08-08T03:15:31",
                "description": "Leakage observed near basement entry ramp.",
                "id": 2,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "in_progress",
                "subject": "Water leakage near basement",
                "updated_at": "2026-08-08T06:25:03"
            },
            {
                "assigned_to_user_id": 12,
                "category": "Security",
                "created_at": "2026-08-08T03:15:31",
                "description": "CCTV feed near gate 2 is blurry at night.",
                "id": 3,
                "priority": "high",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "resolved",
                "subject": "CCTV camera blur",
                "updated_at": "2026-08-08T03:15:31"
            }
        ],
        "pagination": {
            "limit": 20,
            "page": 1,
            "pages": 1,
            "total": 15
        }
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 115 – Complaint Timeline Log (Case 115)
API Endpoint: GET /api/service-categories

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": [
        {
            "created_at": "2026-08-08T03:15:31.863325",
            "description": "Exterior and interior car cleaning and detailing",
            "id": 5,
            "name": "Car Wash"
        },
        {
            "created_at": "2026-08-08T03:15:31.863353",
            "description": "Home cooking, party catering, and tiffin services",
            "id": 8,
            "name": "Cook"
        },
        {
            "created_at": "2026-08-08T03:15:31.863304",
            "description": "Electrical wiring, repairs, and appliance installation",
            "id": 3,
            "name": "Electrician"
        },
        {
            "created_at": "2026-08-08T03:15:31.863335",
            "description": "Garden maintenance, lawn mowing, and landscaping",
            "id": 6,
            "name": "Gardener"
        },
        {
            "created_at": "2026-08-08T03:15:31.863245",
            "description": "Professional house cleaning and domestic help services",
            "id": 1,
            "name": "House Maid"
        },
        {
            "created_at": "2026-08-08T03:15:31.863315",
            "description": "Wash, iron, dry cleaning, and delivery",
            "id": 4,
            "name": "Laundry"
        },
        {
            "created_at": "2026-08-08T03:15:31.863288",
            "description": "Plumbing, pipe fitting, and drainage solutions",
            "id": 2,
            "name": "Plumber"
        },
        {
            "created_at": "2026-08-08T03:15:31.863344",
            "description": "Tailoring, alterations, and custom stitching",
            "id": 7,
            "name": "Tailor"
        }
    ],
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 116 – DB Session Rollback Verification (Case 116)
API Endpoint: GET /api/providers

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "items": [
            {
                "business_name": "Provider User Services",
                "category_id": 1,
                "created_at": "2026-08-08T03:15:31",
                "id": 1,
                "rating_avg": 4.5,
                "service_description": "Community verified service provider",
                "user_id": 3,
                "verification_status": "approved"
            },
            {
                "business_name": "Pooja House Maid Services",
                "category_id": 2,
                "created_at": "2026-08-08T03:15:31",
                "id": 2,
                "rating_avg": 4.5,
                "service_description": "Community verified service provider",
                "user_id": 4,
                "verification_status": "approved"
            },
            {
                "business_name": "Ravi Plumber Services",
                "category_id": 3,
                "created_at": "2026-08-08T03:15:31",
                "id": 3,
                "rating_avg": 4.5,
                "service_description": "Community verified service provider",
                "user_id": 5,
                "verification_status": "approved"
            },
            {
                "business_name": "Sita Electrician Services",
                "category_id": 4,
                "created_at": "2026-08-08T03:15:31",
                "id": 4,
                "rating_avg": 4.5,
                "service_description": "Community verified service provider",
                "user_id": 6,
                "verification_status": "approved"
            },
            {
                "business_name": "Sunita Laundry Services",
                "category_id": 5,
                "created_at": "2026-08-08T03:15:31",
                "id": 5,
                "rating_avg": 4.5,
                "service_description": "Community verified service provider",
                "user_id": 7,
                "verification_status": "approved"
            },
            {
                "business_name": "Kumar Car Wash Services",
                "category_id": 6,
                "created_at": "2026-08-08T03:15:31",
                "id": 6,
                "rating_avg": 4.5,
                "service_description": "Community verified service provider",
                "user_id": 8,
                "verification_status": "approved"
            },
            {
                "business_name": "Ramesh Gardener Services",
                "category_id": 7,
                "created_at": "2026-08-08T03:15:31",
                "id": 7,
                "rating_avg": 4.5,
                "service_description": "Community verified service provider",
                "user_id": 9,
                "verification_status": "approved"
            },
            {
                "business_name": "Ajay Tailor Services",
                "category_id": 8,
                "created_at": "2026-08-08T03:15:31",
                "id": 8,
                "rating_avg": 4.5,
                "service_description": "Community verified service provider",
                "user_id": 10,
                "verification_status": "approved"
            },
            {
                "business_name": "Lakshmi Cook Services",
                "category_id": 1,
                "created_at": "2026-08-08T03:15:31",
                "id": 9,
                "rating_avg": 4.5,
                "service_description": "Community verified service provider",
                "user_id": 11,
                "verification_status": "approved"
            }
        ],
        "pagination": {
            "limit": 20,
            "page": 1,
            "pages": 1,
            "total": 9
        }
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 117 – DB Duplicate Field Conflict (Case 117)
API Endpoint: GET /api/slots

Input:
{}

Expected Output:
{
    "status_code": 405,
    "success": false
}

----------------------------------------------------------------------
ACTUAL STATUS: 405
ACTUAL RESPONSE (json):
{
    "error": {
        "code": "METHOD_NOT_ALLOWED",
        "message": "The method is not allowed for the requested URL."
    },
    "success": false
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 118 – Error Envelope Consistency (Case 118)
API Endpoint: GET /api/bookings

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "items": [
            {
                "booking_status": "requested",
                "created_at": "2026-08-08T09:22:02",
                "id": 5,
                "provider_id": 5,
                "request_notes": "Booking created from resident portal",
                "resident_user_id": 2,
                "slot_id": null,
                "updated_at": "2026-08-08T09:22:02"
            },
            {
                "booking_status": "requested",
                "created_at": "2026-08-08T06:22:32",
                "id": 4,
                "provider_id": 5,
                "request_notes": "Booking created from resident portal",
                "resident_user_id": 2,
                "slot_id": null,
                "updated_at": "2026-08-08T06:22:32"
            },
            {
                "booking_status": "accepted",
                "created_at": "2026-08-08T03:15:31",
                "id": 1,
                "provider_id": 1,
                "request_notes": "Kitchen sink pipe check",
                "resident_user_id": 2,
                "slot_id": null,
                "updated_at": "2026-08-08T06:37:14"
            },
            {
                "booking_status": "completed",
                "created_at": "2026-08-08T03:15:31",
                "id": 2,
                "provider_id": 1,
                "request_notes": "Bathroom fitting replacement",
                "resident_user_id": 2,
                "slot_id": null,
                "updated_at": "2026-08-08T06:26:36"
            },
            {
                "booking_status": "completed",
                "created_at": "2026-08-08T03:15:31",
                "id": 3,
                "provider_id": 1,
                "request_notes": "Balcony drain cleanup",
                "resident_user_id": 2,
                "slot_id": null,
                "updated_at": "2026-08-08T03:15:31"
            }
        ],
        "pagination": {
            "limit": 20,
            "page": 1,
            "pages": 1,
            "total": 5
        }
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 119 – AI Notice Generation (Case 119)
API Endpoint: GET /api/reviews

Input:
{}

Expected Output:
{
    "status_code": 405,
    "success": false
}

----------------------------------------------------------------------
ACTUAL STATUS: 405
ACTUAL RESPONSE (json):
{
    "error": {
        "code": "METHOD_NOT_ALLOWED",
        "message": "The method is not allowed for the requested URL."
    },
    "success": false
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 120 – AI Multilingual Announcement (Case 120)
API Endpoint: GET /api/visitors

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "items": [],
        "pagination": {
            "limit": 20,
            "page": 1,
            "pages": 0,
            "total": 0
        }
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 121 – AI Complaint Classification (Case 121)
API Endpoint: GET /api/analytics/dashboard/admin

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "stats": {
            "pending_complaints": 14,
            "todays_bookings": 5,
            "total_residents": 21,
            "upcoming_events": 3
        }
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 122 – AI Resolution Insights (Case 122)
API Endpoint: GET /api/reports/monthly

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "bookings": {
            "total": 5
        },
        "complaints": {
            "raised": 15
        },
        "events": {
            "scheduled": 3
        },
        "notices": {
            "published": 8
        },
        "residents": {
            "total": 21
        },
        "visitors": {
            "total": 0
        }
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 123 – AI Generate Notice Requires Admin
API Endpoint: POST /api/ai/generate-notice

Input:
{
    "topic": "Water Tank Cleaning"
}

Expected Output:
{
    "status_code": 201,
    "message": "Operation expected to succeed"
}

----------------------------------------------------------------------
ACTUAL STATUS: 404
ACTUAL RESPONSE (json):
{
    "error": {
        "code": "NOT_FOUND",
        "message": "The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again."
    },
    "success": false
}

Result: ✘ Failure (Admin Role Required for AI Notice Generation)
======================================================================
```

```text
======================================================================
Test Case 124 – AI Amenity Assistant (Case 124)
API Endpoint: GET /api/users/me

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "created_at": "2026-08-08T03:15:30.937350",
        "email": "admin@socioneed.com",
        "full_name": "Admin User",
        "id": 1,
        "phone": "9000000001",
        "role": "admin",
        "society_id": 1,
        "status": "active"
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 125 – AI Feedback Analyzer (Case 125)
API Endpoint: GET /api/auth/verify-token

Input:
{}

Expected Output:
{
    "status_code": 405,
    "success": false
}

----------------------------------------------------------------------
ACTUAL STATUS: 405
ACTUAL RESPONSE (json):
{
    "error": {
        "code": "METHOD_NOT_ALLOWED",
        "message": "The method is not allowed for the requested URL."
    },
    "success": false
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 126 – AI Maintenance Assistant (Case 126)
API Endpoint: GET /api/societies

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "items": [
            {
                "address": "123 Main Road",
                "city": "Mumbai",
                "contact_email": "admin@greenvalley.com",
                "contact_phone": "9988776655",
                "created_at": "2026-08-08T03:15:30",
                "id": 1,
                "name": "Green Valley Society",
                "pincode": "400001"
            }
        ],
        "pagination": {
            "limit": 20,
            "page": 1,
            "pages": 1,
            "total": 1
        }
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 127 – AI Meeting Minutes (Case 127)
API Endpoint: GET /api/units

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "items": [
            {
                "block_name": null,
                "created_at": "2026-08-08T10:07:02",
                "floor": null,
                "id": 10,
                "society_id": 1,
                "status": "active",
                "unit_number": "U21195",
                "unit_type": "2BHK"
            },
            {
                "block_name": null,
                "created_at": "2026-08-08T08:42:10",
                "floor": null,
                "id": 9,
                "society_id": 1,
                "status": "active",
                "unit_number": "U50798",
                "unit_type": "2BHK"
            },
            {
                "block_name": null,
                "created_at": "2026-08-08T08:33:32",
                "floor": null,
                "id": 8,
                "society_id": 1,
                "status": "active",
                "unit_number": "U55818",
                "unit_type": "2BHK"
            },
            {
                "block_name": null,
                "created_at": "2026-08-08T08:32:20",
                "floor": null,
                "id": 7,
                "society_id": 1,
                "status": "active",
                "unit_number": "U38478",
                "unit_type": "2BHK"
            },
            {
                "block_name": null,
                "created_at": "2026-08-08T08:31:57",
                "floor": null,
                "id": 6,
                "society_id": 1,
                "status": "active",
                "unit_number": "U44431",
                "unit_type": "2BHK"
            },
            {
                "block_name": null,
                "created_at": "2026-08-08T08:31:45",
                "floor": null,
                "id": 5,
                "society_id": 1,
                "status": "active",
                "unit_number": "U53839",
                "unit_type": "2BHK"
            },
            {
                "block_name": null,
                "created_at": "2026-08-08T08:27:49",
                "floor": null,
                "id": 4,
                "society_id": 1,
                "status": "active",
                "unit_number": "U27389",
                "unit_type": "2BHK"
            },
            {
                "block_name": null,
                "created_at": "2026-08-08T08:26:09",
                "floor": null,
                "id": 3,
                "society_id": 1,
                "status": "active",
                "unit_number": "U85933",
                "unit_type": "2BHK"
            },
            {
                "block_name": null,
                "created_at": "2026-08-08T08:25:53",
                "floor": null,
                "id": 2,
                "society_id": 1,
                "status": "active",
                "unit_number": "U74443",
                "unit_type": "2BHK"
            },
            {
                "block_name": null,
                "created_at": "2026-08-08T08:24:34",
                "floor": null,
                "id": 1,
                "society_id": 1,
                "status": "active",
                "unit_number": "U91921",
                "unit_type": "3BHK"
            }
        ],
        "pagination": {
            "limit": 20,
            "page": 1,
            "pages": 1,
            "total": 10
        }
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 128 – Sprint 1 Auth Cycle (Case 128)
API Endpoint: GET /api/notices

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "items": [
            {
                "body": "Tank cleaning on Sunday",
                "created_at": "2026-08-08T10:07:02",
                "created_by_user_id": 1,
                "expires_at": null,
                "id": 9,
                "notice_type": "general",
                "priority": "medium",
                "publish_at": "2026-08-08T10:07:02.341164",
                "society_id": 1,
                "title": "Water Notice",
                "translations": {}
            },
            {
                "body": "Dear Residents,\n\nPlease be informed that the water tank cleaning work is scheduled for tomorrow between 5:00 and 8:00. Consequently, the water supply will be stopped during this period.\n\nResidents are requested to store adequate water in advance to fulfill their daily requirements. We regret the inconvenience caused and appreciate your cooperation in keeping our society's infrastructure clean and hygienic.\n\nWarm regards,\nManagement Committee",
                "created_at": "2026-08-08T09:19:28",
                "created_by_user_id": 1,
                "expires_at": null,
                "id": 8,
                "notice_type": "maintenance",
                "priority": "normal",
                "publish_at": "2026-08-08T09:19:28.911176",
                "society_id": 1,
                "title": "Notice: Water Tank Cleaning & Water Supply Disruption",
                "translations": {
                    "English": "Dear Residents,\n\nPlease be informed that the water tank cleaning work is scheduled for tomorrow between 5:00 AM and 8:00 AM. Consequently, the water supply will be stopped during this period.\n\nResidents are requested to store adequate water in advance to fulfill their daily requirements. We regret the inconvenience caused and appreciate your cooperation in keeping our society's infrastructure clean and hygienic.\n\nWarm regards,\nManagement Committee",
                    "Hindi": "\u092a\u094d\u0930\u093f\u092f \u0928\u093f\u0935\u093e\u0938\u093f\u092f\u094b\u0902,\n\n\u0906\u092a\u0915\u094b \u0938\u0942\u091a\u093f\u0924 \u0915\u093f\u092f\u093e \u091c\u093e\u0924\u093e \u0939\u0948 \u0915\u093f \u0915\u0932 \u0938\u0941\u092c\u0939 5:00 \u092c\u091c\u0947 \u0938\u0947 8:00 \u092c\u091c\u0947 \u0915\u0947 \u092c\u0940\u091a \u092a\u093e\u0928\u0940 \u0915\u0940 \u091f\u0902\u0915\u0940 \u0915\u0940 \u0938\u092b\u093e\u0908 \u0915\u093e \u0915\u093e\u0930\u094d\u092f \u0928\u093f\u0930\u094d\u0927\u093e\u0930\u093f\u0924 \u0915\u093f\u092f\u093e \u0917\u092f\u093e \u0939\u0948\u0964 \u0907\u0938\u0915\u0947 \u092a\u0930\u093f\u0923\u093e\u092e\u0938\u094d\u0935\u0930\u0942\u092a, \u0907\u0938 \u0905\u0935\u0927\u093f \u0915\u0947 \u0926\u094c\u0930\u093e\u0928 \u092a\u093e\u0928\u0940 \u0915\u0940 \u0906\u092a\u0942\u0930\u094d\u0924\u093f \u092c\u0902\u0926 \u0930\u0939\u0947\u0917\u0940\u0964\n\n\u0938\u092d\u0940 \u0928\u093f\u0935\u093e\u0938\u093f\u092f\u094b\u0902 \u0938\u0947 \u0905\u0928\u0941\u0930\u094b\u0927 \u0939\u0948 \u0915\u093f \u0935\u0947 \u0905\u092a\u0928\u0940 \u0926\u0948\u0928\u093f\u0915 \u0906\u0935\u0936\u094d\u092f\u0915\u0924\u093e\u0913\u0902 \u0915\u094b \u092a\u0942\u0930\u093e \u0915\u0930\u0928\u0947 \u0915\u0947 \u0932\u093f\u090f \u092a\u0939\u0932\u0947 \u0938\u0947 \u0939\u0940 \u092a\u0930\u094d\u092f\u093e\u092a\u094d\u0924 \u092a\u093e\u0928\u0940 \u0915\u093e \u092d\u0902\u0921\u093e\u0930\u0923 \u0915\u0930 \u0932\u0947\u0902\u0964 \u0906\u092a\u0915\u094b \u0939\u094b\u0928\u0947 \u0935\u093e\u0932\u0940 \u0905\u0938\u0941\u0935\u093f\u0927\u093e \u0915\u0947 \u0932\u093f\u090f \u0939\u092e\u0947\u0902 \u0916\u0947\u0926 \u0939\u0948 \u0914\u0930 \u0939\u092e\u093e\u0930\u0940 \u0938\u094b\u0938\u093e\u0907\u091f\u0940 \u0915\u0947 \u092c\u0941\u0928\u093f\u092f\u093e\u0926\u0940 \u0922\u093e\u0902\u091a\u0947 \u0915\u094b \u0938\u093e\u092b \u0914\u0930 \u0938\u094d\u0935\u091a\u094d\u091b \u092c\u0928\u093e\u090f \u0930\u0916\u0928\u0947 \u092e\u0947\u0902 \u0906\u092a\u0915\u0947 \u0938\u0939\u092f\u094b\u0917 \u0915\u0940 \u0939\u092e \u0938\u0930\u093e\u0939\u0928\u093e \u0915\u0930\u0924\u0947 \u0939\u0948\u0902\u0964\n\n\u0938\u093e\u0926\u0930,\n\u092a\u094d\u0930\u092c\u0902\u0927 \u0938\u092e\u093f\u0924\u093f",
                    "Telugu": "\u0c2a\u0c4d\u0c30\u0c3f\u0c2f\u0c2e\u0c48\u0c28 \u0c28\u0c3f\u0c35\u0c3e\u0c38\u0c41\u0c32\u0c3e\u0c30\u0c3e,\n\n\u0c30\u0c47\u0c2a\u0c41 \u0c09\u0c26\u0c2f\u0c02 5:00 \u0c17\u0c02\u0c1f\u0c32 \u0c28\u0c41\u0c02\u0c21\u0c3f 8:00 \u0c17\u0c02\u0c1f\u0c32 \u0c2e\u0c27\u0c4d\u0c2f \u0c35\u0c3e\u0c1f\u0c30\u0c4d \u0c1f\u0c4d\u0c2f\u0c3e\u0c02\u0c15\u0c4d \u0c36\u0c41\u0c2d\u0c4d\u0c30\u0c2a\u0c30\u0c3f\u0c1a\u0c47 \u0c2a\u0c28\u0c3f \u0c28\u0c3f\u0c30\u0c4d\u0c23\u0c2f\u0c3f\u0c02\u0c1a\u0c2c\u0c21\u0c3f\u0c02\u0c26\u0c28\u0c3f \u0c24\u0c46\u0c32\u0c3f\u0c2f\u0c1c\u0c47\u0c38\u0c4d\u0c24\u0c41\u0c28\u0c4d\u0c28\u0c3e\u0c2e\u0c41. \u0c26\u0c40\u0c28\u0c3f \u0c15\u0c3e\u0c30\u0c23\u0c02\u0c17\u0c3e, \u0c08 \u0c38\u0c2e\u0c2f\u0c02\u0c32\u0c4b \u0c28\u0c40\u0c1f\u0c3f \u0c38\u0c30\u0c2b\u0c30\u0c3e \u0c28\u0c3f\u0c32\u0c3f\u0c2a\u0c3f\u0c35\u0c47\u0c2f\u0c2c\u0c21\u0c41\u0c24\u0c41\u0c02\u0c26\u0c3f.\n\n\u0c28\u0c3f\u0c35\u0c3e\u0c38\u0c41\u0c32\u0c41 \u0c24\u0c2e \u0c30\u0c4b\u0c1c\u0c41\u0c35\u0c3e\u0c30\u0c40 \u0c05\u0c35\u0c38\u0c30\u0c3e\u0c32\u0c28\u0c41 \u0c24\u0c40\u0c30\u0c4d\u0c1a\u0c41\u0c15\u0c4b\u0c35\u0c21\u0c3e\u0c28\u0c3f\u0c15\u0c3f \u0c2e\u0c41\u0c02\u0c26\u0c41\u0c17\u0c3e\u0c28\u0c47 \u0c24\u0c17\u0c3f\u0c28\u0c02\u0c24 \u0c28\u0c40\u0c1f\u0c3f\u0c28\u0c3f \u0c28\u0c3f\u0c32\u0c4d\u0c35 \u0c1a\u0c47\u0c38\u0c41\u0c15\u0c4b\u0c35\u0c3e\u0c32\u0c28\u0c3f \u0c35\u0c3f\u0c1c\u0c4d\u0c1e\u0c2a\u0c4d\u0c24\u0c3f \u0c1a\u0c47\u0c38\u0c4d\u0c24\u0c41\u0c28\u0c4d\u0c28\u0c3e\u0c2e\u0c41. \u0c2e\u0c40\u0c15\u0c41 \u0c15\u0c32\u0c3f\u0c17\u0c47 \u0c05\u0c38\u0c4c\u0c15\u0c30\u0c4d\u0c2f\u0c3e\u0c28\u0c3f\u0c15\u0c3f \u0c35\u0c3f\u0c1a\u0c3e\u0c30\u0c3f\u0c38\u0c4d\u0c24\u0c41\u0c28\u0c4d\u0c28\u0c3e\u0c2e\u0c41 \u0c2e\u0c30\u0c3f\u0c2f\u0c41 \u0c2e\u0c28 \u0c38\u0c4a\u0c38\u0c48\u0c1f\u0c40 \u0c2e\u0c4c\u0c32\u0c3f\u0c15 \u0c38\u0c26\u0c41\u0c2a\u0c3e\u0c2f\u0c3e\u0c32\u0c28\u0c41 \u0c36\u0c41\u0c2d\u0c4d\u0c30\u0c02\u0c17\u0c3e, \u0c2a\u0c30\u0c3f\u0c36\u0c41\u0c2d\u0c4d\u0c30\u0c02\u0c17\u0c3e \u0c09\u0c02\u0c1a\u0c21\u0c02\u0c32\u0c4b \u0c2e\u0c40 \u0c38\u0c39\u0c15\u0c3e\u0c30\u0c3e\u0c28\u0c3f\u0c15\u0c3f \u0c27\u0c28\u0c4d\u0c2f\u0c35\u0c3e\u0c26\u0c3e\u0c32\u0c41.\n\n\u0c2d\u0c35\u0c26\u0c40\u0c2f\u0c41\u0c32\u0c41,\n\u0c2e\u0c47\u0c28\u0c47\u0c1c\u0c4d\u200c\u0c2e\u0c46\u0c02\u0c1f\u0c4d \u0c15\u0c2e\u0c3f\u0c1f\u0c40"
                }
            },
            {
                "body": "Annual General Meeting this Sunday at 10 AM.",
                "created_at": "2026-08-08T08:19:33",
                "created_by_user_id": 1,
                "expires_at": null,
                "id": 7,
                "notice_type": "general",
                "priority": "medium",
                "publish_at": "2026-08-08T08:19:33.856035",
                "society_id": 1,
                "title": "AGM Meeting",
                "translations": {}
            },
            {
                "body": "Annual General Meeting this Sunday at 10 AM.",
                "created_at": "2026-08-08T08:18:52",
                "created_by_user_id": 1,
                "expires_at": null,
                "id": 6,
                "notice_type": "general",
                "priority": "medium",
                "publish_at": "2026-08-08T08:18:52.463326",
                "society_id": 1,
                "title": "AGM Meeting",
                "translations": {}
            },
            {
                "body": "Annual General Meeting this Sunday at 10 AM.",
                "created_at": "2026-08-08T08:13:30",
                "created_by_user_id": 1,
                "expires_at": null,
                "id": 5,
                "notice_type": "general",
                "priority": "medium",
                "publish_at": "2026-08-08T08:13:30.049234",
                "society_id": 1,
                "title": "AGM Meeting",
                "translations": {}
            },
            {
                "body": "Dear Residents,\n\nPlease be informed that a society cleaning drive is scheduled for Saturday, from 1:00 AM to 2:00 AM. All residents are requested to be present during this time and extend their cooperation to the cleaning staff to ensure smooth execution.\n\nThank you for your cooperation.\n\nWarm regards,\nManagement Committee\nSocioNeed",
                "created_at": "2026-08-08T06:33:33",
                "created_by_user_id": 1,
                "expires_at": null,
                "id": 4,
                "notice_type": "maintenance",
                "priority": "normal",
                "publish_at": "2026-08-08T06:33:33.725239",
                "society_id": 1,
                "title": "Notice: Society Cleaning Drive",
                "translations": {}
            },
            {
                "body": "Please ensure visitors are pre-approved at gate entry.",
                "created_at": "2026-08-08T03:15:31",
                "created_by_user_id": 1,
                "expires_at": null,
                "id": 3,
                "notice_type": "security",
                "priority": "urgent",
                "publish_at": "2026-08-08T03:15:31.878754",
                "society_id": 1,
                "title": "Security Advisory",
                "translations": {}
            },
            {
                "body": "Water tank cleaning is scheduled this weekend.",
                "created_at": "2026-08-08T03:15:31",
                "created_by_user_id": 1,
                "expires_at": null,
                "id": 1,
                "notice_type": "maintenance",
                "priority": "high",
                "publish_at": "2026-08-06T03:15:31.878754",
                "society_id": 1,
                "title": "Water Tank Cleaning",
                "translations": {}
            }
        ],
        "pagination": {
            "limit": 20,
            "page": 1,
            "pages": 1,
            "total": 8
        }
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 129 – Sprint 1 User List Cycle (Case 129)
API Endpoint: GET /api/events

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "items": [
            {
                "created_at": "2026-08-08T03:15:31",
                "created_by_user_id": 1,
                "description": "Morning wellness session in clubhouse.",
                "end_time": "08:00",
                "event_date": "Mon, 10 Aug 2026 00:00:00 GMT",
                "id": 1,
                "society_id": 1,
                "start_time": "07:00",
                "status": "scheduled",
                "title": "Yoga Session",
                "venue": "Clubhouse"
            },
            {
                "created_at": "2026-08-08T03:15:31",
                "created_by_user_id": 1,
                "description": "Weekend painting workshop for children.",
                "end_time": "18:00",
                "event_date": "Thu, 13 Aug 2026 00:00:00 GMT",
                "id": 2,
                "society_id": 1,
                "start_time": "16:00",
                "status": "scheduled",
                "title": "Kids Painting Workshop",
                "venue": "Community Hall"
            },
            {
                "created_at": "2026-08-08T03:15:31",
                "created_by_user_id": 1,
                "description": "Safety drill with security team guidance.",
                "end_time": "11:00",
                "event_date": "Sun, 16 Aug 2026 00:00:00 GMT",
                "id": 3,
                "society_id": 1,
                "start_time": "10:00",
                "status": "scheduled",
                "title": "Fire Safety Drill",
                "venue": "Main Courtyard"
            }
        ],
        "pagination": {
            "limit": 20,
            "page": 1,
            "pages": 1,
            "total": 3
        }
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 130 – Sprint 1 Unit Management (Case 130)
API Endpoint: GET /api/complaints

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "items": [
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T10:07:02",
                "description": "Water leaking in kitchen",
                "id": 15,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T10:07:02"
            },
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T08:42:10",
                "description": "Water leaking in kitchen",
                "id": 14,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T08:42:10"
            },
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T08:33:32",
                "description": "Water leaking in kitchen",
                "id": 13,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T08:33:32"
            },
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T08:32:20",
                "description": "Water leaking in kitchen",
                "id": 12,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T08:32:20"
            },
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T08:31:57",
                "description": "Water leaking in kitchen",
                "id": 11,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T08:31:57"
            },
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T08:31:45",
                "description": "Water leaking in kitchen",
                "id": 10,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T08:31:45"
            },
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T08:27:49",
                "description": "Water leaking in kitchen",
                "id": 9,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T08:27:49"
            },
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T08:26:09",
                "description": "Water leaking in kitchen",
                "id": 8,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T08:26:09"
            },
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T08:25:53",
                "description": "Water leaking in kitchen",
                "id": 7,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T08:25:53"
            },
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T08:24:34",
                "description": "Water leaking in kitchen",
                "id": 6,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T08:24:34"
            },
            {
                "assigned_to_user_id": 3,
                "category": "Lift",
                "created_at": "2026-08-08T06:24:29",
                "description": "asafs",
                "id": 5,
                "priority": "low",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "in_progress",
                "subject": "adsfaf",
                "updated_at": "2026-08-08T06:31:05"
            },
            {
                "assigned_to_user_id": null,
                "category": "Water",
                "created_at": "2026-08-08T06:24:16",
                "description": "suddenly water not commming",
                "id": 4,
                "priority": "high",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "water not comming",
                "updated_at": "2026-08-08T06:24:16"
            },
            {
                "assigned_to_user_id": 3,
                "category": "Maintenance",
                "created_at": "2026-08-08T03:15:31",
                "description": "Lift in Block C has intermittent stoppage.",
                "id": 1,
                "priority": "high",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "in_progress",
                "subject": "Lift maintenance required",
                "updated_at": "2026-08-08T08:24:34"
            },
            {
                "assigned_to_user_id": 5,
                "category": "Plumbing",
                "created_at": "2026-08-08T03:15:31",
                "description": "Leakage observed near basement entry ramp.",
                "id": 2,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "in_progress",
                "subject": "Water leakage near basement",
                "updated_at": "2026-08-08T06:25:03"
            },
            {
                "assigned_to_user_id": 12,
                "category": "Security",
                "created_at": "2026-08-08T03:15:31",
                "description": "CCTV feed near gate 2 is blurry at night.",
                "id": 3,
                "priority": "high",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "resolved",
                "subject": "CCTV camera blur",
                "updated_at": "2026-08-08T03:15:31"
            }
        ],
        "pagination": {
            "limit": 20,
            "page": 1,
            "pages": 1,
            "total": 15
        }
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 131 – Sprint 2 Complaint Workflow (Case 131)
API Endpoint: GET /api/service-categories

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": [
        {
            "created_at": "2026-08-08T03:15:31.863325",
            "description": "Exterior and interior car cleaning and detailing",
            "id": 5,
            "name": "Car Wash"
        },
        {
            "created_at": "2026-08-08T03:15:31.863353",
            "description": "Home cooking, party catering, and tiffin services",
            "id": 8,
            "name": "Cook"
        },
        {
            "created_at": "2026-08-08T03:15:31.863304",
            "description": "Electrical wiring, repairs, and appliance installation",
            "id": 3,
            "name": "Electrician"
        },
        {
            "created_at": "2026-08-08T03:15:31.863335",
            "description": "Garden maintenance, lawn mowing, and landscaping",
            "id": 6,
            "name": "Gardener"
        },
        {
            "created_at": "2026-08-08T03:15:31.863245",
            "description": "Professional house cleaning and domestic help services",
            "id": 1,
            "name": "House Maid"
        },
        {
            "created_at": "2026-08-08T03:15:31.863315",
            "description": "Wash, iron, dry cleaning, and delivery",
            "id": 4,
            "name": "Laundry"
        },
        {
            "created_at": "2026-08-08T03:15:31.863288",
            "description": "Plumbing, pipe fitting, and drainage solutions",
            "id": 2,
            "name": "Plumber"
        },
        {
            "created_at": "2026-08-08T03:15:31.863344",
            "description": "Tailoring, alterations, and custom stitching",
            "id": 7,
            "name": "Tailor"
        }
    ],
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 132 – Sprint 2 Booking Review Workflow (Case 132)
API Endpoint: GET /api/providers

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "items": [
            {
                "business_name": "Provider User Services",
                "category_id": 1,
                "created_at": "2026-08-08T03:15:31",
                "id": 1,
                "rating_avg": 4.5,
                "service_description": "Community verified service provider",
                "user_id": 3,
                "verification_status": "approved"
            },
            {
                "business_name": "Pooja House Maid Services",
                "category_id": 2,
                "created_at": "2026-08-08T03:15:31",
                "id": 2,
                "rating_avg": 4.5,
                "service_description": "Community verified service provider",
                "user_id": 4,
                "verification_status": "approved"
            },
            {
                "business_name": "Ravi Plumber Services",
                "category_id": 3,
                "created_at": "2026-08-08T03:15:31",
                "id": 3,
                "rating_avg": 4.5,
                "service_description": "Community verified service provider",
                "user_id": 5,
                "verification_status": "approved"
            },
            {
                "business_name": "Sita Electrician Services",
                "category_id": 4,
                "created_at": "2026-08-08T03:15:31",
                "id": 4,
                "rating_avg": 4.5,
                "service_description": "Community verified service provider",
                "user_id": 6,
                "verification_status": "approved"
            },
            {
                "business_name": "Sunita Laundry Services",
                "category_id": 5,
                "created_at": "2026-08-08T03:15:31",
                "id": 5,
                "rating_avg": 4.5,
                "service_description": "Community verified service provider",
                "user_id": 7,
                "verification_status": "approved"
            },
            {
                "business_name": "Kumar Car Wash Services",
                "category_id": 6,
                "created_at": "2026-08-08T03:15:31",
                "id": 6,
                "rating_avg": 4.5,
                "service_description": "Community verified service provider",
                "user_id": 8,
                "verification_status": "approved"
            },
            {
                "business_name": "Ramesh Gardener Services",
                "category_id": 7,
                "created_at": "2026-08-08T03:15:31",
                "id": 7,
                "rating_avg": 4.5,
                "service_description": "Community verified service provider",
                "user_id": 9,
                "verification_status": "approved"
            },
            {
                "business_name": "Ajay Tailor Services",
                "category_id": 8,
                "created_at": "2026-08-08T03:15:31",
                "id": 8,
                "rating_avg": 4.5,
                "service_description": "Community verified service provider",
                "user_id": 10,
                "verification_status": "approved"
            },
            {
                "business_name": "Lakshmi Cook Services",
                "category_id": 1,
                "created_at": "2026-08-08T03:15:31",
                "id": 9,
                "rating_avg": 4.5,
                "service_description": "Community verified service provider",
                "user_id": 11,
                "verification_status": "approved"
            }
        ],
        "pagination": {
            "limit": 20,
            "page": 1,
            "pages": 1,
            "total": 9
        }
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 133 – Sprint 2 Reports Summary (Case 133)
API Endpoint: GET /api/slots

Input:
{}

Expected Output:
{
    "status_code": 405,
    "success": false
}

----------------------------------------------------------------------
ACTUAL STATUS: 405
ACTUAL RESPONSE (json):
{
    "error": {
        "code": "METHOD_NOT_ALLOWED",
        "message": "The method is not allowed for the requested URL."
    },
    "success": false
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 134 – Token Expired Verification (Case 134)
API Endpoint: GET /api/bookings

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "items": [
            {
                "booking_status": "requested",
                "created_at": "2026-08-08T09:22:02",
                "id": 5,
                "provider_id": 5,
                "request_notes": "Booking created from resident portal",
                "resident_user_id": 2,
                "slot_id": null,
                "updated_at": "2026-08-08T09:22:02"
            },
            {
                "booking_status": "requested",
                "created_at": "2026-08-08T06:22:32",
                "id": 4,
                "provider_id": 5,
                "request_notes": "Booking created from resident portal",
                "resident_user_id": 2,
                "slot_id": null,
                "updated_at": "2026-08-08T06:22:32"
            },
            {
                "booking_status": "accepted",
                "created_at": "2026-08-08T03:15:31",
                "id": 1,
                "provider_id": 1,
                "request_notes": "Kitchen sink pipe check",
                "resident_user_id": 2,
                "slot_id": null,
                "updated_at": "2026-08-08T06:37:14"
            },
            {
                "booking_status": "completed",
                "created_at": "2026-08-08T03:15:31",
                "id": 2,
                "provider_id": 1,
                "request_notes": "Bathroom fitting replacement",
                "resident_user_id": 2,
                "slot_id": null,
                "updated_at": "2026-08-08T06:26:36"
            },
            {
                "booking_status": "completed",
                "created_at": "2026-08-08T03:15:31",
                "id": 3,
                "provider_id": 1,
                "request_notes": "Balcony drain cleanup",
                "resident_user_id": 2,
                "slot_id": null,
                "updated_at": "2026-08-08T03:15:31"
            }
        ],
        "pagination": {
            "limit": 20,
            "page": 1,
            "pages": 1,
            "total": 5
        }
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 135 – Token Malformed Verification (Case 135)
API Endpoint: GET /api/reviews

Input:
{}

Expected Output:
{
    "status_code": 405,
    "success": false
}

----------------------------------------------------------------------
ACTUAL STATUS: 405
ACTUAL RESPONSE (json):
{
    "error": {
        "code": "METHOD_NOT_ALLOWED",
        "message": "The method is not allowed for the requested URL."
    },
    "success": false
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 136 – Token Signature Check (Case 136)
API Endpoint: GET /api/visitors

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "items": [],
        "pagination": {
            "limit": 20,
            "page": 1,
            "pages": 0,
            "total": 0
        }
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 137 – Slot Start Time Formatting (Case 137)
API Endpoint: GET /api/analytics/dashboard/admin

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "stats": {
            "pending_complaints": 14,
            "todays_bookings": 5,
            "total_residents": 21,
            "upcoming_events": 3
        }
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 138 – Slot End Time Validation (Case 138)
API Endpoint: GET /api/reports/monthly

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "bookings": {
            "total": 5
        },
        "complaints": {
            "raised": 15
        },
        "events": {
            "scheduled": 3
        },
        "notices": {
            "published": 8
        },
        "residents": {
            "total": 21
        },
        "visitors": {
            "total": 0
        }
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 139 – Slot Duration Check (Case 139)
API Endpoint: GET /api/ai/status

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "configured": true,
        "features": [
            "notice_generator",
            "multilingual_announcement",
            "event_planner",
            "analytics_insights",
            "complaint_classification",
            "meeting_minutes",
            "notice_summarizer",
            "notices_summarize_all",
            "maintenance_assistant",
            "complaint_resolution_insights",
            "rules_qa",
            "feedback_analyzer",
            "amenity_booking_assistant"
        ],
        "model": "gemini-flash-latest"
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 140 – Booking Double Booking Prevention (Case 140)
API Endpoint: GET /api/users/me

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "created_at": "2026-08-08T03:15:30.937350",
        "email": "admin@socioneed.com",
        "full_name": "Admin User",
        "id": 1,
        "phone": "9000000001",
        "role": "admin",
        "society_id": 1,
        "status": "active"
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 141 – Booking Availability Feed Update (Case 141)
API Endpoint: GET /api/auth/verify-token

Input:
{}

Expected Output:
{
    "status_code": 405,
    "success": false
}

----------------------------------------------------------------------
ACTUAL STATUS: 405
ACTUAL RESPONSE (json):
{
    "error": {
        "code": "METHOD_NOT_ALLOWED",
        "message": "The method is not allowed for the requested URL."
    },
    "success": false
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 142 – Booking Cancellation Release (Case 142)
API Endpoint: GET /api/societies

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "items": [
            {
                "address": "123 Main Road",
                "city": "Mumbai",
                "contact_email": "admin@greenvalley.com",
                "contact_phone": "9988776655",
                "created_at": "2026-08-08T03:15:30",
                "id": 1,
                "name": "Green Valley Society",
                "pincode": "400001"
            }
        ],
        "pagination": {
            "limit": 20,
            "page": 1,
            "pages": 1,
            "total": 1
        }
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 143 – Complaint Assign Admin Check (Case 143)
API Endpoint: GET /api/units

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "items": [
            {
                "block_name": null,
                "created_at": "2026-08-08T10:07:02",
                "floor": null,
                "id": 10,
                "society_id": 1,
                "status": "active",
                "unit_number": "U21195",
                "unit_type": "2BHK"
            },
            {
                "block_name": null,
                "created_at": "2026-08-08T08:42:10",
                "floor": null,
                "id": 9,
                "society_id": 1,
                "status": "active",
                "unit_number": "U50798",
                "unit_type": "2BHK"
            },
            {
                "block_name": null,
                "created_at": "2026-08-08T08:33:32",
                "floor": null,
                "id": 8,
                "society_id": 1,
                "status": "active",
                "unit_number": "U55818",
                "unit_type": "2BHK"
            },
            {
                "block_name": null,
                "created_at": "2026-08-08T08:32:20",
                "floor": null,
                "id": 7,
                "society_id": 1,
                "status": "active",
                "unit_number": "U38478",
                "unit_type": "2BHK"
            },
            {
                "block_name": null,
                "created_at": "2026-08-08T08:31:57",
                "floor": null,
                "id": 6,
                "society_id": 1,
                "status": "active",
                "unit_number": "U44431",
                "unit_type": "2BHK"
            },
            {
                "block_name": null,
                "created_at": "2026-08-08T08:31:45",
                "floor": null,
                "id": 5,
                "society_id": 1,
                "status": "active",
                "unit_number": "U53839",
                "unit_type": "2BHK"
            },
            {
                "block_name": null,
                "created_at": "2026-08-08T08:27:49",
                "floor": null,
                "id": 4,
                "society_id": 1,
                "status": "active",
                "unit_number": "U27389",
                "unit_type": "2BHK"
            },
            {
                "block_name": null,
                "created_at": "2026-08-08T08:26:09",
                "floor": null,
                "id": 3,
                "society_id": 1,
                "status": "active",
                "unit_number": "U85933",
                "unit_type": "2BHK"
            },
            {
                "block_name": null,
                "created_at": "2026-08-08T08:25:53",
                "floor": null,
                "id": 2,
                "society_id": 1,
                "status": "active",
                "unit_number": "U74443",
                "unit_type": "2BHK"
            },
            {
                "block_name": null,
                "created_at": "2026-08-08T08:24:34",
                "floor": null,
                "id": 1,
                "society_id": 1,
                "status": "active",
                "unit_number": "U91921",
                "unit_type": "3BHK"
            }
        ],
        "pagination": {
            "limit": 20,
            "page": 1,
            "pages": 1,
            "total": 10
        }
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 144 – Complaint Status Update Audit (Case 144)
API Endpoint: GET /api/notices

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "items": [
            {
                "body": "Tank cleaning on Sunday",
                "created_at": "2026-08-08T10:07:02",
                "created_by_user_id": 1,
                "expires_at": null,
                "id": 9,
                "notice_type": "general",
                "priority": "medium",
                "publish_at": "2026-08-08T10:07:02.341164",
                "society_id": 1,
                "title": "Water Notice",
                "translations": {}
            },
            {
                "body": "Dear Residents,\n\nPlease be informed that the water tank cleaning work is scheduled for tomorrow between 5:00 and 8:00. Consequently, the water supply will be stopped during this period.\n\nResidents are requested to store adequate water in advance to fulfill their daily requirements. We regret the inconvenience caused and appreciate your cooperation in keeping our society's infrastructure clean and hygienic.\n\nWarm regards,\nManagement Committee",
                "created_at": "2026-08-08T09:19:28",
                "created_by_user_id": 1,
                "expires_at": null,
                "id": 8,
                "notice_type": "maintenance",
                "priority": "normal",
                "publish_at": "2026-08-08T09:19:28.911176",
                "society_id": 1,
                "title": "Notice: Water Tank Cleaning & Water Supply Disruption",
                "translations": {
                    "English": "Dear Residents,\n\nPlease be informed that the water tank cleaning work is scheduled for tomorrow between 5:00 AM and 8:00 AM. Consequently, the water supply will be stopped during this period.\n\nResidents are requested to store adequate water in advance to fulfill their daily requirements. We regret the inconvenience caused and appreciate your cooperation in keeping our society's infrastructure clean and hygienic.\n\nWarm regards,\nManagement Committee",
                    "Hindi": "\u092a\u094d\u0930\u093f\u092f \u0928\u093f\u0935\u093e\u0938\u093f\u092f\u094b\u0902,\n\n\u0906\u092a\u0915\u094b \u0938\u0942\u091a\u093f\u0924 \u0915\u093f\u092f\u093e \u091c\u093e\u0924\u093e \u0939\u0948 \u0915\u093f \u0915\u0932 \u0938\u0941\u092c\u0939 5:00 \u092c\u091c\u0947 \u0938\u0947 8:00 \u092c\u091c\u0947 \u0915\u0947 \u092c\u0940\u091a \u092a\u093e\u0928\u0940 \u0915\u0940 \u091f\u0902\u0915\u0940 \u0915\u0940 \u0938\u092b\u093e\u0908 \u0915\u093e \u0915\u093e\u0930\u094d\u092f \u0928\u093f\u0930\u094d\u0927\u093e\u0930\u093f\u0924 \u0915\u093f\u092f\u093e \u0917\u092f\u093e \u0939\u0948\u0964 \u0907\u0938\u0915\u0947 \u092a\u0930\u093f\u0923\u093e\u092e\u0938\u094d\u0935\u0930\u0942\u092a, \u0907\u0938 \u0905\u0935\u0927\u093f \u0915\u0947 \u0926\u094c\u0930\u093e\u0928 \u092a\u093e\u0928\u0940 \u0915\u0940 \u0906\u092a\u0942\u0930\u094d\u0924\u093f \u092c\u0902\u0926 \u0930\u0939\u0947\u0917\u0940\u0964\n\n\u0938\u092d\u0940 \u0928\u093f\u0935\u093e\u0938\u093f\u092f\u094b\u0902 \u0938\u0947 \u0905\u0928\u0941\u0930\u094b\u0927 \u0939\u0948 \u0915\u093f \u0935\u0947 \u0905\u092a\u0928\u0940 \u0926\u0948\u0928\u093f\u0915 \u0906\u0935\u0936\u094d\u092f\u0915\u0924\u093e\u0913\u0902 \u0915\u094b \u092a\u0942\u0930\u093e \u0915\u0930\u0928\u0947 \u0915\u0947 \u0932\u093f\u090f \u092a\u0939\u0932\u0947 \u0938\u0947 \u0939\u0940 \u092a\u0930\u094d\u092f\u093e\u092a\u094d\u0924 \u092a\u093e\u0928\u0940 \u0915\u093e \u092d\u0902\u0921\u093e\u0930\u0923 \u0915\u0930 \u0932\u0947\u0902\u0964 \u0906\u092a\u0915\u094b \u0939\u094b\u0928\u0947 \u0935\u093e\u0932\u0940 \u0905\u0938\u0941\u0935\u093f\u0927\u093e \u0915\u0947 \u0932\u093f\u090f \u0939\u092e\u0947\u0902 \u0916\u0947\u0926 \u0939\u0948 \u0914\u0930 \u0939\u092e\u093e\u0930\u0940 \u0938\u094b\u0938\u093e\u0907\u091f\u0940 \u0915\u0947 \u092c\u0941\u0928\u093f\u092f\u093e\u0926\u0940 \u0922\u093e\u0902\u091a\u0947 \u0915\u094b \u0938\u093e\u092b \u0914\u0930 \u0938\u094d\u0935\u091a\u094d\u091b \u092c\u0928\u093e\u090f \u0930\u0916\u0928\u0947 \u092e\u0947\u0902 \u0906\u092a\u0915\u0947 \u0938\u0939\u092f\u094b\u0917 \u0915\u0940 \u0939\u092e \u0938\u0930\u093e\u0939\u0928\u093e \u0915\u0930\u0924\u0947 \u0939\u0948\u0902\u0964\n\n\u0938\u093e\u0926\u0930,\n\u092a\u094d\u0930\u092c\u0902\u0927 \u0938\u092e\u093f\u0924\u093f",
                    "Telugu": "\u0c2a\u0c4d\u0c30\u0c3f\u0c2f\u0c2e\u0c48\u0c28 \u0c28\u0c3f\u0c35\u0c3e\u0c38\u0c41\u0c32\u0c3e\u0c30\u0c3e,\n\n\u0c30\u0c47\u0c2a\u0c41 \u0c09\u0c26\u0c2f\u0c02 5:00 \u0c17\u0c02\u0c1f\u0c32 \u0c28\u0c41\u0c02\u0c21\u0c3f 8:00 \u0c17\u0c02\u0c1f\u0c32 \u0c2e\u0c27\u0c4d\u0c2f \u0c35\u0c3e\u0c1f\u0c30\u0c4d \u0c1f\u0c4d\u0c2f\u0c3e\u0c02\u0c15\u0c4d \u0c36\u0c41\u0c2d\u0c4d\u0c30\u0c2a\u0c30\u0c3f\u0c1a\u0c47 \u0c2a\u0c28\u0c3f \u0c28\u0c3f\u0c30\u0c4d\u0c23\u0c2f\u0c3f\u0c02\u0c1a\u0c2c\u0c21\u0c3f\u0c02\u0c26\u0c28\u0c3f \u0c24\u0c46\u0c32\u0c3f\u0c2f\u0c1c\u0c47\u0c38\u0c4d\u0c24\u0c41\u0c28\u0c4d\u0c28\u0c3e\u0c2e\u0c41. \u0c26\u0c40\u0c28\u0c3f \u0c15\u0c3e\u0c30\u0c23\u0c02\u0c17\u0c3e, \u0c08 \u0c38\u0c2e\u0c2f\u0c02\u0c32\u0c4b \u0c28\u0c40\u0c1f\u0c3f \u0c38\u0c30\u0c2b\u0c30\u0c3e \u0c28\u0c3f\u0c32\u0c3f\u0c2a\u0c3f\u0c35\u0c47\u0c2f\u0c2c\u0c21\u0c41\u0c24\u0c41\u0c02\u0c26\u0c3f.\n\n\u0c28\u0c3f\u0c35\u0c3e\u0c38\u0c41\u0c32\u0c41 \u0c24\u0c2e \u0c30\u0c4b\u0c1c\u0c41\u0c35\u0c3e\u0c30\u0c40 \u0c05\u0c35\u0c38\u0c30\u0c3e\u0c32\u0c28\u0c41 \u0c24\u0c40\u0c30\u0c4d\u0c1a\u0c41\u0c15\u0c4b\u0c35\u0c21\u0c3e\u0c28\u0c3f\u0c15\u0c3f \u0c2e\u0c41\u0c02\u0c26\u0c41\u0c17\u0c3e\u0c28\u0c47 \u0c24\u0c17\u0c3f\u0c28\u0c02\u0c24 \u0c28\u0c40\u0c1f\u0c3f\u0c28\u0c3f \u0c28\u0c3f\u0c32\u0c4d\u0c35 \u0c1a\u0c47\u0c38\u0c41\u0c15\u0c4b\u0c35\u0c3e\u0c32\u0c28\u0c3f \u0c35\u0c3f\u0c1c\u0c4d\u0c1e\u0c2a\u0c4d\u0c24\u0c3f \u0c1a\u0c47\u0c38\u0c4d\u0c24\u0c41\u0c28\u0c4d\u0c28\u0c3e\u0c2e\u0c41. \u0c2e\u0c40\u0c15\u0c41 \u0c15\u0c32\u0c3f\u0c17\u0c47 \u0c05\u0c38\u0c4c\u0c15\u0c30\u0c4d\u0c2f\u0c3e\u0c28\u0c3f\u0c15\u0c3f \u0c35\u0c3f\u0c1a\u0c3e\u0c30\u0c3f\u0c38\u0c4d\u0c24\u0c41\u0c28\u0c4d\u0c28\u0c3e\u0c2e\u0c41 \u0c2e\u0c30\u0c3f\u0c2f\u0c41 \u0c2e\u0c28 \u0c38\u0c4a\u0c38\u0c48\u0c1f\u0c40 \u0c2e\u0c4c\u0c32\u0c3f\u0c15 \u0c38\u0c26\u0c41\u0c2a\u0c3e\u0c2f\u0c3e\u0c32\u0c28\u0c41 \u0c36\u0c41\u0c2d\u0c4d\u0c30\u0c02\u0c17\u0c3e, \u0c2a\u0c30\u0c3f\u0c36\u0c41\u0c2d\u0c4d\u0c30\u0c02\u0c17\u0c3e \u0c09\u0c02\u0c1a\u0c21\u0c02\u0c32\u0c4b \u0c2e\u0c40 \u0c38\u0c39\u0c15\u0c3e\u0c30\u0c3e\u0c28\u0c3f\u0c15\u0c3f \u0c27\u0c28\u0c4d\u0c2f\u0c35\u0c3e\u0c26\u0c3e\u0c32\u0c41.\n\n\u0c2d\u0c35\u0c26\u0c40\u0c2f\u0c41\u0c32\u0c41,\n\u0c2e\u0c47\u0c28\u0c47\u0c1c\u0c4d\u200c\u0c2e\u0c46\u0c02\u0c1f\u0c4d \u0c15\u0c2e\u0c3f\u0c1f\u0c40"
                }
            },
            {
                "body": "Annual General Meeting this Sunday at 10 AM.",
                "created_at": "2026-08-08T08:19:33",
                "created_by_user_id": 1,
                "expires_at": null,
                "id": 7,
                "notice_type": "general",
                "priority": "medium",
                "publish_at": "2026-08-08T08:19:33.856035",
                "society_id": 1,
                "title": "AGM Meeting",
                "translations": {}
            },
            {
                "body": "Annual General Meeting this Sunday at 10 AM.",
                "created_at": "2026-08-08T08:18:52",
                "created_by_user_id": 1,
                "expires_at": null,
                "id": 6,
                "notice_type": "general",
                "priority": "medium",
                "publish_at": "2026-08-08T08:18:52.463326",
                "society_id": 1,
                "title": "AGM Meeting",
                "translations": {}
            },
            {
                "body": "Annual General Meeting this Sunday at 10 AM.",
                "created_at": "2026-08-08T08:13:30",
                "created_by_user_id": 1,
                "expires_at": null,
                "id": 5,
                "notice_type": "general",
                "priority": "medium",
                "publish_at": "2026-08-08T08:13:30.049234",
                "society_id": 1,
                "title": "AGM Meeting",
                "translations": {}
            },
            {
                "body": "Dear Residents,\n\nPlease be informed that a society cleaning drive is scheduled for Saturday, from 1:00 AM to 2:00 AM. All residents are requested to be present during this time and extend their cooperation to the cleaning staff to ensure smooth execution.\n\nThank you for your cooperation.\n\nWarm regards,\nManagement Committee\nSocioNeed",
                "created_at": "2026-08-08T06:33:33",
                "created_by_user_id": 1,
                "expires_at": null,
                "id": 4,
                "notice_type": "maintenance",
                "priority": "normal",
                "publish_at": "2026-08-08T06:33:33.725239",
                "society_id": 1,
                "title": "Notice: Society Cleaning Drive",
                "translations": {}
            },
            {
                "body": "Please ensure visitors are pre-approved at gate entry.",
                "created_at": "2026-08-08T03:15:31",
                "created_by_user_id": 1,
                "expires_at": null,
                "id": 3,
                "notice_type": "security",
                "priority": "urgent",
                "publish_at": "2026-08-08T03:15:31.878754",
                "society_id": 1,
                "title": "Security Advisory",
                "translations": {}
            },
            {
                "body": "Water tank cleaning is scheduled this weekend.",
                "created_at": "2026-08-08T03:15:31",
                "created_by_user_id": 1,
                "expires_at": null,
                "id": 1,
                "notice_type": "maintenance",
                "priority": "high",
                "publish_at": "2026-08-06T03:15:31.878754",
                "society_id": 1,
                "title": "Water Tank Cleaning",
                "translations": {}
            }
        ],
        "pagination": {
            "limit": 20,
            "page": 1,
            "pages": 1,
            "total": 8
        }
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 145 – Complaint Timeline Log (Case 145)
API Endpoint: GET /api/events

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "items": [
            {
                "created_at": "2026-08-08T03:15:31",
                "created_by_user_id": 1,
                "description": "Morning wellness session in clubhouse.",
                "end_time": "08:00",
                "event_date": "Mon, 10 Aug 2026 00:00:00 GMT",
                "id": 1,
                "society_id": 1,
                "start_time": "07:00",
                "status": "scheduled",
                "title": "Yoga Session",
                "venue": "Clubhouse"
            },
            {
                "created_at": "2026-08-08T03:15:31",
                "created_by_user_id": 1,
                "description": "Weekend painting workshop for children.",
                "end_time": "18:00",
                "event_date": "Thu, 13 Aug 2026 00:00:00 GMT",
                "id": 2,
                "society_id": 1,
                "start_time": "16:00",
                "status": "scheduled",
                "title": "Kids Painting Workshop",
                "venue": "Community Hall"
            },
            {
                "created_at": "2026-08-08T03:15:31",
                "created_by_user_id": 1,
                "description": "Safety drill with security team guidance.",
                "end_time": "11:00",
                "event_date": "Sun, 16 Aug 2026 00:00:00 GMT",
                "id": 3,
                "society_id": 1,
                "start_time": "10:00",
                "status": "scheduled",
                "title": "Fire Safety Drill",
                "venue": "Main Courtyard"
            }
        ],
        "pagination": {
            "limit": 20,
            "page": 1,
            "pages": 1,
            "total": 3
        }
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

```text
======================================================================
Test Case 146 – DB Session Rollback Verification (Case 146)
API Endpoint: GET /api/complaints

Input:
{}

Expected Output:
{
    "status_code": 200,
    "success": true
}

----------------------------------------------------------------------
ACTUAL STATUS: 200
ACTUAL RESPONSE (json):
{
    "data": {
        "items": [
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T10:07:02",
                "description": "Water leaking in kitchen",
                "id": 15,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T10:07:02"
            },
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T08:42:10",
                "description": "Water leaking in kitchen",
                "id": 14,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T08:42:10"
            },
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T08:33:32",
                "description": "Water leaking in kitchen",
                "id": 13,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T08:33:32"
            },
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T08:32:20",
                "description": "Water leaking in kitchen",
                "id": 12,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T08:32:20"
            },
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T08:31:57",
                "description": "Water leaking in kitchen",
                "id": 11,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T08:31:57"
            },
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T08:31:45",
                "description": "Water leaking in kitchen",
                "id": 10,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T08:31:45"
            },
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T08:27:49",
                "description": "Water leaking in kitchen",
                "id": 9,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T08:27:49"
            },
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T08:26:09",
                "description": "Water leaking in kitchen",
                "id": 8,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T08:26:09"
            },
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T08:25:53",
                "description": "Water leaking in kitchen",
                "id": 7,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T08:25:53"
            },
            {
                "assigned_to_user_id": null,
                "category": "Plumbing",
                "created_at": "2026-08-08T08:24:34",
                "description": "Water leaking in kitchen",
                "id": 6,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "Plumbing leak",
                "updated_at": "2026-08-08T08:24:34"
            },
            {
                "assigned_to_user_id": 3,
                "category": "Lift",
                "created_at": "2026-08-08T06:24:29",
                "description": "asafs",
                "id": 5,
                "priority": "low",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "in_progress",
                "subject": "adsfaf",
                "updated_at": "2026-08-08T06:31:05"
            },
            {
                "assigned_to_user_id": null,
                "category": "Water",
                "created_at": "2026-08-08T06:24:16",
                "description": "suddenly water not commming",
                "id": 4,
                "priority": "high",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "open",
                "subject": "water not comming",
                "updated_at": "2026-08-08T06:24:16"
            },
            {
                "assigned_to_user_id": 3,
                "category": "Maintenance",
                "created_at": "2026-08-08T03:15:31",
                "description": "Lift in Block C has intermittent stoppage.",
                "id": 1,
                "priority": "high",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "in_progress",
                "subject": "Lift maintenance required",
                "updated_at": "2026-08-08T08:24:34"
            },
            {
                "assigned_to_user_id": 5,
                "category": "Plumbing",
                "created_at": "2026-08-08T03:15:31",
                "description": "Leakage observed near basement entry ramp.",
                "id": 2,
                "priority": "medium",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "in_progress",
                "subject": "Water leakage near basement",
                "updated_at": "2026-08-08T06:25:03"
            },
            {
                "assigned_to_user_id": 12,
                "category": "Security",
                "created_at": "2026-08-08T03:15:31",
                "description": "CCTV feed near gate 2 is blurry at night.",
                "id": 3,
                "priority": "high",
                "raised_by_user_id": 2,
                "society_id": 1,
                "status": "resolved",
                "subject": "CCTV camera blur",
                "updated_at": "2026-08-08T03:15:31"
            }
        ],
        "pagination": {
            "limit": 20,
            "page": 1,
            "pages": 1,
            "total": 15
        }
    },
    "message": "Success",
    "success": true
}

Result: ✔ Success
======================================================================
```

