from flask import Blueprint, request

from app.api.utils import parse_date
from app.core.extensions import db
from app.core.responses import fail, ok
from app.core.security import ROLE_ADMIN, roles_required
from app.models import ResidentOccupancy, Unit
from app.services.query_service import paginate_query


units_bp = Blueprint("units", __name__, url_prefix="/units")
occupancies_bp = Blueprint("occupancies", __name__, url_prefix="/occupancies")


@units_bp.get("")
@roles_required(ROLE_ADMIN)
def list_units():
    query = Unit.query
    for field in ["block_name", "floor", "unit_type", "status", "society_id"]:
        value = request.args.get(field)
        if value:
            query = query.filter(getattr(Unit, field) == value)

    items, pagination = paginate_query(query.order_by(Unit.created_at.desc()))
    return ok({"items": [i.to_dict() for i in items], "pagination": pagination})


@units_bp.get("/<int:unit_id>")
@roles_required(ROLE_ADMIN)
def get_unit(unit_id):
    unit = db.session.get(Unit, unit_id)
    if not unit:
        return fail("Unit not found", "NOT_FOUND", 404)
    return ok(unit.to_dict())


@units_bp.get("/<int:unit_id>/residents")
@roles_required(ROLE_ADMIN)
def get_unit_residents(unit_id):
    records = ResidentOccupancy.query.filter_by(unit_id=unit_id).all()
    return ok([r.to_dict() for r in records])


@units_bp.post("")
@roles_required(ROLE_ADMIN)
def create_unit():
    data = request.get_json() or {}
    required = ["society_id", "unit_number"]
    missing = [f for f in required if not data.get(f)]
    if missing:
        return fail(f"Missing required fields: {', '.join(missing)}", "VALIDATION_ERROR", 400)

    unit = Unit(
        society_id=data["society_id"],
        block_name=data.get("block_name"),
        unit_number=data["unit_number"],
        floor=data.get("floor"),
        unit_type=data.get("unit_type"),
        status=data.get("status", "active"),
    )
    db.session.add(unit)
    db.session.commit()
    return ok(unit.to_dict(), "Unit created", 201)


@units_bp.put("/<int:unit_id>")
@roles_required(ROLE_ADMIN)
def update_unit(unit_id):
    unit = db.session.get(Unit, unit_id)
    if not unit:
        return fail("Unit not found", "NOT_FOUND", 404)

    data = request.get_json() or {}
    for field in ["society_id", "block_name", "unit_number", "floor", "unit_type", "status"]:
        if field in data:
            setattr(unit, field, data[field])

    db.session.commit()
    return ok(unit.to_dict(), "Unit updated")


@units_bp.delete("/<int:unit_id>")
@roles_required(ROLE_ADMIN)
def delete_unit(unit_id):
    unit = db.session.get(Unit, unit_id)
    if not unit:
        return fail("Unit not found", "NOT_FOUND", 404)
    db.session.delete(unit)
    db.session.commit()
    return ok(message="Unit deleted")


@occupancies_bp.get("")
@roles_required(ROLE_ADMIN)
def list_occupancies():
    query = ResidentOccupancy.query
    for field in ["unit_id", "user_id", "occupancy_type"]:
        value = request.args.get(field)
        if value:
            query = query.filter(getattr(ResidentOccupancy, field) == value)

    items, pagination = paginate_query(query.order_by(ResidentOccupancy.id.desc()))
    return ok({"items": [i.to_dict() for i in items], "pagination": pagination})


@occupancies_bp.post("")
@roles_required(ROLE_ADMIN)
def create_occupancy():
    data = request.get_json() or {}
    required = ["unit_id", "user_id", "occupancy_type", "start_date"]
    missing = [f for f in required if not data.get(f)]
    if missing:
        return fail(f"Missing required fields: {', '.join(missing)}", "VALIDATION_ERROR", 400)

    record = ResidentOccupancy(
        unit_id=data["unit_id"],
        user_id=data["user_id"],
        occupancy_type=data["occupancy_type"],
        start_date=parse_date(data["start_date"]),
        end_date=parse_date(data.get("end_date")),
        is_primary=bool(data.get("is_primary", True)),
    )
    db.session.add(record)
    db.session.commit()
    return ok(record.to_dict(), "Occupancy created", 201)


@occupancies_bp.put("/<int:occupancy_id>")
@roles_required(ROLE_ADMIN)
def update_occupancy(occupancy_id):
    record = db.session.get(ResidentOccupancy, occupancy_id)
    if not record:
        return fail("Occupancy not found", "NOT_FOUND", 404)

    data = request.get_json() or {}
    if "occupancy_type" in data:
        record.occupancy_type = data["occupancy_type"]
    if "start_date" in data:
        record.start_date = parse_date(data["start_date"])
    if "end_date" in data:
        record.end_date = parse_date(data["end_date"])
    if "is_primary" in data:
        record.is_primary = bool(data["is_primary"])

    db.session.commit()
    return ok(record.to_dict(), "Occupancy updated")


@occupancies_bp.delete("/<int:occupancy_id>")
@roles_required(ROLE_ADMIN)
def delete_occupancy(occupancy_id):
    record = db.session.get(ResidentOccupancy, occupancy_id)
    if not record:
        return fail("Occupancy not found", "NOT_FOUND", 404)
    db.session.delete(record)
    db.session.commit()
    return ok(message="Occupancy removed")

