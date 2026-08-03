"""Complaint assignment / status-transition edge cases and side-effects.

Notes:
- There is no external notification dispatcher to mock. The observable
  "side-effect" of assign/status changes is the ComplaintUpdate audit trail
  appended to the complaint; these tests assert those records are created with
  the right status/comment, which is the notification analogue in this system.
- The status endpoint performs NO state-machine validation, so arbitrary status
  strings are accepted today. That behaviour is pinned so a future validation
  change is caught deliberately.
"""


def _auth(token):
    return {"Authorization": f"Bearer {token}"}


def _raise_complaint(client, resident_token, subject="Broken gate"):
    resp = client.post(
        "/api/complaints",
        headers=_auth(resident_token),
        json={"subject": subject, "description": "details", "category": "Maintenance", "priority": "high"},
    )
    assert resp.status_code == 201
    return resp.get_json()["data"]["id"]


def _resident_id(client, resident_token):
    return client.get("/api/users/me", headers=_auth(resident_token)).get_json()["data"]["id"]


def test_assign_requires_assignee(client, admin_token, resident_token):
    cid = _raise_complaint(client, resident_token)
    resp = client.put(f"/api/complaints/{cid}/assign", headers=_auth(admin_token), json={})
    assert resp.status_code == 400
    assert resp.get_json()["error"]["code"] == "VALIDATION_ERROR"


def test_assign_sets_in_progress_and_records_update(client, admin_token, resident_token, security_token):
    cid = _raise_complaint(client, resident_token)
    sec_id = client.get("/api/users/me", headers=_auth(security_token)).get_json()["data"]["id"]

    resp = client.put(
        f"/api/complaints/{cid}/assign",
        headers=_auth(admin_token),
        json={"assigned_to_user_id": sec_id, "comment": "Please handle"},
    )
    assert resp.status_code == 200
    assert resp.get_json()["data"]["status"] == "in_progress"
    assert resp.get_json()["data"]["assigned_to_user_id"] == sec_id

    # Side-effect: the audit trail now contains the submission + assignment entries.
    detail = client.get(f"/api/complaints/{cid}", headers=_auth(admin_token)).get_json()["data"]
    assert len(detail["updates"]) == 2
    last = detail["updates"][-1]
    assert last["status"] == "in_progress"
    assert last["comment"] == "Please handle"


def test_assign_requires_admin_role(client, resident_token):
    cid = _raise_complaint(client, resident_token)
    resp = client.put(
        f"/api/complaints/{cid}/assign",
        headers=_auth(resident_token),
        json={"assigned_to_user_id": 4},
    )
    assert resp.status_code == 403
    assert resp.get_json()["error"]["code"] == "FORBIDDEN"


def test_assign_missing_complaint_returns_404(client, admin_token):
    resp = client.put("/api/complaints/777777/assign", headers=_auth(admin_token), json={"assigned_to_user_id": 4})
    assert resp.status_code == 404
    assert resp.get_json()["error"]["code"] == "NOT_FOUND"


def test_status_update_requires_status_and_comment(client, admin_token, resident_token):
    cid = _raise_complaint(client, resident_token)
    # Missing comment.
    resp = client.put(f"/api/complaints/{cid}/status", headers=_auth(admin_token), json={"status": "resolved"})
    assert resp.status_code == 400
    assert resp.get_json()["error"]["code"] == "VALIDATION_ERROR"
    # Missing status.
    resp2 = client.put(f"/api/complaints/{cid}/status", headers=_auth(admin_token), json={"comment": "done"})
    assert resp2.status_code == 400
    assert resp2.get_json()["error"]["code"] == "VALIDATION_ERROR"


def test_status_update_records_audit_entry(client, admin_token, resident_token):
    cid = _raise_complaint(client, resident_token)
    resp = client.put(
        f"/api/complaints/{cid}/status",
        headers=_auth(admin_token),
        json={"status": "resolved", "comment": "Fixed on site"},
    )
    assert resp.status_code == 200
    assert resp.get_json()["data"]["status"] == "resolved"

    detail = client.get(f"/api/complaints/{cid}", headers=_auth(admin_token)).get_json()["data"]
    last = detail["updates"][-1]
    assert last["status"] == "resolved"
    assert last["comment"] == "Fixed on site"


def test_status_update_accepts_arbitrary_status_today(client, admin_token, resident_token):
    """GAP: no transition state-machine, so an invalid status string is accepted."""
    cid = _raise_complaint(client, resident_token)
    resp = client.put(
        f"/api/complaints/{cid}/status",
        headers=_auth(admin_token),
        json={"status": "not_a_real_status", "comment": "arbitrary"},
    )
    # Pinned current behaviour. If a transition validator is added, expect 400/422 instead.
    assert resp.status_code == 200
    assert resp.get_json()["data"]["status"] == "not_a_real_status"


def test_status_update_forbidden_for_non_assignee(client, admin_token, resident_token, provider_token):
    """A user who is neither admin nor the assignee cannot change status."""
    cid = _raise_complaint(client, resident_token)
    resp = client.put(
        f"/api/complaints/{cid}/status",
        headers=_auth(provider_token),
        json={"status": "resolved", "comment": "nope"},
    )
    assert resp.status_code == 403
    assert resp.get_json()["error"]["code"] == "FORBIDDEN"


def test_assignee_can_update_status_after_assignment(client, admin_token, resident_token, security_token):
    cid = _raise_complaint(client, resident_token)
    sec_id = client.get("/api/users/me", headers=_auth(security_token)).get_json()["data"]["id"]
    client.put(
        f"/api/complaints/{cid}/assign",
        headers=_auth(admin_token),
        json={"assigned_to_user_id": sec_id},
    )

    resp = client.put(
        f"/api/complaints/{cid}/status",
        headers=_auth(security_token),
        json={"status": "resolved", "comment": "Handled by security"},
    )
    assert resp.status_code == 200
    assert resp.get_json()["data"]["status"] == "resolved"


def test_add_update_requires_comment(client, admin_token, resident_token):
    cid = _raise_complaint(client, resident_token)
    resp = client.post(f"/api/complaints/{cid}/updates", headers=_auth(admin_token), json={})
    assert resp.status_code == 400
    assert resp.get_json()["error"]["code"] == "VALIDATION_ERROR"


def test_add_update_forbidden_for_unrelated_user(client, resident_token, provider_token):
    cid = _raise_complaint(client, resident_token)
    resp = client.post(
        f"/api/complaints/{cid}/updates",
        headers=_auth(provider_token),
        json={"comment": "I should not be allowed"},
    )
    assert resp.status_code == 403
    assert resp.get_json()["error"]["code"] == "FORBIDDEN"


def test_status_update_missing_complaint_returns_404(client, admin_token):
    resp = client.put(
        "/api/complaints/654321/status",
        headers=_auth(admin_token),
        json={"status": "resolved", "comment": "x"},
    )
    assert resp.status_code == 404
    assert resp.get_json()["error"]["code"] == "NOT_FOUND"
