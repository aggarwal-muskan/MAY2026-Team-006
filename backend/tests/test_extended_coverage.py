"""SocioNeed - extended backend coverage (112 tests) in a single file.

Merged from the nine previously separate test modules. These sit alongside
tests/test_socioneed_api.py (the 146-case milestone suite) and cover ground
that suite deliberately leaves out: mocked database failure paths, JWT expiry
and tampering, service-slot temporal edges, and the AI endpoints with Gemini
stubbed so the suite stays offline.

Helpers and fixtures are namespaced with the module number they came from
(_auth_07, fake_ai_14, ...) so nothing shadows anything else.

    pytest tests/test_extended_coverage.py -v
"""

import app.api.ai as ai_module
import app.services.gemini_service as gs
import pytest
from app.core.extensions import db
from app.models import User
from app.services.gemini_service import GeminiServiceError
from datetime import UTC, datetime
from datetime import timedelta
from flask_jwt_extended import create_access_token
from sqlalchemy.exc import SQLAlchemyError


# ============================================================================
# test_07_negative_boundary.py
#
# test_07_negative_boundary.py
# ============================================================================

def _auth_07(token):
    return {"Authorization": f"Bearer {token}"}


def test_invalid_email_format_registration(client):
    response = client.post(
        "/api/auth/register",
        json={
            "full_name": "Bad Email User",
            "email": "invalid-email-string",
            "phone": "9876543219",
            "password": "Password123",
            "role": "owner",
            "society_id": 1,
        },
    )
    assert response.status_code == 400
    json_data = response.get_json()
    assert json_data["error"]["code"] == "VALIDATION_ERROR"


def test_short_password_registration(client):
    response = client.post(
        "/api/auth/register",
        json={
            "full_name": "Short Password User",
            "email": "shortpass@socioneed.com",
            "phone": "9876543218",
            "password": "123",
            "role": "owner",
            "society_id": 1,
        },
    )
    assert response.status_code == 400
    json_data = response.get_json()
    assert json_data["error"]["code"] == "VALIDATION_ERROR"


def test_sql_injection_attempt_sanitization(client, resident_token):
    sql_payload = "' OR '1'='1'; DROP TABLE users; --"
    response = client.post(
        "/api/complaints",
        headers=_auth_07(resident_token),
        json={
            "subject": sql_payload,
            "description": f"Testing SQL injection payload: {sql_payload}",
            "category": "Security",
            "priority": "high",
        },
    )
    assert response.status_code == 201
    json_data = response.get_json()
    assert json_data["data"]["subject"] == sql_payload


def test_very_large_request_payload(client, resident_token):
    large_description = "A" * 50000
    response = client.post(
        "/api/complaints",
        headers=_auth_07(resident_token),
        json={
            "subject": "Large Payload Test",
            "description": large_description,
            "category": "Maintenance",
            "priority": "low",
        },
    )
    assert response.status_code == 201
    assert len(response.get_json()["data"]["description"]) == 50000


def test_invalid_or_expired_jwt_token(client):
    invalid_token_headers = {"Authorization": "Bearer invalid.jwt.fake_token_string"}
    response = client.get("/api/users/me", headers=invalid_token_headers)
    assert response.status_code in [401, 422]


def test_non_existent_resource_id_404(client, admin_token):
    complaint_resp = client.get("/api/complaints/999999", headers=_auth_07(admin_token))
    assert complaint_resp.status_code == 404

    unit_resp = client.get("/api/units/999999", headers=_auth_07(admin_token))
    assert unit_resp.status_code == 404


def test_missing_required_authorization_headers(client):
    response = client.get("/api/users/me")
    assert response.status_code == 401


def test_invalid_malformed_json_payload(client):
    response = client.post(
        "/api/auth/login",
        data="INVALID_JSON_RAW_STRING{{{",
        content_type="application/json",
    )
    assert response.status_code in [400, 415, 500]


def test_concurrent_booking_attempts_same_slot(client, admin_token, resident_token):
    prov_resp = client.get("/api/providers", headers=_auth_07(admin_token))
    items = prov_resp.get_json()["data"]["items"]
    provider_id = items[0]["id"]

    ts = datetime.now(UTC).strftime("%H%M%S")
    slot = client.post(
        "/api/slots",
        headers=_auth_07(admin_token),
        json={
            "provider_id": provider_id,
            "slot_start": f"2026-09-01T10:{ts[:2]}:00",
            "slot_end": f"2026-09-01T11:{ts[:2]}:00",
            "is_available": True,
        },
    )
    assert slot.status_code == 201
    slot_id = slot.get_json()["data"]["id"]

    booking1 = client.post(
        "/api/bookings",
        headers=_auth_07(resident_token),
        json={"provider_id": provider_id, "slot_id": slot_id, "request_notes": "First user booking"},
    )
    assert booking1.status_code == 201

    booking2 = client.post(
        "/api/bookings",
        headers=_auth_07(resident_token),
        json={"provider_id": provider_id, "slot_id": slot_id, "request_notes": "Concurrent user booking attempt"},
    )
    assert booking2.status_code == 409
    assert booking2.get_json()["error"]["code"] == "SLOT_UNAVAILABLE"


# ============================================================================
# test_08_auth_forgot_password.py
#
# Edge-case coverage for the password-reset flow.
#
# Note on external dependencies: the current /api/auth/forgot-password endpoint
# performs an in-place password reset (it verifies email/phone ownership and
# writes the new hash directly). There is NO outgoing email or SMS integration in
# the codebase, so there is no external notification client to mock. These tests
# therefore exhaustively cover the validation, ownership-verification and
# error-handling paths of the reset endpoint itself, plus proof that the reset
# actually takes effect (old password rejected, new password accepted).
# ============================================================================

def _auth_08(token):
    return {"Authorization": f"Bearer {token}"}


def _login_08(client, email, password, role=None):
    payload = {"email": email, "password": password}
    if role:
        payload["role"] = role
    return client.post("/api/auth/login", json=payload)


def test_forgot_password_missing_new_password(client):
    resp = client.post(
        "/api/auth/forgot-password",
        json={"email": "resident@socioneed.com"},
    )
    assert resp.status_code == 400
    assert resp.get_json()["error"]["code"] == "VALIDATION_ERROR"


def test_forgot_password_missing_identifier(client):
    resp = client.post(
        "/api/auth/forgot-password",
        json={"new_password": "brandnew123"},
    )
    assert resp.status_code == 400
    assert resp.get_json()["error"]["code"] == "VALIDATION_ERROR"


def test_forgot_password_empty_body(client):
    resp = client.post("/api/auth/forgot-password", json={})
    assert resp.status_code == 400
    assert resp.get_json()["error"]["code"] == "VALIDATION_ERROR"


def test_forgot_password_unknown_user(client):
    resp = client.post(
        "/api/auth/forgot-password",
        json={"email": "ghost@nowhere.com", "new_password": "brandnew123"},
    )
    assert resp.status_code == 404
    assert resp.get_json()["error"]["code"] == "NOT_FOUND"


def test_forgot_password_phone_mismatch_rejected(client):
    """Ownership check: supplying a phone that does not match the account is rejected."""
    resp = client.post(
        "/api/auth/forgot-password",
        json={
            "email": "resident@socioneed.com",
            "phone": "1111111111",
            "new_password": "shouldnotapply123",
        },
    )
    assert resp.status_code == 401
    assert resp.get_json()["error"]["code"] == "UNAUTHORIZED"
    # And the mismatch must NOT have changed the password.
    assert _login_08(client, "resident@socioneed.com", "123456", "owner").status_code == 200


