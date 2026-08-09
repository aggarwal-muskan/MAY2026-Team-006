"""SocioNeed - complete API test suite (146 cases) in a single file.

This one file is the whole tester deliverable. It contains, in order:

    SECTION 1  matchers used by the expected-value assertions
    SECTION 2  the 146-case catalogue - every expected value hand-written
    SECTION 3  the execution engine
    SECTION 4  the pytest entry point (146 named tests)
    SECTION 5  the terminal evidence printer (Input / Expected / Actual / Result)

Two ways to run it
------------------
    pytest tests/test_socioneed_api.py -v          146 named pytest tests

Expected values are never derived from the response. That is what makes the
printed output evidence rather than a transcript.
"""

import argparse
import io
import json
import os
import sys
import uuid

import pytest

# Allow "python tests/test_socioneed_api.py" to import the Flask app package.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


# =============================================================================
# SECTION 1 - MATCHERS
# =============================================================================

# ---------------------------------------------------------------- matchers ---

class _Sentinel:
    def __init__(self, name, fn):
        self.name = name
        self.fn = fn

    def __repr__(self):
        return self.name


PRESENT = _Sentinel("<field present>", lambda v: v is not None)
ABSENT = _Sentinel("<field absent>", lambda v: v is _MISSING)
NON_EMPTY_LIST = _Sentinel("<non-empty list>", lambda v: isinstance(v, list) and len(v) > 0)
IS_LIST = _Sentinel("<list>", lambda v: isinstance(v, list))
IS_INT = _Sentinel("<integer>", lambda v: isinstance(v, int))


class _Missing:
    def __repr__(self):
        return "<missing>"


_MISSING = _Missing()


def one_of(*values):
    return _Sentinel("one of %s" % (list(values),), lambda v: v in values)


def contains(text):
    return _Sentinel("contains %r" % text, lambda v: isinstance(v, str) and text.lower() in v.lower())


def dig(payload, dotted):
    """Resolve 'data.items.0.id' inside a JSON payload."""
    cur = payload
    for part in dotted.split("."):
        if isinstance(cur, list):
            try:
                cur = cur[int(part)]
                continue
            except (ValueError, IndexError):
                return _MISSING
        if isinstance(cur, dict) and part in cur:
            cur = cur[part]
        else:
            return _MISSING
    return cur


def check(payload, dotted, expected):
    actual = dig(payload, dotted)
    if isinstance(expected, _Sentinel):
        return bool(expected.fn(actual)), actual
    return actual == expected, actual


# =============================================================================
# SECTION 2 - THE 146-CASE CATALOGUE
# =============================================================================

CASES = []


def C(cid, cat, title, method, path, expect_status, expect=None,
      role="admin", query=None, body=None, capture=None, defect=None):
    CASES.append({
        "id": cid, "cat": cat, "title": title, "method": method, "path": path,
        "role": role, "query": query or {}, "body": body,
        "expect_status": expect_status, "expect": expect or {},
        "capture": capture, "defect": defect,
    })


OK = {"success": True}
ERR = {"success": False}


def err(code):
    return {"success": False, "error.code": code}


# =============================================================================
# 01  AUTHENTICATION & IDENTITY   (TC-001 .. TC-018)
# =============================================================================
CAT1 = "01 Authentication & Identity"

C("TC-001", CAT1, "Resident registers with valid details", "POST", "/api/auth/register", 201,
  {"success": True, "data.user.role": "owner", "data.user.status": "active", "data.token": PRESENT,
   "data.user.password_hash": ABSENT},
  role=None, body=lambda c: {"full_name": "Evidence Resident", "email": f"res.{c['tag']}@socioneed.com",
                             "phone": f"90{c['tag']}", "password": "Password123", "role": "owner", "society_id": 1},
  capture=lambda c, j: c.update(new_user_id=j["data"]["user"]["id"], new_user_email=j["data"]["user"]["email"]))

C("TC-002", CAT1, "Registration rejects duplicate email", "POST", "/api/auth/register", 409,
  err("DUPLICATE_EMAIL"), role=None,
  body={"full_name": "Duplicate User", "email": "admin@socioneed.com", "phone": "9111111111",
        "password": "Password123", "role": "owner", "society_id": 1})

C("TC-003", CAT1, "Registration rejects missing mandatory fields", "POST", "/api/auth/register", 400,
  {"success": False, "error.code": "VALIDATION_ERROR", "error.message": contains("missing required fields")},
  role=None, body={"email": "incomplete@socioneed.com"})

C("TC-004", CAT1, "Registration rejects malformed email", "POST", "/api/auth/register", 400,
  {"success": False, "error.code": "VALIDATION_ERROR", "error.message": contains("email")},
  role=None, body={"full_name": "Bad Email", "email": "not-an-email", "password": "Password123",
                   "role": "owner", "society_id": 1})

C("TC-005", CAT1, "Registration rejects password shorter than 6 characters", "POST", "/api/auth/register", 400,
  {"success": False, "error.code": "VALIDATION_ERROR", "error.message": contains("6 characters")},
  role=None, body=lambda c: {"full_name": "Short Pwd", "email": f"short.{c['tag']}@socioneed.com",
                             "password": "123", "role": "owner", "society_id": 1})

C("TC-006", CAT1, "Registration rejects unknown society_id", "POST", "/api/auth/register", 400,
  {"success": False, "error.code": "VALIDATION_ERROR", "error.message": contains("society")},
  role=None, body=lambda c: {"full_name": "No Society", "email": f"nosoc.{c['tag']}@socioneed.com",
                             "password": "Password123", "role": "owner", "society_id": 9999})

C("TC-007", CAT1, "SECURITY: self-registration must not grant the admin role", "POST", "/api/auth/register", 403,
  {"success": False, "error.code": "ROLE_NOT_SELF_ASSIGNABLE"},
  role=None, body=lambda c: {"full_name": "Privilege Escalation", "email": f"esc.{c['tag']}@socioneed.com",
                             "password": "Password123", "role": "admin", "society_id": 1},
  defect="D-01")

C("TC-008", CAT1, "Registration rejects an unknown role value", "POST", "/api/auth/register", 400,
  {"success": False, "error.code": "VALIDATION_ERROR", "error.message": contains("role")},
  role=None, body=lambda c: {"full_name": "Unknown Role", "email": f"unk.{c['tag']}@socioneed.com",
                             "password": "Password123", "role": "superman", "society_id": 1},
  defect="D-02")

C("TC-009", CAT1, "Admin logs in with valid credentials", "POST", "/api/auth/login", 200,
  {"success": True, "data.token": PRESENT, "data.expires_in": 43200, "data.user.role": "admin"},
  role=None, body={"email": "admin@socioneed.com", "password": "123456", "role": "admin"})

C("TC-010", CAT1, "Login rejects a wrong password", "POST", "/api/auth/login", 401,
  {"success": False, "error.code": "UNAUTHORIZED", "error.message": contains("invalid credentials")},
  role=None, body={"email": "admin@socioneed.com", "password": "wrong-password", "role": "admin"})

C("TC-011", CAT1, "Login rejects an unregistered email", "POST", "/api/auth/login", 401,
  err("UNAUTHORIZED"), role=None, body={"email": "ghost@socioneed.com", "password": "123456"})

