from datetime import UTC, datetime


def _auth(token):
    return {"Authorization": f"Bearer {token}"}


def test_admin_create_unit(client, admin_token):
    ts = datetime.now(UTC).strftime("%H%M%S")
    response = client.post(
        "/api/units",
        headers=_auth(admin_token),
        json={"society_id": 1, "block_name": "B", "unit_number": f"B-{ts}", "floor": "2"},
    )
    assert response.status_code == 201
    json_data = response.get_json()
    assert json_data["success"] is True
    assert json_data["data"]["block_name"] == "B"


def test_admin_list_and_get_unit(client, admin_token):
    ts = datetime.now(UTC).strftime("%H%M%S")
    create = client.post(
        "/api/units",
        headers=_auth(admin_token),
        json={"society_id": 1, "block_name": "A", "unit_number": f"A-{ts}"},
    )
    assert create.status_code == 201
    unit_id = create.get_json()["data"]["id"]

    units_list = client.get("/api/units", headers=_auth(admin_token))
    assert units_list.status_code == 200
    assert "items" in units_list.get_json()["data"]

    get_unit = client.get(f"/api/units/{unit_id}", headers=_auth(admin_token))
    assert get_unit.status_code == 200
    assert get_unit.get_json()["data"]["id"] == unit_id

    unit_residents = client.get(f"/api/units/{unit_id}/residents", headers=_auth(admin_token))
    assert unit_residents.status_code == 200


def test_admin_update_and_delete_unit(client, admin_token):
    ts = datetime.now(UTC).strftime("%H%M%S")
    create = client.post(
        "/api/units",
        headers=_auth(admin_token),
        json={"society_id": 1, "block_name": "C", "unit_number": f"C-{ts}"},
    )
    assert create.status_code == 201
    unit_id = create.get_json()["data"]["id"]

    update = client.put(
        f"/api/units/{unit_id}",
        headers=_auth(admin_token),
        json={"floor": "5", "notes": "Penthouse level"},
    )
    assert update.status_code == 200
    assert update.get_json()["data"]["floor"] == "5"

    delete = client.delete(f"/api/units/{unit_id}", headers=_auth(admin_token))
    assert delete.status_code == 200
    assert delete.get_json()["message"] == "Unit deleted"


def test_resident_occupancy_lifecycle(client, admin_token):
    ts = datetime.now(UTC).strftime("%H%M%S")
    create_u = client.post(
        "/api/units",
        headers=_auth(admin_token),
        json={"society_id": 1, "block_name": "D", "unit_number": f"D-{ts}"},
    )
    assert create_u.status_code == 201
    unit_id = create_u.get_json()["data"]["id"]

    create_occ = client.post(
        "/api/occupancies",
        headers=_auth(admin_token),
        json={
            "unit_id": unit_id,
            "user_id": 2,
            "occupancy_type": "owner",
            "start_date": "2026-01-01",
        },
    )
    assert create_occ.status_code == 201
    occ_id = create_occ.get_json()["data"]["id"]

    list_occ = client.get("/api/occupancies", headers=_auth(admin_token))
    assert list_occ.status_code == 200

    update_occ = client.put(
        f"/api/occupancies/{occ_id}",
        headers=_auth(admin_token),
        json={"occupancy_type": "tenant"},
    )
    assert update_occ.status_code == 200
    assert update_occ.get_json()["data"]["occupancy_type"] == "tenant"

    del_occ = client.delete(f"/api/occupancies/{occ_id}", headers=_auth(admin_token))
    assert del_occ.status_code == 200


def test_resident_create_unit_forbidden(client, resident_token):
    response = client.post(
        "/api/units",
        headers=_auth(resident_token),
        json={"society_id": 1, "block_name": "X", "unit_number": "X-101"},
    )
    assert response.status_code == 403
    assert response.get_json()["error"]["code"] == "FORBIDDEN"


def test_get_society_details_and_list(client, admin_token):
    societies = client.get("/api/societies", headers=_auth(admin_token))
    assert societies.status_code == 200

    response = client.get("/api/societies/1", headers=_auth(admin_token))
    assert response.status_code == 200
    assert response.get_json()["data"]["name"] == "Green Valley Society"
