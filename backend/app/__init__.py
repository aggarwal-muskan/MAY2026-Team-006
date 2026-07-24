import os

from dotenv import load_dotenv
from flask import Flask

from app.api import create_api_blueprint
from app.core.config import Config
from app.core.extensions import cors, db, jwt, migrate
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

    from app import models  # noqa: F401

    app.register_blueprint(create_api_blueprint())

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
        seed_initial_data()

    return app
