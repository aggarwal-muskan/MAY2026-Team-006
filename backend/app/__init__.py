import os

from dotenv import load_dotenv

_BACKEND_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(_BACKEND_DIR, ".env"))
load_dotenv()

from flask import Flask
from sqlalchemy.exc import IntegrityError

from app.api import create_api_blueprint
from app.core.config import Config
from app.core.error_handlers import register_error_handlers
from app.core.extensions import cors, db, jwt, migrate
from app.core.responses import fail
from app.services.seed_service import seed_initial_data


def create_app(config_class=Config):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_class)
    # Re-read AI settings in case env was updated after class import.
    app.config["GEMINI_API_KEY"] = os.getenv("GEMINI_API_KEY", app.config.get("GEMINI_API_KEY", ""))
    app.config["GEMINI_MODEL"] = os.getenv("GEMINI_MODEL", app.config.get("GEMINI_MODEL", "gemini-flash-latest"))

    os.makedirs(app.instance_path, exist_ok=True)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    # Re-read CORS in case .env changed after Config import.
    cors_origins = [
        origin.strip()
        for origin in os.getenv(
            "CORS_ORIGINS",
            "http://localhost:5173,http://127.0.0.1:5173,http://localhost:5174,http://127.0.0.1:5174",
        ).split(",")
        if origin.strip()
    ]
    app.config["CORS_ORIGINS"] = cors_origins
    cors.init_app(
        app,
        resources={r"/api/*": {"origins": cors_origins}},
        supports_credentials=False,
        allow_headers=["Content-Type", "Authorization"],
        methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
    )

    @jwt.unauthorized_loader
    def on_unauthorized(reason):
        return fail(reason or "Missing authorization token", "UNAUTHORIZED", 401)

    @jwt.invalid_token_loader
    def on_invalid_token(reason):
        return fail(reason or "Invalid authorization token", "UNAUTHORIZED", 401)

    @jwt.expired_token_loader
    def on_expired_token(_jwt_header, _jwt_payload):
        return fail("Token has expired", "TOKEN_EXPIRED", 401)

    @jwt.revoked_token_loader
    def on_revoked_token(_jwt_header, _jwt_payload):
        return fail("Token has been revoked", "TOKEN_REVOKED", 401)

    @jwt.needs_fresh_token_loader
    def on_needs_fresh_token(_jwt_header, _jwt_payload):
        return fail("Fresh token required", "FRESH_TOKEN_REQUIRED", 401)

    from app import models  # noqa: F401

    app.register_blueprint(create_api_blueprint())
    register_error_handlers(app)

    @app.get("/health")
    def health_check():
        return {"status": "ok", "service": "socioneed-backend"}

    @app.get("/api")
    def api_index():
        return {
            "status": "ok",
            "message": "SocioNeed API is running",
            "base": "/api",
            "groups": [
                "/api/auth",
                "/api/users",
                "/api/societies",
                "/api/units",
                "/api/occupancies",
                "/api/notices",
                "/api/events",
                "/api/complaints",
                "/api/service-categories",
                "/api/providers",
                "/api/slots",
                "/api/bookings",
                "/api/reviews",
                "/api/visitors",
                "/api/analytics",
                "/api/reports",
                "/api/ai",
            ],
        }

    @app.get("/favicon.ico")
    def favicon():
        return ("", 204)

    @app.cli.command("seed")
    def seed_command():
        seed_initial_data()
        print("Seed data created.")

    with app.app_context():
        db.create_all()
        _ensure_schema_upgrades()
        try:
            seed_initial_data()
        except IntegrityError:
            db.session.rollback()

    return app


def _ensure_schema_upgrades():
    """Idempotent, migration-free column additions for existing SQLite databases.

    create_all() only creates missing tables, not new columns on existing tables,
    so we add newly introduced nullable columns here if they are absent.
    """
    from sqlalchemy import inspect, text

    try:
        inspector = inspect(db.engine)
        notice_columns = {col["name"] for col in inspector.get_columns("notices")}
        if "translations" not in notice_columns:
            db.session.execute(text("ALTER TABLE notices ADD COLUMN translations TEXT"))
            db.session.commit()
    except Exception:  # noqa: BLE001 - never block startup on a best-effort upgrade
        db.session.rollback()