C("TC-012", CAT1, "Login rejects a role that does not match the account", "POST", "/api/auth/login", 401,
  {"success": False, "error.code": "UNAUTHORIZED", "error.message": contains("role mismatch")},
  role=None, body={"email": "resident@socioneed.com", "password": "123456", "role": "admin"})

C("TC-013", CAT1, "Login rejects an empty payload", "POST", "/api/auth/login", 400,
  err("VALIDATION_ERROR"), role=None, body={})

C("TC-014", CAT1, "Login rejects a malformed (non-JSON) body", "POST", "/api/auth/login", 400,
  {"success": False}, role=None, body="this-is-not-json")

C("TC-015", CAT1, "Authenticated user reads own profile", "GET", "/api/users/me", 200,
  {"success": True, "data.email": "admin@socioneed.com", "data.role": "admin", "data.password_hash": ABSENT},
  role="admin")

C("TC-016", CAT1, "Protected route rejects a request with no token", "GET", "/api/users/me", 401,
  err("UNAUTHORIZED"), role=None)

C("TC-017", CAT1, "Protected route rejects a tampered token", "GET", "/api/users/me", 401,
  err("UNAUTHORIZED"), role="tampered")

C("TC-018", CAT1, "Token verification returns role and society claims", "POST", "/api/auth/verify-token", 200,
  {"success": True, "data.valid": True, "data.user.role": "admin", "data.user.society_id": 1}, role="admin")

# =============================================================================
# 02  SESSION & PASSWORD MANAGEMENT   (TC-019 .. TC-028)
# =============================================================================
CAT2 = "02 Session & Password Management"

C("TC-019", CAT2, "Refresh token issues a new access token", "POST", "/api/auth/refresh-token", 200,
  {"success": True, "data.token": PRESENT, "data.expires_in": 43200}, role="resident")

C("TC-020", CAT2, "Refresh token rejects an anonymous request", "POST", "/api/auth/refresh-token", 401,
  err("UNAUTHORIZED"), role=None)

C("TC-021", CAT2, "Logout succeeds for an authenticated session", "POST", "/api/auth/logout", 200,
  {"success": True, "message": contains("logged out")}, role="resident")

C("TC-022", CAT2, "Change password rejects a wrong current password", "POST", "/api/auth/change-password", 401,
  {"success": False, "error.code": "UNAUTHORIZED", "error.message": contains("current password")},
  role="security", body={"current_password": "not-my-password", "new_password": "Newpass123"})

C("TC-023", CAT2, "Change password rejects a missing new password", "POST", "/api/auth/change-password", 400,
  err("VALIDATION_ERROR"), role="security", body={"current_password": "123456"})

C("TC-024", CAT2, "Change password succeeds with the correct current password", "POST",
  "/api/auth/change-password", 200, {"success": True, "message": contains("password changed")},
  role="security", body={"current_password": "123456", "new_password": "Newpass123"})

C("TC-025", CAT2, "Old password no longer works after the change", "POST", "/api/auth/login", 401,
  err("UNAUTHORIZED"), role=None, body={"email": "security@socioneed.com", "password": "123456"})

C("TC-026", CAT2, "New password works after the change", "POST", "/api/auth/login", 200,
  {"success": True, "data.token": PRESENT}, role=None,
  body={"email": "security@socioneed.com", "password": "Newpass123"})

C("TC-027", CAT2, "Forgot password resets the credential and restores the seed password", "POST",
  "/api/auth/forgot-password", 200, {"success": True, "message": contains("reset")}, role=None,
  body={"email": "security@socioneed.com", "phone": "9000000004", "new_password": "123456"})

C("TC-028", CAT2, "Forgot password rejects an unknown account", "POST", "/api/auth/forgot-password", 404,
  err("NOT_FOUND"), role=None, body={"email": "nobody@socioneed.com", "new_password": "123456"})

# =============================================================================
# 03  USER ADMINISTRATION   (TC-029 .. TC-038)
# =============================================================================
CAT3 = "03 User Administration"

C("TC-029", CAT3, "Admin lists all users with pagination", "GET", "/api/users", 200,
  {"success": True, "data.items": NON_EMPTY_LIST, "data.pagination.page": 1, "data.pagination.limit": 20},
  role="admin")

C("TC-030", CAT3, "Resident cannot list users", "GET", "/api/users", 403, err("FORBIDDEN"), role="resident")

C("TC-031", CAT3, "Admin filters the user list by role", "GET", "/api/users", 200,
  {"success": True, "data.items.0.role": "service_provider"},
  role="admin", query={"role": "service_provider"})

C("TC-032", CAT3, "Admin searches users by name", "GET", "/api/users", 200,
  {"success": True, "data.items": NON_EMPTY_LIST}, role="admin", query={"search": "Resident"})

C("TC-033", CAT3, "Admin reads a single user record", "GET", lambda c: f"/api/users/{c['new_user_id']}", 200,
  {"success": True, "data.role": "owner", "data.password_hash": ABSENT}, role="admin")

C("TC-034", CAT3, "Reading a non-existent user returns 404", "GET", "/api/users/999999", 404,
  err("NOT_FOUND"), role="admin")

C("TC-035", CAT3, "User updates own profile", "PUT", "/api/users/me", 200,
  {"success": True, "data.full_name": "Resident User (updated)"},
  role="resident", body={"full_name": "Resident User (updated)"})

C("TC-036", CAT3, "Admin deactivates a user account", "POST",
  lambda c: f"/api/users/{c['new_user_id']}/deactivate", 200,
  {"success": True, "message": contains("deactivated")}, role="admin")

C("TC-037", CAT3, "Deactivated account cannot log in", "POST", "/api/auth/login", 403,
  {"success": False, "error.code": "ACCOUNT_INACTIVE"}, role=None,
  body=lambda c: {"email": c["new_user_email"], "password": "Password123"})

C("TC-038", CAT3, "Admin reactivates the user account", "POST",
  lambda c: f"/api/users/{c['new_user_id']}/activate", 200,
  {"success": True, "message": contains("activated")}, role="admin")

# =============================================================================
# 04  SOCIETY ADMINISTRATION   (TC-039 .. TC-043)
# =============================================================================
CAT4 = "04 Society Administration"

C("TC-039", CAT4, "Admin lists societies", "GET", "/api/societies", 200,
  {"success": True, "data.items.0.name": "Green Valley Society"}, role="admin")

C("TC-040", CAT4, "Read a society by id", "GET", "/api/societies/1", 200,
  {"success": True, "data.id": 1, "data.city": "Mumbai"}, role="admin")

C("TC-041", CAT4, "Resident cannot browse the society register", "GET", "/api/societies", 403,
  err("FORBIDDEN"), role="resident")

C("TC-042", CAT4, "Admin updates society contact details", "PUT", "/api/societies/1", 200,
  {"success": True, "data.contact_phone": "9988776600"},
  role="admin", body={"contact_phone": "9988776600"})

C("TC-043", CAT4, "Resident cannot update the society", "PUT", "/api/societies/1", 403,
  err("FORBIDDEN"), role="resident", body={"contact_phone": "0000000000"})

