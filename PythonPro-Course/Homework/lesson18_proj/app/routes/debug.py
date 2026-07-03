from time import perf_counter
from flask import Blueprint, jsonify
from sqlalchemy.orm import joinedload
from ..models import Booking
debug_bp = Blueprint("debug", __name__, url_prefix="/debug")
class QueryStats:
    query_count = 0
    @classmethod
    def reset(cls):
        cls.query_count = 0
def serialize_bookings(bookings):
    result = []
    for booking in bookings:
        result.append({
            "title": booking.title,
            "room_name": booking.room.name if booking.room else None,
            "user_name": booking.user.name if booking.user else None,
        })
    return result
def run_measurement(use_joinedload=False):
    QueryStats.reset()
    start = perf_counter()
    query = Booking.query
    if use_joinedload:
        query = query.options(
            joinedload(Booking.room),
            joinedload(Booking.user),
        )
    bookings = query.all()
    data = serialize_bookings(bookings)
    duration_ms = round((perf_counter() - start) * 1000, 2)
    return {
        "query_count": QueryStats.query_count,
        "duration_ms": duration_ms,
        "bookings_count": len(data),
        "bookings": data,
    }
@debug_bp.route("/n-plus-1", methods=["GET"])
def debug_n_plus_1():
    without_optimization = run_measurement(use_joinedload=False)
    with_optimization = run_measurement(use_joinedload=True)
    return jsonify({
        "without_optimization": without_optimization,
        "with_optimization": with_optimization,
        "comparison": {
            "saved_queries": (
                without_optimization["query_count"]
                - with_optimization["query_count"]
            ),
            "saved_time_ms": round(
                without_optimization["duration_ms"]
                - with_optimization["duration_ms"],
                2,
            ),
        },
    })