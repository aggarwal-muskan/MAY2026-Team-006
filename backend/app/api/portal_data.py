from datetime import UTC, date, datetime

from flask import Blueprint, request

from app.api.utils import current_user, parse_date
from app.core.extensions import db
from app.core.responses import fail, ok
from app.core.security import ROLE_ADMIN, ROLE_OWNER, ROLE_SECURITY, ROLE_TENANT, roles_required
from app.models import AppSetting, FamilyMember, MaintenanceBill, ResidentOccupancy, SystemLog, Unit, User
from app.services.auth_service import hash_password
from app.services.query_service import paginate_query


family_members_bp = Blueprint("family_members", __name__, url_prefix="/family-members")
maintenance_bills_bp = Blueprint("maintenance_bills", __name__, url_prefix="/maintenance-bills")
system_logs_bp = Blueprint("system_logs", __name__, url_prefix="/system-logs")
settings_bp = Blueprint("settings", __name__, url_prefix="/settings")
tenants_bp = Blueprint("tenants", __name__, url_prefix="/tenants")


@family_members_bp.get("")
@roles_required(ROLE_OWNER, ROLE_TENANT, ROLE_ADMIN)
def list_family_members():
    actor = current_user()
    resident_user_id = request.args.get("resident_user_id", type=int)
    query = FamilyMember.query

    if actor.role in [ROLE_OWNER, ROLE_TENANT]:
        query = query.filter_by(resident_user_id=actor.id)
    elif resident_user_id:
        query = query.filter_by(resident_user_id=resident_user_id)

    items, pagination = paginate_query(query.order_by(FamilyMember.created_at.desc()))
    return ok({"items": [item.to_dict() for item in items], "pagination": pagination})


@family_members_bp.post("")
@roles_required(ROLE_OWNER, ROLE_TENANT, ROLE_ADMIN)
def create_family_member():
    actor = current_user()
    data = request.get_json() or {}
    resident_user_id = actor.id if actor.role in [ROLE_OWNER, ROLE_TENANT] else data.get("resident_user_id")

    required = ["full_name", "relation"]
    missing = [field for field in required if not data.get(field)]
    if not resident_user_id:
        missing.append("resident_user_id")
    if missing:
        return fail(f"Missing required fields: {', '.join(sorted(set(missing)))}", "VALIDATION_ERROR", 400)

    member = FamilyMember(
        resident_user_id=resident_user_id,
        full_name=data["full_name"],
        relation=data["relation"],
        phone=data.get("phone"),
        age=data.get("age"),
        is_primary_contact=bool(data.get("is_primary_contact", False)),
    )
    db.session.add(member)
    db.session.commit()
    return ok(member.to_dict(), "Family member created", 201)


@family_members_bp.put("/<int:member_id>")
@roles_required(ROLE_OWNER, ROLE_TENANT, ROLE_ADMIN)
def update_family_member(member_id):
    actor = current_user()
    member = db.session.get(FamilyMember, member_id)
    if not member:
        return fail("Family member not found", "NOT_FOUND", 404)
    if actor.role in [ROLE_OWNER, ROLE_TENANT] and member.resident_user_id != actor.id:
        return fail("Forbidden", "FORBIDDEN", 403)

    data = request.get_json() or {}
    for field in ["full_name", "relation", "phone", "age", "is_primary_contact"]:
        if field in data:
            setattr(member, field, data[field])

    db.session.commit()
    return ok(member.to_dict(), "Family member updated")


@family_members_bp.delete("/<int:member_id>")
@roles_required(ROLE_OWNER, ROLE_TENANT, ROLE_ADMIN)
def delete_family_member(member_id):
    actor = current_user()
    member = db.session.get(FamilyMember, member_id)
    if not member:
        return fail("Family member not found", "NOT_FOUND", 404)
    if actor.role in [ROLE_OWNER, ROLE_TENANT] and member.resident_user_id != actor.id:
        return fail("Forbidden", "FORBIDDEN", 403)

    db.session.delete(member)
    db.session.commit()
    return ok(message="Family member removed")


@maintenance_bills_bp.get("")
@roles_required(ROLE_OWNER, ROLE_TENANT, ROLE_ADMIN)
def list_maintenance_bills():
    actor = current_user()
    resident_user_id = request.args.get("resident_user_id", type=int)
    query = MaintenanceBill.query

    if actor.role in [ROLE_OWNER, ROLE_TENANT]:
        query = query.filter_by(resident_user_id=actor.id)
    elif resident_user_id:
        query = query.filter_by(resident_user_id=resident_user_id)

    items, pagination = paginate_query(query.order_by(MaintenanceBill.due_date.desc()))
    return ok({"items": [item.to_dict() for item in items], "pagination": pagination})


