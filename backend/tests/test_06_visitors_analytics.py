def _auth(token):
    return {"Authorization": f"Bearer {token}"}


def test_visitor_checkin_and_checkout(client, security_token):
    visitor = client.post(
        "/api/visitors",
        headers=_auth(security_token),
        json={
            "society_id": 1,
            "recorded_by_user_id": 4,
            "resident_user_id": 2,
            "visitor_name": "Delivery Person (Amazon)",
            "purpose": "Package Delivery",
        },
    )
    assert visitor.status_code == 201
    entry_id = visitor.get_json()["data"]["id"]

    exit_resp = client.put(f"/api/visitors/{entry_id}/exit", headers=_auth(security_token))
    assert exit_resp.status_code == 200
    assert exit_resp.get_json()["message"] == "Exit recorded"


def test_dashboard_analytics(client, admin_token, resident_token):
    admin_dash = client.get("/api/analytics/dashboard/admin", headers=_auth(admin_token))
    assert admin_dash.status_code == 200
    assert "stats" in admin_dash.get_json()["data"]

    resident_dash = client.get("/api/analytics/dashboard/resident", headers=_auth(resident_token))
    assert resident_dash.status_code == 200
    assert "stats" in resident_dash.get_json()["data"]


def test_monthly_reports(client, admin_token):
    monthly = client.get("/api/reports/monthly", headers=_auth(admin_token))
    assert monthly.status_code == 200
    assert monthly.get_json()["success"] is True
