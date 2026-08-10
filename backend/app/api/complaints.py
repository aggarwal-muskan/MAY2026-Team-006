from datetime import UTC, datetime

from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from app.api.utils import current_user
from app.core.extensions import db
from app.core.responses import fail, ok
from app.core.security import ROLE_ADMIN, ROLE_OWNER, ROLE_SECURITY, ROLE_SERVICE_PROVIDER, ROLE_TENANT, roles_required
from app.models import Complaint, ComplaintUpdate, User
from app.services.query_service import paginate_query


complaints_bp = Blueprint("complaints", __name__, url_prefix="/complaints")

ALLOWED_COMPLAINT_STATUSES = {"open", "in_progress", "resolved", "closed"}
ALLOWED_PRIORITIES = {"low", "medium", "high", "urgent"}


@complaints_bp.get("")
@jwt_required()
def list_complaints():
    user = current_user()
    query = Complaint.query

    if user.role in [ROLE_OWNER, ROLE_TENANT]:
        query = query.filter(Complaint.raised_by_user_id == user.id)
    elif user.role == ROLE_SECURITY:
        query = query.filter(Complaint.category == "Security")

    for field in ["status", "category", "priority", "assigned_to_user_id", "society_id"]:
        value = request.args.get(field)
        if value:
            query = query.filter(getattr(Complaint, field) == value)

    search = request.args.get("search")
    if search:
        query = query.filter(db.or_(Complaint.subject.ilike(f"%{search}%"), Complaint.description.ilike(f"%{search}%")))

    items, pagination = paginate_query(query.order_by(Complaint.created_at.desc()))
    return ok({"items": [i.to_dict() for i in items], "pagination": pagination})


@complaints_bp.get("/<int:complaint_id>")
@jwt_required()
def get_complaint(complaint_id):
    user = current_user()
    complaint = db.session.get(Complaint, complaint_id)
    if not complaint:
        return fail("Complaint not found", "NOT_FOUND", 404)

    if user.role != ROLE_ADMIN and user.id not in [complaint.raised_by_user_id, complaint.assigned_to_user_id]:
        return fail("Forbidden", "FORBIDDEN", 403)

    updates = ComplaintUpdate.query.filter_by(complaint_id=complaint_id).order_by(ComplaintUpdate.updated_at.asc()).all()
    payload = complaint.to_dict()
    payload["updates"] = [u.to_dict() for u in updates]
    return ok(payload)


@complaints_bp.post("")
@roles_required(ROLE_OWNER, ROLE_TENANT)
def create_complaint():
    user = current_user()
    data = request.get_json() or {}

    required = ["subject", "description", "category", "priority"]
    missing = [f for f in required if not data.get(f)]
    if missing:
        return fail(f"Missing required fields: {', '.join(missing)}", "VALIDATION_ERROR", 400)

    # D-04 fix: priority is a closed vocabulary, not free text.
    priority = str(data["priority"]).strip().lower()
    if priority not in ALLOWED_PRIORITIES:
        return fail(
            f"Invalid priority '{data['priority']}'. Allowed values: {', '.join(sorted(ALLOWED_PRIORITIES))}",
            "VALIDATION_ERROR",
            400,
        )

    complaint = Complaint(
        society_id=user.society_id,
        raised_by_user_id=user.id,
        subject=data["subject"],
        description=data["description"],
        category=data["category"],
        priority=priority,
        status="open",
    )
    db.session.add(complaint)
    db.session.flush()

    first_update = ComplaintUpdate(
        complaint_id=complaint.id,
        updated_by_user_id=user.id,
        status="open",
        comment="Complaint submitted",
        updated_at=datetime.now(UTC),
    )
    db.session.add(first_update)
    db.session.commit()
    return ok(complaint.to_dict(), "Complaint created", 201)


@complaints_bp.put("/<int:complaint_id>")
@jwt_required()
def update_complaint(complaint_id):
    user = current_user()
    complaint = db.session.get(Complaint, complaint_id)
    if not complaint:
        return fail("Complaint not found", "NOT_FOUND", 404)

    if user.role != ROLE_ADMIN and (complaint.raised_by_user_id != user.id or complaint.status != "open"):
        return fail("Forbidden", "FORBIDDEN", 403)

    data = request.get_json() or {}
    for field in ["subject", "description", "category", "priority"]:
        if field in data:
            setattr(complaint, field, data[field])

    db.session.commit()
    return ok(complaint.to_dict(), "Complaint updated")


