from datetime import UTC, datetime

from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from app.api.utils import current_user, parse_datetime
from app.core.extensions import db
from app.core.responses import fail, ok
from app.core.security import ROLE_ADMIN, ROLE_SERVICE_PROVIDER, roles_required
from app.models import ProviderReview, ProviderSlot, ServiceCategory, ServiceProvider, ServiceBooking
from app.services.query_service import paginate_query


service_categories_bp = Blueprint("service_categories", __name__, url_prefix="/service-categories")
providers_bp = Blueprint("providers", __name__, url_prefix="/providers")
slots_bp = Blueprint("slots", __name__, url_prefix="/slots")
reviews_bp = Blueprint("reviews", __name__, url_prefix="/reviews")


@service_categories_bp.get("")
@jwt_required()
def list_categories():
    return ok([c.to_dict() for c in ServiceCategory.query.order_by(ServiceCategory.name.asc()).all()])


@service_categories_bp.get("/<int:category_id>")
@jwt_required()
def get_category(category_id):
    category = db.session.get(ServiceCategory, category_id)
    if not category:
        return fail("Category not found", "NOT_FOUND", 404)
    return ok(category.to_dict())


@service_categories_bp.post("")
@roles_required(ROLE_ADMIN)
def create_category():
    data = request.get_json() or {}
    if not data.get("name"):
        return fail("name is required", "VALIDATION_ERROR", 400)

    category = ServiceCategory(name=data["name"], description=data.get("description"), created_at=datetime.now(UTC))
    db.session.add(category)
    db.session.commit()
    return ok(category.to_dict(), "Category created", 201)


@service_categories_bp.put("/<int:category_id>")
@roles_required(ROLE_ADMIN)
def update_category(category_id):
    category = db.session.get(ServiceCategory, category_id)
    if not category:
        return fail("Category not found", "NOT_FOUND", 404)

    data = request.get_json() or {}
    for field in ["name", "description"]:
        if field in data:
            setattr(category, field, data[field])

    db.session.commit()
    return ok(category.to_dict(), "Category updated")


@providers_bp.get("")
@jwt_required()
def list_providers():
    query = ServiceProvider.query
    for field in ["category_id", "verification_status"]:
        value = request.args.get(field)
        if value:
            query = query.filter(getattr(ServiceProvider, field) == value)

    if request.args.get("min_rating"):
        query = query.filter(ServiceProvider.rating_avg >= float(request.args["min_rating"]))

    search = request.args.get("search")
    if search:
        query = query.filter(ServiceProvider.business_name.ilike(f"%{search}%"))

    items, pagination = paginate_query(query.order_by(ServiceProvider.created_at.desc()))
    return ok({"items": [i.to_dict() for i in items], "pagination": pagination})


@providers_bp.get("/<int:provider_id>")
@jwt_required()
def get_provider(provider_id):
    provider = db.session.get(ServiceProvider, provider_id)
    if not provider:
        return fail("Provider not found", "NOT_FOUND", 404)
    return ok(provider.to_dict())


@providers_bp.post("")
@roles_required(ROLE_ADMIN, ROLE_SERVICE_PROVIDER)
def create_provider():
    actor = current_user()
    data = request.get_json() or {}
    required = ["category_id", "business_name"]
    missing = [f for f in required if not data.get(f)]
    if missing:
        return fail(f"Missing required fields: {', '.join(missing)}", "VALIDATION_ERROR", 400)

    user_id = data.get("user_id", actor.id)
    provider = ServiceProvider(
        user_id=user_id,
        category_id=data["category_id"],
        business_name=data["business_name"],
        service_description=data.get("service_description"),
        verification_status="pending",
        rating_avg=0,
    )
    db.session.add(provider)
    db.session.commit()
    return ok(provider.to_dict(), "Provider profile created", 201)


@providers_bp.put("/<int:provider_id>")
@roles_required(ROLE_ADMIN, ROLE_SERVICE_PROVIDER)
def update_provider(provider_id):
    actor = current_user()
    provider = db.session.get(ServiceProvider, provider_id)
    if not provider:
        return fail("Provider not found", "NOT_FOUND", 404)

    if actor.role == ROLE_SERVICE_PROVIDER and actor.id != provider.user_id:
        return fail("Forbidden", "FORBIDDEN", 403)

    data = request.get_json() or {}
    for field in ["category_id", "business_name", "service_description", "verification_status"]:
        if field in data:
            setattr(provider, field, data[field])

    db.session.commit()
    return ok(provider.to_dict(), "Provider updated")


