from flask import Blueprint

from app.api.analytics import analytics_bp, reports_bp
from app.api.auth import auth_bp
from app.api.bookings import bookings_bp
from app.api.complaints import complaints_bp
from app.api.emerging_issues import emerging_issues_bp
from app.api.events import events_bp
from app.api.notices import notices_bp
from app.api.providers import providers_bp, reviews_bp, service_categories_bp, slots_bp
from app.api.societies import societies_bp
from app.api.units import occupancies_bp, units_bp
from app.api.users import users_bp
from app.api.visitors import visitors_bp


def create_api_blueprint():
    api = Blueprint("api", __name__, url_prefix="/api")

    api.register_blueprint(auth_bp)
    api.register_blueprint(users_bp)
    api.register_blueprint(societies_bp)
    api.register_blueprint(units_bp)
    api.register_blueprint(occupancies_bp)
    api.register_blueprint(notices_bp)
    api.register_blueprint(events_bp)
    api.register_blueprint(complaints_bp)
    api.register_blueprint(emerging_issues_bp)
    api.register_blueprint(service_categories_bp)
    api.register_blueprint(providers_bp)
    api.register_blueprint(slots_bp)
    api.register_blueprint(bookings_bp)
    api.register_blueprint(reviews_bp)
    api.register_blueprint(visitors_bp)
    api.register_blueprint(analytics_bp)
    api.register_blueprint(reports_bp)

    return api
