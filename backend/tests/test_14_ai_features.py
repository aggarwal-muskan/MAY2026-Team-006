"""AI feature tests for SocioNeed.

Gemini is mocked so tests are deterministic, offline, and free. We monkeypatch
the ``generate_json`` / ``generate_text`` names inside ``app.api.ai`` (where they
are used) rather than calling the real Gemini API.
"""

import pytest

import app.api.ai as ai_module
from app.services.gemini_service import GeminiServiceError


def _auth(token):
    return {"Authorization": f"Bearer {token}"}


# A single superset payload that satisfies every AI endpoint's response shape.
_FAKE_AI_JSON = {
    # notice generator
    "title": "Water Tank Cleaning",
    "body": "Dear Residents, the water tanks will be cleaned on Sunday. Thank you.",
    # multilingual
    "translations": {"English": "Hello", "Hindi": "Namaste", "Telugu": "Namaskaram"},
    # complaint classification
    "category": "Water",
    "priority": "High",
    "sentiment": "Negative",
    "confidence": 0.9,
    "rationale": "No water reported in a block.",
    # analytics / resolution insights
    "insight": "Water issues are the largest and slowest category.",
    "suggested_actions": ["Inspect the Block C supply line"],
    "recommended_actions": ["Schedule a pump inspection"],
    "recurring_issues": ["Block C water pressure recurring"],
    "highlights": ["6 water complaints open over a week"],
    # daily summary
    "headline": "Calm day in the society",
    "summary": "Water maintenance in the morning; yoga in the evening.",
    "sections": [{"label": "Notices", "text": "Water tank cleaning."}],
    # meeting minutes
    "key_discussions": ["Budget for Diwali"],
    "decisions": ["Approve 50k budget"],
    "action_items": [{"task": "Book hall", "responsible": "Secretary", "deadline": "Fri"}],
    "minutes_markdown": "## Minutes",
    # notice summarizer (single + all)
    "what": "Water tank cleaning",
    "when": "Sunday 9-1",
    "where": "All blocks",
    "impact": "Supply affected",
    "action": "Store water",
    "groups": [{"theme": "Maintenance", "items": ["Water tank cleaning Sunday"]}],
    "digest_markdown": "This week: water tank cleaning on Sunday.",
    # rules Q&A
    "answered": True,
    "answer": "Yes, the clubhouse can be booked for private events per Notice 3.",
    "source_hint": "Notice 3",
    # feedback analyzer
    "draft_poll": {"question": "Do you want a new gym?", "options": ["Yes", "No"]},
    "themes": [{"theme": "cost", "mentions": 3}],
    "suggested_next_step": "Share a cost estimate before the vote.",
    "summary_markdown": "62% support a new gym.",
    # amenity booking
    "amenity": "clubhouse",
    "requested_when": "Saturday evening",
    "conflicts": [],
    "suggested_slots": ["Saturday 6:00 PM - 9:00 PM"],
    "note": "Slot appears free; confirm to book.",
    "confirmation_required": True,
    # bill explainer / maintenance
    "explanation": "Your total is the sum of the listed charges.",
    "equipment": "Lift",
    "maintenance_type": "Preventive",
    "checklist": ["Check cables"],
    "recommended_follow_up": "Monthly inspection",
    "assistant_markdown": "## Checklist",
}


@pytest.fixture()
def fake_ai(monkeypatch):
    """Patch Gemini so no network call is made and output is deterministic."""
    monkeypatch.setattr(ai_module, "generate_json", lambda *a, **k: dict(_FAKE_AI_JSON))
    monkeypatch.setattr(ai_module, "generate_text", lambda *a, **k: "AI generated text.")
    return _FAKE_AI_JSON


# --------------------------------------------------------------------------- #
# 1. AI status
# --------------------------------------------------------------------------- #
def test_ai_status_lists_features(client, admin_token):
    resp = client.get("/api/ai/status", headers=_auth(admin_token))
    assert resp.status_code == 200
    features = resp.get_json()["data"]["features"]
    for f in ("complaint_resolution_insights", "rules_qa", "feedback_analyzer",
              "amenity_booking_assistant", "notices_summarize_all"):
        assert f in features