@providers_bp.put("/<int:provider_id>/verify")
@roles_required(ROLE_ADMIN)
def verify_provider(provider_id):
    provider = db.session.get(ServiceProvider, provider_id)
    if not provider:
        return fail("Provider not found", "NOT_FOUND", 404)

    provider.verification_status = "approved"
    db.session.commit()
    return ok(provider.to_dict(), "Provider approved")


@providers_bp.put("/<int:provider_id>/reject")
@roles_required(ROLE_ADMIN)
def reject_provider(provider_id):
    provider = db.session.get(ServiceProvider, provider_id)
    if not provider:
        return fail("Provider not found", "NOT_FOUND", 404)

    provider.verification_status = "rejected"
    db.session.commit()
    return ok(provider.to_dict(), "Provider rejected")


@providers_bp.get("/<int:provider_id>/availability")
@jwt_required()
def provider_availability(provider_id):
    query = ProviderSlot.query.filter_by(provider_id=provider_id, is_available=True)
    if request.args.get("date"):
        d = datetime.fromisoformat(request.args["date"]).date()
        query = query.filter(db.func.date(ProviderSlot.slot_start) == d)
    return ok([s.to_dict() for s in query.order_by(ProviderSlot.slot_start.asc()).all()])


@providers_bp.get("/<int:provider_id>/bookings")
@jwt_required()
def provider_bookings(provider_id):
    items, pagination = paginate_query(ServiceBooking.query.filter_by(provider_id=provider_id).order_by(ServiceBooking.created_at.desc()))
    return ok({"items": [i.to_dict() for i in items], "pagination": pagination})


@providers_bp.get("/<int:provider_id>/earnings")
@jwt_required()
def provider_earnings(provider_id):
    completed = ServiceBooking.query.filter_by(provider_id=provider_id, booking_status="completed").all()
    # Earnings are currently derived from completed job count until amount fields are introduced.
    total_earnings = len(completed) * 500
    return ok({"total_earnings": total_earnings, "completed_bookings": len(completed), "monthly_breakdown": []})


@providers_bp.get("/<int:provider_id>/reviews")
@jwt_required()
def provider_reviews(provider_id):
    rows = ProviderReview.query.filter_by(provider_id=provider_id).order_by(ProviderReview.created_at.desc()).all()
    return ok([r.to_dict() for r in rows])


@slots_bp.get("/<int:provider_id>")
@jwt_required()
def list_slots(provider_id):
    query = ProviderSlot.query.filter_by(provider_id=provider_id)
    if request.args.get("available_only", "false").lower() == "true":
        query = query.filter_by(is_available=True)
    return ok([s.to_dict() for s in query.order_by(ProviderSlot.slot_start.asc()).all()])


@slots_bp.post("")
@roles_required(ROLE_ADMIN, ROLE_SERVICE_PROVIDER)
def create_slot():
    actor = current_user()
    data = request.get_json() or {}
    required = ["provider_id", "slot_start", "slot_end"]
    missing = [f for f in required if not data.get(f)]
    if missing:
        return fail(f"Missing required fields: {', '.join(missing)}", "VALIDATION_ERROR", 400)

    provider = db.session.get(ServiceProvider, data["provider_id"])
    if not provider:
        return fail("Provider not found", "NOT_FOUND", 404)

    if actor.role == ROLE_SERVICE_PROVIDER and provider.user_id != actor.id:
        return fail("Forbidden", "FORBIDDEN", 403)

    slot = ProviderSlot(
        provider_id=provider.id,
        slot_start=parse_datetime(data["slot_start"]),
        slot_end=parse_datetime(data["slot_end"]),
        is_available=bool(data.get("is_available", True)),
    )
    db.session.add(slot)
    db.session.commit()
    return ok(slot.to_dict(), "Slot created", 201)