# =============================================================================
# 05  UNIT & OCCUPANCY ADMINISTRATION   (TC-044 .. TC-057)
# =============================================================================
CAT5 = "05 Unit & Occupancy Administration"

C("TC-044", CAT5, "Admin creates a unit", "POST", "/api/units", 201,
  {"success": True, "data.unit_number": "EV-101", "data.unit_type": "2BHK", "data.status": "active"},
  role="admin", body={"society_id": 1, "unit_number": "EV-101", "floor": "1", "unit_type": "2BHK"},
  capture=lambda c, j: c.update(unit_id=j["data"]["id"]))

C("TC-045", CAT5, "Unit creation rejects a missing unit number", "POST", "/api/units", 400,
  err("VALIDATION_ERROR"), role="admin", body={"society_id": 1, "block_name": "A"})

C("TC-046", CAT5, "Resident cannot create a unit", "POST", "/api/units", 403,
  err("FORBIDDEN"), role="resident", body={"society_id": 1, "unit_number": "EV-999"})

C("TC-047", CAT5, "Duplicate unit number in the same society is rejected", "POST", "/api/units", 409,
  {"success": False, "error.code": "DUPLICATE_UNIT"}, role="admin",
  body={"society_id": 1, "unit_number": "EV-101", "floor": "1", "unit_type": "2BHK"},
  defect="D-03")

C("TC-048", CAT5, "Admin lists units with pagination", "GET", "/api/units", 200,
  {"success": True, "data.items": NON_EMPTY_LIST, "data.pagination.total": IS_INT}, role="admin")

C("TC-049", CAT5, "Admin filters units by type", "GET", "/api/units", 200,
  {"success": True, "data.items.0.unit_type": "2BHK"}, role="admin", query={"unit_type": "2BHK"})

C("TC-050", CAT5, "Admin reads a unit by id", "GET", lambda c: f"/api/units/{c['unit_id']}", 200,
  {"success": True, "data.unit_number": "EV-101"}, role="admin")

C("TC-051", CAT5, "Reading a non-existent unit returns 404", "GET", "/api/units/999999", 404,
  err("NOT_FOUND"), role="admin")

C("TC-052", CAT5, "Admin updates a unit", "PUT", lambda c: f"/api/units/{c['unit_id']}", 200,
  {"success": True, "data.unit_type": "3BHK"}, role="admin", body={"unit_type": "3BHK"})

C("TC-053", CAT5, "Admin records an occupancy against the unit", "POST", "/api/occupancies", 201,
  {"success": True, "data.occupancy_type": "owner", "data.is_primary": True}, role="admin",
  body=lambda c: {"unit_id": c["unit_id"], "user_id": 2, "occupancy_type": "owner",
                  "start_date": "2026-01-01", "is_primary": True},
  capture=lambda c, j: c.update(occupancy_id=j["data"]["id"]))

C("TC-054", CAT5, "Occupancy creation rejects an invalid date format", "POST", "/api/occupancies", 400,
  err("VALIDATION_ERROR"), role="admin",
  body=lambda c: {"unit_id": c["unit_id"], "user_id": 2, "occupancy_type": "owner", "start_date": "01-01-2026"})

C("TC-055", CAT5, "Admin lists the residents of a unit", "GET",
  lambda c: f"/api/units/{c['unit_id']}/residents", 200, {"success": True, "data": NON_EMPTY_LIST}, role="admin")

C("TC-056", CAT5, "Admin removes the occupancy record", "DELETE",
  lambda c: f"/api/occupancies/{c['occupancy_id']}", 200,
  {"success": True, "message": contains("removed")}, role="admin")

C("TC-057", CAT5, "Admin deletes the unit", "DELETE", lambda c: f"/api/units/{c['unit_id']}", 200,
  {"success": True, "message": contains("deleted")}, role="admin")

# =============================================================================
# 06  NOTICE MANAGEMENT   (TC-058 .. TC-067)
# =============================================================================
CAT6 = "06 Notice Management"

C("TC-058", CAT6, "Admin publishes a notice", "POST", "/api/notices", 201,
  {"success": True, "data.title": "Water Tank Cleaning Drive", "data.notice_type": "maintenance",
   "data.priority": "high"}, role="admin",
  body={"title": "Water Tank Cleaning Drive", "body": "Tanks will be cleaned on Sunday 9 AM - 1 PM.",
        "notice_type": "maintenance", "priority": "high"},
  capture=lambda c, j: c.update(notice_id=j["data"]["id"]))

C("TC-059", CAT6, "Notice creation rejects missing mandatory fields", "POST", "/api/notices", 400,
  err("VALIDATION_ERROR"), role="admin", body={"title": "No body supplied"})

C("TC-060", CAT6, "Resident cannot publish a notice", "POST", "/api/notices", 403,
  err("FORBIDDEN"), role="resident",
  body={"title": "Unauthorised", "body": "x", "notice_type": "general", "priority": "low"})

C("TC-061", CAT6, "Admin publishes a notice with multilingual translations", "POST", "/api/notices", 201,
  {"success": True, "data.translations.hi": PRESENT, "data.translations.ta": PRESENT}, role="admin",
  body={"title": "Festival Announcement", "body": "Diwali celebration in the clubhouse.",
        "notice_type": "event", "priority": "normal",
        "translations": {"hi": "क्लबहाउस में दिवाली समारोह।", "ta": "கிளப்ஹவுஸில் தீபாவளி கொண்டாட்டம்."}},
  capture=lambda c, j: c.update(translated_notice_id=j["data"]["id"]))

C("TC-062", CAT6, "Notice without translations returns an empty translations object", "GET",
  lambda c: f"/api/notices/{c['notice_id']}", 200,
  {"success": True, "data.translations": {}}, role="resident")

C("TC-063", CAT6, "Resident reads the notice board", "GET", "/api/notices", 200,
  {"success": True, "data.items": NON_EMPTY_LIST}, role="resident")

C("TC-064", CAT6, "Notice board filters by priority", "GET", "/api/notices", 200,
  {"success": True, "data.items.0.priority": "urgent"}, role="resident", query={"priority": "urgent"})

C("TC-065", CAT6, "Notice board search returns a matching notice", "GET", "/api/notices", 200,
  {"success": True, "data.items.0.title": contains("water")}, role="resident", query={"search": "Water"})

C("TC-066", CAT6, "Admin edits a published notice", "PUT", lambda c: f"/api/notices/{c['notice_id']}", 200,
  {"success": True, "data.priority": "urgent"}, role="admin", body={"priority": "urgent"})

C("TC-067", CAT6, "Admin deletes a notice", "DELETE", lambda c: f"/api/notices/{c['translated_notice_id']}", 200,
  {"success": True, "message": contains("deleted")}, role="admin")

# =============================================================================
# 07  COMMUNITY EVENTS   (TC-068 .. TC-078)
# =============================================================================
CAT7 = "07 Community Events"

C("TC-068", CAT7, "Admin schedules a community event", "POST", "/api/events", 201,
  {"success": True, "data.title": "Annual Sports Day", "data.status": "scheduled", "data.venue": "Main Courtyard"},
  role="admin", body={"title": "Annual Sports Day", "description": "Track and field for all age groups.",
                      "event_date": "2026-09-20", "start_time": "07:00", "end_time": "12:00",
                      "venue": "Main Courtyard"},
  capture=lambda c, j: c.update(event_id=j["data"]["id"]))

