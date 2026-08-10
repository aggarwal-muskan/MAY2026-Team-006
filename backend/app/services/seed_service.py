from datetime import UTC, datetime, timedelta

from sqlalchemy.exc import IntegrityError

from app.core.extensions import db
from app.models import AppSetting, Complaint, ComplaintUpdate, EmergencyAlert, Event, FamilyMember, IncidentReport, MaintenanceBill, Notice, PatrolLog, ServiceBooking, ServiceCategory, ServiceProvider, Society, SystemLog, User, VisitorEntry
from app.services.auth_service import hash_password


DEFAULT_USERS = [
    {
        "role": "admin",
        "full_name": "Admin User",
        "email": "admin@socioneed.com",
        "phone": "9000000001",
    },
    {
        "role": "owner",
        "full_name": "Resident User",
        "email": "resident@socioneed.com",
        "phone": "9000000002",
    },
    {
        "role": "service_provider",
        "full_name": "Provider User",
        "email": "provider@socioneed.com",
        "phone": "9000000003",
    },
    {
        "role": "service_provider",
        "full_name": "Pooja House Maid",
        "email": "provider.housemaid@socioneed.com",
        "phone": "9000000101",
    },
    {
        "role": "service_provider",
        "full_name": "Ravi Plumber",
        "email": "provider.plumber@socioneed.com",
        "phone": "9000000102",
    },
    {
        "role": "service_provider",
        "full_name": "Sita Electrician",
        "email": "provider.electrician@socioneed.com",
        "phone": "9000000103",
    },
    {
        "role": "service_provider",
        "full_name": "Sunita Laundry",
        "email": "provider.laundry@socioneed.com",
        "phone": "9000000104",
    },
    {
        "role": "service_provider",
        "full_name": "Kumar Car Wash",
        "email": "provider.carwash@socioneed.com",
        "phone": "9000000105",
    },
    {
        "role": "service_provider",
        "full_name": "Ramesh Gardener",
        "email": "provider.gardener@socioneed.com",
        "phone": "9000000106",
    },
    {
        "role": "service_provider",
        "full_name": "Ajay Tailor",
        "email": "provider.tailor@socioneed.com",
        "phone": "9000000107",
    },
    {
        "role": "service_provider",
        "full_name": "Lakshmi Cook",
        "email": "provider.cook@socioneed.com",
        "phone": "9000000108",
    },
    {
        "role": "security",
        "full_name": "Security User",
        "email": "security@socioneed.com",
        "phone": "9000000004",
    },
]

DEFAULT_CATEGORIES = [
    ("House Maid", "Professional house cleaning and domestic help services"),
    ("Plumber", "Plumbing, pipe fitting, and drainage solutions"),
    ("Electrician", "Electrical wiring, repairs, and appliance installation"),
    ("Laundry", "Wash, iron, dry cleaning, and delivery"),
    ("Car Wash", "Exterior and interior car cleaning and detailing"),
    ("Gardener", "Garden maintenance, lawn mowing, and landscaping"),
    ("Tailor", "Tailoring, alterations, and custom stitching"),
    ("Cook", "Home cooking, party catering, and tiffin services"),
]

DEFAULT_PROVIDER_EMAIL_CATEGORY = {
    "provider.housemaid@socioneed.com": "House Maid",
    "provider.plumber@socioneed.com": "Plumber",
    "provider.electrician@socioneed.com": "Electrician",
    "provider.laundry@socioneed.com": "Laundry",
    "provider.carwash@socioneed.com": "Car Wash",
    "provider.gardener@socioneed.com": "Gardener",
    "provider.tailor@socioneed.com": "Tailor",
    "provider.cook@socioneed.com": "Cook",
}


