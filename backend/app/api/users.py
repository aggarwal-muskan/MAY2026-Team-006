from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from app.api.utils import current_user
from app.core.extensions import db
from app.core.responses import fail, ok
from app.core.security import ROLE_ADMIN, roles_required
from app.models import User
from app.services.auth_service import hash_password
from app.services.query_service import paginate_query


users_bp = Blueprint("users", __name__, url_prefix="/users")


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
            )
        )

    users, pagination = paginate_query(query.order_by(User.created_at.desc()))
    return ok({"items": [u.to_dict(exclude=["password_hash"]) for u in users], "pagination": pagination})


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

    db.session.commit()
    return ok(user.to_dict(exclude=["password_hash"]), "Profile updated")


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
    )
    db.session.add(user)
    db.session.commit()
    return ok(user.to_dict(exclude=["password_hash"]), "User created", 201)


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
    editable_fields = ["full_name", "phone"]
    if requester.role == ROLE_ADMIN:
        editable_fields.extend(["email", "role", "society_id", "status"])

    for field in editable_fields:
        if field in data:
            setattr(target, field, data[field])

    if data.get("password"):
        target.password_hash = hash_password(data["password"])

    db.session.commit()
    return ok(target.to_dict(exclude=["password_hash"]), "User updated")


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

