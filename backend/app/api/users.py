import os
from uuid import uuid4
from datetime import date

from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required
from werkzeug.utils import secure_filename

from app.api.utils import current_user
from app.core.extensions import db
from app.core.responses import fail, ok
from app.core.security import ROLE_ADMIN, roles_required
from app.models import ResidentOccupancy, Unit, User
from app.services.auth_service import hash_password
from app.services.query_service import paginate_query


users_bp = Blueprint("users", __name__, url_prefix="/users")

ALLOWED_PROFILE_IMAGE_EXTENSIONS = {"jpg", "jpeg", "png", "webp"}
MAX_PROFILE_IMAGE_BYTES = 5 * 1024 * 1024


def _unit_number_for_user_id(user_id):
    occupancy = (
        ResidentOccupancy.query.filter_by(user_id=user_id)
        .order_by(ResidentOccupancy.is_primary.desc(), ResidentOccupancy.start_date.desc())
        .first()
    )
    if not occupancy:
        return None
    unit = db.session.get(Unit, occupancy.unit_id)
    return unit.unit_number if unit else None


def _attach_unit_details(users):
    if not users:
        return []
    user_ids = [item.id for item in users]
    occupancies = (
        ResidentOccupancy.query.filter(ResidentOccupancy.user_id.in_(user_ids))
        .order_by(ResidentOccupancy.user_id.asc(), ResidentOccupancy.is_primary.desc(), ResidentOccupancy.start_date.desc())
        .all()
    )
    occupancy_by_user_id = {}
    for occupancy in occupancies:
        if occupancy.user_id not in occupancy_by_user_id:
            occupancy_by_user_id[occupancy.user_id] = occupancy

    unit_ids = [occ.unit_id for occ in occupancy_by_user_id.values() if occ and occ.unit_id]
    units = {unit.id: unit for unit in Unit.query.filter(Unit.id.in_(unit_ids or [-1])).all()}

    payload = []
    for user in users:
        data = user.to_dict(exclude=["password_hash"])
        occ = occupancy_by_user_id.get(user.id)
        unit = units.get(occ.unit_id) if occ else None
        unit_number = unit.unit_number if unit else None
        data["unit_number"] = unit_number
        data["flat_number"] = unit_number or user.flat_number
        payload.append(data)
    return payload


@users_bp.get("")
@roles_required(ROLE_ADMIN)
def list_users():
    query = User.query
    for field in ["role", "status", "society_id"]:
        value = request.args.get(field)
        if value:
            query = query.filter(getattr(User, field) == value)

    search = request.args.get("search")
    if search:
        query = query.filter(
            db.or_(
                User.full_name.ilike(f"%{search}%"),
                User.email.ilike(f"%{search}%"),
                User.phone.ilike(f"%{search}%"),
                User.flat_number.ilike(f"%{search}%"),
            )
        )

    users, pagination = paginate_query(query.order_by(User.created_at.desc()))
    return ok({"items": _attach_unit_details(users), "pagination": pagination})


@users_bp.get("/me")
@jwt_required()
def me():
    user = current_user()
    if not user:
        return fail("User not found", "NOT_FOUND", 404)
    return ok(user.to_dict(exclude=["password_hash"]))


@users_bp.put("/me")
@jwt_required()
def update_me():
    user = current_user()
    data = request.get_json() or {}

    if "full_name" in data:
        user.full_name = data["full_name"]
    if "phone" in data:
        user.phone = data["phone"]
    if "flat_number" in data:
        user.flat_number = data["flat_number"]

    db.session.commit()
    payload = user.to_dict(exclude=["password_hash"])
    payload["unit_number"] = _unit_number_for_user_id(user.id)
    payload["flat_number"] = payload.get("unit_number") or user.flat_number
    return ok(payload, "Profile updated")


@users_bp.post("/me/profile-image")
@jwt_required()
def upload_profile_image():
    user = current_user()
    file = request.files.get("image")
    if not file:
        return fail("Image file is required", "VALIDATION_ERROR", 400)

    filename = secure_filename(file.filename or "")
    if "." not in filename:
        return fail("Invalid file name", "VALIDATION_ERROR", 400)

    extension = filename.rsplit(".", 1)[1].lower()
    if extension not in ALLOWED_PROFILE_IMAGE_EXTENSIONS:
        return fail("Unsupported file type. Allowed: jpg, jpeg, png, webp", "VALIDATION_ERROR", 400)

    file.seek(0, os.SEEK_END)
    file_size = file.tell()
    file.seek(0)
    if file_size > MAX_PROFILE_IMAGE_BYTES:
        return fail("File too large. Maximum allowed size is 5MB", "VALIDATION_ERROR", 400)

    uploads_dir = os.path.join(current_app.instance_path, "uploads", "profiles")
    os.makedirs(uploads_dir, exist_ok=True)

    stored_name = f"user-{user.id}-{uuid4().hex[:8]}.{extension}"
    file.save(os.path.join(uploads_dir, stored_name))

    image_path = f"/uploads/profiles/{stored_name}"
    user.profile_image_url = image_path
    db.session.commit()

    payload = user.to_dict(exclude=["password_hash"])
    payload["profile_image_url"] = image_path
    payload["flat_number"] = _unit_number_for_user_id(user.id) or user.flat_number
    return ok(payload, "Profile image updated")


