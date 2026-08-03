"""Edge-case coverage for the password-reset flow.

Note on external dependencies: the current /api/auth/forgot-password endpoint
performs an in-place password reset (it verifies email/phone ownership and
writes the new hash directly). There is NO outgoing email or SMS integration in
the codebase, so there is no external notification client to mock. These tests
therefore exhaustively cover the validation, ownership-verification and
error-handling paths of the reset endpoint itself, plus proof that the reset
actually takes effect (old password rejected, new password accepted).
"""


def _auth(token):
    return {"Authorization": f"Bearer {token}"}


def _login(client, email, password, role=None):
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
    assert _login(client, "resident@socioneed.com", "123456", "owner").status_code == 200


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
    assert _login(client, "provider@socioneed.com", "123456").status_code == 401
    # New password works.
    assert _login(client, "provider@socioneed.com", "resetpass456").status_code == 200

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

    assert _login(client, "security@socioneed.com", "phonereset789").status_code == 200

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

    good = _login(client, "resident@socioneed.com", "roundtrip321", "owner")
    assert good.status_code == 200
    assert "token" in good.get_json()["data"]

    client.post(
        "/api/auth/forgot-password",
        json={"email": "resident@socioneed.com", "phone": "9000000002", "new_password": "123456"},
    )
