from app.core.extensions import db
from app.models.base import SerializerMixin, TimestampMixin, UpdateTimestampMixin


class Society(db.Model, TimestampMixin, SerializerMixin):
    __tablename__ = "societies"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    address = db.Column(db.String(500), nullable=False)
    city = db.Column(db.String(120), nullable=False)
    pincode = db.Column(db.String(20), nullable=False)
    contact_email = db.Column(db.String(255))
    contact_phone = db.Column(db.String(30))


class User(db.Model, TimestampMixin, SerializerMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    society_id = db.Column(db.Integer, db.ForeignKey("societies.id", ondelete="CASCADE"), nullable=False)
    role = db.Column(db.String(40), nullable=False)
    full_name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    phone = db.Column(db.String(30), unique=True)
    password_hash = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(20), nullable=False, default="active")

    society = db.relationship("Society", backref=db.backref("users", lazy=True))


class Unit(db.Model, TimestampMixin, SerializerMixin):
    __tablename__ = "units"

    id = db.Column(db.Integer, primary_key=True)
    society_id = db.Column(db.Integer, db.ForeignKey("societies.id", ondelete="CASCADE"), nullable=False)
    block_name = db.Column(db.String(50))
    unit_number = db.Column(db.String(20), nullable=False)
    floor = db.Column(db.String(20))
    unit_type = db.Column(db.String(40))
    status = db.Column(db.String(20), nullable=False, default="active")

    __table_args__ = (db.UniqueConstraint("society_id", "block_name", "unit_number", name="uq_unit_society"),)


class ResidentOccupancy(db.Model, SerializerMixin):
    __tablename__ = "resident_occupancies"

    id = db.Column(db.Integer, primary_key=True)
    unit_id = db.Column(db.Integer, db.ForeignKey("units.id", ondelete="CASCADE"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    occupancy_type = db.Column(db.String(20), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date)
    is_primary = db.Column(db.Boolean, nullable=False, default=True)

    unit = db.relationship("Unit", backref=db.backref("occupancies", lazy=True, cascade="all, delete-orphan"))
    user = db.relationship("User", backref=db.backref("occupancies", lazy=True, cascade="all, delete-orphan"))


class ServiceCategory(db.Model, TimestampMixin, SerializerMixin):
    __tablename__ = "service_categories"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False, unique=True)
    description = db.Column(db.Text)


class ServiceProvider(db.Model, TimestampMixin, SerializerMixin):
    __tablename__ = "service_providers"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False, unique=True)
    category_id = db.Column(db.Integer, db.ForeignKey("service_categories.id", ondelete="RESTRICT"), nullable=False)
    business_name = db.Column(db.String(200), nullable=False)
    service_description = db.Column(db.Text)
    verification_status = db.Column(db.String(20), nullable=False, default="pending")
    rating_avg = db.Column(db.Float, nullable=False, default=0)

    user = db.relationship("User", backref=db.backref("provider_profile", uselist=False))
    category = db.relationship("ServiceCategory", backref=db.backref("providers", lazy=True))


class ProviderSlot(db.Model, TimestampMixin, SerializerMixin):
    __tablename__ = "provider_slots"

    id = db.Column(db.Integer, primary_key=True)
    provider_id = db.Column(db.Integer, db.ForeignKey("service_providers.id", ondelete="CASCADE"), nullable=False)
    slot_start = db.Column(db.DateTime, nullable=False)
    slot_end = db.Column(db.DateTime, nullable=False)
    is_available = db.Column(db.Boolean, nullable=False, default=True)

    __table_args__ = (db.UniqueConstraint("provider_id", "slot_start", "slot_end", name="uq_provider_slot"),)