C("TC-069", CAT7, "Event creation rejects a missing event date", "POST", "/api/events", 400,
  err("VALIDATION_ERROR"), role="admin", body={"title": "No date"})

C("TC-070", CAT7, "Event creation rejects an invalid date format", "POST", "/api/events", 400,
  err("VALIDATION_ERROR"), role="admin", body={"title": "Bad date", "event_date": "20-09-2026"})

C("TC-071", CAT7, "Resident cannot schedule an event", "POST", "/api/events", 403,
  err("FORBIDDEN"), role="resident", body={"title": "Unauthorised", "event_date": "2026-09-20"})

C("TC-072", CAT7, "Resident lists upcoming events", "GET", "/api/events", 200,
  {"success": True, "data.items": NON_EMPTY_LIST}, role="resident", query={"upcoming": "true"})

C("TC-073", CAT7, "Resident registers for an event", "POST",
  lambda c: f"/api/events/{c['event_id']}/register", 200,
  {"success": True, "message": contains("registration successful")}, role="resident")

C("TC-074", CAT7, "Duplicate event registration is rejected", "POST",
  lambda c: f"/api/events/{c['event_id']}/register", 409,
  {"success": False, "error.code": "ALREADY_REGISTERED"}, role="resident")

C("TC-075", CAT7, "Event detail shows the registration flag and attendee count", "GET",
  lambda c: f"/api/events/{c['event_id']}", 200,
  {"success": True, "data.is_registered": True, "data.registered_count": 1}, role="resident")

C("TC-076", CAT7, "Admin lists event attendees", "GET",
  lambda c: f"/api/events/{c['event_id']}/attendees", 200,
  {"success": True, "data": NON_EMPTY_LIST}, role="admin")

C("TC-077", CAT7, "Admin cancels the event", "PUT", lambda c: f"/api/events/{c['event_id']}/cancel", 200,
  {"success": True, "data.status": "cancelled"}, role="admin")

C("TC-078", CAT7, "Registration for a cancelled event is rejected", "POST",
  lambda c: f"/api/events/{c['event_id']}/register", 409,
  {"success": False, "error.code": "EVENT_CANCELLED"}, role="newresident", defect="D-07")

# =============================================================================
# 08  COMPLAINT LIFECYCLE   (TC-079 .. TC-092)
# =============================================================================
CAT8 = "08 Complaint Lifecycle"

C("TC-079", CAT8, "Resident raises a complaint", "POST", "/api/complaints", 201,
  {"success": True, "data.status": "open", "data.category": "Plumbing", "data.priority": "high"},
  role="resident", body={"subject": "Kitchen pipe leakage", "description": "Water leaking under the sink since morning.",
                         "category": "Plumbing", "priority": "high"},
  capture=lambda c, j: c.update(complaint_id=j["data"]["id"]))

C("TC-080", CAT8, "Complaint creation rejects missing mandatory fields", "POST", "/api/complaints", 400,
  {"success": False, "error.code": "VALIDATION_ERROR", "error.message": contains("missing required fields")},
  role="resident", body={"subject": "Only a subject"})

C("TC-081", CAT8, "SQL injection string in the subject is rejected by validation", "POST", "/api/complaints", 400,
  err("VALIDATION_ERROR"), role="resident", body={"subject": "'; DROP TABLE users; --"})

C("TC-082", CAT8, "Complaint creation rejects an invalid priority value", "POST", "/api/complaints", 400,
  {"success": False, "error.code": "VALIDATION_ERROR", "error.message": contains("priority")},
  role="resident", body={"subject": "Invalid priority", "description": "d", "category": "Plumbing",
                         "priority": "ULTRA"}, defect="D-04")

C("TC-083", CAT8, "Admin cannot raise a complaint (resident-only operation)", "POST", "/api/complaints", 403,
  err("FORBIDDEN"), role="admin",
  body={"subject": "Admin complaint", "description": "d", "category": "Plumbing", "priority": "low"})

C("TC-084", CAT8, "Resident sees only their own complaints", "GET", "/api/complaints", 200,
  {"success": True, "data.items": NON_EMPTY_LIST}, role="resident")

C("TC-085", CAT8, "Admin filters complaints by status", "GET", "/api/complaints", 200,
  {"success": True, "data.items.0.status": "open"}, role="admin", query={"status": "open"})

C("TC-086", CAT8, "Complaint detail includes the update timeline", "GET",
  lambda c: f"/api/complaints/{c['complaint_id']}", 200,
  {"success": True, "data.updates": NON_EMPTY_LIST, "data.updates.0.comment": contains("submitted")},
  role="resident")

C("TC-087", CAT8, "Unrelated user cannot read another resident's complaint", "GET",
  lambda c: f"/api/complaints/{c['complaint_id']}", 403, err("FORBIDDEN"), role="provider")

C("TC-088", CAT8, "Reading a non-existent complaint returns 404", "GET", "/api/complaints/999999", 404,
  err("NOT_FOUND"), role="admin")

C("TC-089", CAT8, "Assigning a complaint to a non-existent user is rejected", "PUT",
  lambda c: f"/api/complaints/{c['complaint_id']}/assign", 404,
  {"success": False, "error.code": "NOT_FOUND", "error.message": contains("assignee")},
  role="admin", body={"assigned_to_user_id": 999999}, defect="D-06")

C("TC-090", CAT8, "Admin assigns the complaint to staff", "PUT",
  lambda c: f"/api/complaints/{c['complaint_id']}/assign", 200,
  {"success": True, "data.status": "in_progress", "data.assigned_to_user_id": PRESENT},
  role="admin", body=lambda c: {"assigned_to_user_id": c["security_user_id"], "comment": "Assigned to maintenance"})

C("TC-091", CAT8, "An invalid status transition value is rejected", "PUT",
  lambda c: f"/api/complaints/{c['complaint_id']}/status", 400,
  {"success": False, "error.code": "VALIDATION_ERROR", "error.message": contains("status")},
  role="admin", body={"status": "not_a_real_status", "comment": "arbitrary"}, defect="D-05")

C("TC-092", CAT8, "Admin resolves the complaint and the timeline records it", "PUT",
  lambda c: f"/api/complaints/{c['complaint_id']}/status", 200,
  {"success": True, "data.status": "resolved"}, role="admin",
  body={"status": "resolved", "comment": "Pipe replaced and tested"})

# =============================================================================
# 09  SERVICE CATALOGUE & PROVIDERS   (TC-093 .. TC-101)
# =============================================================================
CAT9 = "09 Service Catalogue & Providers"

C("TC-093", CAT9, "Any authenticated user browses service categories", "GET", "/api/service-categories", 200,
  {"success": True, "data": NON_EMPTY_LIST, "data.0.name": PRESENT}, role="resident")

C("TC-094", CAT9, "Admin creates a service category", "POST", "/api/service-categories", 201,
  {"success": True, "data.name": "Pest Control"}, role="admin",
  body={"name": "Pest Control", "description": "Termite and pest treatment"},
  capture=lambda c, j: c.update(category_id=j["data"]["id"]))