@maintenance_bills_bp.post("")
@roles_required(ROLE_ADMIN)
def create_maintenance_bill():
    data = request.get_json() or {}
    required = ["resident_user_id", "month_label", "amount", "due_date"]
    missing = [field for field in required if not data.get(field)]
    if missing:
        return fail(f"Missing required fields: {', '.join(missing)}", "VALIDATION_ERROR", 400)

    bill = MaintenanceBill(
        resident_user_id=data["resident_user_id"],
        month_label=data["month_label"],
        amount=float(data["amount"]),
        due_date=parse_date(data["due_date"]),
        status=str(data.get("status", "unpaid")).lower(),
        notes=data.get("notes"),
    )
    db.session.add(bill)
    db.session.commit()
    return ok(bill.to_dict(), "Maintenance bill created", 201)


@maintenance_bills_bp.put("/<int:bill_id>/pay")
@roles_required(ROLE_OWNER, ROLE_TENANT, ROLE_ADMIN)
def pay_maintenance_bill(bill_id):
    actor = current_user()
    bill = db.session.get(MaintenanceBill, bill_id)
    if not bill:
        return fail("Maintenance bill not found", "NOT_FOUND", 404)
    if actor.role in [ROLE_OWNER, ROLE_TENANT] and bill.resident_user_id != actor.id:
        return fail("Forbidden", "FORBIDDEN", 403)
    if str(bill.status).lower() == "paid":
        return fail("Bill already paid", "DUPLICATE", 409)

    bill.status = "paid"
    bill.paid_date = datetime.now(UTC).date()
    db.session.commit()
    return ok(bill.to_dict(), "Payment recorded")


@system_logs_bp.get("")
@roles_required(ROLE_ADMIN)
def list_system_logs():
    query = SystemLog.query
    action = request.args.get("action")
    if action:
        query = query.filter(SystemLog.action.ilike(f"%{action}%"))
    items, pagination = paginate_query(query.order_by(SystemLog.created_at.desc()))
    return ok({"items": [item.to_dict() for item in items], "pagination": pagination})


@settings_bp.get("")
@roles_required(ROLE_ADMIN)
def get_settings():
    rows = AppSetting.query.order_by(AppSetting.setting_key.asc()).all()
    return ok({item.setting_key: item.setting_value for item in rows})


@settings_bp.put("")
@roles_required(ROLE_ADMIN)
def update_settings():
    data = request.get_json() or {}
    if not isinstance(data, dict) or not data:
        return fail("No settings provided", "VALIDATION_ERROR", 400)

    for key, value in data.items():
        record = AppSetting.query.filter_by(setting_key=key).first()
        if not record:
            record = AppSetting(setting_key=key, setting_value=str(value))
            db.session.add(record)
        else:
            record.setting_value = str(value)

    db.session.commit()
    return ok({item.setting_key: item.setting_value for item in AppSetting.query.all()}, "Settings updated")


@tenants_bp.get("")
@roles_required(ROLE_ADMIN)
def list_tenants():
    search = request.args.get("search", "").strip().lower()
    tenant_users = User.query.filter_by(role="tenant").all()
    tenant_ids = [u.id for u in tenant_users]

    occupancies = ResidentOccupancy.query.filter(ResidentOccupancy.user_id.in_(tenant_ids or [-1])).all()
    unit_ids = [record.unit_id for record in occupancies]
    units = {unit.id: unit for unit in Unit.query.filter(Unit.id.in_(unit_ids or [-1])).all()}

    owners_by_unit_id = {}
    owner_occupancies = ResidentOccupancy.query.filter(ResidentOccupancy.unit_id.in_(unit_ids or [-1]), ResidentOccupancy.occupancy_type == "owner").all()
    owner_ids = [record.user_id for record in owner_occupancies]
    owners = {owner.id: owner for owner in User.query.filter(User.id.in_(owner_ids or [-1])).all()}
    for owner_occ in owner_occupancies:
        if owner_occ.unit_id not in owners_by_unit_id and owner_occ.user_id in owners:
            owners_by_unit_id[owner_occ.unit_id] = owners[owner_occ.user_id]

    items = []
    for tenant in tenant_users:
        occ = next((record for record in occupancies if record.user_id == tenant.id and record.is_primary), None)
        if not occ:
            occ = next((record for record in occupancies if record.user_id == tenant.id), None)
        unit = units.get(occ.unit_id) if occ else None
        owner = owners_by_unit_id.get(unit.id) if unit else None
        row = {
            "id": tenant.id,
            "name": tenant.full_name,
            "email": tenant.email,
            "phone": tenant.phone,
            "flat": unit.unit_number if unit else (tenant.flat_number or "-"),
            "owner": owner.full_name if owner else "-",
            "owner_user_id": owner.id if owner else None,
            "leaseStart": occ.start_date.isoformat() if occ and occ.start_date else None,
            "leaseEnd": occ.end_date.isoformat() if occ and occ.end_date else None,
            "status": tenant.status,
        }
        if search:
            values = [
                row["name"],
                row["email"],
                row["phone"],
                row["flat"],
                row["owner"],
                row["status"],
            ]
            if not any(search in str(value or "").lower() for value in values):
                continue
        items.append(row)

    return ok({"items": items, "pagination": {"page": 1, "limit": len(items), "total": len(items), "pages": 1}})


