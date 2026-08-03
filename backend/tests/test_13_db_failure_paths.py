"""Database failure / rollback paths.

These tests deliberately induce database errors and assert that the API returns
a consistent error envelope and rolls back, rather than leaking a stack trace or
committing partial state:

- A raw SQLAlchemyError on commit -> 500 DB_ERROR (registered error handler).
- An IntegrityError from a real unique-constraint violation -> 409 CONFLICT.
- After each failure the session must recover so subsequent requests succeed.
"""

from sqlalchemy.exc import SQLAlchemyError

from app.core.extensions import db


def _auth(token):
    return {"Authorization": f"Bearer {token}"}


def _unique_email():
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
            "email": _unique_email(),
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
        json={"full_name": "X", "email": _unique_email(), "password": "123456", "role": "owner", "society_id": 1},
    )
    assert failed.status_code == 500
    monkeypatch.undo()

    # The handler rolled back; a normal request now works.
    ok_resp = client.post(
        "/api/auth/register",
        json={"full_name": "Recovered", "email": _unique_email(), "password": "123456", "role": "owner", "society_id": 1},
    )
    assert ok_resp.status_code == 201


def test_duplicate_phone_triggers_integrity_conflict(client):
    """Phone uniqueness is enforced at the DB layer (not pre-checked in code),
    so a duplicate phone surfaces as an IntegrityError -> 409 CONFLICT."""
    resp = client.post(
        "/api/auth/register",
        json={
            "full_name": "Phone Clash",
            "email": _unique_email(),
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
        headers=_auth(resident_token),
        json={"subject": "S", "description": "D", "category": "Maintenance", "priority": "low"},
    )
    assert resp.status_code == 500
    assert resp.get_json()["error"]["code"] == "DB_ERROR"
    monkeypatch.undo()

    # No partial complaint persisted; a real create afterward succeeds.
    ok_resp = client.post(
        "/api/complaints",
        headers=_auth(resident_token),
        json={"subject": "Real", "description": "D", "category": "Maintenance", "priority": "low"},
    )
    assert ok_resp.status_code == 201


def test_category_create_commit_failure_returns_db_error(client, admin_token, monkeypatch):
    def boom():
        raise SQLAlchemyError("simulated failure")

    monkeypatch.setattr(db.session, "commit", boom)
    resp = client.post(
        "/api/service-categories",
        headers=_auth(admin_token),
        json={"name": "TransientCategory", "description": "should not persist"},
    )
    assert resp.status_code == 500
    assert resp.get_json()["error"]["code"] == "DB_ERROR"


def test_duplicate_category_name_conflict(client, admin_token):
    """service_categories.name is unique -> duplicate creation is a 409 CONFLICT."""
    name = "UniqueCat_DBTest"
    first = client.post(
        "/api/service-categories",
        headers=_auth(admin_token),
        json={"name": name, "description": "first"},
    )
    assert first.status_code == 201

    dup = client.post(
        "/api/service-categories",
        headers=_auth(admin_token),
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
        json={"full_name": "Shape", "email": _unique_email(), "password": "123456", "role": "owner", "society_id": 1},
    )
    body = resp.get_json()
    assert set(body.keys()) == {"success", "error"}
    assert set(body["error"].keys()) == {"code", "message"}
    assert body["success"] is False