@users_bp.get("/<int:user_id>")
@jwt_required()
def get_user(user_id):
    requester = current_user()
    if not requester:
        return fail("User not found", "NOT_FOUND", 404)

    target = db.session.get(User, user_id)
    if not target:
        return fail("User not found", "NOT_FOUND", 404)

    if requester.role != ROLE_ADMIN and requester.id != target.id:
        return fail("Forbidden", "FORBIDDEN", 403)

    return ok(target.to_dict(exclude=["password_hash"]))


@users_bp.post("")
@roles_required(ROLE_ADMIN)
def create_user():
    data = request.get_json() or {}
    required_fields = ["society_id", "role", "full_name", "email", "password"]
    missing = [field for field in required_fields if not data.get(field)]
    if missing:
        return fail(f"Missing required fields: {', '.join(missing)}", "VALIDATION_ERROR", 400)

    if User.query.filter_by(email=data["email"]).first():
        return fail("Email already exists", "DUPLICATE_EMAIL", 409)

    user = User(
        society_id=data["society_id"],
        role=data["role"],
        full_name=data["full_name"],
        email=data["email"],
        phone=data.get("phone"),
        password_hash=hash_password(data["password"]),
        status=data.get("status", "active"),
        flat_number=data.get("flat_number"),
    )
    db.session.add(user)
    db.session.commit()
    if data.get("flat_number") and data.get("role") in {"owner", "tenant"}:
        unit_number = str(data["flat_number"]).strip()
        if unit_number:
            unit = Unit.query.filter_by(society_id=user.society_id, unit_number=unit_number).first()
            if not unit:
                unit = Unit(
                    society_id=user.society_id,
                    block_name=unit_number.split("-")[0] if "-" in unit_number else None,
                    unit_number=unit_number,
                    status="active",
                )
                db.session.add(unit)
                db.session.flush()

            occupancy = ResidentOccupancy.query.filter_by(user_id=user.id, unit_id=unit.id).first()
            if not occupancy:
                occupancy = ResidentOccupancy(
                    unit_id=unit.id,
                    user_id=user.id,
                    occupancy_type="owner" if user.role == "owner" else "tenant",
                    start_date=date.today(),
                    is_primary=True,
                )
                db.session.add(occupancy)
            db.session.commit()

    payload = user.to_dict(exclude=["password_hash"])
    payload["unit_number"] = _unit_number_for_user_id(user.id)
    payload["flat_number"] = payload.get("unit_number") or user.flat_number
    return ok(payload, "User created", 201)


@users_bp.put("/<int:user_id>")
@jwt_required()
def update_user(user_id):
    requester = current_user()
    target = db.session.get(User, user_id)
    if not target:
        return fail("User not found", "NOT_FOUND", 404)

    if requester.role != ROLE_ADMIN and requester.id != target.id:
        return fail("Forbidden", "FORBIDDEN", 403)

    data = request.get_json() or {}
    editable_fields = ["full_name", "phone", "flat_number"]
    if requester.role == ROLE_ADMIN:
        editable_fields.extend(["email", "role", "society_id", "status", "profile_image_url"])

    for field in editable_fields:
        if field in data:
            setattr(target, field, data[field])

    if data.get("password"):
        target.password_hash = hash_password(data["password"])

    if "flat_number" in data and target.role in {"owner", "tenant"}:
        unit_number = str(data.get("flat_number") or "").strip()
        if unit_number:
            unit = Unit.query.filter_by(society_id=target.society_id, unit_number=unit_number).first()
            if not unit:
                unit = Unit(
                    society_id=target.society_id,
                    block_name=unit_number.split("-")[0] if "-" in unit_number else None,
                    unit_number=unit_number,
                    status="active",
                )
                db.session.add(unit)
                db.session.flush()

            occupancy = ResidentOccupancy.query.filter_by(user_id=target.id, is_primary=True).first()
            if occupancy:
                occupancy.unit_id = unit.id
                occupancy.occupancy_type = "owner" if target.role == "owner" else "tenant"
            else:
                db.session.add(
                    ResidentOccupancy(
                        unit_id=unit.id,
                        user_id=target.id,
                        occupancy_type="owner" if target.role == "owner" else "tenant",
                        start_date=date.today(),
                        is_primary=True,
                    )
                )

    db.session.commit()
    payload = target.to_dict(exclude=["password_hash"])
    payload["unit_number"] = _unit_number_for_user_id(target.id)
    payload["flat_number"] = payload.get("unit_number") or target.flat_number
    return ok(payload, "User updated")


@users_bp.delete("/<int:user_id>")
@roles_required(ROLE_ADMIN)
def delete_user(user_id):
    user = db.session.get(User, user_id)
    if not user:
        return fail("User not found", "NOT_FOUND", 404)
    db.session.delete(user)
    db.session.commit()
    return ok(message="User deleted successfully")


@users_bp.post("/<int:user_id>/activate")
@roles_required(ROLE_ADMIN)
def activate_user(user_id):
    user = db.session.get(User, user_id)
    if not user:
        return fail("User not found", "NOT_FOUND", 404)
    user.status = "active"
    db.session.commit()
    return ok(message="User activated")


@users_bp.post("/<int:user_id>/deactivate")
@roles_required(ROLE_ADMIN)
def deactivate_user(user_id):
    user = db.session.get(User, user_id)
    if not user:
        return fail("User not found", "NOT_FOUND", 404)
    user.status = "inactive"
    db.session.commit()
    return ok(message="User deactivated")

