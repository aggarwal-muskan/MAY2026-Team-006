from datetime import UTC, datetime


def _auth(token):
    return {"Authorization": f"Bearer {token}"}


def test_auth_register_and_login(client):
    ts = datetime.now(UTC).strftime("%Y%m%d%H%M%S")
    email = f"s1_{ts}@socioneed.com"

    reg = client.post(
        "/api/auth/register",
        json={
            "full_name": "Sprint One User",
            "email": email,
            "phone": "9111100000",
            "password": "123456",
            "role": "owner",
            "society_id": 1,
        },
    )
    assert reg.status_code == 201

    login = client.post(
        "/api/auth/login",
        json={"email": email, "password": "123456", "role": "owner"},
    )
    assert login.status_code == 200
    assert login.get_json()["success"] is True


def test_auth_forgot_and_change_password(client, admin_token):
    forgot = client.post(
        "/api/auth/forgot-password",
        json={
            "email": "security@socioneed.com",
            "phone": "9000000004",
            "new_password": "newpass123",
        },
    )
    assert forgot.status_code == 200

    login_with_new_password = client.post(
        "/api/auth/login",
        json={"email": "security@socioneed.com", "password": "newpass123", "role": "security"},
    )
    assert login_with_new_password.status_code == 200

    change = client.post(
        "/api/auth/change-password",
        headers=_auth(admin_token),
        json={"current_password": "123456", "new_password": "adminpass456"},
    )
    assert change.status_code == 200

    relogin_admin = client.post(
        "/api/auth/login",
        json={"email": "admin@socioneed.com", "password": "adminpass456", "role": "admin"},
    )
    assert relogin_admin.status_code == 200


def test_users_me_and_list(client, admin_token):
    me = client.get("/api/users/me", headers=_auth(admin_token))
    assert me.status_code == 200

    users = client.get("/api/users", headers=_auth(admin_token))
    assert users.status_code == 200
    assert "items" in users.get_json()["data"]


def test_create_update_delete_unit(client, admin_token):
    ts = datetime.now(UTC).strftime("%H%M%S")
    create = client.post(
        "/api/units",
        headers=_auth(admin_token),
        json={"society_id": 1, "block_name": "A", "unit_number": f"A-{ts}"},
    )
    assert create.status_code == 201
    unit_id = create.get_json()["data"]["id"]

    update = client.put(
        f"/api/units/{unit_id}",
        headers=_auth(admin_token),
        json={"floor": "4"},
    )
    assert update.status_code == 200

    delete = client.delete(f"/api/units/{unit_id}", headers=_auth(admin_token))
    assert delete.status_code == 200


def test_notice_and_event_lifecycle(client, admin_token, resident_token):
    notice = client.post(
        "/api/notices",
        headers=_auth(admin_token),
        json={"title": "S1 Notice", "body": "Body", "notice_type": "General", "priority": "high"},
    )
    assert notice.status_code == 201
    notice_id = notice.get_json()["data"]["id"]

    notice_get = client.get(f"/api/notices/{notice_id}", headers=_auth(admin_token))
    assert notice_get.status_code == 200

    event = client.post(
        "/api/events",
        headers=_auth(admin_token),
        json={"title": "S1 Event", "event_date": "2026-12-25"},
    )
    assert event.status_code == 201
    event_id = event.get_json()["data"]["id"]

    event_get = client.get(f"/api/events/{event_id}", headers=_auth(resident_token))
    assert event_get.status_code == 200

    register = client.post(f"/api/events/{event_id}/register", headers=_auth(resident_token))
    assert register.status_code == 200

    unregister = client.post(f"/api/events/{event_id}/unregister", headers=_auth(resident_token))
    assert unregister.status_code == 200

    client.delete(f"/api/notices/{notice_id}", headers=_auth(admin_token))
    client.delete(f"/api/events/{event_id}", headers=_auth(admin_token))

