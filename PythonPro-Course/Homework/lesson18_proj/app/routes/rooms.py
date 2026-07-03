import re

from flask import Blueprint, Response, jsonify, request
from ..models import Room
from ..services import rooms_service as rs

rooms_bp = Blueprint('rooms', __name__, url_prefix="/api/rooms")

# def validate_room_create(data):


@rooms_bp.route("/")
def get_rooms() -> Response:
    return jsonify([r.to_dict() for r in rs.get_rooms_all()])


@rooms_bp.route("/<int:room_id>")
def get_room(room_id: int) -> Response:
    return jsonify(rs.get_room_by_id(room_id).to_dict())


@rooms_bp.route("/", methods=["POST"])
def create_room():
    request.json()
