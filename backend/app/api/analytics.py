from flask import Blueprint

from app.core.responses import ok
from app.core.security import ROLE_ADMIN, ROLE_OWNER, ROLE_SECURITY, ROLE_SERVICE_PROVIDER, ROLE_TENANT, roles_required
from app.models import Complaint, Event, Notice, ServiceBooking, User, VisitorEntry


analytics_bp = Blueprint("analytics", __name__, url_prefix="/analytics")
reports_bp = Blueprint("reports", __name__, url_prefix="/reports")


@analytics_bp.get("/dashboard/admin")
@roles_required(ROLE_ADMIN)
def admin_dashboard():
    return ok(
        {
            "stats": {
                "total_residents": User.query.filter(User.role.in_(["owner", "tenant"])).count(),
                "pending_complaints": Complaint.query.filter(Complaint.status.in_(["open", "in_progress"])).count(),
                "todays_bookings": ServiceBooking.query.count(),
                "upcoming_events": Event.query.filter_by(status="scheduled").count(),
            }
        }
    )


@analytics_bp.get("/dashboard/resident")
@roles_required(ROLE_OWNER, ROLE_TENANT)
def resident_dashboard():
    return ok({"stats": {"pending_complaints": 0, "active_bookings": 0, "unread_notices": 0, "upcoming_events": 0}})


@analytics_bp.get("/dashboard/provider")
@roles_required(ROLE_SERVICE_PROVIDER)
def provider_dashboard():
    return ok({"stats": {"todays_bookings": 0, "pending_requests": 0, "completed_this_month": 0, "rating_avg": 0}})


@analytics_bp.get("/dashboard/security")
@roles_required(ROLE_SECURITY)
def security_dashboard():
    return ok({"stats": {"visitors_today": VisitorEntry.query.count(), "pending_approvals": 0, "currently_inside": VisitorEntry.query.filter_by(exit_time=None).count()}})


@analytics_bp.get("/complaints")
@roles_required(ROLE_ADMIN)
def complaints_analytics():
    open_count = Complaint.query.filter_by(status="open").count()
    in_progress = Complaint.query.filter_by(status="in_progress").count()
    resolved = Complaint.query.filter_by(status="resolved").count()
    closed = Complaint.query.filter_by(status="closed").count()
    return ok({"status_breakdown": {"open": open_count, "in_progress": in_progress, "resolved": resolved, "closed": closed}})


@analytics_bp.get("/bookings")
@roles_required(ROLE_ADMIN)
def bookings_analytics():
    statuses = ["requested", "accepted", "declined", "cancelled", "completed"]
    return ok({"status_breakdown": {status: ServiceBooking.query.filter_by(booking_status=status).count() for status in statuses}})


@analytics_bp.get("/revenue")
@roles_required(ROLE_ADMIN)
def revenue_analytics():
    completed = ServiceBooking.query.filter_by(booking_status="completed").count()
    return ok({"estimated_revenue": completed * 500})


@reports_bp.get("/monthly")
@roles_required(ROLE_ADMIN)
def monthly_report():
    return ok(
        {
            "residents": {"total": User.query.filter(User.role.in_(["owner", "tenant"])).count()},
            "complaints": {"raised": Complaint.query.count()},
            "events": {"scheduled": Event.query.count()},
            "notices": {"published": Notice.query.count()},
            "bookings": {"total": ServiceBooking.query.count()},
            "visitors": {"total": VisitorEntry.query.count()},
        }
    )


@reports_bp.post("/export")
@roles_required(ROLE_ADMIN)
def export_report():
    return ok({"download_url": "/api/reports/download/mock-report.csv", "expires_at": "2099-01-01T00:00:00Z"})
