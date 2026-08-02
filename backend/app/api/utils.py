from datetime import date, datetime

from flask_jwt_extended import get_jwt_identity

from app.core.error_handlers import ValidationError
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
    try:
        return datetime.fromisoformat(value).date()
    except (TypeError, ValueError) as error:
        raise ValidationError(f"Invalid date format: {value}") from error


def parse_datetime(value):
    if value is None:
        return None
    if isinstance(value, datetime):
        return value
    try:
        return datetime.fromisoformat(value)
    except (TypeError, ValueError) as error:
        raise ValidationError(f"Invalid datetime format: {value}") from error

