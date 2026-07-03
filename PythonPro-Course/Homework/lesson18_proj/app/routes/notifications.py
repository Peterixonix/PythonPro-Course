from flask import Blueprint, jsonify, request
from ..services import notification_service as ns
from .utils import http_err
notifications_bp = Blueprint(
    "notifications",
    __name__,
    url_prefix="/api/notifications"
)
@notifications_bp.route("/", methods=["GET"])
def get_notifications():
    user_id = request.args.get("user_id", type=int)
    notifications = ns.get_unread_notifications(user_id=user_id)
    return jsonify({
        "notifications": [n.to_dict() for n in notifications],
        "total": len(notifications),
    })
@notifications_bp.route("/<int:notification_id>/read", methods=["POST"])
def mark_notification_read(notification_id):
    try:
        notification = ns.mark_as_read(notification_id)
        return jsonify({
            "message": "Powiadomienie oznaczone jako przeczytane",
            "notification": notification.to_dict(),
        })
    except ValueError as e:
        return http_err(str(e), 404)
@notifications_bp.route("/generate-reminders", methods=["POST"])
def generate_reminders():
    created = ns.create_upcoming_booking_reminders()
    return jsonify({
        "message": "Przypomnienia wygenerowane",
        "created": created,
    })