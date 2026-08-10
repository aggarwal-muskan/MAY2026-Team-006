from datetime import UTC, datetime

from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from app.api.utils import current_user, parse_date
from app.core.extensions import db
from app.core.responses import fail, ok
from app.core.security import ROLE_ADMIN, ROLE_OWNER, ROLE_TENANT, roles_required
from app.models import Event, EventRegistration
from app.services.query_service import paginate_query


events_bp = Blueprint("events", __name__, url_prefix="/events")


@events_bp.get("")
@jwt_required()
def list_events():
    query = Event.query
    for field in ["status", "society_id"]:
        value = request.args.get(field)
        if value:
            query = query.filter(getattr(Event, field) == value)

    if request.args.get("upcoming", "false").lower() == "true":
        query = query.filter(Event.event_date >= datetime.now(UTC).date())

    search = request.args.get("search")
    if search:
        query = query.filter(db.or_(Event.title.ilike(f"%{search}%"), Event.venue.ilike(f"%{search}%")))

    items, pagination = paginate_query(query.order_by(Event.event_date.asc()))
    return ok({"items": [i.to_dict() for i in items], "pagination": pagination})


@events_bp.get("/<int:event_id>")
@jwt_required()
def get_event(event_id):
    event = db.session.get(Event, event_id)
    if not event:
        return fail("Event not found", "NOT_FOUND", 404)

    user = current_user()
    registered = EventRegistration.query.filter_by(event_id=event_id, user_id=user.id).first() is not None
    attendees = EventRegistration.query.filter_by(event_id=event_id).count()

    payload = event.to_dict()
    payload["registered_count"] = attendees
    payload["is_registered"] = registered
    return ok(payload)


@events_bp.get("/<int:event_id>/attendees")
@roles_required(ROLE_ADMIN)
def list_event_attendees(event_id):
    rows = EventRegistration.query.filter_by(event_id=event_id).order_by(EventRegistration.registered_at.desc()).all()
    return ok([r.to_dict() for r in rows])


@events_bp.post("")
@roles_required(ROLE_ADMIN)
def create_event():
    actor = current_user()
    data = request.get_json() or {}
    required = ["title", "event_date"]
    missing = [f for f in required if not data.get(f)]
    if missing:
        return fail(f"Missing required fields: {', '.join(missing)}", "VALIDATION_ERROR", 400)

    event = Event(
        society_id=actor.society_id,
        created_by_user_id=actor.id,
        title=data["title"],
        description=data.get("description"),
        event_date=parse_date(data["event_date"]),
        start_time=data.get("start_time"),
        end_time=data.get("end_time"),
        venue=data.get("venue"),
        status=data.get("status", "scheduled"),
    )
    db.session.add(event)
    db.session.commit()
    return ok(event.to_dict(), "Event created", 201)


@events_bp.put("/<int:event_id>")
@roles_required(ROLE_ADMIN)
def update_event(event_id):
    event = db.session.get(Event, event_id)
    if not event:
        return fail("Event not found", "NOT_FOUND", 404)

    data = request.get_json() or {}
    for field in ["title", "description", "start_time", "end_time", "venue", "status"]:
        if field in data:
            setattr(event, field, data[field])
    if "event_date" in data:
        event.event_date = parse_date(data["event_date"])

    db.session.commit()
    return ok(event.to_dict(), "Event updated")


@events_bp.delete("/<int:event_id>")
@roles_required(ROLE_ADMIN)
def delete_event(event_id):
    event = db.session.get(Event, event_id)
    if not event:
        return fail("Event not found", "NOT_FOUND", 404)
    db.session.delete(event)
    db.session.commit()
    return ok(message="Event deleted")


@events_bp.post("/<int:event_id>/register")
@roles_required(ROLE_OWNER, ROLE_TENANT)
def register_event(event_id):
    user = current_user()
    event = db.session.get(Event, event_id)
    if not event:
        return fail("Event not found", "NOT_FOUND", 404)

    # D-07 fix: a cancelled event must stop accepting registrations.
    if str(event.status).lower() == "cancelled":
        return fail("This event has been cancelled", "EVENT_CANCELLED", 409)

    existing = EventRegistration.query.filter_by(event_id=event_id, user_id=user.id).first()
    if existing:
        return fail("Already registered", "ALREADY_REGISTERED", 409)

    registration = EventRegistration(event_id=event_id, user_id=user.id, registered_at=datetime.now(UTC))
    db.session.add(registration)
    db.session.commit()
    return ok(registration.to_dict(), "Registration successful")


@events_bp.post("/<int:event_id>/unregister")
@roles_required(ROLE_OWNER, ROLE_TENANT)
def unregister_event(event_id):
    user = current_user()
    registration = EventRegistration.query.filter_by(event_id=event_id, user_id=user.id).first()
    if not registration:
        return fail("Registration not found", "NOT_FOUND", 404)

    db.session.delete(registration)
    db.session.commit()
    return ok(message="Registration cancelled")


@events_bp.put("/<int:event_id>/cancel")
@roles_required(ROLE_ADMIN)
def cancel_event(event_id):
    event = db.session.get(Event, event_id)
    if not event:
        return fail("Event not found", "NOT_FOUND", 404)

    event.status = "cancelled"
    db.session.commit()
    return ok(event.to_dict(), "Event cancelled")