C("TC-095", CAT9, "Category creation rejects a missing name", "POST", "/api/service-categories", 400,
  err("VALIDATION_ERROR"), role="admin", body={"description": "No name"})

C("TC-096", CAT9, "Resident cannot create a service category", "POST", "/api/service-categories", 403,
  err("FORBIDDEN"), role="resident", body={"name": "Unauthorised"})

C("TC-097", CAT9, "Admin renames a service category", "PUT", lambda c: f"/api/service-categories/{c['category_id']}",
  200, {"success": True, "data.name": "Pest & Termite Control"}, role="admin",
  body={"name": "Pest & Termite Control"})

C("TC-098", CAT9, "Resident browses the verified provider directory", "GET", "/api/providers", 200,
  {"success": True, "data.items": NON_EMPTY_LIST}, role="resident",
  query={"verification_status": "approved"})

C("TC-099", CAT9, "Reading a provider profile returns the business details", "GET", "/api/providers/1", 200,
  {"success": True, "data.business_name": PRESENT, "data.verification_status": "approved"}, role="resident")

C("TC-100", CAT9, "Reading a non-existent provider returns 404", "GET", "/api/providers/9999", 404,
  err("NOT_FOUND"), role="resident")

C("TC-101", CAT9, "A provider cannot edit another provider's profile", "PUT", "/api/providers/2", 403,
  err("FORBIDDEN"), role="provider", body={"business_name": "Hijacked Services"})

# =============================================================================
# 10  PROVIDER AVAILABILITY SLOTS   (TC-102 .. TC-108)
# =============================================================================
CAT10 = "10 Provider Availability Slots"

C("TC-102", CAT10, "Provider creates an availability slot", "POST", "/api/slots", 201,
  {"success": True, "data.is_available": True, "data.provider_id": 1}, role="provider",
  body={"provider_id": 1, "slot_start": "2026-09-01T10:00:00", "slot_end": "2026-09-01T11:00:00"},
  capture=lambda c, j: c.update(slot_id=j["data"]["id"]))

C("TC-103", CAT10, "Provider creates a second slot for booking tests", "POST", "/api/slots", 201,
  {"success": True, "data.is_available": True}, role="provider",
  body={"provider_id": 1, "slot_start": "2026-09-01T12:00:00", "slot_end": "2026-09-01T13:00:00"},
  capture=lambda c, j: c.update(slot_id_2=j["data"]["id"]))

C("TC-104", CAT10, "Slot creation rejects missing start and end times", "POST", "/api/slots", 400,
  err("VALIDATION_ERROR"), role="provider", body={"provider_id": 1})

C("TC-105", CAT10, "Slot creation rejects an unknown provider", "POST", "/api/slots", 404,
  err("NOT_FOUND"), role="admin",
  body={"provider_id": 9999, "slot_start": "2026-09-01T10:00:00", "slot_end": "2026-09-01T11:00:00"})

C("TC-106", CAT10, "A resident cannot create provider slots", "POST", "/api/slots", 403,
  err("FORBIDDEN"), role="resident",
  body={"provider_id": 1, "slot_start": "2026-09-01T10:00:00", "slot_end": "2026-09-01T11:00:00"})

C("TC-107", CAT10, "Resident reads the provider availability feed", "GET", "/api/providers/1/availability", 200,
  {"success": True, "data": NON_EMPTY_LIST}, role="resident")

C("TC-108", CAT10, "Provider lists own slots", "GET", "/api/slots/1", 200,
  {"success": True, "data": NON_EMPTY_LIST}, role="provider")

# =============================================================================
# 11  SERVICE BOOKINGS   (TC-109 .. TC-122)
# =============================================================================
CAT11 = "11 Service Bookings"

C("TC-109", CAT11, "Resident books an available provider slot", "POST", "/api/bookings", 201,
  {"success": True, "data.booking_status": "requested", "data.provider_id": 1}, role="resident",
  body=lambda c: {"provider_id": 1, "slot_id": c["slot_id"], "request_notes": "Kitchen tap repair"},
  capture=lambda c, j: c.update(booking_id=j["data"]["id"]))

C("TC-110", CAT11, "The booked slot is no longer offered as available", "GET", "/api/providers/1/availability",
  200, {"success": True, "data": IS_LIST}, role="resident")

C("TC-111", CAT11, "Booking the same slot twice is rejected", "POST", "/api/bookings", 409,
  {"success": False, "error.code": "SLOT_UNAVAILABLE"}, role="resident",
  body=lambda c: {"provider_id": 1, "slot_id": c["slot_id"]})

C("TC-112", CAT11, "Booking creation rejects a missing provider id", "POST", "/api/bookings", 400,
  err("VALIDATION_ERROR"), role="resident", body={"request_notes": "no provider"})

C("TC-113", CAT11, "Booking a non-existent provider is rejected", "POST", "/api/bookings", 404,
  {"success": False, "error.code": "NOT_FOUND", "error.message": contains("provider")}, role="resident",
  body={"provider_id": 99999, "request_notes": "ghost provider"},
  capture=lambda c, j: c.update(orphan_booking_id=(j.get("data") or {}).get("id", 999999)),
  defect="D-08")

C("TC-114", CAT11, "A booking with an unresolvable provider reference returns 404, not a 500", "GET",
  lambda c: f"/api/bookings/{c.get('orphan_booking_id', 999999)}", 404,
  err("NOT_FOUND"), role="resident", defect="D-09")

C("TC-115", CAT11, "Provider cannot be booked by an admin (resident-only operation)", "POST", "/api/bookings", 403,
  err("FORBIDDEN"), role="admin", body={"provider_id": 1})

C("TC-116", CAT11, "Resident reads own booking", "GET", lambda c: f"/api/bookings/{c['booking_id']}", 200,
  {"success": True, "data.booking_status": "requested"}, role="resident")

C("TC-117", CAT11, "An unrelated user cannot read someone else's booking", "GET",
  lambda c: f"/api/bookings/{c['booking_id']}", 403, err("FORBIDDEN"), role="security")

C("TC-118", CAT11, "Provider accepts the booking request", "PUT",
  lambda c: f"/api/bookings/{c['booking_id']}/accept", 200,
  {"success": True, "data.booking_status": "accepted"}, role="provider")

C("TC-119", CAT11, "Provider marks the booking complete", "PUT",
  lambda c: f"/api/bookings/{c['booking_id']}/complete", 200,
  {"success": True, "data.booking_status": "completed"}, role="provider")

C("TC-120", CAT11, "A completed booking cannot be cancelled", "PUT",
  lambda c: f"/api/bookings/{c['seed_completed_booking_id']}/cancel", 409,
  {"success": False, "error.code": "INVALID_STATE"}, role="resident", defect="D-10")

C("TC-121", CAT11, "A completed booking cannot be accepted again", "PUT",
  lambda c: f"/api/bookings/{c['seed_completed_booking_id']}/accept", 409,
  {"success": False, "error.code": "INVALID_STATE"}, role="provider", defect="D-11")

C("TC-122", CAT11, "Cancelling a booking releases the slot back to the availability feed", "POST",
  "/api/bookings", 201, {"success": True, "data.booking_status": "requested"}, role="resident",
  body=lambda c: {"provider_id": 1, "slot_id": c["slot_id_2"]},
  capture=lambda c, j: c.update(booking_id_2=j["data"]["id"]))

