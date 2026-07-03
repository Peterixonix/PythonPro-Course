from datetime import datetime, timedelta, timezone
from ..db import db
from ..models import Notification, User, Booking
def create_admin_notification_for_booking(booking):
    admins = User.query.filter_by(is_admin=True).all()
    notifications = []
    for admin in admins:
        notification = Notification(
            user_id=admin.id,
            message=(
                f"Nowa rezerwacja: '{booking.title}' "
                f"w sali '{booking.room.name}' "
                f"przez użytkownika '{booking.user.name}'."
            ),
        )
        db.session.add(notification)
        notifications.append(notification)
    return notifications
def get_unread_notifications(user_id=None):
    query = Notification.query.filter_by(is_read=False)
    if user_id is not None:
        query = query.filter(Notification.user_id == user_id)
    return query.order_by(Notification.created_at.desc()).all()
def mark_as_read(notification_id):
    notification = Notification.query.get(notification_id)
    if not notification:
        raise ValueError("Powiadomienie nie istnieje.")
    if notification.is_read:
        return notification
    notification.is_read = True
    db.session.commit()
    return notification
def create_upcoming_booking_reminders():
    now = datetime.now(timezone.utc)
    one_hour_later = now + timedelta(hours=1)
    window_end = one_hour_later + timedelta(minutes=5)
    bookings = Booking.query.filter(
        Booking.status == "confirmed",
        Booking.start_time >= one_hour_later,
        Booking.start_time <= window_end
    ).all()
    created = 0
    for booking in bookings:
        existing = Notification.query.filter(
            Notification.user_id == booking.user_id,
            Notification.message.like(f"%Przypomnienie%{booking.id}%")
        ).first()
        if existing:
            continue
        notification = Notification(
            user_id=booking.user_id,
            message=(
                f"Przypomnienie: rezerwacja #{booking.id} "
                f"'{booking.title}' zaczyna się za około 1 godzinę."
            ),
        )
        db.session.add(notification)
        created += 1
    db.session.commit()
    return created