"""Booking concurrency, slot-availability transitions and rollback behaviour.

Covers: a slot can only be booked once (second booking on a held slot ->
409 SLOT_UNAVAILABLE), declining/cancelling releases the slot so it can be
re-booked, booking a non-existent slot, access-control on read/cancel, and a
simulated commit failure that must roll back and leave the slot untouched.
"""

from sqlalchemy.exc import SQLAlchemyError

from app.core.extensions import db


def _auth(token):
    return {"Authorization": f"Bearer {token}"}


def _provider_id(client, admin_token):
    return client.get("/api/providers", headers=_auth(admin_token)).get_json()["data"]["items"][0]["id"]


def _make_slot(client, admin_token, pid, start, end):
    resp = client.post(
        "/api/slots",
        headers=_auth(admin_token),
        json={"provider_id": pid, "slot_start": start, "slot_end": end, "is_available": True},
    )
    assert resp.status_code == 201
    return resp.get_json()["data"]["id"]


def test_slot_cannot_be_double_booked(client, admin_token, resident_token):
    pid = _provider_id(client, admin_token)
    slot_id = _make_slot(client, admin_token, pid, "2026-12-01T10:00:00", "2026-12-01T11:00:00")

    first = client.post(
        "/api/bookings",
        headers=_auth(resident_token),
        json={"provider_id": pid, "slot_id": slot_id},
    )
    assert first.status_code == 201

    second = client.post(
        "/api/bookings",
        headers=_auth(resident_token),
        json={"provider_id": pid, "slot_id": slot_id},
    )
    assert second.status_code == 409
    assert second.get_json()["error"]["code"] == "SLOT_UNAVAILABLE"


def test_booking_marks_slot_unavailable_in_availability_feed(client, admin_token, resident_token):
    pid = _provider_id(client, admin_token)
    slot_id = _make_slot(client, admin_token, pid, "2026-12-02T10:00:00", "2026-12-02T11:00:00")

    client.post("/api/bookings", headers=_auth(resident_token), json={"provider_id": pid, "slot_id": slot_id})

    avail = client.get(f"/api/providers/{pid}/availability", headers=_auth(admin_token)).get_json()["data"]
    assert slot_id not in [s["id"] for s in avail]


def test_declined_booking_releases_slot_for_rebooking(client, admin_token, resident_token, provider_token):
    pid = _provider_id(client, admin_token)
    slot_id = _make_slot(client, admin_token, pid, "2026-12-03T10:00:00", "2026-12-03T11:00:00")

    b1 = client.post("/api/bookings", headers=_auth(resident_token), json={"provider_id": pid, "slot_id": slot_id})
    b1_id = b1.get_json()["data"]["id"]

    decline = client.put(f"/api/bookings/{b1_id}/decline", headers=_auth(provider_token))
    assert decline.status_code == 200
    assert decline.get_json()["data"]["booking_status"] == "declined"

    # Slot freed -> a new booking on the same slot now succeeds.
    b2 = client.post("/api/bookings", headers=_auth(resident_token), json={"provider_id": pid, "slot_id": slot_id})
    assert b2.status_code == 201


def test_cancelled_booking_releases_slot(client, admin_token, resident_token):
    pid = _provider_id(client, admin_token)
    slot_id = _make_slot(client, admin_token, pid, "2026-12-04T10:00:00", "2026-12-04T11:00:00")

    b1 = client.post("/api/bookings", headers=_auth(resident_token), json={"provider_id": pid, "slot_id": slot_id})
    b1_id = b1.get_json()["data"]["id"]

    cancel = client.put(f"/api/bookings/{b1_id}/cancel", headers=_auth(resident_token))
    assert cancel.status_code == 200
    assert cancel.get_json()["data"]["booking_status"] == "cancelled"

    avail = client.get(f"/api/providers/{pid}/availability", headers=_auth(admin_token)).get_json()["data"]
    assert slot_id in [s["id"] for s in avail]


def test_booking_missing_provider_field(client, resident_token):
    resp = client.post("/api/bookings", headers=_auth(resident_token), json={"request_notes": "no provider"})
    assert resp.status_code == 400
    assert resp.get_json()["error"]["code"] == "VALIDATION_ERROR"


def test_booking_unavailable_slot_rejected(client, admin_token, resident_token):
    """A slot explicitly created as unavailable cannot be booked."""
    pid = _provider_id(client, admin_token)
    created = client.post(
        "/api/slots",
        headers=_auth(admin_token),
        json={"provider_id": pid, "slot_start": "2026-12-05T10:00:00", "slot_end": "2026-12-05T11:00:00", "is_available": False},
    )
    slot_id = created.get_json()["data"]["id"]

    resp = client.post("/api/bookings", headers=_auth(resident_token), json={"provider_id": pid, "slot_id": slot_id})
    assert resp.status_code == 409
    assert resp.get_json()["error"]["code"] == "SLOT_UNAVAILABLE"


def test_get_booking_forbidden_for_unrelated_user(client, admin_token, resident_token, security_token):
    pid = _provider_id(client, admin_token)
    slot_id = _make_slot(client, admin_token, pid, "2026-12-06T10:00:00", "2026-12-06T11:00:00")
    b = client.post("/api/bookings", headers=_auth(resident_token), json={"provider_id": pid, "slot_id": slot_id})
    b_id = b.get_json()["data"]["id"]

    # A security user who is neither the resident nor the provider is forbidden.
    resp = client.get(f"/api/bookings/{b_id}", headers=_auth(security_token))
    assert resp.status_code == 403
    assert resp.get_json()["error"]["code"] == "FORBIDDEN"


def test_cancel_booking_forbidden_for_non_owner(client, admin_token, resident_token, security_token):
    pid = _provider_id(client, admin_token)
    slot_id = _make_slot(client, admin_token, pid, "2026-12-07T10:00:00", "2026-12-07T11:00:00")
    b = client.post("/api/bookings", headers=_auth(resident_token), json={"provider_id": pid, "slot_id": slot_id})
    b_id = b.get_json()["data"]["id"]

    resp = client.put(f"/api/bookings/{b_id}/cancel", headers=_auth(security_token))
    assert resp.status_code == 403


def test_accept_missing_booking_returns_404(client, provider_token):
    resp = client.put("/api/bookings/888888/accept", headers=_auth(provider_token))
    assert resp.status_code == 404
    assert resp.get_json()["error"]["code"] == "NOT_FOUND"


def test_booking_commit_failure_rolls_back(client, admin_token, resident_token, monkeypatch):
    """If the commit fails, the API returns a consistent 500 and the transaction is rolled back."""
    pid = _provider_id(client, admin_token)
    slot_id = _make_slot(client, admin_token, pid, "2026-12-08T10:00:00", "2026-12-08T11:00:00")

    def boom():
        raise SQLAlchemyError("simulated commit failure")

    monkeypatch.setattr(db.session, "commit", boom)
    resp = client.post("/api/bookings", headers=_auth(resident_token), json={"provider_id": pid, "slot_id": slot_id})
    assert resp.status_code == 500
    assert resp.get_json()["error"]["code"] == "DB_ERROR"
    monkeypatch.undo()

    # Rollback means the slot was never consumed: it is still bookable.
    ok_resp = client.post("/api/bookings", headers=_auth(resident_token), json={"provider_id": pid, "slot_id": slot_id})
    assert ok_resp.status_code == 201
