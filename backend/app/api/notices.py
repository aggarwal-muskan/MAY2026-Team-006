from datetime import UTC, datetime

from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from app.api.utils import current_user, parse_datetime
from app.core.extensions import db
from app.core.responses import fail, ok
from app.core.security import ROLE_ADMIN, roles_required
from app.models import Notice
from app.services.query_service import paginate_query


notices_bp = Blueprint("notices", __name__, url_prefix="/notices")


@notices_bp.get("")
@jwt_required()
def list_notices():
    query = Notice.query

    for field in ["notice_type", "priority", "society_id"]:
        value = request.args.get(field)
        if value:
            query = query.filter(getattr(Notice, field) == value)

    if request.args.get("active_only", "true").lower() == "true":
        now = datetime.now(UTC)
        query = query.filter(db.or_(Notice.expires_at.is_(None), Notice.expires_at > now))

    search = request.args.get("search")
    if search:
        query = query.filter(db.or_(Notice.title.ilike(f"%{search}%"), Notice.body.ilike(f"%{search}%")))

    items, pagination = paginate_query(query.order_by(Notice.publish_at.desc()))
    return ok({"items": [i.to_dict() for i in items], "pagination": pagination})


@notices_bp.get("/<int:notice_id>")
@jwt_required()
def get_notice(notice_id):
    notice = db.session.get(Notice, notice_id)
    if not notice:
        return fail("Notice not found", "NOT_FOUND", 404)
    return ok(notice.to_dict())


@notices_bp.post("")
@roles_required(ROLE_ADMIN)
def create_notice():
    actor = current_user()
    data = request.get_json() or {}

    required = ["title", "body", "notice_type", "priority"]
    missing = [f for f in required if not data.get(f)]
    if missing:
        return fail(f"Missing required fields: {', '.join(missing)}", "VALIDATION_ERROR", 400)

    notice = Notice(
        society_id=actor.society_id,
        created_by_user_id=actor.id,
        title=data["title"],
        body=data["body"],
        notice_type=data["notice_type"],
        priority=data.get("priority", "normal"),
        publish_at=parse_datetime(data.get("publish_at")) or datetime.now(UTC),
        expires_at=parse_datetime(data.get("expires_at")),
    )
    db.session.add(notice)
    db.session.commit()
    return ok(notice.to_dict(), "Notice created", 201)


@notices_bp.put("/<int:notice_id>")
@roles_required(ROLE_ADMIN)
def update_notice(notice_id):
    notice = db.session.get(Notice, notice_id)
    if not notice:
        return fail("Notice not found", "NOT_FOUND", 404)

    data = request.get_json() or {}
    for field in ["title", "body", "notice_type", "priority"]:
        if field in data:
            setattr(notice, field, data[field])

    if "publish_at" in data:
        notice.publish_at = parse_datetime(data["publish_at"])
    if "expires_at" in data:
        notice.expires_at = parse_datetime(data["expires_at"])

    db.session.commit()
    return ok(notice.to_dict(), "Notice updated")


@notices_bp.delete("/<int:notice_id>")
@roles_required(ROLE_ADMIN)
def delete_notice(notice_id):
    notice = db.session.get(Notice, notice_id)
    if not notice:
        return fail("Notice not found", "NOT_FOUND", 404)
    db.session.delete(notice)
    db.session.commit()
    return ok(message="Notice deleted")


@notices_bp.post("/<int:notice_id>/publish")
@roles_required(ROLE_ADMIN)
def publish_notice(notice_id):
    notice = db.session.get(Notice, notice_id)
    if not notice:
        return fail("Notice not found", "NOT_FOUND", 404)

    notice.publish_at = datetime.now(UTC)
    db.session.commit()
    return ok(notice.to_dict(), "Notice published")