def test_forgot_password_resets_and_invalidates_old_password(client):
    reset = client.post(
        "/api/auth/forgot-password",
        json={
            "email": "provider@socioneed.com",
            "phone": "9000000003",
            "new_password": "resetpass456",
        },
    )
    assert reset.status_code == 200
    assert reset.get_json()["message"] == "Password reset successful"

    # Old password no longer works.
    assert _login_08(client, "provider@socioneed.com", "123456").status_code == 401
    # New password works.
    assert _login_08(client, "provider@socioneed.com", "resetpass456").status_code == 200

    # Restore for isolation-safety if the DB were shared.
    client.post(
        "/api/auth/forgot-password",
        json={"email": "provider@socioneed.com", "phone": "9000000003", "new_password": "123456"},
    )


def test_forgot_password_by_phone_identifier(client):
    """The identifier field accepts a phone number as well as an email."""
    reset = client.post(
        "/api/auth/forgot-password",
        json={"email": "9000000004", "new_password": "phonereset789"},
    )
    assert reset.status_code == 200

    assert _login_08(client, "security@socioneed.com", "phonereset789").status_code == 200

    client.post(
        "/api/auth/forgot-password",
        json={"email": "9000000004", "new_password": "123456"},
    )


def test_forgot_password_new_login_uses_role_after_reset(client):
    reset = client.post(
        "/api/auth/forgot-password",
        json={"email": "resident@socioneed.com", "phone": "9000000002", "new_password": "roundtrip321"},
    )
    assert reset.status_code == 200

    good = _login_08(client, "resident@socioneed.com", "roundtrip321", "owner")
    assert good.status_code == 200
    assert "token" in good.get_json()["data"]

    client.post(
        "/api/auth/forgot-password",
        json={"email": "resident@socioneed.com", "phone": "9000000002", "new_password": "123456"},
    )


# ============================================================================
# test_09_token_lifecycle.py
#
# Token lifecycle & security edge cases.
#
# Covers expired access tokens, malformed/invalid tokens, missing tokens, the
# refresh path (including refresh for a deleted user), and documents the current
# revocation behaviour: logout returns success but does NOT add the token to a
# denylist, so the token remains usable afterwards. That last test is a guard
# that pins the current (no server-side revocation) behaviour so any future
# change is caught deliberately.
# ============================================================================

def _auth_09(token):
    return {"Authorization": f"Bearer {token}"}


def _make_token_09(app, identity="1", role="admin", society_id=1, expires_delta=None):
    with app.app_context():
        return create_access_token(
            identity=str(identity),
            additional_claims={"role": role, "society_id": society_id},
            expires_delta=expires_delta,
        )


def test_expired_token_rejected_on_verify(app, client):
    expired = _make_token_09(app, expires_delta=timedelta(seconds=-30))
    resp = client.post("/api/auth/verify-token", headers=_auth_09(expired))
    assert resp.status_code == 401
    assert resp.get_json()["error"]["code"] == "TOKEN_EXPIRED"


def test_expired_token_rejected_on_protected_resource(app, client):
    expired = _make_token_09(app, expires_delta=timedelta(seconds=-1))
    resp = client.get("/api/complaints", headers=_auth_09(expired))
    assert resp.status_code == 401
    assert resp.get_json()["error"]["code"] == "TOKEN_EXPIRED"


def test_malformed_token_rejected(client):
    resp = client.post("/api/auth/verify-token", headers={"Authorization": "Bearer not.a.real.jwt"})
    assert resp.status_code == 401
    assert resp.get_json()["error"]["code"] == "UNAUTHORIZED"


def test_token_signed_with_wrong_secret_rejected(client):
    import jwt as pyjwt

    forged = pyjwt.encode({"sub": "1", "role": "admin"}, "totally-wrong-secret-key-32bytes-long!!", algorithm="HS256")
    resp = client.post("/api/auth/verify-token", headers=_auth_09(forged))
    assert resp.status_code == 401
    assert resp.get_json()["error"]["code"] == "UNAUTHORIZED"


def test_missing_token_rejected(client):
    resp = client.post("/api/auth/verify-token")
    assert resp.status_code == 401
    assert resp.get_json()["error"]["code"] == "UNAUTHORIZED"


def test_wrong_scheme_header_rejected(client):
    resp = client.post("/api/auth/verify-token", headers={"Authorization": "Token abc.def.ghi"})
    assert resp.status_code == 401


def test_valid_token_verifies_claims(client, admin_token):
    resp = client.post("/api/auth/verify-token", headers=_auth_09(admin_token))
    assert resp.status_code == 200
    data = resp.get_json()["data"]
    assert data["valid"] is True
    assert data["user"]["role"] == "admin"


def test_refresh_token_issues_working_token(client, resident_token):
    refresh = client.post("/api/auth/refresh-token", headers=_auth_09(resident_token))
    assert refresh.status_code == 200
    new_token = refresh.get_json()["data"]["token"]

    # The freshly minted token is usable on a protected endpoint.
    check = client.post("/api/auth/verify-token", headers=_auth_09(new_token))
    assert check.status_code == 200


def test_refresh_with_expired_token_rejected(app, client):
    expired = _make_token_09(app, identity="2", role="owner", expires_delta=timedelta(seconds=-5))
    resp = client.post("/api/auth/refresh-token", headers=_auth_09(expired))
    assert resp.status_code == 401
    assert resp.get_json()["error"]["code"] == "TOKEN_EXPIRED"


def test_refresh_for_deleted_user_returns_not_found(app, client):
    """A structurally-valid token whose user no longer exists must not mint a new token."""
    # Create then delete a throwaway user, and mint a token bound to its id.
    with app.app_context():
        user = User(
            society_id=1,
            role="owner",
            full_name="Temp Refresh User",
            email="temp_refresh@socioneed.com",
            phone="9123456780",
            password_hash="x",
            status="active",
        )
        db.session.add(user)
        db.session.commit()
        uid = user.id
        token = create_access_token(identity=str(uid), additional_claims={"role": "owner", "society_id": 1})
        db.session.delete(user)
        db.session.commit()

    resp = client.post("/api/auth/refresh-token", headers=_auth_09(token))
    assert resp.status_code == 404
    assert resp.get_json()["error"]["code"] == "NOT_FOUND"


def test_logout_does_not_revoke_token(client, admin_token):
    """Documents current behaviour: no server-side denylist, so the token still works after logout."""
    logout = client.post("/api/auth/logout", headers=_auth_09(admin_token))
    assert logout.status_code == 200

    still_valid = client.post("/api/auth/verify-token", headers=_auth_09(admin_token))
    assert still_valid.status_code == 200


# ============================================================================
# test_10_slots_edge_cases.py
#
# Slot-creation edge cases and time validation.
#
# Covers required-field validation, invalid datetime formats, unknown provider,
# role/ownership enforcement, duplicate-slot uniqueness (transaction rollback via
# the IntegrityError handler), and the CURRENT behaviour for overlapping slots and
# end < start times. The overlap / end<start tests assert what the API does today
# (it accepts them, because no temporal validation exists) so the gap is visible
# and pinned; if validation is later added these tests should be updated to expect
# a 400/409.
# ============================================================================