@slots_bp.put("/<int:slot_id>")
@roles_required(ROLE_ADMIN, ROLE_SERVICE_PROVIDER)
def update_slot(slot_id):
    actor = current_user()
    slot = db.session.get(ProviderSlot, slot_id)
    if not slot:
        return fail("Slot not found", "NOT_FOUND", 404)

    provider = db.session.get(ServiceProvider, slot.provider_id)
    if actor.role == ROLE_SERVICE_PROVIDER and provider.user_id != actor.id:
        return fail("Forbidden", "FORBIDDEN", 403)

    data = request.get_json() or {}
    if "slot_start" in data:
        slot.slot_start = parse_datetime(data["slot_start"])
    if "slot_end" in data:
        slot.slot_end = parse_datetime(data["slot_end"])
    if "is_available" in data:
        slot.is_available = bool(data["is_available"])

    db.session.commit()
    return ok(slot.to_dict(), "Slot updated")


@slots_bp.delete("/<int:slot_id>")
@roles_required(ROLE_ADMIN, ROLE_SERVICE_PROVIDER)
def delete_slot(slot_id):
    actor = current_user()
    slot = db.session.get(ProviderSlot, slot_id)
    if not slot:
        return fail("Slot not found", "NOT_FOUND", 404)

    provider = db.session.get(ServiceProvider, slot.provider_id)
    if actor.role == ROLE_SERVICE_PROVIDER and provider.user_id != actor.id:
        return fail("Forbidden", "FORBIDDEN", 403)

    db.session.delete(slot)
    db.session.commit()
    return ok(message="Slot deleted")


@reviews_bp.get("/provider/<int:provider_id>")
@jwt_required()
def get_reviews(provider_id):
    rows = ProviderReview.query.filter_by(provider_id=provider_id).order_by(ProviderReview.created_at.desc()).all()
    total = len(rows)
    avg = round(sum(r.rating for r in rows) / total, 2) if total else 0
    return ok({"items": [r.to_dict() for r in rows], "summary": {"average_rating": avg, "total_reviews": total}})


@reviews_bp.post("")
@roles_required("owner", "tenant")
def create_review():
    actor = current_user()
    data = request.get_json() or {}

    required = ["provider_id", "booking_id", "rating"]
    missing = [f for f in required if not data.get(f)]
    if missing:
        return fail(f"Missing required fields: {', '.join(missing)}", "VALIDATION_ERROR", 400)

    booking = db.session.get(ServiceBooking, data["booking_id"])
    if not booking or booking.resident_user_id != actor.id or booking.booking_status != "completed":
        return fail("Booking not eligible for review", "UNPROCESSABLE", 422)

    existing = ProviderReview.query.filter_by(booking_id=booking.id, resident_user_id=actor.id).first()
    if existing:
        return fail("Review already exists for this booking", "DUPLICATE", 409)

    review = ProviderReview(
        provider_id=data["provider_id"],
        resident_user_id=actor.id,
        booking_id=booking.id,
        rating=int(data["rating"]),
        feedback=data.get("feedback"),
    )
    db.session.add(review)
    db.session.flush()

    provider_reviews = ProviderReview.query.filter_by(provider_id=review.provider_id).all()
    avg = sum(r.rating for r in provider_reviews) / len(provider_reviews)
    provider = db.session.get(ServiceProvider, review.provider_id)
    provider.rating_avg = round(avg, 2)

    db.session.commit()
    return ok(review.to_dict(), "Review created", 201)


@reviews_bp.put("/<int:review_id>")
@jwt_required()
def update_review(review_id):
    actor = current_user()
    review = db.session.get(ProviderReview, review_id)
    if not review:
        return fail("Review not found", "NOT_FOUND", 404)

    if actor.role != ROLE_ADMIN and actor.id != review.resident_user_id:
        return fail("Forbidden", "FORBIDDEN", 403)

    data = request.get_json() or {}
    if "rating" in data:
        review.rating = int(data["rating"])
    if "feedback" in data:
        review.feedback = data["feedback"]

    db.session.commit()
    return ok(review.to_dict(), "Review updated")


@reviews_bp.delete("/<int:review_id>")
@jwt_required()
def delete_review(review_id):
    actor = current_user()
    review = db.session.get(ProviderReview, review_id)
    if not review:
        return fail("Review not found", "NOT_FOUND", 404)

    if actor.role != ROLE_ADMIN and actor.id != review.resident_user_id:
        return fail("Forbidden", "FORBIDDEN", 403)

    db.session.delete(review)
    db.session.commit()
    return ok(message="Review deleted")


