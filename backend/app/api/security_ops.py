from datetime import UTC, datetime

from flask import Blueprint, request

from app.api.utils import current_user
from app.core.extensions import db
from app.core.responses import fail, ok
from app.core.security import ROLE_ADMIN, ROLE_SECURITY, roles_required
from app.models import EmergencyAlert, IncidentReport, PatrolLog
from app.services.query_service import paginate_query


patrol_logs_bp = Blueprint("patrol_logs", __name__, url_prefix="/patrol-logs")
emergency_alerts_bp = Blueprint("emergency_alerts", __name__, url_prefix="/emergency-alerts")
incident_reports_bp = Blueprint("incident_reports", __name__, url_prefix="/incident-reports")


@patrol_logs_bp.get("")
@roles_required(ROLE_ADMIN, ROLE_SECURITY)
def list_patrol_logs():
    query = PatrolLog.query
    checkpoint = request.args.get("checkpoint")
    if checkpoint:
        query = query.filter(PatrolLog.checkpoint.ilike(f"%{checkpoint}%"))
    search = request.args.get("search")
    if search:
        query = query.filter(db.or_(PatrolLog.checkpoint.ilike(f"%{search}%"), PatrolLog.note.ilike(f"%{search}%")))
    items, pagination = paginate_query(query.order_by(PatrolLog.patrol_time.desc()))
    return ok({"items": [item.to_dict() for item in items], "pagination": pagination})


@patrol_logs_bp.post("")
@roles_required(ROLE_SECURITY)
def create_patrol_log():
    actor = current_user()
    data = request.get_json() or {}
    required = ["checkpoint", "note"]
    missing = [field for field in required if not data.get(field)]
    if missing:
        return fail(f"Missing required fields: {', '.join(missing)}", "VALIDATION_ERROR", 400)

    log = PatrolLog(
        society_id=actor.society_id,
        recorded_by_user_id=actor.id,
        checkpoint=data["checkpoint"],
        note=data["note"],
        status=data.get("status", "logged"),
        patrol_time=datetime.now(UTC),
    )
    db.session.add(log)
    db.session.commit()
    return ok(log.to_dict(), "Patrol log created", 201)


@emergency_alerts_bp.get("")
@roles_required(ROLE_ADMIN, ROLE_SECURITY)
def list_emergency_alerts():
    query = EmergencyAlert.query
    status = request.args.get("status")
    if status:
        query = query.filter(EmergencyAlert.status == status)
    search = request.args.get("search")
    if search:
        query = query.filter(db.or_(EmergencyAlert.title.ilike(f"%{search}%"), EmergencyAlert.description.ilike(f"%{search}%")))
    items, pagination = paginate_query(query.order_by(EmergencyAlert.alert_time.desc()))
    return ok({"items": [item.to_dict() for item in items], "pagination": pagination})


@emergency_alerts_bp.post("")
@roles_required(ROLE_ADMIN, ROLE_SECURITY)
def create_emergency_alert():
    actor = current_user()
    data = request.get_json() or {}
    required = ["title", "description"]
    missing = [field for field in required if not data.get(field)]
    if missing:
        return fail(f"Missing required fields: {', '.join(missing)}", "VALIDATION_ERROR", 400)

    alert = EmergencyAlert(
        society_id=actor.society_id,
        created_by_user_id=actor.id,
        title=data["title"],
        description=data["description"],
        priority=str(data.get("priority", "medium")).lower(),
        status=str(data.get("status", "active")).lower(),
        alert_time=datetime.now(UTC),
    )
    db.session.add(alert)
    db.session.commit()
    return ok(alert.to_dict(), "Emergency alert created", 201)


@incident_reports_bp.get("")
@roles_required(ROLE_ADMIN, ROLE_SECURITY)
def list_incident_reports():
    query = IncidentReport.query
    status = request.args.get("status")
    if status:
        query = query.filter(IncidentReport.status == status)
    search = request.args.get("search")
    if search:
        query = query.filter(db.or_(IncidentReport.incident_type.ilike(f"%{search}%"), IncidentReport.location.ilike(f"%{search}%"), IncidentReport.description.ilike(f"%{search}%")))
    items, pagination = paginate_query(query.order_by(IncidentReport.occurred_at.desc()))
    return ok({"items": [item.to_dict() for item in items], "pagination": pagination})


@incident_reports_bp.post("")
@roles_required(ROLE_ADMIN, ROLE_SECURITY)
def create_incident_report():
    actor = current_user()
    data = request.get_json() or {}
    required = ["incident_type", "location", "description"]
    missing = [field for field in required if not data.get(field)]
    if missing:
        return fail(f"Missing required fields: {', '.join(missing)}", "VALIDATION_ERROR", 400)

    incident = IncidentReport(
        society_id=actor.society_id,
        reported_by_user_id=actor.id,
        incident_type=data["incident_type"],
        location=data["location"],
        description=data["description"],
        severity=str(data.get("severity", "medium")).lower(),
        status=str(data.get("status", "open")).lower(),
        occurred_at=datetime.now(UTC),
    )
    db.session.add(incident)
    db.session.commit()
    return ok(incident.to_dict(), "Incident reported", 201)