def _auth_10(token):
    return {"Authorization": f"Bearer {token}"}


def _provider_id_10(client, admin_token):
    resp = client.get("/api/providers", headers=_auth_10(admin_token))
    return resp.get_json()["data"]["items"][0]["id"]


def _slot_body_10(provider_id, start, end, available=True):
    return {"provider_id": provider_id, "slot_start": start, "slot_end": end, "is_available": available}


def test_slot_missing_fields(client, admin_token):
    pid = _provider_id_10(client, admin_token)
    resp = client.post("/api/slots", headers=_auth_10(admin_token), json={"provider_id": pid})
    assert resp.status_code == 400
    assert resp.get_json()["error"]["code"] == "VALIDATION_ERROR"


def test_slot_unknown_provider(client, admin_token):
    resp = client.post(
        "/api/slots",
        headers=_auth_10(admin_token),
        json=_slot_body_10(999999, "2026-11-01T10:00:00", "2026-11-01T11:00:00"),
    )
    assert resp.status_code == 404
    assert resp.get_json()["error"]["code"] == "NOT_FOUND"


def test_slot_invalid_start_datetime_format(client, admin_token):
    pid = _provider_id_10(client, admin_token)
    resp = client.post(
        "/api/slots",
        headers=_auth_10(admin_token),
        json=_slot_body_10(pid, "01-11-2026 10am", "2026-11-01T11:00:00"),
    )
    assert resp.status_code == 400
    assert resp.get_json()["error"]["code"] == "VALIDATION_ERROR"


def test_slot_invalid_end_datetime_format(client, admin_token):
    pid = _provider_id_10(client, admin_token)
    resp = client.post(
        "/api/slots",
        headers=_auth_10(admin_token),
        json=_slot_body_10(pid, "2026-11-01T10:00:00", "not-a-datetime"),
    )
    assert resp.status_code == 400
    assert resp.get_json()["error"]["code"] == "VALIDATION_ERROR"


def test_slot_duplicate_is_conflict_and_rolls_back(client, admin_token):
    """Identical (provider, start, end) violates uq_provider_slot -> 409, session recovers."""
    pid = _provider_id_10(client, admin_token)
    body = _slot_body_10(pid, "2026-11-05T09:00:00", "2026-11-05T10:00:00")

    first = client.post("/api/slots", headers=_auth_10(admin_token), json=body)
    assert first.status_code == 201

    dup = client.post("/api/slots", headers=_auth_10(admin_token), json=body)
    assert dup.status_code == 409
    assert dup.get_json()["error"]["code"] == "CONFLICT"

    # After the rollback the session must still be healthy: a different slot succeeds.
    recover = client.post(
        "/api/slots",
        headers=_auth_10(admin_token),
        json=_slot_body_10(pid, "2026-11-05T11:00:00", "2026-11-05T12:00:00"),
    )
    assert recover.status_code == 201


def test_slot_overlapping_currently_allowed(client, admin_token):
    """GAP: overlapping (non-identical) slots are accepted today (no overlap validation)."""
    pid = _provider_id_10(client, admin_token)
    base = client.post(
        "/api/slots",
        headers=_auth_10(admin_token),
        json=_slot_body_10(pid, "2026-11-10T09:00:00", "2026-11-10T11:00:00"),
    )
    assert base.status_code == 201

    overlapping = client.post(
        "/api/slots",
        headers=_auth_10(admin_token),
        json=_slot_body_10(pid, "2026-11-10T10:00:00", "2026-11-10T12:00:00"),
    )
    # Pinned current behaviour: accepted. Change to expect 409 if overlap validation is added.
    assert overlapping.status_code == 201


def test_slot_end_before_start_currently_allowed(client, admin_token):
    """GAP: end < start is accepted today (no temporal ordering validation)."""
    pid = _provider_id_10(client, admin_token)
    resp = client.post(
        "/api/slots",
        headers=_auth_10(admin_token),
        json=_slot_body_10(pid, "2026-11-15T14:00:00", "2026-11-15T10:00:00"),
    )
    assert resp.status_code == 201  # Pinned current behaviour.


def test_slot_zero_duration_currently_allowed(client, admin_token):
    """GAP: start == end (zero-length slot) is accepted today."""
    pid = _provider_id_10(client, admin_token)
    resp = client.post(
        "/api/slots",
        headers=_auth_10(admin_token),
        json=_slot_body_10(pid, "2026-11-16T10:00:00", "2026-11-16T10:00:00"),
    )
    assert resp.status_code == 201


def test_slot_creation_requires_privileged_role(client, resident_token, admin_token):
    pid = _provider_id_10(client, admin_token)
    resp = client.post(
        "/api/slots",
        headers=_auth_10(resident_token),
        json=_slot_body_10(pid, "2026-11-20T10:00:00", "2026-11-20T11:00:00"),
    )
    assert resp.status_code == 403
    assert resp.get_json()["error"]["code"] == "FORBIDDEN"


def test_provider_cannot_create_slot_for_other_provider(client, admin_token, provider_token):
    """A service_provider may only manage their own slots."""
    # Find a provider profile that does NOT belong to the logged-in provider user.
    providers = client.get("/api/providers", headers=_auth_10(admin_token)).get_json()["data"]["items"]
    me = client.get("/api/users/me", headers=_auth_10(provider_token)).get_json()["data"]
    foreign = next(p for p in providers if p["user_id"] != me["id"])

    resp = client.post(
        "/api/slots",
        headers=_auth_10(provider_token),
        json=_slot_body_10(foreign["id"], "2026-11-25T10:00:00", "2026-11-25T11:00:00"),
    )
    assert resp.status_code == 403
    assert resp.get_json()["error"]["code"] == "FORBIDDEN"


def test_update_slot_with_invalid_datetime(client, admin_token):
    pid = _provider_id_10(client, admin_token)
    created = client.post(
        "/api/slots",
        headers=_auth_10(admin_token),
        json=_slot_body_10(pid, "2026-11-28T10:00:00", "2026-11-28T11:00:00"),
    )
    slot_id = created.get_json()["data"]["id"]

    resp = client.put(
        f"/api/slots/{slot_id}",
        headers=_auth_10(admin_token),
        json={"slot_start": "garbage"},
    )
    assert resp.status_code == 400
    assert resp.get_json()["error"]["code"] == "VALIDATION_ERROR"


def test_update_missing_slot_returns_404(client, admin_token):
    resp = client.put("/api/slots/987654", headers=_auth_10(admin_token), json={"is_available": False})
    assert resp.status_code == 404
    assert resp.get_json()["error"]["code"] == "NOT_FOUND"


# ============================================================================
# test_11_bookings_concurrency.py
#
# Booking concurrency, slot-availability transitions and rollback behaviour.
#
# Covers: a slot can only be booked once (second booking on a held slot ->
# 409 SLOT_UNAVAILABLE), declining/cancelling releases the slot so it can be
# re-booked, booking a non-existent slot, access-control on read/cancel, and a
# simulated commit failure that must roll back and leave the slot untouched.
# ============================================================================

def _auth_11(token):
    return {"Authorization": f"Bearer {token}"}


def _provider_id_11(client, admin_token):
    return client.get("/api/providers", headers=_auth_11(admin_token)).get_json()["data"]["items"][0]["id"]


