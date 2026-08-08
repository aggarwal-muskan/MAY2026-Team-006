from datetime import UTC, datetime, timedelta

from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required
from sqlalchemy import func

from app.core.responses import fail, ok
from app.core.security import ROLE_ADMIN, ROLE_OWNER, ROLE_TENANT, roles_required
from app.models import Complaint, Event, Notice, ServiceBooking, User, VisitorEntry
from app.services import ai_prompts
from app.services.gemini_service import GeminiServiceError, generate_json, generate_text


ai_bp = Blueprint("ai", __name__, url_prefix="/ai")


def _ai_error(error: Exception):
    message = str(error) or "AI request failed"
    code = "AI_CONFIG_ERROR" if "GEMINI_API_KEY" in message else "AI_ERROR"
    status = 503 if code == "AI_CONFIG_ERROR" else 502
    return fail(message, code, status)


def _require_text(data: dict, field: str, label: str | None = None) -> str:
    value = str(data.get(field) or "").strip()
    if not value:
        raise ValueError(f"{label or field} is required")
    return value


@ai_bp.get("/status")
@jwt_required()
def ai_status():
    configured = bool(str(current_app.config.get("GEMINI_API_KEY") or "").strip())
    return ok(
        {
            "configured": configured,
            "model": current_app.config.get("GEMINI_MODEL") or "gemini-flash-latest",
            "features": [
                "notice_generator",
                "multilingual_announcement",
                "event_planner",
                "analytics_insights",
                "complaint_classification",
                "meeting_minutes",
                "notice_summarizer",
                "notices_summarize_all",
                "maintenance_assistant",
                "complaint_resolution_insights",
                "rules_qa",
                "feedback_analyzer",
                "amenity_booking_assistant",
            ],
        }
    )


@ai_bp.post("/notices/generate")
@roles_required(ROLE_ADMIN)
def generate_notice():
    data = request.get_json() or {}
    try:
        topic = _require_text(data, "topic", "topic")
        result = generate_json(
            ai_prompts.notice_generator_prompt(
                topic=topic,
                date=str(data.get("date") or "").strip(),
                time_range=str(data.get("time") or data.get("time_range") or "").strip(),
                extra=str(data.get("extra") or data.get("additional_information") or "").strip(),
            ),
            system=ai_prompts.SOCIETY_SYSTEM,
        )
        return ok(
            {
                "title": str(result.get("title") or topic).strip(),
                "body": str(result.get("body") or "").strip(),
            },
            "Notice draft generated",
        )
    except ValueError as error:
        return fail(str(error), "VALIDATION_ERROR", 400)
    except GeminiServiceError as error:
        return _ai_error(error)


@ai_bp.post("/announcements/translate")
@roles_required(ROLE_ADMIN)
def translate_announcement():
    data = request.get_json() or {}
    try:
        text = _require_text(data, "text", "announcement text")
        languages = data.get("languages") or ["English", "Hindi", "Telugu"]
        if not isinstance(languages, list) or not languages:
            return fail("languages must be a non-empty list", "VALIDATION_ERROR", 400)
        languages = [str(item).strip() for item in languages if str(item).strip()]
        result = generate_json(
            ai_prompts.translate_announcement_prompt(text, languages),
            system=ai_prompts.SOCIETY_SYSTEM,
        )
        translations = result.get("translations") or result
        if not isinstance(translations, dict):
            return fail("AI returned invalid translation payload", "AI_ERROR", 502)
        return ok({"translations": translations}, "Translations generated")
    except ValueError as error:
        return fail(str(error), "VALIDATION_ERROR", 400)
    except GeminiServiceError as error:
        return _ai_error(error)


