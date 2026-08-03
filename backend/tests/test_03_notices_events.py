def _auth(token):
    return {"Authorization": f"Bearer {token}"}


def test_admin_create_notice(client, admin_token):
    response = client.post(
        "/api/notices",
        headers=_auth(admin_token),
        json={
            "title": "Water Shutdown Maintenance",
            "body": "Water supply will be suspended from 10 AM to 2 PM on Sunday.",
            "notice_type": "Maintenance",
            "priority": "high",
        },
    )
    assert response.status_code == 201
    json_data = response.get_json()
    assert json_data["success"] is True
    assert json_data["data"]["title"] == "Water Shutdown Maintenance"


def test_get_notice_by_id(client, resident_token, admin_token):
    notice = client.post(
        "/api/notices",
        headers=_auth(admin_token),
        json={"title": "General Notice", "body": "Annual General Meeting next month.", "notice_type": "General", "priority": "normal"},
    )
    assert notice.status_code == 201
    notice_id = notice.get_json()["data"]["id"]

    get_resp = client.get(f"/api/notices/{notice_id}", headers=_auth(resident_token))
    assert get_resp.status_code == 200
    assert get_resp.get_json()["data"]["id"] == notice_id

    client.delete(f"/api/notices/{notice_id}", headers=_auth(admin_token))


def test_event_lifecycle_and_registration(client, admin_token, resident_token):
    event = client.post(
        "/api/events",
        headers=_auth(admin_token),
        json={
            "title": "Diwali Cultural Night",
            "description": "Celebration in central lawn",
            "event_date": "2026-11-12",
            "location": "Clubhouse Lawn",
        },
    )
    assert event.status_code == 201
    event_id = event.get_json()["data"]["id"]

    reg = client.post(f"/api/events/{event_id}/register", headers=_auth(resident_token))
    assert reg.status_code == 200
    assert reg.get_json()["message"] == "Registration successful"

    unreg = client.post(f"/api/events/{event_id}/unregister", headers=_auth(resident_token))
    assert unreg.status_code == 200
    assert unreg.get_json()["message"] == "Registration cancelled"

    del_resp = client.delete(f"/api/events/{event_id}", headers=_auth(admin_token))
    assert del_resp.status_code == 200