def _make_slot_11(client, admin_token, pid, start, end):
    resp = client.post(
        "/api/slots",
        headers=_auth_11(admin_token),
        json={"provider_id": pid, "slot_start": start, "slot_end": end, "is_available": True},
    )
    assert resp.status_code == 201
    return resp.get_json()["data"]["id"]


def test_slot_cannot_be_double_booked(client, admin_token, resident_token):
    pid = _provider_id_11(client, admin_token)
    slot_id = _make_slot_11(client, admin_token, pid, "2026-12-01T10:00:00", "2026-12-01T11:00:00")

    first = client.post(
        "/api/bookings",
        headers=_auth_11(resident_token),
        json={"provider_id": pid, "slot_id": slot_id},
    )
    assert first.status_code == 201

    second = client.post(
        "/api/bookings",
        headers=_auth_11(resident_token),
        json={"provider_id": pid, "slot_id": slot_id},
    )
    assert second.status_code == 409
    assert second.get_json()["error"]["code"] == "SLOT_UNAVAILABLE"


def test_booking_marks_slot_unavailable_in_availability_feed(client, admin_token, resident_token):
    pid = _provider_id_11(client, admin_token)
    slot_id = _make_slot_11(client, admin_token, pid, "2026-12-02T10:00:00", "2026-12-02T11:00:00")

    client.post("/api/bookings", headers=_auth_11(resident_token), json={"provider_id": pid, "slot_id": slot_id})

    avail = client.get(f"/api/providers/{pid}/availability", headers=_auth_11(admin_token)).get_json()["data"]
    assert slot_id not in [s["id"] for s in avail]


def test_declined_booking_releases_slot_for_rebooking(client, admin_token, resident_token, provider_token):
    pid = _provider_id_11(client, admin_token)
    slot_id = _make_slot_11(client, admin_token, pid, "2026-12-03T10:00:00", "2026-12-03T11:00:00")

    b1 = client.post("/api/bookings", headers=_auth_11(resident_token), json={"provider_id": pid, "slot_id": slot_id})
    b1_id = b1.get_json()["data"]["id"]

    decline = client.put(f"/api/bookings/{b1_id}/decline", headers=_auth_11(provider_token))
    assert decline.status_code == 200
    assert decline.get_json()["data"]["booking_status"] == "declined"

    # Slot freed -> a new booking on the same slot now succeeds.
    b2 = client.post("/api/bookings", headers=_auth_11(resident_token), json={"provider_id": pid, "slot_id": slot_id})
    assert b2.status_code == 201


def test_cancelled_booking_releases_slot(client, admin_token, resident_token):
    pid = _provider_id_11(client, admin_token)
    slot_id = _make_slot_11(client, admin_token, pid, "2026-12-04T10:00:00", "2026-12-04T11:00:00")

    b1 = client.post("/api/bookings", headers=_auth_11(resident_token), json={"provider_id": pid, "slot_id": slot_id})
    b1_id = b1.get_json()["data"]["id"]

    cancel = client.put(f"/api/bookings/{b1_id}/cancel", headers=_auth_11(resident_token))
    assert cancel.status_code == 200
    assert cancel.get_json()["data"]["booking_status"] == "cancelled"

    avail = client.get(f"/api/providers/{pid}/availability", headers=_auth_11(admin_token)).get_json()["data"]
    assert slot_id in [s["id"] for s in avail]


def test_booking_missing_provider_field(client, resident_token):
    resp = client.post("/api/bookings", headers=_auth_11(resident_token), json={"request_notes": "no provider"})
    assert resp.status_code == 400
    assert resp.get_json()["error"]["code"] == "VALIDATION_ERROR"


def test_booking_unavailable_slot_rejected(client, admin_token, resident_token):
    """A slot explicitly created as unavailable cannot be booked."""
    pid = _provider_id_11(client, admin_token)
    created = client.post(
        "/api/slots",
        headers=_auth_11(admin_token),
        json={"provider_id": pid, "slot_start": "2026-12-05T10:00:00", "slot_end": "2026-12-05T11:00:00", "is_available": False},
    )
    slot_id = created.get_json()["data"]["id"]

    resp = client.post("/api/bookings", headers=_auth_11(resident_token), json={"provider_id": pid, "slot_id": slot_id})
    assert resp.status_code == 409
    assert resp.get_json()["error"]["code"] == "SLOT_UNAVAILABLE"


def test_get_booking_forbidden_for_unrelated_user(client, admin_token, resident_token, security_token):
    pid = _provider_id_11(client, admin_token)
    slot_id = _make_slot_11(client, admin_token, pid, "2026-12-06T10:00:00", "2026-12-06T11:00:00")
    b = client.post("/api/bookings", headers=_auth_11(resident_token), json={"provider_id": pid, "slot_id": slot_id})
    b_id = b.get_json()["data"]["id"]

    # A security user who is neither the resident nor the provider is forbidden.
    resp = client.get(f"/api/bookings/{b_id}", headers=_auth_11(security_token))
    assert resp.status_code == 403
    assert resp.get_json()["error"]["code"] == "FORBIDDEN"


def test_cancel_booking_forbidden_for_non_owner(client, admin_token, resident_token, security_token):
    pid = _provider_id_11(client, admin_token)
    slot_id = _make_slot_11(client, admin_token, pid, "2026-12-07T10:00:00", "2026-12-07T11:00:00")
    b = client.post("/api/bookings", headers=_auth_11(resident_token), json={"provider_id": pid, "slot_id": slot_id})
    b_id = b.get_json()["data"]["id"]

    resp = client.put(f"/api/bookings/{b_id}/cancel", headers=_auth_11(security_token))
    assert resp.status_code == 403


def test_accept_missing_booking_returns_404(client, provider_token):
    resp = client.put("/api/bookings/888888/accept", headers=_auth_11(provider_token))
    assert resp.status_code == 404
    assert resp.get_json()["error"]["code"] == "NOT_FOUND"


def test_booking_commit_failure_rolls_back(client, admin_token, resident_token, monkeypatch):
    """If the commit fails, the API returns a consistent 500 and the transaction is rolled back."""
    pid = _provider_id_11(client, admin_token)
    slot_id = _make_slot_11(client, admin_token, pid, "2026-12-08T10:00:00", "2026-12-08T11:00:00")

    def boom():
        raise SQLAlchemyError("simulated commit failure")

    monkeypatch.setattr(db.session, "commit", boom)
    resp = client.post("/api/bookings", headers=_auth_11(resident_token), json={"provider_id": pid, "slot_id": slot_id})
    assert resp.status_code == 500
    assert resp.get_json()["error"]["code"] == "DB_ERROR"
    monkeypatch.undo()

    # Rollback means the slot was never consumed: it is still bookable.
    ok_resp = client.post("/api/bookings", headers=_auth_11(resident_token), json={"provider_id": pid, "slot_id": slot_id})
    assert ok_resp.status_code == 201


# ============================================================================
# test_12_complaints_transitions.py
#
# Complaint assignment / status-transition edge cases and side-effects.
#
# Notes:
# - There is no external notification dispatcher to mock. The observable
#   "side-effect" of assign/status changes is the ComplaintUpdate audit trail
#   appended to the complaint; these tests assert those records are created with
#   the right status/comment, which is the notification analogue in this system.
# - The status endpoint performs NO state-machine validation, so arbitrary status
#   strings are accepted today. That behaviour is pinned so a future validation
#   change is caught deliberately.
# ============================================================================