# --------------------------------------------------------------------------- #
# 2. Notice generator (existing)
# --------------------------------------------------------------------------- #
def test_notice_generate_success(client, admin_token, fake_ai):
    resp = client.post("/api/ai/notices/generate", headers=_auth(admin_token),
                       json={"topic": "Water tank cleaning", "date": "Sunday"})
    assert resp.status_code == 200
    data = resp.get_json()["data"]
    assert data["title"] and data["body"]


def test_notice_generate_missing_topic_fails(client, admin_token, fake_ai):
    resp = client.post("/api/ai/notices/generate", headers=_auth(admin_token), json={})
    assert resp.status_code == 400


def test_notice_generate_requires_admin(client, resident_token, fake_ai):
    resp = client.post("/api/ai/notices/generate", headers=_auth(resident_token),
                       json={"topic": "x"})
    assert resp.status_code == 403


# --------------------------------------------------------------------------- #
# 3. Multilingual announcement (existing)
# --------------------------------------------------------------------------- #
def test_translate_success(client, admin_token, fake_ai):
    resp = client.post("/api/ai/announcements/translate", headers=_auth(admin_token),
                       json={"text": "Water off tomorrow", "languages": ["Hindi", "Telugu"]})
    assert resp.status_code == 200
    assert isinstance(resp.get_json()["data"]["translations"], dict)


def test_translate_missing_text_fails(client, admin_token, fake_ai):
    resp = client.post("/api/ai/announcements/translate", headers=_auth(admin_token), json={})
    assert resp.status_code == 400


# --------------------------------------------------------------------------- #
# 4. Admin AI Complaint classification & Priority Assessment
# --------------------------------------------------------------------------- #
def test_classify_complaint_success(client, resident_token, fake_ai):
    resp = client.post("/api/ai/complaints/classify", headers=_auth(resident_token),
                       json={"subject": "No water", "description": "No water in Block B since morning."})
    assert resp.status_code == 200
    data = resp.get_json()["data"]
    assert data["category"] == "Water"
    assert data["priority"] in {"High", "Medium", "Low"}
    assert data["suggestion_only"] is True  # AI is advisory, admin overrides


def test_admin_ai_classify_complaint_and_priority(client, admin_token, fake_ai):
    resp = client.post("/api/ai/complaints/classify", headers=_auth(admin_token),
                       json={"subject": "Severe lift malfunction", "description": "Lift trapped on 4th floor with noise."})
    assert resp.status_code == 200
    data = resp.get_json()["data"]
    assert "priority" in data
    assert "category" in data


def test_classify_missing_description_fails(client, resident_token, fake_ai):
    resp = client.post("/api/ai/complaints/classify", headers=_auth(resident_token),
                       json={"subject": "No water"})
    assert resp.status_code == 400


# --------------------------------------------------------------------------- #
# 5. NEW: Summarize all notices at once
# --------------------------------------------------------------------------- #
def test_summarize_all_with_payload(client, resident_token, fake_ai):
    resp = client.post("/api/ai/notices/summarize-all", headers=_auth(resident_token),
                       json={"notices": [{"title": "Water", "body": "Cleaning Sunday"}]})
    assert resp.status_code == 200
    data = resp.get_json()["data"]
    assert data["count"] == 1
    assert "groups" in data


def test_summarize_all_requires_auth(client, fake_ai):
    resp = client.post("/api/ai/notices/summarize-all", json={"notices": [{"title": "x", "body": "y"}]})
    assert resp.status_code == 401


