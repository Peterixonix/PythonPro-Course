from datetime import datetime, timedelta, timezone
from sqlalchemy import func, extract
from sqlalchemy.orm import joinedload
from ..db import db
from ..models import Booking, Room, User
def get_dashboard_summary():
    now = datetime.now(timezone.utc)
    next_24h = now + timedelta(hours=24)
    last_30_days = now - timedelta(days=30)
    total_rooms = Room.query.filter_by(is_active=True).count()
    total_bookings = Booking.query.count()
    total_users = User.query.count()
    bookings_today = Booking.query.filter(
        Booking.status != "cancelled",
        func.date(Booking.start_time) == now.date()
    ).count()
    upcoming = Booking.query.options(
        joinedload(Booking.room),
        joinedload(Booking.user)
    ).filter(
        Booking.status == "confirmed",
        Booking.start_time >= now,
        Booking.start_time <= next_24h
    ).order_by(Booking.start_time.asc()).limit(10).all()
    top_users = db.session.query(
        User.name,
        func.count(Booking.id).label("booking_count")
    ).join(Booking).filter(
        Booking.status != "cancelled"
    ).group_by(User.id, User.name).order_by(
        func.count(Booking.id).desc()
    ).limit(5).all()
    room_utilization_raw = db.session.query(
        Room.name,
        func.coalesce(
            func.sum(
                extract("epoch", Booking.end_time - Booking.start_time) / 3600
            ),
            0
        ).label("hours")
    ).outerjoin(
        Booking,
        (Booking.room_id == Room.id)
        & (Booking.status != "cancelled")
        & (Booking.start_time >= last_30_days)
    ).filter(
        Room.is_active == True
    ).group_by(Room.id, Room.name).all()
    max_hours = max([float(r.hours or 0) for r in room_utilization_raw], default=0)
    room_utilization = []
    for room in room_utilization_raw:
        hours = round(float(room.hours or 0), 1)
        utilization = 0 if max_hours == 0 else round((hours / max_hours) * 100, 1)
        room_utilization.append({
            "room": room.name,
            "hours": hours,
            "utilization": utilization,
        })
    stats = {
        "total_rooms": total_rooms,
        "total_bookings": total_bookings,
        "bookings_today": bookings_today,
        "total_users": total_users,
    }
    top_users_data = [
        {"name": user.name, "booking_count": user.booking_count}
        for user in top_users
    ]
    return stats, upcoming, top_users_data, room_utilization
def get_department_distribution():
    """
    Wykres kołowy: rozkład rezerwacji per departament.
    """
    rows = db.session.query(
        User.department.label("department"),
        func.count(Booking.id).label("count")
    ).join(Booking, Booking.user_id == User.id).filter(
        Booking.status != "cancelled"
    ).group_by(User.department).order_by(
        func.count(Booking.id).desc()
    ).all()
    return [
        {
            "department": row.department or "Brak departamentu",
            "count": row.count,
        }
        for row in rows
    ]
def get_booking_heatmap():
    """
    Heatmapa: dzień tygodnia x godzina.
    Wymaganie z lesson-18:
    - extract('dow', ...)
    - extract('hour', ...)
    """
    rows = db.session.query(
        extract("dow", Booking.start_time).label("weekday"),
        extract("hour", Booking.start_time).label("hour"),
        func.count(Booking.id).label("count")
    ).filter(
        Booking.status != "cancelled"
    ).group_by(
        extract("dow", Booking.start_time),
        extract("hour", Booking.start_time)
    ).order_by(
        extract("dow", Booking.start_time),
        extract("hour", Booking.start_time)
    ).all()
    weekday_labels = {
        0: "Nd",
        1: "Pn",
        2: "Wt",
        3: "Śr",
        4: "Cz",
        5: "Pt",
        6: "Sb",
    }
    return [
        {
            "weekday": int(row.weekday),
            "weekday_label": weekday_labels[int(row.weekday)],
            "hour": int(row.hour),
            "count": row.count,
        }
        for row in rows
    ]
def get_booking_trend(days=30):
    """
    Trend: liczba rezerwacji dziennie w ostatnich 30 dniach.
    """
    now = datetime.now(timezone.utc)
    start_date = now.date() - timedelta(days=days - 1)
    rows = db.session.query(
        func.date(Booking.start_time).label("day"),
        func.count(Booking.id).label("count")
    ).filter(
        Booking.status != "cancelled",
        func.date(Booking.start_time) >= start_date
    ).group_by(
        func.date(Booking.start_time)
    ).order_by(
        func.date(Booking.start_time)
    ).all()
    counts_by_day = {str(row.day): row.count for row in rows}
    trend = []
    for i in range(days):
        current_day = start_date + timedelta(days=i)
        day_str = current_day.isoformat()
        trend.append({
            "date": day_str,
            "count": counts_by_day.get(day_str, 0),
        })
    return trend
def get_dashboard_api_stats():
    return {
        "department_distribution": get_department_distribution(),
        "booking_heatmap": get_booking_heatmap(),
        "booking_trend_30d": get_booking_trend(30),
    }