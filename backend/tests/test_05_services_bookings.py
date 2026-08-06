from datetime import UTC, datetime


def _auth(token):
    return {"Authorization": f"Bearer {token}"}


def _get_provider_id(client, admin_token, provider_token=None):
    if provider_token:
        me_resp = client.get("/api/users/me", headers=_auth(provider_token))
        if me_resp.status_code == 200:
            p_user_id = me_resp.get_json()["data"]["id"]
            providers_resp = client.get("/api/providers", headers=_auth(admin_token))
            if providers_resp.status_code == 200:
                for item in providers_resp.get_json()["data"]["items"]:
                    if item.get("user_id") == p_user_id:
                        return item["id"]

            cat_resp = client.get("/api/service-categories", headers=_auth(admin_token))
            cats = cat_resp.get_json()["data"]
            c_id = cats[0]["id"] if isinstance(cats, list) and len(cats) > 0 else 1

            create_resp = client.post(
                "/api/providers",
                headers=_auth(admin_token),
                json={
                    "user_id": p_user_id,
                    "category_id": c_id,
                    "business_name": "Test Service Co",
                    "service_description": "General repairs",
                },
            )
            if create_resp.status_code in (200, 201):
                return create_resp.get_json()["data"]["id"]

    resp = client.get("/api/providers", headers=_auth(admin_token))
    items = resp.get_json()["data"]["items"]
    if len(items) > 0:
        return items[0]["id"]

    users_resp = client.get("/api/users?role=service_provider", headers=_auth(admin_token))
    p_user_id = users_resp.get_json()["data"]["items"][0]["id"]
    cat_resp = client.get("/api/service-categories", headers=_auth(admin_token))
    cats = cat_resp.get_json()["data"]
    c_id = cats[0]["id"] if isinstance(cats, list) and len(cats) > 0 else 1

    create_resp = client.post(
        "/api/providers",
        headers=_auth(admin_token),
        json={
            "user_id": p_user_id,
            "category_id": c_id,
            "business_name": "Test Service Co",
            "service_description": "General repairs",
        },
    )
    return create_resp.get_json()["data"]["id"]


def test_service_category_crud(client, admin_token):
    ts = datetime.now(UTC).strftime("%H%M%S")
    create_cat = client.post(
        "/api/service-categories",
        headers=_auth(admin_token),
        json={"name": f"Carpentry_{ts}", "description": "Furniture repairs"},
    )
    assert create_cat.status_code == 201
    cat_id = create_cat.get_json()["data"]["id"]

    list_cats = client.get("/api/service-categories", headers=_auth(admin_token))
    assert list_cats.status_code == 200

    get_cat = client.get(f"/api/service-categories/{cat_id}", headers=_auth(admin_token))
    assert get_cat.status_code == 200

    update_cat = client.put(
        f"/api/service-categories/{cat_id}",
        headers=_auth(admin_token),
        json={"description": "Updated furniture repairs"},
    )
    assert update_cat.status_code == 200


def test_provider_profile_get_update_slots(client, admin_token):
    provider_id = _get_provider_id(client, admin_token)

    get_prov = client.get(f"/api/providers/{provider_id}", headers=_auth(admin_token))
    assert get_prov.status_code == 200

    update_prov = client.put(
        f"/api/providers/{provider_id}",
        headers=_auth(admin_token),
        json={"business_name": "Updated Handy Services"},
    )
    assert update_prov.status_code == 200
    assert update_prov.get_json()["data"]["business_name"] == "Updated Handy Services"

    prov_avail = client.get(f"/api/providers/{provider_id}/availability", headers=_auth(admin_token))
    assert prov_avail.status_code == 200


def test_service_slot_creation_and_deletion(client, admin_token):
    provider_id = _get_provider_id(client, admin_token)
    ts = datetime.now(UTC).strftime("%H%M%S")
    slot = client.post(
        "/api/slots",
        headers=_auth(admin_token),
        json={
            "provider_id": provider_id,
            "slot_start": f"2026-08-01T14:{ts[:2]}:00",
            "slot_end": f"2026-08-01T15:{ts[:2]}:00",
            "is_available": True,
        },
    )
    assert slot.status_code == 201
    slot_id = slot.get_json()["data"]["id"]

    del_slot = client.delete(f"/api/slots/{slot_id}", headers=_auth(admin_token))
    assert del_slot.status_code == 200