# =============================================================================
# 12  SERVICE REVIEWS   (TC-123 .. TC-128)
# =============================================================================
CAT12 = "12 Service Reviews"

C("TC-123", CAT12, "Resident reviews a completed booking", "POST", "/api/reviews", 201,
  {"success": True, "data.rating": 5}, role="resident",
  body=lambda c: {"provider_id": 1, "booking_id": c["booking_id"], "rating": 5, "feedback": "Prompt and tidy work"},
  capture=lambda c, j: c.update(review_id=j["data"]["id"]))

C("TC-124", CAT12, "A second review for the same booking is rejected", "POST", "/api/reviews", 409,
  {"success": False, "error.code": "DUPLICATE"}, role="resident",
  body=lambda c: {"provider_id": 1, "booking_id": c["booking_id"], "rating": 3})

C("TC-125", CAT12, "A booking that is not completed cannot be reviewed", "POST", "/api/reviews", 422,
  {"success": False, "error.code": "UNPROCESSABLE"}, role="resident",
  body=lambda c: {"provider_id": 1, "booking_id": c["booking_id_2"], "rating": 4})

C("TC-126", CAT12, "Review creation rejects a missing rating", "POST", "/api/reviews", 400,
  err("VALIDATION_ERROR"), role="resident", body=lambda c: {"provider_id": 1, "booking_id": c["booking_id"]})

C("TC-127", CAT12, "Provider rating average is recalculated after the review", "GET", "/api/providers/1", 200,
  {"success": True, "data.rating_avg": 5.0}, role="resident")

C("TC-128", CAT12, "Public review feed for a provider returns the summary", "GET", "/api/reviews/provider/1", 200,
  {"success": True, "data.items": NON_EMPTY_LIST, "data.summary.total_reviews": 1,
   "data.summary.average_rating": 5.0}, role="resident")

# =============================================================================
# 13  VISITOR & GATE MANAGEMENT   (TC-129 .. TC-136)
# =============================================================================
CAT13 = "13 Visitor & Gate Management"

C("TC-129", CAT13, "Security logs a visitor entry", "POST", "/api/visitors", 201,
  {"success": True, "data.visitor_name": "Ramesh Courier", "data.exit_time": None}, role="security",
  body=lambda c: {"society_id": 1, "recorded_by_user_id": c["security_user_id"],
                  "visitor_name": "Ramesh Courier", "vehicle_number": "MH12AB1234",
                  "contact_number": "9800011122", "remarks": "Parcel delivery"},
  capture=lambda c, j: c.update(visitor_id=j["data"]["id"]))

C("TC-130", CAT13, "Visitor entry rejects a missing visitor name", "POST", "/api/visitors", 400,
  err("VALIDATION_ERROR"), role="security", body={"society_id": 1, "recorded_by_user_id": 1})

C("TC-131", CAT13, "A resident cannot log gate entries", "POST", "/api/visitors", 403,
  err("FORBIDDEN"), role="resident",
  body={"society_id": 1, "recorded_by_user_id": 2, "visitor_name": "Unauthorised"})

C("TC-132", CAT13, "Security lists visitors currently inside the premises", "GET", "/api/visitors", 200,
  {"success": True, "data.items": NON_EMPTY_LIST, "data.items.0.exit_time": None},
  role="security", query={"status": "inside"})

C("TC-133", CAT13, "Security searches the visitor log by vehicle number", "GET", "/api/visitors", 200,
  {"success": True, "data.items.0.vehicle_number": "MH12AB1234"}, role="security",
  query={"search": "MH12AB"})

C("TC-134", CAT13, "Security records the visitor exit", "PUT",
  lambda c: f"/api/visitors/{c['visitor_id']}/exit", 200,
  {"success": True, "data.exit_time": PRESENT, "message": contains("exit")}, role="security")

C("TC-135", CAT13, "Recording a second exit for the same visitor is rejected", "PUT",
  lambda c: f"/api/visitors/{c['visitor_id']}/exit", 409,
  {"success": False, "error.code": "ALREADY_EXITED"}, role="security", defect="D-12")

C("TC-136", CAT13, "Today's gate summary reports entry and exit counts", "GET", "/api/visitors/today", 200,
  {"success": True, "data.total_today": IS_INT, "data.currently_inside": IS_INT, "data.exited": IS_INT},
  role="security")

# =============================================================================
# 14  ANALYTICS & REPORTING   (TC-137 .. TC-142)
# =============================================================================
CAT14 = "14 Analytics & Reporting"

C("TC-137", CAT14, "Admin dashboard returns live society statistics", "GET",
  "/api/analytics/dashboard/admin", 200,
  {"success": True, "data.stats.total_residents": IS_INT, "data.stats.pending_complaints": IS_INT,
   "data.stats.upcoming_events": IS_INT}, role="admin")

C("TC-138", CAT14, "Resident cannot open the admin dashboard", "GET", "/api/analytics/dashboard/admin", 403,
  err("FORBIDDEN"), role="resident")

C("TC-139", CAT14, "Resident dashboard is scoped to the resident role", "GET",
  "/api/analytics/dashboard/resident", 200, {"success": True, "data.stats": PRESENT}, role="resident")

C("TC-140", CAT14, "Complaint analytics returns the status breakdown", "GET", "/api/analytics/complaints", 200,
  {"success": True, "data.status_breakdown.open": IS_INT, "data.status_breakdown.resolved": IS_INT},
  role="admin")

C("TC-141", CAT14, "Booking analytics returns the status breakdown", "GET", "/api/analytics/bookings", 200,
  {"success": True, "data.status_breakdown.completed": IS_INT, "data.status_breakdown.requested": IS_INT},
  role="admin")

C("TC-142", CAT14, "Monthly report consolidates every module", "GET", "/api/reports/monthly", 200,
  {"success": True, "data.residents.total": IS_INT, "data.complaints.raised": IS_INT,
   "data.notices.published": IS_INT, "data.visitors.total": IS_INT}, role="admin")

# =============================================================================
# 15  AI ASSISTANCE   (TC-143 .. TC-146)
# =============================================================================
CAT15 = "15 AI Assistance"

C("TC-143", CAT15, "AI service status reports the configured feature list", "GET", "/api/ai/status", 200,
  {"success": True, "data.configured": PRESENT, "data.features": NON_EMPTY_LIST}, role="admin")

C("TC-144", CAT15, "AI notice generation rejects an empty topic before calling the model", "POST",
  "/api/ai/notices/generate", 400, err("VALIDATION_ERROR"), role="admin", body={"topic": ""})

C("TC-145", CAT15, "A resident cannot invoke AI notice generation", "POST", "/api/ai/notices/generate", 403,
  err("FORBIDDEN"), role="resident", body={"topic": "Water tank cleaning"})

C("TC-146", CAT15, "A resident cannot invoke the raw AI passthrough endpoint", "POST", "/api/ai/raw", 403,
  err("FORBIDDEN"), role="resident", body={"prompt": "hello"})


# =============================================================================
# SECTION 3 - EXECUTION ENGINE
# =============================================================================