def _auth_12(token):
    return {"Authorization": f"Bearer {token}"}


def _raise_complaint_12(client, resident_token, subject="Broken gate"):
    resp = client.post(
        "/api/complaints",
        headers=_auth_12(resident_token),
        json={"subject": subject, "description": "details", "category": "Maintenance", "priority": "high"},
    )
    assert resp.status_code == 201
    return resp.get_json()["data"]["id"]


def _resident_id_12(client, resident_token):
    return client.get("/api/users/me", headers=_auth_12(resident_token)).get_json()["data"]["id"]


def test_assign_requires_assignee(client, admin_token, resident_token):
    cid = _raise_complaint_12(client, resident_token)
    resp = client.put(f"/api/complaints/{cid}/assign", headers=_auth_12(admin_token), json={})
    assert resp.status_code == 400
    assert resp.get_json()["error"]["code"] == "VALIDATION_ERROR"


def test_assign_sets_in_progress_and_records_update(client, admin_token, resident_token, security_token):
    cid = _raise_complaint_12(client, resident_token)
    sec_id = client.get("/api/users/me", headers=_auth_12(security_token)).get_json()["data"]["id"]

    resp = client.put(
        f"/api/complaints/{cid}/assign",
        headers=_auth_12(admin_token),
        json={"assigned_to_user_id": sec_id, "comment": "Please handle"},
    )
    assert resp.status_code == 200
    assert resp.get_json()["data"]["status"] == "in_progress"
    assert resp.get_json()["data"]["assigned_to_user_id"] == sec_id

    # Side-effect: the audit trail now contains the submission + assignment entries.
    detail = client.get(f"/api/complaints/{cid}", headers=_auth_12(admin_token)).get_json()["data"]
    assert len(detail["updates"]) == 2
    last = detail["updates"][-1]
    assert last["status"] == "in_progress"
    assert last["comment"] == "Please handle"


def test_assign_requires_admin_role(client, resident_token):
    cid = _raise_complaint_12(client, resident_token)
    resp = client.put(
        f"/api/complaints/{cid}/assign",
        headers=_auth_12(resident_token),
        json={"assigned_to_user_id": 4},
    )
    assert resp.status_code == 403
    assert resp.get_json()["error"]["code"] == "FORBIDDEN"


def test_assign_missing_complaint_returns_404(client, admin_token):
    resp = client.put("/api/complaints/777777/assign", headers=_auth_12(admin_token), json={"assigned_to_user_id": 4})
    assert resp.status_code == 404
    assert resp.get_json()["error"]["code"] == "NOT_FOUND"


def test_status_update_requires_status_and_comment(client, admin_token, resident_token):
    cid = _raise_complaint_12(client, resident_token)
    # Missing comment.
    resp = client.put(f"/api/complaints/{cid}/status", headers=_auth_12(admin_token), json={"status": "resolved"})
    assert resp.status_code == 400
    assert resp.get_json()["error"]["code"] == "VALIDATION_ERROR"
    # Missing status.
    resp2 = client.put(f"/api/complaints/{cid}/status", headers=_auth_12(admin_token), json={"comment": "done"})
    assert resp2.status_code == 400
    assert resp2.get_json()["error"]["code"] == "VALIDATION_ERROR"


def test_status_update_records_audit_entry(client, admin_token, resident_token):
    cid = _raise_complaint_12(client, resident_token)
    resp = client.put(
        f"/api/complaints/{cid}/status",
        headers=_auth_12(admin_token),
        json={"status": "resolved", "comment": "Fixed on site"},
    )
    assert resp.status_code == 200
    assert resp.get_json()["data"]["status"] == "resolved"

    detail = client.get(f"/api/complaints/{cid}", headers=_auth_12(admin_token)).get_json()["data"]
    last = detail["updates"][-1]
    assert last["status"] == "resolved"
    assert last["comment"] == "Fixed on site"


def test_status_update_rejects_arbitrary_status(client, admin_token, resident_token):
    """An unknown status string is rejected (defect D-05, fixed in Milestone 4).

    Previously this test pinned the buggy behaviour: any string was written
    straight into the status column, which broke every status filter and
    dashboard count downstream. The expectation was updated when the
    validator was added.
    """
    cid = _raise_complaint_12(client, resident_token)
    resp = client.put(
        f"/api/complaints/{cid}/status",
        headers=_auth_12(admin_token),
        json={"status": "not_a_real_status", "comment": "arbitrary"},
    )
    assert resp.status_code == 400
    assert resp.get_json()["error"]["code"] == "VALIDATION_ERROR"

    unchanged = client.get(f"/api/complaints/{cid}", headers=_auth_12(admin_token))
    assert unchanged.get_json()["data"]["status"] == "open"


def test_status_update_forbidden_for_non_assignee(client, admin_token, resident_token, provider_token):
    """A user who is neither admin nor the assignee cannot change status."""
    cid = _raise_complaint_12(client, resident_token)
    resp = client.put(
        f"/api/complaints/{cid}/status",
        headers=_auth_12(provider_token),
        json={"status": "resolved", "comment": "nope"},
    )
    assert resp.status_code == 403
    assert resp.get_json()["error"]["code"] == "FORBIDDEN"


def test_assignee_can_update_status_after_assignment(client, admin_token, resident_token, security_token):
    cid = _raise_complaint_12(client, resident_token)
    sec_id = client.get("/api/users/me", headers=_auth_12(security_token)).get_json()["data"]["id"]
    client.put(
        f"/api/complaints/{cid}/assign",
        headers=_auth_12(admin_token),
        json={"assigned_to_user_id": sec_id},
    )

    resp = client.put(
        f"/api/complaints/{cid}/status",
        headers=_auth_12(security_token),
        json={"status": "resolved", "comment": "Handled by security"},
    )
    assert resp.status_code == 200
    assert resp.get_json()["data"]["status"] == "resolved"


def test_add_update_requires_comment(client, admin_token, resident_token):
    cid = _raise_complaint_12(client, resident_token)
    resp = client.post(f"/api/complaints/{cid}/updates", headers=_auth_12(admin_token), json={})
    assert resp.status_code == 400
    assert resp.get_json()["error"]["code"] == "VALIDATION_ERROR"


def test_add_update_forbidden_for_unrelated_user(client, resident_token, provider_token):
    cid = _raise_complaint_12(client, resident_token)
    resp = client.post(
        f"/api/complaints/{cid}/updates",
        headers=_auth_12(provider_token),
        json={"comment": "I should not be allowed"},
    )
    assert resp.status_code == 403
    assert resp.get_json()["error"]["code"] == "FORBIDDEN"


def test_status_update_missing_complaint_returns_404(client, admin_token):
    resp = client.put(
        "/api/complaints/654321/status",
        headers=_auth_12(admin_token),
        json={"status": "resolved", "comment": "x"},
    )
    assert resp.status_code == 404
    assert resp.get_json()["error"]["code"] == "NOT_FOUND"


# ============================================================================
# test_13_db_failure_paths.py
#
# Database failure / rollback paths.
#
# These tests deliberately induce database errors and assert that the API returns
# a consistent error envelope and rolls back, rather than leaking a stack trace or
# committing partial state:
#
# - A raw SQLAlchemyError on commit -> 500 DB_ERROR (registered error handler).
# - An IntegrityError from a real unique-constraint violation -> 409 CONFLICT.
# - After each failure the session must recover so subsequent requests succeed.
# ============================================================================