def test_booking_decline_and_cancel_workflow(client, admin_token, resident_token, provider_token):
    provider_id = _get_provider_id(client, admin_token, provider_token)
    ts = datetime.now(UTC).strftime("%H%M%S")

    slot1 = client.post(
        "/api/slots",
        headers=_auth(admin_token),
        json={
            "provider_id": provider_id,
            "slot_start": f"2026-08-03T10:{ts[:2]}:00",
            "slot_end": f"2026-08-03T11:{ts[:2]}:00",
            "is_available": True,
        },
    )
    slot1_id = slot1.get_json()["data"]["id"]

    booking1 = client.post(
        "/api/bookings",
        headers=_auth(resident_token),
        json={"provider_id": provider_id, "slot_id": slot1_id, "request_notes": "Test decline"},
    )
    b1_id = booking1.get_json()["data"]["id"]

    get_b1 = client.get(f"/api/bookings/{b1_id}", headers=_auth(resident_token))
    assert get_b1.status_code == 200

    decline = client.put(f"/api/bookings/{b1_id}/decline", headers=_auth(provider_token))
    assert decline.status_code == 200
    assert decline.get_json()["data"]["booking_status"] == "declined"

    slot2 = client.post(
        "/api/slots",
        headers=_auth(admin_token),
        json={
            "provider_id": provider_id,
            "slot_start": f"2026-08-04T10:{ts[:2]}:00",
            "slot_end": f"2026-08-04T11:{ts[:2]}:00",
            "is_available": True,
        },
    )
    slot2_id = slot2.get_json()["data"]["id"]

    booking2 = client.post(
        "/api/bookings",
        headers=_auth(resident_token),
        json={"provider_id": provider_id, "slot_id": slot2_id, "request_notes": "Test cancellation"},
    )
    b2_id = booking2.get_json()["data"]["id"]

    cancel = client.put(f"/api/bookings/{b2_id}/cancel", headers=_auth(resident_token))
    assert cancel.status_code == 200
    assert cancel.get_json()["data"]["booking_status"] == "cancelled"


def test_booking_review_full_workflow(client, admin_token, resident_token, provider_token):
    provider_id = _get_provider_id(client, admin_token, provider_token)
    ts = datetime.now(UTC).strftime("%H%M%S")

    slot = client.post(
        "/api/slots",
        headers=_auth(admin_token),
        json={
            "provider_id": provider_id,
            "slot_start": f"2026-08-02T09:{ts[:2]}:00",
            "slot_end": f"2026-08-02T10:{ts[:2]}:00",
            "is_available": True,
        },
    )
    assert slot.status_code == 201
    slot_id = slot.get_json()["data"]["id"]

    booking = client.post(
        "/api/bookings",
        headers=_auth(resident_token),
        json={"provider_id": provider_id, "slot_id": slot_id, "request_notes": "Plumbing fixture installation"},
    )
    assert booking.status_code == 201
    booking_id = booking.get_json()["data"]["id"]

    list_bookings = client.get("/api/bookings", headers=_auth(resident_token))
    assert list_bookings.status_code == 200

    accept = client.put(f"/api/bookings/{booking_id}/accept", headers=_auth(provider_token))
    assert accept.status_code == 200

    complete = client.put(f"/api/bookings/{booking_id}/complete", headers=_auth(provider_token))
    assert complete.status_code == 200

    review = client.post(
        "/api/reviews",
        headers=_auth(resident_token),
        json={"provider_id": provider_id, "booking_id": booking_id, "rating": 5, "feedback": "Prompt and clean job!"},
    )
    assert review.status_code == 201
    assert review.get_json()["data"]["rating"] == 5

    reviews_list = client.get(f"/api/reviews/provider/{provider_id}", headers=_auth(resident_token))
    assert reviews_list.status_code == 200
