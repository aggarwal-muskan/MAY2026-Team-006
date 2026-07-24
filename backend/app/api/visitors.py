from datetime import UTC, datetime

from flask import Blueprint, request

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

    return ok(
        {
            "total_today": len(entries),
            "currently_inside": len(inside),
            "exited": len(entries) - len(inside),
            "entries": [e.to_dict() for e in entries],
        }
    )


@visitors_bp.post("")
@roles_required(ROLE_SECURITY)
def create_visitor():
    data = request.get_json() or {}
    required = ["society_id", "recorded_by_user_id", "visitor_name"]
    missing = [f for f in required if not data.get(f)]
    if missing:
        return fail(f"Missing required fields: {', '.join(missing)}", "VALIDATION_ERROR", 400)

    entry = VisitorEntry(
        society_id=data["society_id"],
        recorded_by_user_id=data["recorded_by_user_id"],
        resident_user_id=data.get("resident_user_id"),
        visitor_name=data["visitor_name"],
        vehicle_number=data.get("vehicle_number"),
        contact_number=data.get("contact_number"),
        entry_time=datetime.now(UTC),
        remarks=data.get("remarks"),
    )

    db.session.add(entry)
    db.session.commit()
    return ok(entry.to_dict(), "Visitor entry created", 201)


@visitors_bp.put("/<int:entry_id>/exit")
@roles_required(ROLE_ADMIN, ROLE_SECURITY)
def exit_visitor(entry_id):
    entry = db.session.get(VisitorEntry, entry_id)
    if not entry:
        return fail("Visitor entry not found", "NOT_FOUND", 404)

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
    for field in ["visitor_name", "contact_number", "vehicle_number", "remarks", "resident_user_id"]:
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


