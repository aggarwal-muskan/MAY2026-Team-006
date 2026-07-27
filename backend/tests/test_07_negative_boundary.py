from datetime import UTC, datetime


def _auth(token):
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
        headers=_auth(resident_token),
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
        headers=_auth(resident_token),
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
    complaint_resp = client.get("/api/complaints/999999", headers=_auth(admin_token))
    assert complaint_resp.status_code == 404

    unit_resp = client.get("/api/units/999999", headers=_auth(admin_token))
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
    prov_resp = client.get("/api/providers", headers=_auth(admin_token))
    items = prov_resp.get_json()["data"]["items"]
    provider_id = items[0]["id"]

    ts = datetime.now(UTC).strftime("%H%M%S")
    slot = client.post(
        "/api/slots",
        headers=_auth(admin_token),
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
        headers=_auth(resident_token),
        json={"provider_id": provider_id, "slot_id": slot_id, "request_notes": "First user booking"},
    )
    assert booking1.status_code == 201

    booking2 = client.post(
        "/api/bookings",
        headers=_auth(resident_token),
        json={"provider_id": provider_id, "slot_id": slot_id, "request_notes": "Concurrent user booking attempt"},
    )
    assert booking2.status_code == 409
    assert booking2.get_json()["error"]["code"] == "SLOT_UNAVAILABLE"
