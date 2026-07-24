from flask import Blueprint, request
from flask_jwt_extended import create_access_token, get_jwt, get_jwt_identity, jwt_required
from sqlalchemy import or_

from app.core.extensions import db
from app.core.responses import fail, ok
from app.models import Society, User
from app.services.auth_service import hash_password, verify_password


auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


ROLE_ALIASES = {
    "resident": "owner",
    "owner": "owner",
    "admin": "admin",
    "provider": "service_provider",
    "service_provider": "service_provider",
    "security": "security",
}


@auth_bp.post("/register")
def register():
    data = request.get_json() or {}

    required_fields = ["full_name", "email", "password", "role", "society_id"]
    missing = [field for field in required_fields if not data.get(field)]
    if missing:
        return fail(f"Missing required fields: {', '.join(missing)}", "VALIDATION_ERROR", 400)

    if User.query.filter_by(email=data["email"]).first():
        return fail("Email already registered", "DUPLICATE_EMAIL", 409)

    society = db.session.get(Society, data["society_id"])
    if not society:
        return fail("Invalid society_id", "VALIDATION_ERROR", 400)

    user = User(
        society_id=society.id,
        role=data["role"],
        full_name=data["full_name"],
        email=data["email"],
        phone=data.get("phone"),
        password_hash=hash_password(data["password"]),
        status="active",
    )
    db.session.add(user)
    db.session.commit()

    token = create_access_token(
        identity=str(user.id),
        additional_claims={"role": user.role, "society_id": user.society_id},
    )
    return ok({"user": user.to_dict(exclude=["password_hash"]), "token": token}, "Registration successful", 201)


@auth_bp.post("/login")
def login():
    data = request.get_json() or {}
    email = (data.get("email") or "").strip()
    password = data.get("password")

    if not email or not password:
        return fail("Email and password are required", "VALIDATION_ERROR", 400)

    user = User.query.filter(or_(User.email == email, User.phone == email)).first()
    if not user or not verify_password(password, user.password_hash):
        return fail("Invalid credentials", "UNAUTHORIZED", 401)

    if user.status != "active":
        return fail("Account is not active", "ACCOUNT_INACTIVE", 403)

    requested_role = data.get("role")
    if requested_role:
        requested_role = ROLE_ALIASES.get(str(requested_role).strip().lower())
        if not requested_role:
            return fail("Invalid role", "VALIDATION_ERROR", 400)
    if requested_role and user.role != requested_role:
        return fail("Role mismatch", "UNAUTHORIZED", 401)

    token = create_access_token(
        identity=str(user.id),
        additional_claims={"role": user.role, "society_id": user.society_id},
    )

    return ok(
        {
            "token": token,
            "expires_in": 43200,
            "user": user.to_dict(exclude=["password_hash"]),
        },
        "Login successful",
    )


@auth_bp.post("/logout")
@jwt_required()
def logout():
    return ok(message="Logged out successfully")


@auth_bp.post("/verify-token")
@jwt_required()
def verify_token():
    claims = get_jwt()
    user_id = get_jwt_identity()
    return ok({"valid": True, "user": {"id": int(user_id), **claims}})


@auth_bp.post("/refresh-token")
@jwt_required()
def refresh_token():
    user_id = get_jwt_identity()
    user = db.session.get(User, user_id)
    if not user:
        return fail("User not found", "NOT_FOUND", 404)

    token = create_access_token(
        identity=str(user.id),
        additional_claims={"role": user.role, "society_id": user.society_id},
    )
    return ok({"token": token, "expires_in": 43200})


@auth_bp.post("/forgot-password")
def forgot_password():
    data = request.get_json() or {}
    identifier = (data.get("email") or "").strip()
    phone = (data.get("phone") or "").strip()
    new_password = data.get("new_password")

    if not identifier or not new_password:
        return fail("email and new_password are required", "VALIDATION_ERROR", 400)

    user = User.query.filter(or_(User.email == identifier, User.phone == identifier)).first()
    if not user:
        return fail("User not found", "NOT_FOUND", 404)

    if phone and user.phone != phone:
        return fail("Phone does not match account", "UNAUTHORIZED", 401)

    user.password_hash = hash_password(new_password)
    db.session.commit()
    return ok(message="Password reset successful")


@auth_bp.post("/change-password")
@jwt_required()
def change_password():
    user_id = get_jwt_identity()
    user = db.session.get(User, user_id)
    if not user:
        return fail("User not found", "NOT_FOUND", 404)

    data = request.get_json() or {}
    current_password = data.get("current_password")
    new_password = data.get("new_password")

    if not current_password or not new_password:
        return fail("current_password and new_password are required", "VALIDATION_ERROR", 400)

    if not verify_password(current_password, user.password_hash):
        return fail("Current password is incorrect", "UNAUTHORIZED", 401)

    user.password_hash = hash_password(new_password)
    db.session.commit()
    return ok(message="Password changed successfully")