def _auth_13(token):
    return {"Authorization": f"Bearer {token}"}


def _unique_email_13():
    import uuid

    return f"user_{uuid.uuid4().hex[:10]}@socioneed.com"


def test_register_commit_failure_returns_db_error(client, monkeypatch):
    def boom():
        raise SQLAlchemyError("simulated failure")

    monkeypatch.setattr(db.session, "commit", boom)
    resp = client.post(
        "/api/auth/register",
        json={
            "full_name": "DB Fail User",
            "email": _unique_email_13(),
            "password": "123456",
            "role": "owner",
            "society_id": 1,
        },
    )
    assert resp.status_code == 500
    body = resp.get_json()
    assert body["success"] is False
    assert body["error"]["code"] == "DB_ERROR"


def test_session_recovers_after_commit_failure(client, monkeypatch):
    def boom():
        raise SQLAlchemyError("simulated failure")

    monkeypatch.setattr(db.session, "commit", boom)
    failed = client.post(
        "/api/auth/register",
        json={"full_name": "X", "email": _unique_email_13(), "password": "123456", "role": "owner", "society_id": 1},
    )
    assert failed.status_code == 500
    monkeypatch.undo()

    # The handler rolled back; a normal request now works.
    ok_resp = client.post(
        "/api/auth/register",
        json={"full_name": "Recovered", "email": _unique_email_13(), "password": "123456", "role": "owner", "society_id": 1},
    )
    assert ok_resp.status_code == 201


def test_duplicate_phone_triggers_integrity_conflict(client):
    """Phone uniqueness is enforced at the DB layer (not pre-checked in code),
    so a duplicate phone surfaces as an IntegrityError -> 409 CONFLICT."""
    resp = client.post(
        "/api/auth/register",
        json={
            "full_name": "Phone Clash",
            "email": _unique_email_13(),
            "phone": "9000000002",  # already used by the seeded resident
            "password": "123456",
            "role": "owner",
            "society_id": 1,
        },
    )
    assert resp.status_code == 409
    assert resp.get_json()["error"]["code"] == "CONFLICT"


def test_complaint_create_commit_failure_rolls_back(client, resident_token, monkeypatch):
    def boom():
        raise SQLAlchemyError("simulated failure")

    monkeypatch.setattr(db.session, "commit", boom)
    resp = client.post(
        "/api/complaints",
        headers=_auth_13(resident_token),
        json={"subject": "S", "description": "D", "category": "Maintenance", "priority": "low"},
    )
    assert resp.status_code == 500
    assert resp.get_json()["error"]["code"] == "DB_ERROR"
    monkeypatch.undo()

    # No partial complaint persisted; a real create afterward succeeds.
    ok_resp = client.post(
        "/api/complaints",
        headers=_auth_13(resident_token),
        json={"subject": "Real", "description": "D", "category": "Maintenance", "priority": "low"},
    )
    assert ok_resp.status_code == 201


def test_category_create_commit_failure_returns_db_error(client, admin_token, monkeypatch):
    def boom():
        raise SQLAlchemyError("simulated failure")

    monkeypatch.setattr(db.session, "commit", boom)
    resp = client.post(
        "/api/service-categories",
        headers=_auth_13(admin_token),
        json={"name": "TransientCategory", "description": "should not persist"},
    )
    assert resp.status_code == 500
    assert resp.get_json()["error"]["code"] == "DB_ERROR"


def test_duplicate_category_name_conflict(client, admin_token):
    """service_categories.name is unique -> duplicate creation is a 409 CONFLICT."""
    name = "UniqueCat_DBTest"
    first = client.post(
        "/api/service-categories",
        headers=_auth_13(admin_token),
        json={"name": name, "description": "first"},
    )
    assert first.status_code == 201

    dup = client.post(
        "/api/service-categories",
        headers=_auth_13(admin_token),
        json={"name": name, "description": "second"},
    )
    assert dup.status_code == 409
    assert dup.get_json()["error"]["code"] == "CONFLICT"


def test_error_envelope_shape_is_consistent(client, monkeypatch):
    """Every failure path must use the same {success, error:{code,message}} envelope."""
    def boom():
        raise SQLAlchemyError("simulated failure")

    monkeypatch.setattr(db.session, "commit", boom)
    resp = client.post(
        "/api/auth/register",
        json={"full_name": "Shape", "email": _unique_email_13(), "password": "123456", "role": "owner", "society_id": 1},
    )
    body = resp.get_json()
    assert set(body.keys()) == {"success", "error"}
    assert set(body["error"].keys()) == {"code", "message"}
    assert body["success"] is False


# ============================================================================
# test_14_ai_features.py
#
# AI feature tests for SocioNeed.
#
# Gemini is mocked so tests are deterministic, offline, and free. We monkeypatch
# the ``generate_json`` / ``generate_text`` names inside ``app.api.ai`` (where they
# are used) rather than calling the real Gemini API.
# ============================================================================

def _auth_14(token):
    return {"Authorization": f"Bearer {token}"}


_FAKE_AI_JSON_14 = {
    # notice generator
    "title": "Water Tank Cleaning",
    "body": "Dear Residents, the water tanks will be cleaned on Sunday. Thank you.",
    # multilingual
    "translations": {"English": "Hello", "Hindi": "Namaste", "Telugu": "Namaskaram"},
    # complaint classification
    "category": "Water",
    "priority": "High",
    "sentiment": "Negative",
    "confidence": 0.9,
    "rationale": "No water reported in a block.",
    # analytics / resolution insights
    "insight": "Water issues are the largest and slowest category.",
    "suggested_actions": ["Inspect the Block C supply line"],
    "recommended_actions": ["Schedule a pump inspection"],
    "recurring_issues": ["Block C water pressure recurring"],
    "highlights": ["6 water complaints open over a week"],
    # daily summary
    "headline": "Calm day in the society",
    "summary": "Water maintenance in the morning; yoga in the evening.",
    "sections": [{"label": "Notices", "text": "Water tank cleaning."}],
    # meeting minutes
    "key_discussions": ["Budget for Diwali"],
    "decisions": ["Approve 50k budget"],
    "action_items": [{"task": "Book hall", "responsible": "Secretary", "deadline": "Fri"}],
    "minutes_markdown": "## Minutes",
    # notice summarizer (single + all)
    "what": "Water tank cleaning",
    "when": "Sunday 9-1",
    "where": "All blocks",
    "impact": "Supply affected",
    "action": "Store water",
    "groups": [{"theme": "Maintenance", "items": ["Water tank cleaning Sunday"]}],
    "digest_markdown": "This week: water tank cleaning on Sunday.",
    # rules Q&A
    "answered": True,
    "answer": "Yes, the clubhouse can be booked for private events per Notice 3.",
    "source_hint": "Notice 3",
    # feedback analyzer
    "draft_poll": {"question": "Do you want a new gym?", "options": ["Yes", "No"]},
    "themes": [{"theme": "cost", "mentions": 3}],
    "suggested_next_step": "Share a cost estimate before the vote.",
    "summary_markdown": "62% support a new gym.",
    # amenity booking
    "amenity": "clubhouse",
    "requested_when": "Saturday evening",
    "conflicts": [],
    "suggested_slots": ["Saturday 6:00 PM - 9:00 PM"],
    "note": "Slot appears free; confirm to book.",
    "confirmation_required": True,
    # bill explainer / maintenance
    "explanation": "Your total is the sum of the listed charges.",
    "equipment": "Lift",
    "maintenance_type": "Preventive",
    "checklist": ["Check cables"],
    "recommended_follow_up": "Monthly inspection",
    "assistant_markdown": "## Checklist",
}


