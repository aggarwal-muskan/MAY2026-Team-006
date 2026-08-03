def _auth(token):
    return {"Authorization": f"Bearer {token}"}


def test_resident_create_complaint(client, resident_token):
    response = client.post(
        "/api/complaints",
        headers=_auth(resident_token),
        json={
            "subject": "Elevator Malfunction",
            "description": "Elevator in Block A is making loud screeching noise.",
            "category": "Maintenance",
            "priority": "high",
        },
    )
    assert response.status_code == 201
    json_data = response.get_json()
    assert json_data["success"] is True
    assert json_data["data"]["status"] == "open"


def test_complaint_get_update_delete(client, admin_token, resident_token):
    create = client.post(
        "/api/complaints",
        headers=_auth(resident_token),
        json={
            "subject": "Water Leakage in Bathroom",
            "description": "Pipe leaking behind flush tank.",
            "category": "Plumbing",
            "priority": "high",
        },
    )
    assert create.status_code == 201
    cid = create.get_json()["data"]["id"]

    list_resp = client.get("/api/complaints", headers=_auth(resident_token))
    assert list_resp.status_code == 200

    get_resp = client.get(f"/api/complaints/{cid}", headers=_auth(admin_token))
    assert get_resp.status_code == 200

    update_resp = client.put(
        f"/api/complaints/{cid}",
        headers=_auth(admin_token),
        json={"priority": "medium"},
    )
    assert update_resp.status_code == 200
    assert update_resp.get_json()["data"]["priority"] == "medium"

    del_resp = client.delete(f"/api/complaints/{cid}", headers=_auth(admin_token))
    assert del_resp.status_code == 200
    assert del_resp.get_json()["message"] == "Complaint deleted"


def test_complaint_assignment_and_resolution(client, admin_token, resident_token):
    create = client.post(
        "/api/complaints",
        headers=_auth(resident_token),
        json={
            "subject": "Streetlight Bulb Blown",
            "description": "Pole #4 near gate 2 light bulb broken.",
            "category": "Electrical",
            "priority": "medium",
        },
    )
    assert create.status_code == 201
    cid = create.get_json()["data"]["id"]

    assign = client.put(
        f"/api/complaints/{cid}/assign",
        headers=_auth(admin_token),
        json={"assigned_to_user_id": 4, "comment": "Assigned electrician to fix pole light."},
    )
    assert assign.status_code == 200
    assert assign.get_json()["data"]["status"] == "in_progress"

    status = client.put(
        f"/api/complaints/{cid}/status",
        headers=_auth(admin_token),
        json={"status": "resolved", "comment": "Bulb replaced successfully."},
    )
    assert status.status_code == 200
    assert status.get_json()["data"]["status"] == "resolved"


def test_add_complaint_timeline_update(client, admin_token, resident_token):
    create = client.post(
        "/api/complaints",
        headers=_auth(resident_token),
        json={
            "subject": "Garbage Disposal Delay",
            "description": "Bin not cleared on 2nd floor.",
            "category": "Sanitation",
            "priority": "low",
        },
    )
    assert create.status_code == 201
    cid = create.get_json()["data"]["id"]

    update = client.post(
        f"/api/complaints/{cid}/updates",
        headers=_auth(resident_token),
        json={"comment": "Resident followed up regarding morning pickup schedule."},
    )
    assert update.status_code == 201
    assert update.get_json()["message"] == "Update added"