@ai_bp.post("/events/plan")
@roles_required(ROLE_ADMIN)
def plan_event():
    data = request.get_json() or {}
    try:
        event_name = _require_text(data, "event_name", "event name")
        expected = data.get("expected_residents")
        if expected is not None and expected != "":
            expected = int(expected)
        else:
            expected = None
        result = generate_json(
            ai_prompts.event_planner_prompt(
                event_name=event_name,
                expected_residents=expected,
                duration=str(data.get("duration") or "").strip(),
                budget=str(data.get("budget") or "").strip(),
                notes=str(data.get("notes") or "").strip(),
            ),
            system=ai_prompts.SOCIETY_SYSTEM,
        )
        return ok(result, "Event plan generated")
    except ValueError as error:
        return fail(str(error), "VALIDATION_ERROR", 400)
    except GeminiServiceError as error:
        return _ai_error(error)


def _complaint_category_counts() -> dict[str, int]:
    rows = (
        Complaint.query.with_entities(Complaint.category, func.count(Complaint.id))
        .group_by(Complaint.category)
        .all()
    )
    return {str(category or "Other"): int(count) for category, count in rows}


def _build_analytics_snapshot() -> dict:
    now = datetime.now(UTC)
    month_ago = now - timedelta(days=30)
    return {
        "residents": User.query.filter(User.role.in_(["owner", "tenant"])).count(),
        "pending_complaints": Complaint.query.filter(
            Complaint.status.in_(["open", "in_progress"])
        ).count(),
        "complaints_by_category": _complaint_category_counts(),
        "complaints_last_30_days": Complaint.query.filter(Complaint.created_at >= month_ago).count(),
        "upcoming_events": Event.query.filter_by(status="scheduled").count(),
        "published_notices": Notice.query.count(),
        "bookings_total": ServiceBooking.query.count(),
        "visitors_total": VisitorEntry.query.count(),
        "visitors_open": VisitorEntry.query.filter_by(exit_time=None).count(),
    }


@ai_bp.post("/analytics/insights")
@roles_required(ROLE_ADMIN)
def analytics_insights():
    data = request.get_json() or {}
    stats = data.get("stats") if isinstance(data.get("stats"), dict) else _build_analytics_snapshot()
    try:
        result = generate_json(
            ai_prompts.analytics_insights_prompt(stats),
            system=ai_prompts.SOCIETY_SYSTEM,
        )
        return ok({"stats": stats, **result}, "Insights generated")
    except GeminiServiceError as error:
        return _ai_error(error)


@ai_bp.post("/complaints/classify")
@roles_required(ROLE_OWNER, ROLE_TENANT, ROLE_ADMIN)
def classify_complaint():
    data = request.get_json() or {}
    try:
        subject = str(data.get("subject") or data.get("title") or "").strip()
        description = _require_text(data, "description", "description")
        result = generate_json(
            ai_prompts.complaint_classify_prompt(subject, description),
            system=ai_prompts.SOCIETY_SYSTEM,
        )
        category = str(result.get("category") or "Other").strip()
        priority = str(result.get("priority") or "Medium").strip().title()
        if priority not in {"High", "Medium", "Low"}:
            priority = "Medium"
        return ok(
            {
                "category": category,
                "priority": priority,
                "sentiment": str(result.get("sentiment") or "Neutral"),
                "confidence": result.get("confidence"),
                "rationale": result.get("rationale"),
                "suggestion_only": True,
            },
            "Complaint classified",
        )
    except ValueError as error:
        return fail(str(error), "VALIDATION_ERROR", 400)
    except GeminiServiceError as error:
        return _ai_error(error)


@ai_bp.post("/meetings/minutes")
@roles_required(ROLE_ADMIN)
def meeting_minutes():
    data = request.get_json() or {}
    try:
        notes = _require_text(data, "notes", "meeting notes")
        result = generate_json(
            ai_prompts.meeting_minutes_prompt(
                notes=notes,
                meeting_title=str(data.get("title") or "").strip(),
                meeting_date=str(data.get("date") or "").strip(),
            ),
            system=ai_prompts.SOCIETY_SYSTEM,
        )
        return ok(result, "Meeting minutes generated")
    except ValueError as error:
        return fail(str(error), "VALIDATION_ERROR", 400)
    except GeminiServiceError as error:
        return _ai_error(error)


