from flask import Blueprint, request

from app.core.extensions import db
from app.core.responses import fail, ok
from app.core.security import ROLE_ADMIN, roles_required
from app.models import Society
from app.services.query_service import paginate_query


societies_bp = Blueprint("societies", __name__, url_prefix="/societies")


@societies_bp.get("")
@roles_required(ROLE_ADMIN)
def list_societies():
    societies, pagination = paginate_query(Society.query.order_by(Society.created_at.desc()))
    return ok({"items": [s.to_dict() for s in societies], "pagination": pagination})


@societies_bp.get("/<int:society_id>")
@roles_required(ROLE_ADMIN)
def get_society(society_id):
    society = db.session.get(Society, society_id)
    if not society:
        return fail("Society not found", "NOT_FOUND", 404)
    return ok(society.to_dict())


@societies_bp.post("")
@roles_required(ROLE_ADMIN)
def create_society():
    data = request.get_json() or {}
    required = ["name", "address", "city", "pincode"]
    missing = [f for f in required if not data.get(f)]
    if missing:
        return fail(f"Missing required fields: {', '.join(missing)}", "VALIDATION_ERROR", 400)

    society = Society(**{k: data.get(k) for k in ["name", "address", "city", "pincode", "contact_email", "contact_phone"]})
    db.session.add(society)
    db.session.commit()
    return ok(society.to_dict(), "Society created", 201)


@societies_bp.put("/<int:society_id>")
@roles_required(ROLE_ADMIN)
def update_society(society_id):
    society = db.session.get(Society, society_id)
    if not society:
        return fail("Society not found", "NOT_FOUND", 404)

    data = request.get_json() or {}
    for field in ["name", "address", "city", "pincode", "contact_email", "contact_phone"]:
        if field in data:
            setattr(society, field, data[field])

    db.session.commit()
    return ok(society.to_dict(), "Society updated")

