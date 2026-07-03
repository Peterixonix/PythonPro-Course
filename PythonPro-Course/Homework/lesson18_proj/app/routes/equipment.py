from flask import Blueprint, jsonify, request
from ..db import db
from app.models import Equipment

equipment_bp = Blueprint("equipment", __name__, url_prefix="/api/equipments")


@equipment_bp.route("/")
def get_all_equipments():
    return jsonify([e.to_dict() for e in Equipment.query.all()])


@equipment_bp.route("/", methods=["POST"])
def create_equipment():
    data = request.json()

    eq = Equipment(name=data['name'], icon=data['icon'])
    db.session.add(eq)
    db.session.commit()
    return jsonify(eq.to_dict())