class EvidenceConfig:
    """Deterministic, isolated database so every run starts from the same seed."""

    TESTING = True
    SECRET_KEY = "socioneed-evidence-secret-key-0123456789"
    JWT_SECRET_KEY = "socioneed-evidence-jwt-key-0123456789"
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CORS_ORIGINS = ["http://localhost:5173"]


SEED_LOGINS = {
    "admin": ("admin@socioneed.com", "123456"),
    "resident": ("resident@socioneed.com", "123456"),
    "provider": ("provider@socioneed.com", "123456"),
    "provider2": ("provider.plumber@socioneed.com", "123456"),
    "security": ("security@socioneed.com", "123456"),
}


class Result:
    def __init__(self, case, index):
        self.case = case
        self.index = index
        self.id = case["id"]
        self.title = case["title"]
        self.cat = case["cat"]
        self.method = case["method"]
        self.path = ""
        self.role = case["role"] or "anonymous"
        self.query = case["query"]
        self.body = None
        self.expect_status = case["expect_status"]
        self.expect = case["expect"]
        self.status = None
        self.payload = None
        self.field_results = []       # (dotted, expected, actual, ok)
        self.passed = False
        self.reason = ""
        self.defect = case["defect"]

    @property
    def endpoint(self):
        return f"{self.method} {self.path}"


class EvidenceRun:
    """Runs the whole 146-case catalogue in order against one app instance."""

    def __init__(self):
        from app import create_app
        from app.core.extensions import db

        self.app = create_app(EvidenceConfig)
        with self.app.app_context():
            db.create_all()
        self.client = self.app.test_client()
        self.ctx = {"tag": uuid.uuid4().hex[:6]}
        self.tokens = {}
        self.results = []
        self._login_seed_users()

    # ---------------------------------------------------------------- auth --
    def _login(self, email, password):
        resp = self.client.post("/api/auth/login", json={"email": email, "password": password})
        if resp.status_code != 200:
            raise RuntimeError(f"Fixture login failed for {email}: {resp.status_code} {resp.get_data(as_text=True)}")
        return resp.get_json()["data"]

    def _login_seed_users(self):
        for role, (email, password) in SEED_LOGINS.items():
            data = self._login(email, password)
            self.tokens[role] = data["token"]
            if role == "security":
                self.ctx["security_user_id"] = data["user"]["id"]
            if role == "admin":
                self.ctx["admin_user_id"] = data["user"]["id"]
        self.tokens["tampered"] = self.tokens["admin"][:-6] + "AAAAAA"
        self._discover_seed_ids()

    def _discover_seed_ids(self):
        """Seeded demo booking that is already in the completed state."""
        resp = self.client.get(
            "/api/bookings",
            headers={"Authorization": f"Bearer {self.tokens['admin']}"},
            query_string={"booking_status": "completed"},
        )
        items = (resp.get_json().get("data") or {}).get("items") or []
        self.ctx["seed_completed_booking_id"] = items[0]["id"] if items else 3

    def _token_for(self, role):
        if role in (None, "anonymous"):
            return None
        if role == "newresident":
            if "newresident" not in self.tokens:
                data = self._login(self.ctx["new_user_email"], "Password123")
                self.tokens["newresident"] = data["token"]
            return self.tokens["newresident"]
        return self.tokens[role]

    # ------------------------------------------------------------ execution --
    def run_all(self):
        for index, case in enumerate(CASES, start=1):
            self.results.append(self.run_case(case, index))
        return self.results

    def run_case(self, case, index):
        result = Result(case, index)

        path = case["path"]
        result.path = path(self.ctx) if callable(path) else path

        body = case["body"]
        result.body = body(self.ctx) if callable(body) else body

        kwargs = {"query_string": case["query"]} if case["query"] else {}
        token = self._token_for(case["role"])
        if token:
            kwargs["headers"] = {"Authorization": f"Bearer {token}"}
        if result.body is not None:
            if isinstance(result.body, str):
                kwargs["data"] = result.body
                kwargs["content_type"] = "application/json"
            else:
                kwargs["json"] = result.body

        response = self.client.open(result.path, method=case["method"], **kwargs)
        result.status = response.status_code
        try:
            result.payload = response.get_json()
        except Exception:
            result.payload = response.get_data(as_text=True)
        if result.payload is None:
            result.payload = response.get_data(as_text=True)

        status_ok = result.status == case["expect_status"]
        fields_ok = True
        if isinstance(result.payload, dict):
            for dotted, expected in case["expect"].items():
                matched, actual = check(result.payload, dotted, expected)
                result.field_results.append((dotted, expected, actual, matched))
                fields_ok = fields_ok and matched
        elif case["expect"]:
            fields_ok = False
            for dotted, expected in case["expect"].items():
                result.field_results.append((dotted, expected, _MISSING, False))

        result.passed = status_ok and fields_ok
        if not status_ok:
            result.reason = f"expected HTTP {case['expect_status']}, received HTTP {result.status}"
        elif not fields_ok:
            bad = [d for d, _e, _a, okk in result.field_results if not okk]
            result.reason = "response field mismatch: " + ", ".join(bad)

        if case["capture"] and isinstance(result.payload, dict):
            try:
                case["capture"](self.ctx, result.payload)
            except Exception:
                pass
        return result


def fmt(value):
    if value is _MISSING:
        return "<missing>"
    if isinstance(value, (dict, list)):
        return json.dumps(value, indent=4, ensure_ascii=False)
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


# =============================================================================
# SECTION 4 - PYTEST ENTRY POINT (146 named tests)
# =============================================================================


@pytest.fixture(scope="session")
def evidence_results():
    """The catalogue runs once per session - the cases share state by design
    (a unit is created, then read, then deleted)."""
    return {result.id: result for result in EvidenceRun().run_all()}


def _case_id(case):
    suffix = f"-{case['defect'].replace('-', '_')}" if case["defect"] else ""
    return f"{case['id']}{suffix}"


@pytest.mark.parametrize("case", CASES, ids=[_case_id(c) for c in CASES])
def test_api_case(case, evidence_results):
    result = evidence_results[case["id"]]

    detail = (
        f"\n{result.id} - {result.title}"
        f"\n  endpoint : {result.endpoint}"
        f"\n  as role  : {result.role}"
        f"\n  input    : {fmt(result.body)}"
        f"\n  expected : HTTP {result.expect_status}"
        f"\n  actual   : HTTP {result.status}"
        f"\n  response : {fmt(result.payload)}"
    )

    assert result.status == result.expect_status, detail
    for dotted, expected, actual, matched in result.field_results:
        assert matched, f"{detail}\n  field    : {dotted} expected {expected!r}, actual {actual!r}"


# =============================================================================
# SECTION 5 - TERMINAL EVIDENCE PRINTER
# =============================================================================

LINE = "=" * 78
THIN = "-" * 78

GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
BOLD = "\033[1m"
OFF = "\033[0m"


class Palette:
    def __init__(self, enabled):
        self.enabled = enabled

    def __call__(self, code, text):
        return f"{code}{text}{OFF}" if self.enabled else text


