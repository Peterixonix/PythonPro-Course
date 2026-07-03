from io import BytesIO
from datetime import datetime, timezone
from sqlalchemy import func, extract
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from ..db import db
from ..models import Booking, Room, User
def get_monthly_report_data(month_str: str):
    try:
        start_date = datetime.strptime(month_str, "%Y-%m").replace(tzinfo=timezone.utc)
    except ValueError:
        raise ValueError("Parametr month musi mieć format YYYY-MM")
    if start_date.month == 12:
        end_date = start_date.replace(year=start_date.year + 1, month=1)
    else:
        end_date = start_date.replace(month=start_date.month + 1)
    base_query = Booking.query.filter(
        Booking.status != "cancelled",
        Booking.start_time >= start_date,
        Booking.start_time < end_date,
    )
    total_bookings = base_query.count()
    bookings = base_query.all()
    total_hours = round(sum(b.duration_hours for b in bookings), 2)
    total_revenue = round(sum(b.total_cost for b in bookings), 2)
    top_rooms = db.session.query(
        Room.name,
        func.count(Booking.id).label("booking_count"),
        func.coalesce(
            func.sum(extract("epoch", Booking.end_time - Booking.start_time) / 3600),
            0
        ).label("hours")
    ).join(Booking).filter(
        Booking.status != "cancelled",
        Booking.start_time >= start_date,
        Booking.start_time < end_date,
    ).group_by(Room.id, Room.name).order_by(
        func.count(Booking.id).desc()
    ).limit(10).all()
    top_users = db.session.query(
        User.name,
        func.count(Booking.id).label("booking_count"),
        func.coalesce(
            func.sum(extract("epoch", Booking.end_time - Booking.start_time) / 3600),
            0
        ).label("hours")
    ).join(Booking).filter(
        Booking.status != "cancelled",
        Booking.start_time >= start_date,
        Booking.start_time < end_date,
    ).group_by(User.id, User.name).order_by(
        func.count(Booking.id).desc()
    ).limit(10).all()
    return {
        "month": month_str,
        "summary": {
            "total_bookings": total_bookings,
            "total_hours": total_hours,
            "total_revenue": total_revenue,
        },
        "top_rooms": [
            {
                "name": row.name,
                "booking_count": row.booking_count,
                "hours": round(float(row.hours or 0), 2),
            }
            for row in top_rooms
        ],
        "top_users": [
            {
                "name": row.name,
                "booking_count": row.booking_count,
                "hours": round(float(row.hours or 0), 2),
            }
            for row in top_users
        ]
    }
def generate_monthly_report_pdf(month_str: str):
    report = get_monthly_report_data(month_str)
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4
    y = height - 50
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(50, y, f"Raport miesieczny rezerwacji - {report['month']}")
    y -= 40
    pdf.setFont("Helvetica", 12)
    pdf.drawString(50, y, f"Liczba rezerwacji: {report['summary']['total_bookings']}")
    y -= 20
    pdf.drawString(50, y, f"Laczny czas: {report['summary']['total_hours']} h")
    y -= 20
    pdf.drawString(50, y, f"Przychod: {report['summary']['total_revenue']} PLN")
    y -= 40
    pdf.setFont("Helvetica-Bold", 13)
    pdf.drawString(50, y, "Top 10 sal")
    y -= 25
    pdf.setFont("Helvetica", 11)
    for room in report["top_rooms"]:
        pdf.drawString(
            60,
            y,
            f"{room['name']} | rezerwacje: {room['booking_count']} | godziny: {room['hours']}"
        )
        y -= 18
        if y < 80:
            pdf.showPage()
            y = height - 50
    y -= 20
    pdf.setFont("Helvetica-Bold", 13)
    pdf.drawString(50, y, "Top 10 uzytkownikow")
    y -= 25
    pdf.setFont("Helvetica", 11)
    for user in report["top_users"]:
        pdf.drawString(
            60,
            y,
            f"{user['name']} | rezerwacje: {user['booking_count']} | godziny: {user['hours']}"
        )
        y -= 18
        if y < 80:
            pdf.showPage()
            y = height - 50
    pdf.save()
    buffer.seek(0)
    return buffer