@ai_bp.post("/notices/summarize")
@jwt_required()
def summarize_notice():
    data = request.get_json() or {}
    try:
        title = str(data.get("title") or "Society Notice").strip()
        body = _require_text(data, "body", "notice body")
        result = generate_json(
            ai_prompts.notice_summarizer_prompt(title, body),
            system=ai_prompts.SOCIETY_SYSTEM,
        )
        return ok(result, "Notice summarized")
    except ValueError as error:
        return fail(str(error), "VALIDATION_ERROR", 400)
    except GeminiServiceError as error:
        return _ai_error(error)


@ai_bp.post("/maintenance/assist")
@roles_required(ROLE_ADMIN)
def maintenance_assist():
    data = request.get_json() or {}
    try:
        query = str(data.get("query") or data.get("question") or "").strip()
        equipment = str(data.get("equipment") or "").strip()
        notes = str(data.get("notes") or "").strip()
        if not query and not equipment and not notes:
            return fail("Provide query, equipment, or notes", "VALIDATION_ERROR", 400)
        if not query:
            query = f"Create a maintenance checklist for {equipment or 'society equipment'}."
        result = generate_json(
            ai_prompts.maintenance_assistant_prompt(query, equipment, notes),
            system=ai_prompts.SOCIETY_SYSTEM,
        )
        return ok(result, "Maintenance guidance generated")
    except GeminiServiceError as error:
        return _ai_error(error)


def _active_notices(limit: int = 25) -> list[dict]:
    now = datetime.now(UTC)
    query = (
        Notice.query.filter(Notice.publish_at <= now)
        .filter((Notice.expires_at.is_(None)) | (Notice.expires_at >= now))
        .order_by(Notice.publish_at.desc())
        .limit(limit)
    )
    return [
        {
            "title": n.title,
            "type": n.notice_type,
            "priority": n.priority,
            "publish_at": n.publish_at.isoformat() if n.publish_at else None,
            "body": (n.body or "")[:400],
        }
        for n in query.all()
    ]


@ai_bp.post("/notices/summarize-all")
@jwt_required()
def summarize_all_notices():
    """Single 'Summarize Notices' option: one combined digest of all active notices."""
    data = request.get_json() or {}
    notices = data.get("notices")
    if not isinstance(notices, list) or not notices:
        notices = _active_notices()
    if not notices:
        return ok(
            {"headline": "No active notices", "groups": [], "digest_markdown": "There are no active notices right now."},
            "No active notices to summarize",
        )
    try:
        result = generate_json(
            ai_prompts.notices_summarize_all_prompt(notices),
            system=ai_prompts.SOCIETY_SYSTEM,
        )
        return ok({"count": len(notices), **result}, "Notices summarized")
    except GeminiServiceError as error:
        return _ai_error(error)


def _resolution_snapshot() -> dict:
    now = datetime.now(UTC)
    week_ago = now - timedelta(days=7)
    open_statuses = ["open", "in_progress"]

    total = Complaint.query.count()
    resolved = Complaint.query.filter(Complaint.status.in_(["resolved", "closed"])).count()
    pending = Complaint.query.filter(Complaint.status.in_(open_statuses)).count()
    pending_over_7_days = Complaint.query.filter(
        Complaint.status.in_(open_statuses), Complaint.created_at <= week_ago
    ).count()

    pending_by_category = {
        str(cat or "Other"): int(count)
        for cat, count in (
            Complaint.query.with_entities(Complaint.category, func.count(Complaint.id))
            .filter(Complaint.status.in_(open_statuses))
            .group_by(Complaint.category)
            .all()
        )
    }
    return {
        "total_complaints": total,
        "resolved": resolved,
        "pending": pending,
        "pending_over_7_days": pending_over_7_days,
        "pending_by_category": pending_by_category,
    }


