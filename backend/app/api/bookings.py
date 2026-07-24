from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from app.api.utils import current_user
from app.core.extensions import db
from app.core.responses import fail, ok
from app.core.security import ROLE_ADMIN, ROLE_OWNER, ROLE_SERVICE_PROVIDER, ROLE_TENANT, roles_required
from app.models import ProviderSlot, ServiceBooking, ServiceProvider
from app.services.query_service import paginate_query


bookings_bp = Blueprint("bookings", __name__, url_prefix="/bookings")


@bookings_bp.get("")
@jwt_required()
def list_bookings():
    user = current_user()
    query = ServiceBooking.query

    if user.role in [ROLE_OWNER, ROLE_TENANT]:
        query = query.filter_by(resident_user_id=user.id)
    elif user.role == ROLE_SERVICE_PROVIDER:
        provider = ServiceProvider.query.filter_by(user_id=user.id).first()
        if not provider:
            return ok({"items": [], "pagination": {"page": 1, "limit": 20, "total": 0, "pages": 0}})
        query = query.filter_by(provider_id=provider.id)

    for field in ["booking_status", "provider_id", "resident_user_id"]:
        value = request.args.get(field)
        if value:
            query = query.filter(getattr(ServiceBooking, field) == value)

    items, pagination = paginate_query(query.order_by(ServiceBooking.created_at.desc()))
    return ok({"items": [i.to_dict() for i in items], "pagination": pagination})


@bookings_bp.get("/<int:booking_id>")
@jwt_required()
def get_booking(booking_id):
    user = current_user()
    booking = db.session.get(ServiceBooking, booking_id)
    if not booking:
        return fail("Booking not found", "NOT_FOUND", 404)

    provider = db.session.get(ServiceProvider, booking.provider_id)
    if user.role != ROLE_ADMIN and user.id not in [booking.resident_user_id, provider.user_id]:
        return fail("Forbidden", "FORBIDDEN", 403)

    return ok(booking.to_dict())


@bookings_bp.post("")
@roles_required(ROLE_OWNER, ROLE_TENANT)
def create_booking():
    user = current_user()
    data = request.get_json() or {}

    required = ["provider_id"]
    missing = [f for f in required if not data.get(f)]
    if missing:
        return fail(f"Missing required fields: {', '.join(missing)}", "VALIDATION_ERROR", 400)

    slot = None
    if data.get("slot_id"):
        slot = db.session.get(ProviderSlot, data["slot_id"])
        if not slot or not slot.is_available:
            return fail("Slot unavailable", "SLOT_UNAVAILABLE", 409)

    booking = ServiceBooking(
        resident_user_id=user.id,
        provider_id=data["provider_id"],
        slot_id=data.get("slot_id"),
        booking_status="requested",
        request_notes=data.get("request_notes"),
    )

    if slot:
        slot.is_available = False

    db.session.add(booking)
    db.session.commit()
    return ok(booking.to_dict(), "Booking created", 201)


@bookings_bp.put("/<int:booking_id>/accept")
@roles_required(ROLE_SERVICE_PROVIDER)
def accept_booking(booking_id):
    actor = current_user()
    booking = db.session.get(ServiceBooking, booking_id)
    if not booking:
        return fail("Booking not found", "NOT_FOUND", 404)

    provider = db.session.get(ServiceProvider, booking.provider_id)
    if not provider or provider.user_id != actor.id:
        return fail("Forbidden", "FORBIDDEN", 403)

    booking.booking_status = "accepted"
    db.session.commit()
    return ok(booking.to_dict(), "Booking accepted")


@bookings_bp.put("/<int:booking_id>/decline")
@roles_required(ROLE_SERVICE_PROVIDER)
def decline_booking(booking_id):
    actor = current_user()
    booking = db.session.get(ServiceBooking, booking_id)
    if not booking:
        return fail("Booking not found", "NOT_FOUND", 404)

    provider = db.session.get(ServiceProvider, booking.provider_id)
    if not provider or provider.user_id != actor.id:
        return fail("Forbidden", "FORBIDDEN", 403)

    booking.booking_status = "declined"
    if booking.slot_id:
        slot = db.session.get(ProviderSlot, booking.slot_id)
        if slot:
            slot.is_available = True

    db.session.commit()
    return ok(booking.to_dict(), "Booking declined")


@bookings_bp.put("/<int:booking_id>/complete")
@roles_required(ROLE_SERVICE_PROVIDER)
def complete_booking(booking_id):
    actor = current_user()
    booking = db.session.get(ServiceBooking, booking_id)
    if not booking:
        return fail("Booking not found", "NOT_FOUND", 404)

    provider = db.session.get(ServiceProvider, booking.provider_id)
    if not provider or provider.user_id != actor.id:
        return fail("Forbidden", "FORBIDDEN", 403)

    booking.booking_status = "completed"
    db.session.commit()
    return ok(booking.to_dict(), "Booking completed")


@bookings_bp.put("/<int:booking_id>/cancel")
@jwt_required()
def cancel_booking(booking_id):
    actor = current_user()
    booking = db.session.get(ServiceBooking, booking_id)
    if not booking:
        return fail("Booking not found", "NOT_FOUND", 404)

    if actor.role != ROLE_ADMIN and booking.resident_user_id != actor.id:
        return fail("Forbidden", "FORBIDDEN", 403)

    booking.booking_status = "cancelled"
    if booking.slot_id:
        slot = db.session.get(ProviderSlot, booking.slot_id)
        if slot:
            slot.is_available = True

    db.session.commit()
    return ok(booking.to_dict(), "Booking cancelled")


@bookings_bp.delete("/<int:booking_id>")
@roles_required(ROLE_ADMIN)
def delete_booking(booking_id):
    booking = db.session.get(ServiceBooking, booking_id)
    if not booking:
        return fail("Booking not found", "NOT_FOUND", 404)
    db.session.delete(booking)
    db.session.commit()
    return ok(message="Booking deleted")