@complaints_bp.put("/<int:complaint_id>/assign")
@roles_required(ROLE_ADMIN)
def assign_complaint(complaint_id):
    user = current_user()
    complaint = db.session.get(Complaint, complaint_id)
    if not complaint:
        return fail("Complaint not found", "NOT_FOUND", 404)

    data = request.get_json() or {}
    if not data.get("assigned_to_user_id"):
        return fail("assigned_to_user_id is required", "VALIDATION_ERROR", 400)

    if complaint.status == "closed":
        return fail("Closed complaints cannot be assigned", "INVALID_STATUS_TRANSITION", 409)

    assignee = db.session.get(User, int(data["assigned_to_user_id"]))
    if not assignee:
        return fail("Assigned user not found", "NOT_FOUND", 404)
    if assignee.society_id != complaint.society_id:
        return fail("Assigned user belongs to a different society", "VALIDATION_ERROR", 400)
    if assignee.role not in {ROLE_ADMIN, ROLE_SECURITY, ROLE_SERVICE_PROVIDER}:
        return fail("Assigned user role is not eligible", "VALIDATION_ERROR", 400)

    if complaint.assigned_to_user_id and int(complaint.assigned_to_user_id) == int(assignee.id):
        return fail("Complaint already assigned to this user", "DUPLICATE", 409)

    complaint.assigned_to_user_id = assignee.id
    complaint.status = "in_progress"
    update = ComplaintUpdate(
        complaint_id=complaint.id,
        updated_by_user_id=user.id,
        status=complaint.status,
        comment=data.get("comment", "Complaint assigned"),
        updated_at=datetime.now(UTC),
    )
    db.session.add(update)
    db.session.commit()
    return ok(complaint.to_dict(), "Complaint assigned")


@complaints_bp.put("/<int:complaint_id>/status")
@jwt_required()
def update_complaint_status(complaint_id):
    user = current_user()
    complaint = db.session.get(Complaint, complaint_id)
    if not complaint:
        return fail("Complaint not found", "NOT_FOUND", 404)

    if user.role != ROLE_ADMIN and user.id != complaint.assigned_to_user_id:
        return fail("Forbidden", "FORBIDDEN", 403)

    data = request.get_json() or {}
    status = data.get("status")
    comment = data.get("comment")

    if not status or not comment:
        return fail("status and comment are required", "VALIDATION_ERROR", 400)

    status = str(status).strip().lower()
    current_status = str(complaint.status or "").lower()
    if status not in ALLOWED_COMPLAINT_STATUSES:
        return fail("Invalid complaint status", "VALIDATION_ERROR", 400)
    if status == current_status:
        return fail("Complaint is already in this status", "DUPLICATE", 409)
    if current_status == "closed":
        return fail("Closed complaints cannot be updated", "INVALID_STATUS_TRANSITION", 409)
    if status == "in_progress" and not complaint.assigned_to_user_id:
        return fail("Assign complaint before moving to in_progress", "VALIDATION_ERROR", 400)

    complaint.status = status
    update = ComplaintUpdate(
        complaint_id=complaint.id,
        updated_by_user_id=user.id,
        status=status,
        comment=comment,
        updated_at=datetime.now(UTC),
    )
    db.session.add(update)
    db.session.commit()
    return ok(complaint.to_dict(), "Complaint status updated")


@complaints_bp.post("/<int:complaint_id>/updates")
@jwt_required()
def add_complaint_update(complaint_id):
    user = current_user()
    complaint = db.session.get(Complaint, complaint_id)
    if not complaint:
        return fail("Complaint not found", "NOT_FOUND", 404)

    if user.role != ROLE_ADMIN and user.id not in [complaint.raised_by_user_id, complaint.assigned_to_user_id]:
        return fail("Forbidden", "FORBIDDEN", 403)

    data = request.get_json() or {}
    if not data.get("comment"):
        return fail("comment is required", "VALIDATION_ERROR", 400)

    update = ComplaintUpdate(
        complaint_id=complaint.id,
        updated_by_user_id=user.id,
        status=complaint.status,
        comment=data["comment"],
        updated_at=datetime.now(UTC),
    )
    db.session.add(update)
    db.session.commit()
    return ok(update.to_dict(), "Update added", 201)


@complaints_bp.delete("/<int:complaint_id>")
@roles_required(ROLE_ADMIN)
def delete_complaint(complaint_id):
    complaint = db.session.get(Complaint, complaint_id)
    if not complaint:
        return fail("Complaint not found", "NOT_FOUND", 404)
    db.session.delete(complaint)
    db.session.commit()
    return ok(message="Complaint deleted")


