import os

from dotenv import load_dotenv
from flask import Flask
from sqlalchemy.exc import IntegrityError

from app.api import create_api_blueprint
from app.core.config import Config
from app.core.error_handlers import register_error_handlers
from app.core.extensions import cors, db, jwt, migrate
from app.core.responses import fail
from app.services.seed_service import seed_initial_data


load_dotenv()


def create_app(config_class=Config):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_class)

    os.makedirs(app.instance_path, exist_ok=True)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    cors.init_app(app, resources={r"/api/*": {"origins": app.config["CORS_ORIGINS"]}})

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
        try:
            seed_initial_data()
        except IntegrityError:
            db.session.rollback()

    return app
