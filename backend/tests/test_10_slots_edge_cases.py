"""Slot-creation edge cases and time validation.

Covers required-field validation, invalid datetime formats, unknown provider,
role/ownership enforcement, duplicate-slot uniqueness (transaction rollback via
the IntegrityError handler), and the CURRENT behaviour for overlapping slots and
end < start times. The overlap / end<start tests assert what the API does today
(it accepts them, because no temporal validation exists) so the gap is visible
and pinned; if validation is later added these tests should be updated to expect
a 400/409.
"""


def _auth(token):
    return {"Authorization": f"Bearer {token}"}


def _provider_id(client, admin_token):
    resp = client.get("/api/providers", headers=_auth(admin_token))
    return resp.get_json()["data"]["items"][0]["id"]


def _slot_body(provider_id, start, end, available=True):
    return {"provider_id": provider_id, "slot_start": start, "slot_end": end, "is_available": available}


def test_slot_missing_fields(client, admin_token):
    pid = _provider_id(client, admin_token)
    resp = client.post("/api/slots", headers=_auth(admin_token), json={"provider_id": pid})
    assert resp.status_code == 400
    assert resp.get_json()["error"]["code"] == "VALIDATION_ERROR"


def test_slot_unknown_provider(client, admin_token):
    resp = client.post(
        "/api/slots",
        headers=_auth(admin_token),
        json=_slot_body(999999, "2026-11-01T10:00:00", "2026-11-01T11:00:00"),
    )
    assert resp.status_code == 404
    assert resp.get_json()["error"]["code"] == "NOT_FOUND"


def test_slot_invalid_start_datetime_format(client, admin_token):
    pid = _provider_id(client, admin_token)
    resp = client.post(
        "/api/slots",
        headers=_auth(admin_token),
        json=_slot_body(pid, "01-11-2026 10am", "2026-11-01T11:00:00"),
    )
    assert resp.status_code == 400
    assert resp.get_json()["error"]["code"] == "VALIDATION_ERROR"


def test_slot_invalid_end_datetime_format(client, admin_token):
    pid = _provider_id(client, admin_token)
    resp = client.post(
        "/api/slots",
        headers=_auth(admin_token),
        json=_slot_body(pid, "2026-11-01T10:00:00", "not-a-datetime"),
    )
    assert resp.status_code == 400
    assert resp.get_json()["error"]["code"] == "VALIDATION_ERROR"


def test_slot_duplicate_is_conflict_and_rolls_back(client, admin_token):
    """Identical (provider, start, end) violates uq_provider_slot -> 409, session recovers."""
    pid = _provider_id(client, admin_token)
    body = _slot_body(pid, "2026-11-05T09:00:00", "2026-11-05T10:00:00")

    first = client.post("/api/slots", headers=_auth(admin_token), json=body)
    assert first.status_code == 201

    dup = client.post("/api/slots", headers=_auth(admin_token), json=body)
    assert dup.status_code == 409
    assert dup.get_json()["error"]["code"] == "CONFLICT"

    # After the rollback the session must still be healthy: a different slot succeeds.
    recover = client.post(
        "/api/slots",
        headers=_auth(admin_token),
        json=_slot_body(pid, "2026-11-05T11:00:00", "2026-11-05T12:00:00"),
    )
    assert recover.status_code == 201


def test_slot_overlapping_currently_allowed(client, admin_token):
    """GAP: overlapping (non-identical) slots are accepted today (no overlap validation)."""
    pid = _provider_id(client, admin_token)
    base = client.post(
        "/api/slots",
        headers=_auth(admin_token),
        json=_slot_body(pid, "2026-11-10T09:00:00", "2026-11-10T11:00:00"),
    )
    assert base.status_code == 201

    overlapping = client.post(
        "/api/slots",
        headers=_auth(admin_token),
        json=_slot_body(pid, "2026-11-10T10:00:00", "2026-11-10T12:00:00"),
    )
    # Pinned current behaviour: accepted. Change to expect 409 if overlap validation is added.
    assert overlapping.status_code == 201


def test_slot_end_before_start_currently_allowed(client, admin_token):
    """GAP: end < start is accepted today (no temporal ordering validation)."""
    pid = _provider_id(client, admin_token)
    resp = client.post(
        "/api/slots",
        headers=_auth(admin_token),
        json=_slot_body(pid, "2026-11-15T14:00:00", "2026-11-15T10:00:00"),
    )
    assert resp.status_code == 201  # Pinned current behaviour.


def test_slot_zero_duration_currently_allowed(client, admin_token):
    """GAP: start == end (zero-length slot) is accepted today."""
    pid = _provider_id(client, admin_token)
    resp = client.post(
        "/api/slots",
        headers=_auth(admin_token),
        json=_slot_body(pid, "2026-11-16T10:00:00", "2026-11-16T10:00:00"),
    )
    assert resp.status_code == 201


def test_slot_creation_requires_privileged_role(client, resident_token, admin_token):
    pid = _provider_id(client, admin_token)
    resp = client.post(
        "/api/slots",
        headers=_auth(resident_token),
        json=_slot_body(pid, "2026-11-20T10:00:00", "2026-11-20T11:00:00"),
    )
    assert resp.status_code == 403
    assert resp.get_json()["error"]["code"] == "FORBIDDEN"


def test_provider_cannot_create_slot_for_other_provider(client, admin_token, provider_token):
    """A service_provider may only manage their own slots."""
    # Find a provider profile that does NOT belong to the logged-in provider user.
    providers = client.get("/api/providers", headers=_auth(admin_token)).get_json()["data"]["items"]
    me = client.get("/api/users/me", headers=_auth(provider_token)).get_json()["data"]
    foreign = next(p for p in providers if p["user_id"] != me["id"])

    resp = client.post(
        "/api/slots",
        headers=_auth(provider_token),
        json=_slot_body(foreign["id"], "2026-11-25T10:00:00", "2026-11-25T11:00:00"),
    )
    assert resp.status_code == 403
    assert resp.get_json()["error"]["code"] == "FORBIDDEN"


def test_update_slot_with_invalid_datetime(client, admin_token):
    pid = _provider_id(client, admin_token)
    created = client.post(
        "/api/slots",
        headers=_auth(admin_token),
        json=_slot_body(pid, "2026-11-28T10:00:00", "2026-11-28T11:00:00"),
    )
    slot_id = created.get_json()["data"]["id"]

    resp = client.put(
        f"/api/slots/{slot_id}",
        headers=_auth(admin_token),
        json={"slot_start": "garbage"},
    )
    assert resp.status_code == 400
    assert resp.get_json()["error"]["code"] == "VALIDATION_ERROR"


def test_update_missing_slot_returns_404(client, admin_token):
    resp = client.put("/api/slots/987654", headers=_auth(admin_token), json={"is_available": False})
    assert resp.status_code == 404
    assert resp.get_json()["error"]["code"] == "NOT_FOUND"