# --------------------------------------------------------------------------- #
# 6. NEW: Complaint resolution insights
# --------------------------------------------------------------------------- #
def test_resolution_insights_with_stats(client, admin_token, fake_ai):
    resp = client.post("/api/ai/complaints/resolution-insights", headers=_auth(admin_token),
                       json={"stats": {"pending": 9, "pending_over_7_days": 6}})
    assert resp.status_code == 200
    data = resp.get_json()["data"]
    assert data["stats"]["pending"] == 9
    assert "recommended_actions" in data


def test_resolution_insights_requires_admin(client, resident_token, fake_ai):
    resp = client.post("/api/ai/complaints/resolution-insights", headers=_auth(resident_token), json={})
    assert resp.status_code == 403


# --------------------------------------------------------------------------- #
# 7. NEW: Circular / Rules Q&A (document-grounded)
# --------------------------------------------------------------------------- #
def test_rules_qa_success(client, resident_token, fake_ai):
    resp = client.post("/api/ai/knowledge/ask", headers=_auth(resident_token),
                       json={"question": "Can I book the clubhouse?",
                             "documents": ["Notice 3: clubhouse may be booked for private events."]})
    assert resp.status_code == 200
    data = resp.get_json()["data"]
    assert data["answered"] is True
    assert data["answer"]


def test_rules_qa_missing_question_fails(client, resident_token, fake_ai):
    resp = client.post("/api/ai/knowledge/ask", headers=_auth(resident_token),
                       json={"documents": ["some rule"]})
    assert resp.status_code == 400


# --------------------------------------------------------------------------- #
# 8. NEW: Poll & Feedback analyzer
# --------------------------------------------------------------------------- #
def test_feedback_analyze_success(client, admin_token, fake_ai):
    resp = client.post("/api/ai/feedback/analyze", headers=_auth(admin_token),
                       json={"goal": "gauge interest in a gym",
                             "responses": ["Too costly", "Great idea", "Need space"]})
    assert resp.status_code == 200
    data = resp.get_json()["data"]
    assert data["response_count"] == 3
    assert "themes" in data


def test_feedback_analyze_empty_fails(client, admin_token, fake_ai):
    resp = client.post("/api/ai/feedback/analyze", headers=_auth(admin_token), json={})
    assert resp.status_code == 400


def test_feedback_requires_admin(client, resident_token, fake_ai):
    resp = client.post("/api/ai/feedback/analyze", headers=_auth(resident_token),
                       json={"goal": "x"})
    assert resp.status_code == 403


# --------------------------------------------------------------------------- #
# 9. NEW: Amenity booking assistant
# --------------------------------------------------------------------------- #
def test_amenity_assist_success(client, resident_token, fake_ai):
    resp = client.post("/api/ai/amenities/assist", headers=_auth(resident_token),
                       json={"request": "book the clubhouse next Saturday evening for 30 people"})
    assert resp.status_code == 200
    data = resp.get_json()["data"]
    assert data["confirmation_required"] is True  # AI never finalizes a booking
    assert "suggested_slots" in data


def test_amenity_assist_missing_request_fails(client, resident_token, fake_ai):
    resp = client.post("/api/ai/amenities/assist", headers=_auth(resident_token), json={})
    assert resp.status_code == 400


# --------------------------------------------------------------------------- #
# 10. AI error handling (config vs provider errors)
# --------------------------------------------------------------------------- #
def test_ai_provider_error_returns_502(client, admin_token, monkeypatch):
    def boom(*a, **k):
        raise GeminiServiceError("model overloaded")
    monkeypatch.setattr(ai_module, "generate_json", boom)
    resp = client.post("/api/ai/notices/generate", headers=_auth(admin_token),
                       json={"topic": "x"})
    assert resp.status_code == 502
    assert resp.get_json()["error"]["code"] == "AI_ERROR"


def test_ai_config_error_returns_503(client, admin_token, monkeypatch):
    def missing_key(*a, **k):
        raise GeminiServiceError("GEMINI_API_KEY is missing. Add it to backend/.env.")
    monkeypatch.setattr(ai_module, "generate_json", missing_key)
    resp = client.post("/api/ai/notices/generate", headers=_auth(admin_token),
                       json={"topic": "x"})
    assert resp.status_code == 503
    assert resp.get_json()["error"]["code"] == "AI_CONFIG_ERROR"