@ai_bp.post("/complaints/resolution-insights")
@roles_required(ROLE_ADMIN)
def complaint_resolution_insights():
    data = request.get_json() or {}
    stats = data.get("stats") if isinstance(data.get("stats"), dict) else _resolution_snapshot()
    try:
        result = generate_json(
            ai_prompts.complaint_resolution_insights_prompt(stats),
            system=ai_prompts.SOCIETY_SYSTEM,
        )
        return ok({"stats": stats, **result}, "Resolution insights generated")
    except GeminiServiceError as error:
        return _ai_error(error)


@ai_bp.post("/knowledge/ask")
@jwt_required()
def rules_qa():
    """Document-grounded Q&A over society notices/rules. Not a free-form chatbot."""
    data = request.get_json() or {}
    try:
        question = _require_text(data, "question", "question")
        documents = data.get("documents")
        if isinstance(documents, list):
            documents = "\n\n".join(str(item) for item in documents if str(item).strip())
        documents = str(documents or "").strip()
        if not documents:
            notices = _active_notices(limit=30)
            documents = "\n\n".join(f"{n['title']}: {n['body']}" for n in notices)
        if not documents:
            return ok(
                {"answered": False, "answer": "No society documents are available to answer from.", "source_hint": None},
                "No documents available",
            )
        result = generate_json(
            ai_prompts.rules_qa_prompt(question, documents),
            system=ai_prompts.SOCIETY_SYSTEM,
        )
        return ok(result, "Answer generated")
    except ValueError as error:
        return fail(str(error), "VALIDATION_ERROR", 400)
    except GeminiServiceError as error:
        return _ai_error(error)


@ai_bp.post("/feedback/analyze")
@roles_required(ROLE_ADMIN)
def feedback_analyze():
    data = request.get_json() or {}
    goal = str(data.get("goal") or "").strip()
    poll_question = str(data.get("poll_question") or data.get("question") or "").strip()
    responses = data.get("responses") or []
    if not isinstance(responses, list):
        return fail("responses must be a list", "VALIDATION_ERROR", 400)
    responses = [str(item).strip() for item in responses if str(item).strip()]
    if not goal and not poll_question and not responses:
        return fail("Provide a goal, poll_question, or responses", "VALIDATION_ERROR", 400)
    try:
        result = generate_json(
            ai_prompts.feedback_analyze_prompt(goal, poll_question, responses),
            system=ai_prompts.SOCIETY_SYSTEM,
        )
        return ok({"response_count": len(responses), **result}, "Feedback analyzed")
    except GeminiServiceError as error:
        return _ai_error(error)


@ai_bp.post("/amenities/assist")
@roles_required(ROLE_OWNER, ROLE_TENANT, ROLE_ADMIN)
def amenity_booking_assist():
    """AI proposes amenity slots; the app still confirms and writes the booking."""
    data = request.get_json() or {}
    try:
        request_text = _require_text(data, "request", "booking request")
        existing = data.get("existing_bookings")
        if not isinstance(existing, list):
            existing = []
        result = generate_json(
            ai_prompts.amenity_booking_prompt(request_text, existing),
            system=ai_prompts.SOCIETY_SYSTEM,
        )
        result.setdefault("confirmation_required", True)
        return ok(result, "Booking suggestions generated")
    except ValueError as error:
        return fail(str(error), "VALIDATION_ERROR", 400)
    except GeminiServiceError as error:
        return _ai_error(error)


@ai_bp.post("/raw")
@roles_required(ROLE_ADMIN)
def raw_prompt():
    data = request.get_json() or {}
    try:
        prompt = _require_text(data, "prompt", "prompt")
        text = generate_text(prompt, system=ai_prompts.SOCIETY_SYSTEM)
        return ok({"text": text})
    except ValueError as error:
        return fail(str(error), "VALIDATION_ERROR", 400)
    except GeminiServiceError as error:
        return _ai_error(error)