@pytest.fixture()
def fake_ai_14(monkeypatch):
    """Patch Gemini so no network call is made and output is deterministic."""
    monkeypatch.setattr(ai_module, "generate_json", lambda *a, **k: dict(_FAKE_AI_JSON_14))
    monkeypatch.setattr(ai_module, "generate_text", lambda *a, **k: "AI generated text.")
    return _FAKE_AI_JSON_14


def test_ai_status_lists_features(client, admin_token):
    resp = client.get("/api/ai/status", headers=_auth_14(admin_token))
    assert resp.status_code == 200
    features = resp.get_json()["data"]["features"]
    for f in ("complaint_resolution_insights", "rules_qa", "feedback_analyzer",
              "amenity_booking_assistant", "notices_summarize_all"):
        assert f in features


def test_notice_generate_success(client, admin_token, fake_ai_14):
    resp = client.post("/api/ai/notices/generate", headers=_auth_14(admin_token),
                       json={"topic": "Water tank cleaning", "date": "Sunday"})
    assert resp.status_code == 200
    data = resp.get_json()["data"]
    assert data["title"] and data["body"]


def test_notice_generate_missing_topic_fails(client, admin_token, fake_ai_14):
    resp = client.post("/api/ai/notices/generate", headers=_auth_14(admin_token), json={})
    assert resp.status_code == 400


def test_notice_generate_requires_admin(client, resident_token, fake_ai_14):
    resp = client.post("/api/ai/notices/generate", headers=_auth_14(resident_token),
                       json={"topic": "x"})
    assert resp.status_code == 403


def test_translate_success(client, admin_token, fake_ai_14):
    resp = client.post("/api/ai/announcements/translate", headers=_auth_14(admin_token),
                       json={"text": "Water off tomorrow", "languages": ["Hindi", "Telugu"]})
    assert resp.status_code == 200
    assert isinstance(resp.get_json()["data"]["translations"], dict)


def test_translate_missing_text_fails(client, admin_token, fake_ai_14):
    resp = client.post("/api/ai/announcements/translate", headers=_auth_14(admin_token), json={})
    assert resp.status_code == 400


def test_classify_complaint_success(client, resident_token, fake_ai_14):
    resp = client.post("/api/ai/complaints/classify", headers=_auth_14(resident_token),
                       json={"subject": "No water", "description": "No water in Block B since morning."})
    assert resp.status_code == 200
    data = resp.get_json()["data"]
    assert data["category"] == "Water"
    assert data["priority"] in {"High", "Medium", "Low"}
    assert data["suggestion_only"] is True  # AI is advisory, admin overrides


def test_admin_ai_classify_complaint_and_priority(client, admin_token, fake_ai_14):
    resp = client.post("/api/ai/complaints/classify", headers=_auth_14(admin_token),
                       json={"subject": "Severe lift malfunction", "description": "Lift trapped on 4th floor with noise."})
    assert resp.status_code == 200
    data = resp.get_json()["data"]
    assert "priority" in data
    assert "category" in data


def test_classify_missing_description_fails(client, resident_token, fake_ai_14):
    resp = client.post("/api/ai/complaints/classify", headers=_auth_14(resident_token),
                       json={"subject": "No water"})
    assert resp.status_code == 400


def test_summarize_all_with_payload(client, resident_token, fake_ai_14):
    resp = client.post("/api/ai/notices/summarize-all", headers=_auth_14(resident_token),
                       json={"notices": [{"title": "Water", "body": "Cleaning Sunday"}]})
    assert resp.status_code == 200
    data = resp.get_json()["data"]
    assert data["count"] == 1
    assert "groups" in data


def test_summarize_all_requires_auth(client, fake_ai_14):
    resp = client.post("/api/ai/notices/summarize-all", json={"notices": [{"title": "x", "body": "y"}]})
    assert resp.status_code == 401


def test_resolution_insights_with_stats(client, admin_token, fake_ai_14):
    resp = client.post("/api/ai/complaints/resolution-insights", headers=_auth_14(admin_token),
                       json={"stats": {"pending": 9, "pending_over_7_days": 6}})
    assert resp.status_code == 200
    data = resp.get_json()["data"]
    assert data["stats"]["pending"] == 9
    assert "recommended_actions" in data


def test_resolution_insights_requires_admin(client, resident_token, fake_ai_14):
    resp = client.post("/api/ai/complaints/resolution-insights", headers=_auth_14(resident_token), json={})
    assert resp.status_code == 403


def test_rules_qa_success(client, resident_token, fake_ai_14):
    resp = client.post("/api/ai/knowledge/ask", headers=_auth_14(resident_token),
                       json={"question": "Can I book the clubhouse?",
                             "documents": ["Notice 3: clubhouse may be booked for private events."]})
    assert resp.status_code == 200
    data = resp.get_json()["data"]
    assert data["answered"] is True
    assert data["answer"]


def test_rules_qa_missing_question_fails(client, resident_token, fake_ai_14):
    resp = client.post("/api/ai/knowledge/ask", headers=_auth_14(resident_token),
                       json={"documents": ["some rule"]})
    assert resp.status_code == 400


def test_feedback_analyze_success(client, admin_token, fake_ai_14):
    resp = client.post("/api/ai/feedback/analyze", headers=_auth_14(admin_token),
                       json={"goal": "gauge interest in a gym",
                             "responses": ["Too costly", "Great idea", "Need space"]})
    assert resp.status_code == 200
    data = resp.get_json()["data"]
    assert data["response_count"] == 3
    assert "themes" in data


def test_feedback_analyze_empty_fails(client, admin_token, fake_ai_14):
    resp = client.post("/api/ai/feedback/analyze", headers=_auth_14(admin_token), json={})
    assert resp.status_code == 400


def test_feedback_requires_admin(client, resident_token, fake_ai_14):
    resp = client.post("/api/ai/feedback/analyze", headers=_auth_14(resident_token),
                       json={"goal": "x"})
    assert resp.status_code == 403


def test_amenity_assist_success(client, resident_token, fake_ai_14):
    resp = client.post("/api/ai/amenities/assist", headers=_auth_14(resident_token),
                       json={"request": "book the clubhouse next Saturday evening for 30 people"})
    assert resp.status_code == 200
    data = resp.get_json()["data"]
    assert data["confirmation_required"] is True  # AI never finalizes a booking
    assert "suggested_slots" in data


def test_amenity_assist_missing_request_fails(client, resident_token, fake_ai_14):
    resp = client.post("/api/ai/amenities/assist", headers=_auth_14(resident_token), json={})
    assert resp.status_code == 400


def test_ai_provider_error_returns_502(client, admin_token, monkeypatch):
    def boom(*a, **k):
        raise GeminiServiceError("model overloaded")
    monkeypatch.setattr(ai_module, "generate_json", boom)
    resp = client.post("/api/ai/notices/generate", headers=_auth_14(admin_token),
                       json={"topic": "x"})
    assert resp.status_code == 502
    assert resp.get_json()["error"]["code"] == "AI_ERROR"


