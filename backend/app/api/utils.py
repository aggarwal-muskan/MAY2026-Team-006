from datetime import date, datetime

from flask_jwt_extended import get_jwt_identity

from app.core.extensions import db
from app.models import User


def current_user():
    identity = get_jwt_identity()
    if not identity:
        return None
    return db.session.get(User, identity)


def parse_date(value):
    if value is None:
        return None
    if isinstance(value, date):
        return value
    return datetime.fromisoformat(value).date()


def parse_datetime(value):
    if value is None:
        return None
    if isinstance(value, datetime):
        return value
    return datetime.fromisoformat(value)