def _ensure_provider_profiles_for_provider_users():
    provider_users = User.query.filter_by(role="service_provider").order_by(User.id.asc()).all()
    categories = ServiceCategory.query.order_by(ServiceCategory.id.asc()).all()
    if not provider_users or not categories:
        return

    categories_by_name = {category.name.lower(): category for category in categories}

    for index, provider_user in enumerate(provider_users):
        existing_profile = ServiceProvider.query.filter_by(user_id=provider_user.id).first()
        desired_category = None

        mapped_category_name = DEFAULT_PROVIDER_EMAIL_CATEGORY.get(provider_user.email, "")
        if mapped_category_name:
            desired_category = categories_by_name.get(mapped_category_name.lower())
        if not desired_category:
            desired_category = categories[index % len(categories)]

        if existing_profile:
            if existing_profile.verification_status != "approved":
                existing_profile.verification_status = "approved"
            if desired_category and existing_profile.category_id != desired_category.id:
                existing_profile.category_id = desired_category.id
            continue

        profile = ServiceProvider(
            user_id=provider_user.id,
            category_id=desired_category.id,
            business_name=f"{provider_user.full_name} Services",
            service_description="Community verified service provider",
            verification_status="approved",
            rating_avg=4.5,
        )
        try:
            db.session.add(profile)
            db.session.flush()
        except IntegrityError:
            db.session.rollback()
            # Another process/request inserted this profile first.
            existing_profile = ServiceProvider.query.filter_by(user_id=provider_user.id).first()
            if existing_profile and desired_category and existing_profile.category_id != desired_category.id:
                existing_profile.category_id = desired_category.id
            if existing_profile and existing_profile.verification_status != "approved":
                existing_profile.verification_status = "approved"


