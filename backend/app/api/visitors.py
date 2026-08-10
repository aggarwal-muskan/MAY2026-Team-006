from datetime import UTC, datetime

from flask import Blueprint, request

from app.api.utils import current_user
from app.core.extensions import db
from app.core.responses import fail, ok
from app.core.security import ROLE_ADMIN, ROLE_SECURITY, roles_required
from app.models import VisitorEntry
from app.services.query_service import paginate_query


visitors_bp = Blueprint("visitors", __name__, url_prefix="/visitors")


@visitors_bp.get("")
@roles_required(ROLE_ADMIN, ROLE_SECURITY)
def list_visitors():
    query = VisitorEntry.query

    if request.args.get("date"):
        d = request.args["date"]
        query = query.filter(db.func.date(VisitorEntry.entry_time) == d)

    status = request.args.get("status")
    if status == "inside":
        query = query.filter(VisitorEntry.exit_time.is_(None))
    elif status == "exited":
        query = query.filter(VisitorEntry.exit_time.isnot(None))
    elif status == "pending":
        query = query.filter(VisitorEntry.approval_status == "pending")
    elif status == "approved":
        query = query.filter(VisitorEntry.approval_status == "approved")
    elif status == "rejected":
        query = query.filter(VisitorEntry.approval_status == "rejected")

    approval_status = request.args.get("approval_status")
    if approval_status:
        query = query.filter(VisitorEntry.approval_status == approval_status)

    if request.args.get("vehicle_only", "false").lower() == "true":
        query = query.filter(VisitorEntry.vehicle_number.isnot(None))

    for field in ["resident_user_id"]:
        value = request.args.get(field)
        if value:
            query = query.filter(getattr(VisitorEntry, field) == value)

    search = request.args.get("search")
    if search:
        query = query.filter(db.or_(VisitorEntry.visitor_name.ilike(f"%{search}%"), VisitorEntry.vehicle_number.ilike(f"%{search}%")))

    items, pagination = paginate_query(query.order_by(VisitorEntry.entry_time.desc()))
    return ok({"items": [i.to_dict() for i in items], "pagination": pagination})


@visitors_bp.get("/<int:entry_id>")
@roles_required(ROLE_ADMIN, ROLE_SECURITY)
def get_visitor(entry_id):
    entry = db.session.get(VisitorEntry, entry_id)
    if not entry:
        return fail("Visitor entry not found", "NOT_FOUND", 404)
    return ok(entry.to_dict())


@visitors_bp.get("/today")
@roles_required(ROLE_ADMIN, ROLE_SECURITY)
def visitors_today():
    today = datetime.now(UTC).date().isoformat()
    entries = VisitorEntry.query.filter(db.func.date(VisitorEntry.entry_time) == today).all()
    inside = [e for e in entries if e.exit_time is None]
    pending = [e for e in entries if (e.approval_status or "pending") == "pending"]

    return ok(
        {
            "total_today": len(entries),
            "currently_inside": len(inside),
            "exited": len(entries) - len(inside),
            "pending_approvals": len(pending),
            "entries": [e.to_dict() for e in entries],
        }
    )


@visitors_bp.post("")
@roles_required(ROLE_SECURITY)
def create_visitor():
    actor = current_user()
    data = request.get_json() or {}
    required = ["visitor_name"]
    missing = [f for f in required if not data.get(f)]
    if missing:
        return fail(f"Missing required fields: {', '.join(missing)}", "VALIDATION_ERROR", 400)

    entry = VisitorEntry(
        society_id=data.get("society_id") or actor.society_id,
        recorded_by_user_id=data.get("recorded_by_user_id") or actor.id,
        resident_user_id=data.get("resident_user_id"),
        visitor_name=data["visitor_name"],
        purpose=data.get("purpose"),
        flat_number=data.get("flat_number"),
        vehicle_number=data.get("vehicle_number"),
        vehicle_type=data.get("vehicle_type"),
        contact_number=data.get("contact_number"),
        approval_status=str(data.get("approval_status", "pending")).lower(),
        entry_time=datetime.now(UTC),
        remarks=data.get("remarks"),
    )

    db.session.add(entry)
    db.session.commit()
    return ok(entry.to_dict(), "Visitor entry created", 201)


@visitors_bp.put("/<int:entry_id>/approve")
@roles_required(ROLE_ADMIN, ROLE_SECURITY)
def approve_visitor(entry_id):
    actor = current_user()
    entry = db.session.get(VisitorEntry, entry_id)
    if not entry:
        return fail("Visitor entry not found", "NOT_FOUND", 404)

    entry.approval_status = "approved"
    entry.approved_by_user_id = actor.id
    entry.approved_at = datetime.now(UTC)
    db.session.commit()
    return ok(entry.to_dict(), "Visitor approved")


@visitors_bp.put("/<int:entry_id>/reject")
@roles_required(ROLE_ADMIN, ROLE_SECURITY)
def reject_visitor(entry_id):
    actor = current_user()
    entry = db.session.get(VisitorEntry, entry_id)
    if not entry:
        return fail("Visitor entry not found", "NOT_FOUND", 404)

    entry.approval_status = "rejected"
    entry.approved_by_user_id = actor.id
    entry.approved_at = datetime.now(UTC)
    db.session.commit()
    return ok(entry.to_dict(), "Visitor rejected")


@visitors_bp.put("/<int:entry_id>/exit")
@roles_required(ROLE_ADMIN, ROLE_SECURITY)
def exit_visitor(entry_id):
    entry = db.session.get(VisitorEntry, entry_id)
    if not entry:
        return fail("Visitor entry not found", "NOT_FOUND", 404)

    # D-12 fix: a second exit call used to overwrite the original exit timestamp,
    # destroying the gate audit trail.
    if entry.exit_time is not None:
        return fail("Exit already recorded for this visitor", "ALREADY_EXITED", 409)

    entry.exit_time = datetime.now(UTC)

    db.session.commit()
    return ok(entry.to_dict(), "Exit recorded")


@visitors_bp.put("/<int:entry_id>")
@roles_required(ROLE_ADMIN, ROLE_SECURITY)
def update_visitor(entry_id):
    entry = db.session.get(VisitorEntry, entry_id)
    if not entry:
        return fail("Visitor entry not found", "NOT_FOUND", 404)

    data = request.get_json() or {}
    for field in ["visitor_name", "contact_number", "vehicle_number", "vehicle_type", "purpose", "flat_number", "remarks", "resident_user_id", "approval_status"]:
        if field in data:
            setattr(entry, field, data[field])

    db.session.commit()
    return ok(entry.to_dict(), "Visitor entry updated")


@visitors_bp.delete("/<int:entry_id>")
@roles_required(ROLE_ADMIN)
def delete_visitor(entry_id):
    entry = db.session.get(VisitorEntry, entry_id)
    if not entry:
        return fail("Visitor entry not found", "NOT_FOUND", 404)

    db.session.delete(entry)
    db.session.commit()
    return ok(message="Visitor entry deleted")


