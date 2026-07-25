from datetime import datetime

from sqlalchemy import func

from app.core.extensions import db


class TimestampMixin:
    created_at = db.Column(db.DateTime, nullable=False, default=func.now())


class UpdateTimestampMixin:
    updated_at = db.Column(db.DateTime, nullable=False, default=func.now(), onupdate=func.now())


class SerializerMixin:
    def to_dict(self, include=None, exclude=None):
        include = include or []
        exclude = set(exclude or [])

        data = {}
        for column in self.__table__.columns:
            key = column.name
            if key in exclude:
                continue
            value = getattr(self, key)
            if isinstance(value, datetime):
                value = value.isoformat()
            data[key] = value

        for key in include:
            data[key] = getattr(self, key)
        return data