def _seed_demo_transactions(society):
    admin_user = User.query.filter_by(email="admin@socioneed.com").first()
    resident_user = User.query.filter_by(email="resident@socioneed.com").first()
    provider_user = User.query.filter_by(email="provider@socioneed.com").first()
    security_user = User.query.filter_by(email="security@socioneed.com").first()

    if not admin_user or not resident_user or not provider_user or not security_user:
        return

    _ensure_provider_profiles_for_provider_users()

    category = ServiceCategory.query.order_by(ServiceCategory.id.asc()).first()
    provider_profile = ServiceProvider.query.filter_by(user_id=provider_user.id).first()
    if not provider_profile and category:
        provider_profile = ServiceProvider(
            user_id=provider_user.id,
            category_id=category.id,
            business_name="CityFix Services",
            service_description="General home maintenance and repairs",
            verification_status="approved",
            rating_avg=4.6,
        )
        db.session.add(provider_profile)
        db.session.flush()

    now = datetime.now(UTC)

    if Notice.query.count() == 0:
        notices = [
            Notice(
                society_id=society.id,
                created_by_user_id=admin_user.id,
                title="Water Tank Cleaning",
                body="Water tank cleaning is scheduled this weekend.",
                notice_type="maintenance",
                priority="high",
                publish_at=now - timedelta(days=2),
            ),
            Notice(
                society_id=society.id,
                created_by_user_id=admin_user.id,
                title="Community Meeting",
                body="Monthly community meeting on Sunday at 6 PM.",
                notice_type="event",
                priority="normal",
                publish_at=now - timedelta(days=1),
            ),
            Notice(
                society_id=society.id,
                created_by_user_id=admin_user.id,
                title="Security Advisory",
                body="Please ensure visitors are pre-approved at gate entry.",
                notice_type="security",
                priority="urgent",
                publish_at=now,
            ),
        ]
        db.session.add_all(notices)

    if Event.query.count() == 0:
        events = [
            Event(
                society_id=society.id,
                created_by_user_id=admin_user.id,
                title="Yoga Session",
                description="Morning wellness session in clubhouse.",
                event_date=(now + timedelta(days=2)).date(),
                start_time="07:00",
                end_time="08:00",
                venue="Clubhouse",
                status="scheduled",
            ),
            Event(
                society_id=society.id,
                created_by_user_id=admin_user.id,
                title="Kids Painting Workshop",
                description="Weekend painting workshop for children.",
                event_date=(now + timedelta(days=5)).date(),
                start_time="16:00",
                end_time="18:00",
                venue="Community Hall",
                status="scheduled",
            ),
            Event(
                society_id=society.id,
                created_by_user_id=admin_user.id,
                title="Fire Safety Drill",
                description="Safety drill with security team guidance.",
                event_date=(now + timedelta(days=8)).date(),
                start_time="10:00",
                end_time="11:00",
                venue="Main Courtyard",
                status="scheduled",
            ),
        ]
        db.session.add_all(events)

    if Complaint.query.count() == 0:
        complaints = [
            {
                "subject": "Lift maintenance required",
                "description": "Lift in Block C has intermittent stoppage.",
                "category": "Maintenance",
                "priority": "high",
                "status": "open",
                "assigned": None,
            },
            {
                "subject": "Water leakage near basement",
                "description": "Leakage observed near basement entry ramp.",
                "category": "Plumbing",
                "priority": "medium",
                "status": "in_progress",
                "assigned": security_user.id,
            },
            {
                "subject": "CCTV camera blur",
                "description": "CCTV feed near gate 2 is blurry at night.",
                "category": "Security",
                "priority": "high",
                "status": "resolved",
                "assigned": security_user.id,
            },
        ]

        for payload in complaints:
            complaint = Complaint(
                society_id=society.id,
                raised_by_user_id=resident_user.id,
                assigned_to_user_id=payload["assigned"],
                subject=payload["subject"],
                description=payload["description"],
                category=payload["category"],
                priority=payload["priority"],
                status=payload["status"],
            )
            db.session.add(complaint)
            db.session.flush()
            db.session.add(
                ComplaintUpdate(
                    complaint_id=complaint.id,
                    updated_by_user_id=admin_user.id,
                    status=complaint.status,
                    comment="Seeded demo complaint state",
                    updated_at=now,
                )
            )

    if ServiceBooking.query.count() == 0 and provider_profile:
        bookings = [
            ServiceBooking(
                resident_user_id=resident_user.id,
                provider_id=provider_profile.id,
                booking_status="requested",
                request_notes="Kitchen sink pipe check",
            ),
            ServiceBooking(
                resident_user_id=resident_user.id,
                provider_id=provider_profile.id,
                booking_status="accepted",
                request_notes="Bathroom fitting replacement",
            ),
            ServiceBooking(
                resident_user_id=resident_user.id,
                provider_id=provider_profile.id,
                booking_status="completed",
                request_notes="Balcony drain cleanup",
            ),
        ]
        db.session.add_all(bookings)

    if VisitorEntry.query.count() == 0:
        visitors = [
            VisitorEntry(
                society_id=society.id,
                recorded_by_user_id=security_user.id,
                resident_user_id=resident_user.id,
                visitor_name="Ramesh Courier",
                purpose="Package Delivery",
                flat_number="A-101",
                vehicle_number="MH12AB1234",
                vehicle_type="Van",
                contact_number="9876500001",
                approval_status="approved",
                approved_by_user_id=security_user.id,
                approved_at=now - timedelta(hours=3),
                entry_time=now - timedelta(hours=3),
                exit_time=now - timedelta(hours=2, minutes=45),
                remarks="Amazon package delivery",
            ),
            VisitorEntry(
                society_id=society.id,
                recorded_by_user_id=security_user.id,
                resident_user_id=resident_user.id,
                visitor_name="Seema Agarwal",
                purpose="Family Visit",
                flat_number="A-101",
                vehicle_number="DL02AB8901",
                vehicle_type="Car",
                contact_number="9876500002",
                approval_status="pending",
                entry_time=now - timedelta(minutes=35),
                remarks="Waiting for resident approval",
            ),
            VisitorEntry(
                society_id=society.id,
                recorded_by_user_id=security_user.id,
                visitor_name="Cable TV Technician",
                purpose="Repair Visit",
                flat_number="B-201",
                vehicle_type="Bike",
                approval_status="approved",
                approved_by_user_id=security_user.id,
                approved_at=now - timedelta(hours=1),
                entry_time=now - timedelta(hours=1),
                remarks="Network repair",
            ),
        ]
        db.session.add_all(visitors)

    if PatrolLog.query.count() == 0:
        db.session.add_all([
            PatrolLog(society_id=society.id, recorded_by_user_id=security_user.id, checkpoint="Gate A", note="All clear", patrol_time=now - timedelta(hours=4), status="logged"),
            PatrolLog(society_id=society.id, recorded_by_user_id=security_user.id, checkpoint="Basement", note="Vehicle area checked", patrol_time=now - timedelta(hours=2), status="logged"),
        ])

    if EmergencyAlert.query.count() == 0:
        db.session.add_all([
            EmergencyAlert(society_id=society.id, created_by_user_id=security_user.id, title="Fire Alarm Test", description="Routine fire alarm system check.", priority="low", status="completed", alert_time=now - timedelta(days=1)),
            EmergencyAlert(society_id=society.id, created_by_user_id=security_user.id, title="Power Outage", description="Generator backup active during electrical maintenance.", priority="high", status="active", alert_time=now - timedelta(hours=5)),
        ])

    if IncidentReport.query.count() == 0:
        db.session.add_all([
            IncidentReport(society_id=society.id, reported_by_user_id=security_user.id, incident_type="Trespassing", location="Back Gate", description="Unauthorized person attempted entry.", severity="high", status="under_investigation", occurred_at=now - timedelta(hours=6)),
            IncidentReport(society_id=society.id, reported_by_user_id=security_user.id, incident_type="Vandalism", location="Garden Area", description="Bench damaged near children play area.", severity="medium", status="resolved", occurred_at=now - timedelta(days=2)),
        ])

    if FamilyMember.query.count() == 0:
        db.session.add_all([
            FamilyMember(resident_user_id=resident_user.id, full_name="Resident User", relation="Self", phone=resident_user.phone, age=35, is_primary_contact=True),
            FamilyMember(resident_user_id=resident_user.id, full_name="Rohan Resident", relation="Spouse", phone="9000001001", age=37, is_primary_contact=False),
        ])

    if MaintenanceBill.query.count() == 0:
        db.session.add_all([
            MaintenanceBill(resident_user_id=resident_user.id, month_label="June 2026", amount=3450, due_date=(now + timedelta(days=7)).date(), status="unpaid", notes="Includes maintenance, water, electricity"),
            MaintenanceBill(resident_user_id=resident_user.id, month_label="May 2026", amount=3250, due_date=(now - timedelta(days=20)).date(), status="paid", paid_date=(now - timedelta(days=18)).date(), notes="Paid online"),
        ])

    if SystemLog.query.count() == 0:
        db.session.add_all([
            SystemLog(user_id=admin_user.id, action="User Login", details="Admin logged in"),
            SystemLog(user_id=security_user.id, action="Visitor Entry", details="Seeded visitor entry created"),
            SystemLog(user_id=resident_user.id, action="Complaint Created", details="Seeded complaint record"),
        ])

    if AppSetting.query.count() == 0:
        db.session.add_all([
            AppSetting(setting_key="maintenance_reminders", setting_value="true"),
            AppSetting(setting_key="email_alerts", setting_value="true"),
            AppSetting(setting_key="auto_approvals", setting_value="false"),
        ])

    db.session.commit()


def seed_initial_data():
    society = Society.query.first()
    if not society:
        society = Society(
            name="Green Valley Society",
            address="123 Main Road",
            city="Mumbai",
            pincode="400001",
            contact_email="admin@greenvalley.com",
            contact_phone="9988776655",
        )
        db.session.add(society)
        db.session.flush()

    existing_emails = {u.email for u in User.query.all()}
    for user_payload in DEFAULT_USERS:
        if user_payload["email"] in existing_emails:
            continue
        user = User(
            society_id=society.id,
            role=user_payload["role"],
            full_name=user_payload["full_name"],
            email=user_payload["email"],
            phone=user_payload["phone"],
            password_hash=hash_password("123456"),
            status="active",
            created_at=datetime.now(UTC),
        )
        db.session.add(user)

    existing_categories = {c.name for c in ServiceCategory.query.all()}
    for name, description in DEFAULT_CATEGORIES:
        if name in existing_categories:
            continue
        db.session.add(ServiceCategory(name=name, description=description, created_at=datetime.now(UTC)))

    db.session.commit()
    _seed_demo_transactions(society)

