"""Token lifecycle & security edge cases.

Covers expired access tokens, malformed/invalid tokens, missing tokens, the
refresh path (including refresh for a deleted user), and documents the current
revocation behaviour: logout returns success but does NOT add the token to a
denylist, so the token remains usable afterwards. That last test is a guard
that pins the current (no server-side revocation) behaviour so any future
change is caught deliberately.
"""

from datetime import timedelta

from flask_jwt_extended import create_access_token

from app.core.extensions import db
from app.models import User


def _auth(token):
    return {"Authorization": f"Bearer {token}"}


def _make_token(app, identity="1", role="admin", society_id=1, expires_delta=None):
    with app.app_context():
        return create_access_token(
            identity=str(identity),
            additional_claims={"role": role, "society_id": society_id},
            expires_delta=expires_delta,
        )


def test_expired_token_rejected_on_verify(app, client):
    expired = _make_token(app, expires_delta=timedelta(seconds=-30))
    resp = client.post("/api/auth/verify-token", headers=_auth(expired))
    assert resp.status_code == 401
    assert resp.get_json()["error"]["code"] == "TOKEN_EXPIRED"


def test_expired_token_rejected_on_protected_resource(app, client):
    expired = _make_token(app, expires_delta=timedelta(seconds=-1))
    resp = client.get("/api/complaints", headers=_auth(expired))
    assert resp.status_code == 401
    assert resp.get_json()["error"]["code"] == "TOKEN_EXPIRED"


def test_malformed_token_rejected(client):
    resp = client.post("/api/auth/verify-token", headers={"Authorization": "Bearer not.a.real.jwt"})
    assert resp.status_code == 401
    assert resp.get_json()["error"]["code"] == "UNAUTHORIZED"


def test_token_signed_with_wrong_secret_rejected(client):
    import jwt as pyjwt

    forged = pyjwt.encode({"sub": "1", "role": "admin"}, "totally-wrong-secret-key-32bytes-long!!", algorithm="HS256")
    resp = client.post("/api/auth/verify-token", headers=_auth(forged))
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
    resp = client.post("/api/auth/verify-token", headers=_auth(admin_token))
    assert resp.status_code == 200
    data = resp.get_json()["data"]
    assert data["valid"] is True
    assert data["user"]["role"] == "admin"


def test_refresh_token_issues_working_token(client, resident_token):
    refresh = client.post("/api/auth/refresh-token", headers=_auth(resident_token))
    assert refresh.status_code == 200
    new_token = refresh.get_json()["data"]["token"]

    # The freshly minted token is usable on a protected endpoint.
    check = client.post("/api/auth/verify-token", headers=_auth(new_token))
    assert check.status_code == 200


def test_refresh_with_expired_token_rejected(app, client):
    expired = _make_token(app, identity="2", role="owner", expires_delta=timedelta(seconds=-5))
    resp = client.post("/api/auth/refresh-token", headers=_auth(expired))
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

    resp = client.post("/api/auth/refresh-token", headers=_auth(token))
    assert resp.status_code == 404
    assert resp.get_json()["error"]["code"] == "NOT_FOUND"


def test_logout_does_not_revoke_token(client, admin_token):
    """Documents current behaviour: no server-side denylist, so the token still works after logout."""
    logout = client.post("/api/auth/logout", headers=_auth(admin_token))
    assert logout.status_code == 200

    still_valid = client.post("/api/auth/verify-token", headers=_auth(admin_token))
    assert still_valid.status_code == 200