class ServiceBooking(db.Model, TimestampMixin, UpdateTimestampMixin, SerializerMixin):
    __tablename__ = "service_bookings"

    id = db.Column(db.Integer, primary_key=True)
    resident_user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    provider_id = db.Column(db.Integer, db.ForeignKey("service_providers.id", ondelete="CASCADE"), nullable=False)
    slot_id = db.Column(db.Integer, db.ForeignKey("provider_slots.id", ondelete="SET NULL"))
    booking_status = db.Column(db.String(20), nullable=False, default="requested")
    request_notes = db.Column(db.Text)

    resident = db.relationship("User", foreign_keys=[resident_user_id])
    provider = db.relationship("ServiceProvider", backref=db.backref("bookings", lazy=True))
    slot = db.relationship("ProviderSlot", backref=db.backref("bookings", lazy=True))


class Notice(db.Model, TimestampMixin, SerializerMixin):
    __tablename__ = "notices"

    id = db.Column(db.Integer, primary_key=True)
    society_id = db.Column(db.Integer, db.ForeignKey("societies.id", ondelete="CASCADE"), nullable=False)
    created_by_user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    body = db.Column(db.Text, nullable=False)
    notice_type = db.Column(db.String(30), nullable=False)
    priority = db.Column(db.String(20), nullable=False, default="normal")
    publish_at = db.Column(db.DateTime, nullable=False)
    expires_at = db.Column(db.DateTime)


class Event(db.Model, TimestampMixin, SerializerMixin):
    __tablename__ = "events"

    id = db.Column(db.Integer, primary_key=True)
    society_id = db.Column(db.Integer, db.ForeignKey("societies.id", ondelete="CASCADE"), nullable=False)
    created_by_user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    event_date = db.Column(db.Date, nullable=False)
    start_time = db.Column(db.String(20))
    end_time = db.Column(db.String(20))
    venue = db.Column(db.String(255))
    status = db.Column(db.String(20), nullable=False, default="scheduled")


class EventRegistration(db.Model, TimestampMixin, SerializerMixin):
    __tablename__ = "event_registrations"

    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey("events.id", ondelete="CASCADE"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    registered_at = db.Column(db.DateTime, nullable=False)

    __table_args__ = (db.UniqueConstraint("event_id", "user_id", name="uq_event_user"),)


class Complaint(db.Model, TimestampMixin, UpdateTimestampMixin, SerializerMixin):
    __tablename__ = "complaints"

    id = db.Column(db.Integer, primary_key=True)
    society_id = db.Column(db.Integer, db.ForeignKey("societies.id", ondelete="CASCADE"), nullable=False)
    raised_by_user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    assigned_to_user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="SET NULL"))
    subject = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    priority = db.Column(db.String(20), nullable=False, default="medium")
    status = db.Column(db.String(20), nullable=False, default="open")


class ComplaintUpdate(db.Model, SerializerMixin):
    __tablename__ = "complaint_updates"

    id = db.Column(db.Integer, primary_key=True)
    complaint_id = db.Column(db.Integer, db.ForeignKey("complaints.id", ondelete="CASCADE"), nullable=False)
    updated_by_user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    status = db.Column(db.String(20), nullable=False)
    comment = db.Column(db.Text, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)


class VisitorEntry(db.Model, SerializerMixin):
    __tablename__ = "visitor_entries"

    id = db.Column(db.Integer, primary_key=True)
    society_id = db.Column(db.Integer, db.ForeignKey("societies.id", ondelete="CASCADE"), nullable=False)
    recorded_by_user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    resident_user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="SET NULL"))
    visitor_name = db.Column(db.String(200), nullable=False)
    vehicle_number = db.Column(db.String(30))
    contact_number = db.Column(db.String(30))
    entry_time = db.Column(db.DateTime, nullable=False)
    exit_time = db.Column(db.DateTime)
    remarks = db.Column(db.Text)


class ProviderReview(db.Model, TimestampMixin, SerializerMixin):
    __tablename__ = "provider_reviews"

    id = db.Column(db.Integer, primary_key=True)
    provider_id = db.Column(db.Integer, db.ForeignKey("service_providers.id", ondelete="CASCADE"), nullable=False)
    resident_user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    booking_id = db.Column(db.Integer, db.ForeignKey("service_bookings.id", ondelete="SET NULL"))
    rating = db.Column(db.Integer, nullable=False)
    feedback = db.Column(db.Text)
