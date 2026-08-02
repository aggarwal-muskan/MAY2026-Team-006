from flask import request
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from werkzeug.exceptions import HTTPException

from app.core.extensions import db
from app.core.responses import fail


class ApiError(Exception):
    def __init__(self, message="Request failed", code="BAD_REQUEST", status=400):
        super().__init__(message)
        self.message = message
        self.code = code
        self.status = status


class ValidationError(ApiError):
    def __init__(self, message="Invalid input data"):
        super().__init__(message=message, code="VALIDATION_ERROR", status=400)


def _is_api_request():
    path = request.path or ""
    return path.startswith("/api")


def register_error_handlers(app):
    @app.errorhandler(ApiError)
    def handle_api_error(error):
        return fail(error.message, error.code, error.status)

    @app.errorhandler(IntegrityError)
    def handle_integrity_error(_error):
        db.session.rollback()
        return fail("Database constraint violation", "CONFLICT", 409)

    @app.errorhandler(SQLAlchemyError)
    def handle_sqlalchemy_error(_error):
        db.session.rollback()
        return fail("Database operation failed", "DB_ERROR", 500)

    @app.errorhandler(ValueError)
    @app.errorhandler(TypeError)
    def handle_value_or_type_error(error):
        if _is_api_request():
            return fail(str(error) or "Invalid input data", "VALIDATION_ERROR", 400)
        raise error

    @app.errorhandler(HTTPException)
    def handle_http_exception(error):
        if _is_api_request():
            code = str(error.name or "HTTP_ERROR").upper().replace(" ", "_")
            return fail(error.description or "Request failed", code, error.code or 400)
        return error

    @app.errorhandler(Exception)
    def handle_unexpected_error(_error):
        db.session.rollback()
        if _is_api_request():
            return fail("Unexpected server error", "INTERNAL_SERVER_ERROR", 500)
        raise _error