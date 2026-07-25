from datetime import UTC, datetime


def _auth(token):
    return {"Authorization": f"Bearer {token}"}


def _get_first_provider(client, admin_token):
    resp = client.get("/api/providers", headers=_auth(admin_token))
    assert resp.status_code == 200
    items = resp.get_json()["data"]["items"]
    if len(items) > 0:
        return items[0]["id"]

    users_resp = client.get("/api/users?role=service_provider", headers=_auth(admin_token))
    assert users_resp.status_code == 200
    provider_users = users_resp.get_json()["data"]["items"]
    assert len(provider_users) > 0

    categories_resp = client.get("/api/service-categories", headers=_auth(admin_token))
    assert categories_resp.status_code == 200
    categories = categories_resp.get_json()["data"]
    assert len(categories) > 0

    create_resp = client.post(
        "/api/providers",
        headers=_auth(admin_token),
        json={
            "user_id": provider_users[0]["id"],
            "category_id": categories[0]["id"],
            "business_name": "Pytest Provider",
            "service_description": "Auto-created for tests",
        },
    )
    assert create_resp.status_code == 201
    return create_resp.get_json()["data"]["id"]


def test_complaint_lifecycle(client, admin_token, resident_token):
    create = client.post(
        "/api/complaints",
        headers=_auth(resident_token),
        json={"subject": "Water leak", "description": "Near kitchen", "category": "Maintenance", "priority": "high"},
    )
    assert create.status_code == 201
    cid = create.get_json()["data"]["id"]

    detail = client.get(f"/api/complaints/{cid}", headers=_auth(resident_token))
    assert detail.status_code == 200
    assert "updates" in detail.get_json()["data"]

    assign = client.put(
        f"/api/complaints/{cid}/assign",
        headers=_auth(admin_token),
        json={"assigned_to_user_id": 4, "comment": "Assign security"},
    )
    assert assign.status_code == 200

    status = client.put(
        f"/api/complaints/{cid}/status",
        headers=_auth(admin_token),
        json={"status": "resolved", "comment": "done"},
    )
    assert status.status_code == 200


def test_booking_and_review_lifecycle(client, admin_token, resident_token, provider_token):
    provider_id = _get_first_provider(client, admin_token)

    ts = datetime.now(UTC).strftime("%H%M%S")
    slot = client.post(
        "/api/slots",
        headers=_auth(admin_token),
        json={
            "provider_id": provider_id,
            "slot_start": f"2026-07-30T10:{ts[:2]}:00",
            "slot_end": f"2026-07-30T11:{ts[:2]}:00",
            "is_available": True,
        },
    )
    assert slot.status_code == 201
    slot_id = slot.get_json()["data"]["id"]

    booking = client.post(
        "/api/bookings",
        headers=_auth(resident_token),
        json={"provider_id": provider_id, "slot_id": slot_id, "request_notes": "Test booking"},
    )
    assert booking.status_code == 201
    booking_id = booking.get_json()["data"]["id"]

    accept = client.put(f"/api/bookings/{booking_id}/accept", headers=_auth(provider_token))
    assert accept.status_code == 200

    complete = client.put(f"/api/bookings/{booking_id}/complete", headers=_auth(provider_token))
    assert complete.status_code == 200

    review = client.post(
        "/api/reviews",
        headers=_auth(resident_token),
        json={"provider_id": provider_id, "booking_id": booking_id, "rating": 5, "feedback": "great"},
    )
    assert review.status_code == 201


def test_visitors_analytics_reports(client, admin_token, security_token, resident_token):
    visitor = client.post(
        "/api/visitors",
        headers=_auth(security_token),
        json={
            "society_id": 1,
            "recorded_by_user_id": 4,
            "resident_user_id": 2,
            "visitor_name": "Guest One",
        },
    )
    assert visitor.status_code == 201
    entry_id = visitor.get_json()["data"]["id"]

    exit_call = client.put(f"/api/visitors/{entry_id}/exit", headers=_auth(security_token))
    assert exit_call.status_code == 200

    admin_dash = client.get("/api/analytics/dashboard/admin", headers=_auth(admin_token))
    assert admin_dash.status_code == 200

    resident_dash = client.get("/api/analytics/dashboard/resident", headers=_auth(resident_token))
    assert resident_dash.status_code == 200

    monthly = client.get("/api/reports/monthly", headers=_auth(admin_token))
    assert monthly.status_code == 200