@tenants_bp.post("")
@roles_required(ROLE_ADMIN)
def create_tenant():
    actor = current_user()
    data = request.get_json() or {}

    required = ["full_name", "email", "password", "flat_number"]
    missing = [field for field in required if not str(data.get(field, "")).strip()]
    if missing:
        return fail(f"Missing required fields: {', '.join(missing)}", "VALIDATION_ERROR", 400)

    email = str(data["email"]).strip().lower()
    if User.query.filter_by(email=email).first():
        return fail("Email already exists", "DUPLICATE_EMAIL", 409)

    tenant = User(
        society_id=actor.society_id,
        role="tenant",
        full_name=str(data["full_name"]).strip(),
        email=email,
        phone=str(data.get("phone") or "").strip() or None,
        flat_number=str(data.get("flat_number") or "").strip() or None,
        password_hash=hash_password(str(data["password"])),
        status=str(data.get("status") or "active").strip().lower(),
    )
    db.session.add(tenant)
    db.session.flush()

    flat_number = str(data.get("flat_number") or "").strip()
    unit = Unit.query.filter_by(society_id=actor.society_id, unit_number=flat_number).first()
    if not unit:
        unit = Unit(
            society_id=actor.society_id,
            block_name=flat_number.split("-")[0] if "-" in flat_number else None,
            unit_number=flat_number,
            status="active",
        )
        db.session.add(unit)
        db.session.flush()

    lease_start = parse_date(data["leaseStart"]) if data.get("leaseStart") else date.today()
    lease_end = parse_date(data["leaseEnd"]) if data.get("leaseEnd") else None
    occupancy = ResidentOccupancy(
        unit_id=unit.id,
        user_id=tenant.id,
        occupancy_type="tenant",
        start_date=lease_start,
        end_date=lease_end,
        is_primary=True,
    )
    db.session.add(occupancy)
    db.session.commit()

    return ok({
        "id": tenant.id,
        "name": tenant.full_name,
        "email": tenant.email,
        "phone": tenant.phone,
        "flat": unit.unit_number,
        "owner": "-",
        "leaseStart": occupancy.start_date.isoformat() if occupancy.start_date else None,
        "leaseEnd": occupancy.end_date.isoformat() if occupancy.end_date else None,
        "status": tenant.status,
    }, "Tenant created", 201)


@tenants_bp.put("/<int:tenant_id>")
@roles_required(ROLE_ADMIN)
def update_tenant(tenant_id):
    actor = current_user()
    tenant = db.session.get(User, tenant_id)
    if not tenant or tenant.role != "tenant":
        return fail("Tenant not found", "NOT_FOUND", 404)

    data = request.get_json() or {}
    if "full_name" in data:
        tenant.full_name = str(data["full_name"]).strip()
    if "phone" in data:
        tenant.phone = str(data["phone"]).strip() or None
    if "status" in data:
        tenant.status = str(data["status"]).strip().lower()
    if "email" in data:
        next_email = str(data["email"]).strip().lower()
        if next_email and next_email != tenant.email and User.query.filter_by(email=next_email).first():
            return fail("Email already exists", "DUPLICATE_EMAIL", 409)
        tenant.email = next_email
    if "password" in data and str(data.get("password") or "").strip():
        tenant.password_hash = hash_password(str(data.get("password")))

    occupancy = ResidentOccupancy.query.filter_by(user_id=tenant.id, is_primary=True).first()
    if not occupancy:
        occupancy = ResidentOccupancy.query.filter_by(user_id=tenant.id).first()

    flat_number = str(data.get("flat_number") or data.get("flat") or "").strip()
    if flat_number:
        tenant.flat_number = flat_number
        unit = Unit.query.filter_by(society_id=actor.society_id, unit_number=flat_number).first()
        if not unit:
            unit = Unit(
                society_id=actor.society_id,
                block_name=flat_number.split("-")[0] if "-" in flat_number else None,
                unit_number=flat_number,
                status="active",
            )
            db.session.add(unit)
            db.session.flush()

        if occupancy:
            occupancy.unit_id = unit.id
            occupancy.occupancy_type = "tenant"
        else:
            occupancy = ResidentOccupancy(
                unit_id=unit.id,
                user_id=tenant.id,
                occupancy_type="tenant",
                start_date=date.today(),
                is_primary=True,
            )
            db.session.add(occupancy)

    if occupancy:
        if "leaseStart" in data and data.get("leaseStart"):
            occupancy.start_date = parse_date(data["leaseStart"])
        if "leaseEnd" in data:
            occupancy.end_date = parse_date(data["leaseEnd"]) if data.get("leaseEnd") else None

    db.session.commit()
    return ok(message="Tenant updated")