def test_ai_config_error_returns_503(client, admin_token, monkeypatch):
    def missing_key(*a, **k):
        raise GeminiServiceError("GEMINI_API_KEY is missing. Add it to backend/.env.")
    monkeypatch.setattr(ai_module, "generate_json", missing_key)
    resp = client.post("/api/ai/notices/generate", headers=_auth_14(admin_token),
                       json={"topic": "x"})
    assert resp.status_code == 503
    assert resp.get_json()["error"]["code"] == "AI_CONFIG_ERROR"


def test_event_plan_success(client, admin_token, fake_ai_14):
    resp = client.post("/api/ai/events/plan", headers=_auth_14(admin_token),
                       json={"event_name": "Diwali", "expected_residents": "200",
                             "duration": "4h", "budget": "50000"})
    assert resp.status_code == 200


def test_event_plan_missing_name_fails(client, admin_token, fake_ai_14):
    resp = client.post("/api/ai/events/plan", headers=_auth_14(admin_token), json={})
    assert resp.status_code == 400


def test_analytics_insights_with_stats(client, admin_token, fake_ai_14):
    resp = client.post("/api/ai/analytics/insights", headers=_auth_14(admin_token),
                       json={"stats": {"water": 35, "parking": 27}})
    assert resp.status_code == 200
    assert resp.get_json()["data"]["stats"]["water"] == 35


def test_analytics_insights_default_snapshot(client, admin_token, fake_ai_14):
    # No stats provided -> backend aggregates from DB.
    resp = client.post("/api/ai/analytics/insights", headers=_auth_14(admin_token), json={})
    assert resp.status_code == 200
    assert "stats" in resp.get_json()["data"]


def test_meeting_minutes_success(client, admin_token, fake_ai_14):
    resp = client.post("/api/ai/meetings/minutes", headers=_auth_14(admin_token),
                       json={"notes": "Discussed budget and security.", "title": "AGM"})
    assert resp.status_code == 200


def test_meeting_minutes_missing_notes_fails(client, admin_token, fake_ai_14):
    resp = client.post("/api/ai/meetings/minutes", headers=_auth_14(admin_token), json={})
    assert resp.status_code == 400


def test_notice_summarize_single_success(client, resident_token, fake_ai_14):
    resp = client.post("/api/ai/notices/summarize", headers=_auth_14(resident_token),
                       json={"title": "Water", "body": "Cleaning Sunday 9-1, supply affected."})
    assert resp.status_code == 200


def test_maintenance_assist_success(client, admin_token, fake_ai_14):
    resp = client.post("/api/ai/maintenance/assist", headers=_auth_14(admin_token),
                       json={"equipment": "Lift", "query": "monthly checklist"})
    assert resp.status_code == 200


def test_maintenance_assist_empty_fails(client, admin_token, fake_ai_14):
    resp = client.post("/api/ai/maintenance/assist", headers=_auth_14(admin_token), json={})
    assert resp.status_code == 400


def test_raw_prompt_admin_only(client, resident_token, fake_ai_14):
    resp = client.post("/api/ai/raw", headers=_auth_14(resident_token), json={"prompt": "hi"})
    assert resp.status_code == 403


def test_raw_prompt_success(client, admin_token, fake_ai_14):
    resp = client.post("/api/ai/raw", headers=_auth_14(admin_token), json={"prompt": "hi"})
    assert resp.status_code == 200
    assert resp.get_json()["data"]["text"]


def test_summarize_all_default_db_path(client, resident_token, fake_ai_14):
    # No notices in payload -> backend pulls active notices from DB.
    resp = client.post("/api/ai/notices/summarize-all", headers=_auth_14(resident_token), json={})
    assert resp.status_code == 200


def test_resolution_insights_default_db_path(client, admin_token, fake_ai_14):
    resp = client.post("/api/ai/complaints/resolution-insights", headers=_auth_14(admin_token), json={})
    assert resp.status_code == 200
    assert "stats" in resp.get_json()["data"]


def test_rules_qa_default_db_documents(client, resident_token, fake_ai_14):
    # No documents supplied -> backend uses active notices as the knowledge base.
    resp = client.post("/api/ai/knowledge/ask", headers=_auth_14(resident_token),
                       json={"question": "What is scheduled?"})
    assert resp.status_code == 200


# ============================================================================
# test_15_gemini_service.py
#
# Unit tests for the Gemini service latency optimizations (client stubbed).
# ============================================================================

class _FakeModels_15:
    def __init__(self, text='{"ok": true}'):
        self.calls = 0
        self.last_config = None
        self.last_model = None
        self._text = text

    def generate_content(self, model=None, contents=None, config=None):
        self.calls += 1
        self.last_config = config
        self.last_model = model
        return type("Resp", (), {"text": self._text})()


class _FakeClient_15:
    def __init__(self, text='{"ok": true}'):
        self.models = _FakeModels_15(text)


@pytest.fixture()
def fake_client_15(app, monkeypatch):
    """Stub the cached genai client so no network call happens."""
    client = _FakeClient_15()
    monkeypatch.setattr(gs, "_client", lambda: client)
    gs.clear_response_cache()
    return client


def test_generate_json_parses_and_uses_json_config(app, fake_client_15):
    with app.app_context():
        result = gs.generate_json("do something", system="sys")
    assert result == {"ok": True}
    # JSON mode should request strict JSON output for speed + reliability.
    assert fake_client_15.models.last_config.response_mime_type == "application/json"
    assert fake_client_15.models.last_config.max_output_tokens == 2048


def test_response_cache_avoids_second_call(app, fake_client_15):
    with app.app_context():
        gs.generate_json("same prompt", system="sys")
        gs.generate_json("same prompt", system="sys")
    # Second identical call is served from cache → underlying model hit once.
    assert fake_client_15.models.calls == 1


def test_cache_clear_forces_new_call(app, fake_client_15):
    with app.app_context():
        gs.generate_json("prompt A")
        gs.clear_response_cache()
        gs.generate_json("prompt A")
    assert fake_client_15.models.calls == 2


def test_thinking_disabled_for_2_5_models(app, fake_client_15):
    app.config["GEMINI_MODEL"] = "gemini-2.5-flash"
    with app.app_context():
        gs.generate_json("hello")
    cfg = fake_client_15.models.last_config
    assert cfg.thinking_config is not None
    assert cfg.thinking_config.thinking_budget == 0


def test_no_thinking_config_for_non_2_5_models(app, fake_client_15):
    app.config["GEMINI_MODEL"] = "gemini-2.0-flash"
    with app.app_context():
        gs.generate_json("hello")
    assert fake_client_15.models.last_config.thinking_config is None


def test_empty_response_raises(app, monkeypatch):
    client = _FakeClient_15(text="")
    monkeypatch.setattr(gs, "_client", lambda: client)
    gs.clear_response_cache()
    with app.app_context():
        with pytest.raises(GeminiServiceError):
            gs.generate_text("x", use_cache=False)


def test_missing_api_key_raises(app):
    app.config["GEMINI_API_KEY"] = ""
    # Bypass the stub so the real _client() key check runs.
    with app.app_context():
        with pytest.raises(GeminiServiceError):
            gs.generate_text("x", use_cache=False)