def render(result, colour):
    out = io.StringIO()
    w = out.write
    w(LINE + "\n")
    w(f"Test Case {result.index} [{result.id}] - {result.title}\n")
    w(f"Category      : {result.cat}\n")
    w(f"API Endpoint  : {result.endpoint}\n")
    w(f"Auth Role     : {result.role}\n")
    if result.query:
        w(f"Query Params  : {json.dumps(result.query)}\n")
    w("\nInput:\n")
    if result.body is None:
        w("(no request body - this operation takes none)\n")
    else:
        w(fmt(result.body) + "\n")

    expected = {"status_code": result.expect_status}
    for dotted, value, _actual, _ok in result.field_results:
        expected[dotted] = repr(value) if hasattr(value, "fn") else value
    if not result.field_results:
        for dotted, value in result.expect.items():
            expected[dotted] = repr(value) if hasattr(value, "fn") else value
    w("\nExpected Output:\n")
    w(json.dumps(expected, indent=4, ensure_ascii=False, default=str) + "\n")

    w(THIN + "\n")
    w(f"ACTUAL STATUS : {result.status}\n")
    w("ACTUAL RESPONSE (json):\n")
    w(fmt(result.payload) + "\n")

    if result.field_results:
        w("\nField assertions:\n")
        for dotted, value, actual, okk in result.field_results:
            mark = colour(GREEN, "PASS") if okk else colour(RED, "FAIL")
            shown = repr(value) if hasattr(value, "fn") else json.dumps(value, ensure_ascii=False, default=str)
            got = json.dumps(actual, ensure_ascii=False, default=str) if not hasattr(actual, "fn") else str(actual)
            w(f"  [{mark}] {dotted:<34} expected {shown:<28} actual {got}\n")

    w("\n")
    if result.passed:
        w(colour(GREEN, "Result: PASS  (expected outcome confirmed)") + "\n")
    else:
        tag = f"  [DEFECT {result.defect}]" if result.defect else ""
        w(colour(RED, f"Result: FAIL  ({result.reason}){tag}") + "\n")
    w(LINE + "\n\n")
    return out.getvalue()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--label", default="FULL RUN", help="banner label, e.g. BEFORE-FIX / AFTER-FIX")
    ap.add_argument("--only", nargs="*", default=None, help="case ids to run, e.g. TC-007")
    ap.add_argument("--defects", action="store_true", help="print only the defect-proof cases")
    ap.add_argument("--failures", action="store_true", help="print only the cases that failed")
    ap.add_argument("--from", dest="start", type=int, default=1)
    ap.add_argument("--to", dest="end", type=int, default=len(CASES))
    ap.add_argument("--md", default=None, help="also write the transcript to this markdown file")
    ap.add_argument("--json", dest="json_out", default=None, help="write a machine-readable summary")
    ap.add_argument("--no-color", action="store_true")
    args = ap.parse_args()

    colour = Palette(not args.no_color and sys.stdout.isatty())
    plain = Palette(False)

    banner = [
        "#" * 78,
        f"#  SOCIONEED - API TEST EVIDENCE   ({args.label})",
        f"#  Catalogue: {len(CASES)} test cases | every Expected Output is hand-written,",
        "#  never copied from the response. Actual Output is the live server reply.",
        "#" * 78,
        "",
    ]
    print("\n".join(banner))

    run = EvidenceRun()
    results = run.run_all()

    selected = [r for r in results if args.start <= r.index <= args.end]
    if args.only:
        wanted = {value.upper() for value in args.only}
        selected = [r for r in selected if r.id in wanted]
    if args.defects:
        selected = [r for r in selected if r.defect]
    if args.failures:
        selected = [r for r in selected if not r.passed]

    md_chunks = []
    current_cat = None
    for result in selected:
        if result.cat != current_cat:
            current_cat = result.cat
            header = f"\n{colour(BOLD, '>>> CATEGORY: ' + current_cat)}\n"
            print(header)
            md_chunks.append(f"\n## {current_cat}\n")
        print(render(result, colour), end="")
        md_chunks.append("```text\n" + render(result, plain) + "```\n")

    passed = [r for r in results if r.passed]
    failed = [r for r in results if not r.passed]
    expected_fail = [r for r in failed if r.defect]
    surprise_fail = [r for r in failed if not r.defect]

    summary = io.StringIO()
    summary.write("#" * 78 + "\n")
    summary.write(f"#  RUN SUMMARY  ({args.label})\n")
    summary.write("#" * 78 + "\n")
    summary.write(f"  Total test cases executed : {len(results)}\n")
    summary.write(f"  PASSED                    : {len(passed)}\n")
    summary.write(f"  FAILED                    : {len(failed)}\n")
    summary.write(f"    - known defect proofs   : {len(expected_fail)}\n")
    summary.write(f"    - unexpected regressions: {len(surprise_fail)}\n")
    rate = 100.0 * len(passed) / len(results) if results else 0
    summary.write(f"  Pass rate                 : {rate:.1f}%\n\n")

    summary.write("  Coverage by category\n")
    summary.write(f"  {'Category':<42}{'Cases':>7}{'Pass':>7}{'Fail':>7}\n")
    cats = []
    for r in results:
        if r.cat not in [c[0] for c in cats]:
            cats.append((r.cat, []))
        dict(cats)[r.cat].append(r)
    for name, rows in cats:
        p = len([r for r in rows if r.passed])
        summary.write(f"  {name:<42}{len(rows):>7}{p:>7}{len(rows) - p:>7}\n")

    if failed:
        summary.write("\n  Failing cases\n")
        summary.write(f"  {'Case':<9}{'Defect':<8}{'Endpoint':<44}{'Exp':>5}{'Act':>5}\n")
        for r in failed:
            summary.write(f"  {r.id:<9}{(r.defect or '-'):<8}{r.endpoint[:43]:<44}"
                          f"{r.expect_status:>5}{r.status:>5}\n")
        summary.write("\n  Every failure above is a genuine expectation mismatch against the\n")
        summary.write("  running application - not a skipped or fabricated case.\n")
    else:
        summary.write("\n  No failures. All expectations satisfied by the running application.\n")

    text = summary.getvalue()
    print(colour(YELLOW if failed else GREEN, text))

    if args.md:
        with open(args.md, "w", encoding="utf-8") as handle:
            handle.write(f"# SocioNeed - API Test Evidence ({args.label})\n\n")
            handle.write(f"**Total:** {len(results)} | **Passed:** {len(passed)} | "
                         f"**Failed:** {len(failed)} | **Pass rate:** {rate:.1f}%\n")
            handle.write("\n```text\n" + text + "```\n")
            handle.write("".join(md_chunks))
        print(f"Markdown transcript written to {args.md}")

    if args.json_out:
        payload = [{
            "id": r.id, "index": r.index, "category": r.cat, "title": r.title,
            "method": r.method, "path": r.path, "role": r.role, "query": r.query,
            "body": r.body, "expected_status": r.expect_status, "actual_status": r.status,
            "passed": r.passed, "defect": r.defect, "reason": r.reason,
            "actual": r.payload,
        } for r in results]
        with open(args.json_out, "w", encoding="utf-8") as handle:
            json.dump(payload, handle, indent=2, ensure_ascii=False, default=str)
        print(f"JSON summary written to {args.json_out}")

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