# --------------------------------------------------------------------------- #
# 11. Remaining existing AI endpoints (coverage)
# --------------------------------------------------------------------------- #
def test_event_plan_success(client, admin_token, fake_ai):
    resp = client.post("/api/ai/events/plan", headers=_auth(admin_token),
                       json={"event_name": "Diwali", "expected_residents": "200",
                             "duration": "4h", "budget": "50000"})
    assert resp.status_code == 200


def test_event_plan_missing_name_fails(client, admin_token, fake_ai):
    resp = client.post("/api/ai/events/plan", headers=_auth(admin_token), json={})
    assert resp.status_code == 400


def test_analytics_insights_with_stats(client, admin_token, fake_ai):
    resp = client.post("/api/ai/analytics/insights", headers=_auth(admin_token),
                       json={"stats": {"water": 35, "parking": 27}})
    assert resp.status_code == 200
    assert resp.get_json()["data"]["stats"]["water"] == 35


def test_analytics_insights_default_snapshot(client, admin_token, fake_ai):
    # No stats provided -> backend aggregates from DB.
    resp = client.post("/api/ai/analytics/insights", headers=_auth(admin_token), json={})
    assert resp.status_code == 200
    assert "stats" in resp.get_json()["data"]


def test_meeting_minutes_success(client, admin_token, fake_ai):
    resp = client.post("/api/ai/meetings/minutes", headers=_auth(admin_token),
                       json={"notes": "Discussed budget and security.", "title": "AGM"})
    assert resp.status_code == 200


def test_meeting_minutes_missing_notes_fails(client, admin_token, fake_ai):
    resp = client.post("/api/ai/meetings/minutes", headers=_auth(admin_token), json={})
    assert resp.status_code == 400


def test_notice_summarize_single_success(client, resident_token, fake_ai):
    resp = client.post("/api/ai/notices/summarize", headers=_auth(resident_token),
                       json={"title": "Water", "body": "Cleaning Sunday 9-1, supply affected."})
    assert resp.status_code == 200


def test_maintenance_assist_success(client, admin_token, fake_ai):
    resp = client.post("/api/ai/maintenance/assist", headers=_auth(admin_token),
                       json={"equipment": "Lift", "query": "monthly checklist"})
    assert resp.status_code == 200


def test_maintenance_assist_empty_fails(client, admin_token, fake_ai):
    resp = client.post("/api/ai/maintenance/assist", headers=_auth(admin_token), json={})
    assert resp.status_code == 400


def test_raw_prompt_admin_only(client, resident_token, fake_ai):
    resp = client.post("/api/ai/raw", headers=_auth(resident_token), json={"prompt": "hi"})
    assert resp.status_code == 403


def test_raw_prompt_success(client, admin_token, fake_ai):
    resp = client.post("/api/ai/raw", headers=_auth(admin_token), json={"prompt": "hi"})
    assert resp.status_code == 200
    assert resp.get_json()["data"]["text"]


def test_summarize_all_default_db_path(client, resident_token, fake_ai):
    # No notices in payload -> backend pulls active notices from DB.
    resp = client.post("/api/ai/notices/summarize-all", headers=_auth(resident_token), json={})
    assert resp.status_code == 200


def test_resolution_insights_default_db_path(client, admin_token, fake_ai):
    resp = client.post("/api/ai/complaints/resolution-insights", headers=_auth(admin_token), json={})
    assert resp.status_code == 200
    assert "stats" in resp.get_json()["data"]


def test_rules_qa_default_db_documents(client, resident_token, fake_ai):
    # No documents supplied -> backend uses active notices as the knowledge base.
    resp = client.post("/api/ai/knowledge/ask", headers=_auth(resident_token),
                       json={"question": "What is scheduled?"})
    assert resp.status_code == 200
