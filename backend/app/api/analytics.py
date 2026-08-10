from datetime import UTC, datetime

from flask import Blueprint, Response

from app.api.utils import current_user
from app.core.extensions import db
from app.core.responses import ok
from app.core.security import ROLE_ADMIN, ROLE_OWNER, ROLE_SECURITY, ROLE_SERVICE_PROVIDER, ROLE_TENANT, roles_required
from app.models import Complaint, EmergencyAlert, Event, IncidentReport, Notice, ServiceBooking, ServiceProvider, User, VisitorEntry


analytics_bp = Blueprint("analytics", __name__, url_prefix="/analytics")
reports_bp = Blueprint("reports", __name__, url_prefix="/reports")


def _build_monthly_report_payload():
    complaint_breakdown = {
        "open": Complaint.query.filter_by(status="open").count(),
        "in_progress": Complaint.query.filter_by(status="in_progress").count(),
        "resolved": Complaint.query.filter_by(status="resolved").count(),
        "closed": Complaint.query.filter_by(status="closed").count(),
    }
    booking_breakdown = {
        "requested": ServiceBooking.query.filter_by(booking_status="requested").count(),
        "accepted": ServiceBooking.query.filter_by(booking_status="accepted").count(),
        "declined": ServiceBooking.query.filter_by(booking_status="declined").count(),
        "cancelled": ServiceBooking.query.filter_by(booking_status="cancelled").count(),
        "completed": ServiceBooking.query.filter_by(booking_status="completed").count(),
    }
    return {
        "residents": {"total": User.query.filter(User.role.in_(["owner", "tenant"])).count()},
        "complaints": {"raised": Complaint.query.count(), "status_breakdown": complaint_breakdown},
        "events": {"scheduled": Event.query.count()},
        "notices": {"published": Notice.query.count()},
        "bookings": {"total": ServiceBooking.query.count(), "status_breakdown": booking_breakdown},
        "visitors": {"total": VisitorEntry.query.count()},
    }


@analytics_bp.get("/dashboard/admin")
@roles_required(ROLE_ADMIN)
def admin_dashboard():
    today = datetime.now(UTC).date()
    return ok(
        {
            "stats": {
                "total_residents": User.query.filter(User.role.in_(["owner", "tenant"])).count(),
                "pending_complaints": Complaint.query.filter(Complaint.status.in_(["open", "in_progress"])).count(),
                "todays_bookings": ServiceBooking.query.filter(db.func.date(ServiceBooking.created_at) == today).count(),
                "upcoming_events": Event.query.filter(Event.status == "scheduled", Event.event_date >= today).count(),
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
    actor = current_user()
    provider = ServiceProvider.query.filter_by(user_id=actor.id).first()
    today = datetime.now(UTC).date()
    month_start = today.replace(day=1)
    if not provider:
        return ok({"stats": {"todays_bookings": 0, "pending_requests": 0, "completed_this_month": 0, "rating_avg": 0}})

    bookings = ServiceBooking.query.filter_by(provider_id=provider.id)
    return ok(
        {
            "stats": {
                "todays_bookings": bookings.filter(db.func.date(ServiceBooking.created_at) == today).count(),
                "pending_requests": bookings.filter_by(booking_status="requested").count(),
                "completed_this_month": bookings.filter(
                    ServiceBooking.booking_status == "completed",
                    db.func.date(ServiceBooking.created_at) >= month_start,
                ).count(),
                "rating_avg": provider.rating_avg or 0,
            }
        }
    )


@analytics_bp.get("/dashboard/security")
@roles_required(ROLE_SECURITY)
def security_dashboard():
    today = datetime.now(UTC).date()
    recent_entries = VisitorEntry.query.order_by(VisitorEntry.entry_time.desc()).limit(5).all()
    return ok({
        "stats": {
            "visitors_today": VisitorEntry.query.filter(db.func.date(VisitorEntry.entry_time) == today).count(),
            "pending_approvals": VisitorEntry.query.filter_by(approval_status="pending").count(),
            "currently_inside": VisitorEntry.query.filter(VisitorEntry.exit_time.is_(None)).count(),
            "active_alerts": EmergencyAlert.query.filter(EmergencyAlert.status.in_(["active", "open"])).count(),
            "open_incidents": IncidentReport.query.filter(IncidentReport.status.in_(["open", "under_investigation"])).count(),
        },
        "recent_entries": [entry.to_dict() for entry in recent_entries],
    })


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
    return ok(_build_monthly_report_payload())


@reports_bp.get("/monthly/export.csv")
@roles_required(ROLE_ADMIN)
def export_monthly_report_csv():
    report_payload = _build_monthly_report_payload()
    rows = [
        ("metric", "value"),
        ("residents.total", report_payload.get("residents", {}).get("total", 0)),
        ("complaints.raised", report_payload.get("complaints", {}).get("raised", 0)),
        ("events.scheduled", report_payload.get("events", {}).get("scheduled", 0)),
        ("notices.published", report_payload.get("notices", {}).get("published", 0)),
        ("bookings.total", report_payload.get("bookings", {}).get("total", 0)),
        ("visitors.total", report_payload.get("visitors", {}).get("total", 0)),
    ]

    for status, value in report_payload.get("complaints", {}).get("status_breakdown", {}).items():
        rows.append((f"complaints.{status}", value))
    for status, value in report_payload.get("bookings", {}).get("status_breakdown", {}).items():
        rows.append((f"bookings.{status}", value))

    csv_content = "\n".join([f"{key},{value}" for key, value in rows])
    filename = f"monthly-report-{datetime.now(UTC).date().isoformat()}.csv"
    return Response(
        csv_content,
        mimetype="text/csv",
        headers={"Content-Disposition": f"attachment; filename={filename}"},
    )


@reports_bp.post("/export")
@roles_required(ROLE_ADMIN)
def export_report():
    return ok({"download_url": "/api/reports/monthly/export.csv", "expires_at": "2099-01-01T00:00:00Z"})
