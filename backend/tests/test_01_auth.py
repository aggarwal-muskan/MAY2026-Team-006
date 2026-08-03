from datetime import UTC, datetime


def _auth(token):
    return {"Authorization": f"Bearer {token}"}


def test_auth_register_success(client):
    ts = datetime.now(UTC).strftime("%Y%m%d%H%M%S")
    email = f"user_{ts}@socioneed.com"
    response = client.post(
        "/api/auth/register",
        json={
            "full_name": "Test User",
            "email": email,
            "phone": "9876543210",
            "password": "Password123",
            "role": "owner",
            "society_id": 1,
        },
    )
    assert response.status_code == 201
    json_data = response.get_json()
    assert json_data["success"] is True
    assert "token" in json_data["data"]


def test_auth_register_duplicate_email(client):
    response = client.post(
        "/api/auth/register",
        json={
            "full_name": "Admin User Duplicate",
            "email": "admin@socioneed.com",
            "phone": "9999999999",
            "password": "Password123",
            "role": "owner",
            "society_id": 1,
        },
    )
    assert response.status_code == 409
    json_data = response.get_json()
    assert json_data["success"] is False
    assert json_data["error"]["code"] == "DUPLICATE_EMAIL"


def test_auth_register_missing_fields(client):
    response = client.post(
        "/api/auth/register",
        json={"email": "incomplete@socioneed.com"},
    )
    assert response.status_code == 400
    json_data = response.get_json()
    assert json_data["success"] is False
    assert json_data["error"]["code"] == "VALIDATION_ERROR"


def test_auth_login_success(client):
    response = client.post(
        "/api/auth/login",
        json={"email": "admin@socioneed.com", "password": "123456", "role": "admin"},
    )
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data["success"] is True
    assert "token" in json_data["data"]


def test_auth_login_invalid_password(client):
    response = client.post(
        "/api/auth/login",
        json={"email": "admin@socioneed.com", "password": "wrongpassword", "role": "admin"},
    )
    assert response.status_code == 401
    json_data = response.get_json()
    assert json_data["success"] is False
    assert json_data["error"]["code"] == "UNAUTHORIZED"


def test_auth_forgot_password(client):
    response = client.post(
        "/api/auth/forgot-password",
        json={
            "email": "security@socioneed.com",
            "phone": "9000000004",
            "new_password": "newsecpass123",
        },
    )
    assert response.status_code == 200
    assert response.get_json()["message"] == "Password reset successful"

    # Reset password back for other tests
    client.post(
        "/api/auth/forgot-password",
        json={
            "email": "security@socioneed.com",
            "phone": "9000000004",
            "new_password": "123456",
        },
    )


def test_auth_change_password(client, admin_token):
    response = client.post(
        "/api/auth/change-password",
        headers=_auth(admin_token),
        json={"current_password": "123456", "new_password": "newadminpass123"},
    )
    assert response.status_code == 200
    assert response.get_json()["message"] == "Password changed successfully"

    # Change back so admin_token remains usable
    client.post(
        "/api/auth/change-password",
        headers=_auth(admin_token),
        json={"current_password": "newadminpass123", "new_password": "123456"},
    )


def test_auth_verify_and_refresh_token(client, admin_token):
    verify = client.post("/api/auth/verify-token", headers=_auth(admin_token))
    assert verify.status_code == 200
    assert verify.get_json()["data"]["valid"] is True

    refresh = client.post("/api/auth/refresh-token", headers=_auth(admin_token))
    assert refresh.status_code == 200
    assert "token" in refresh.get_json()["data"]


def test_auth_logout(client, admin_token):
    logout = client.post("/api/auth/logout", headers=_auth(admin_token))
    assert logout.status_code == 200
    assert logout.get_json()["message"] == "Logged out successfully"


def test_auth_unauthorized_access(client):
    response = client.get("/api/users/me")
    assert response.status_code == 401


def test_user_management_and_status_update(client, admin_token):
    get_user = client.get("/api/users/2", headers=_auth(admin_token))
    assert get_user.status_code == 200
    assert get_user.get_json()["data"]["id"] == 2

    status_update = client.post(
        "/api/users/2/activate",
        headers=_auth(admin_token),
    )
    assert status_update.status_code == 200
