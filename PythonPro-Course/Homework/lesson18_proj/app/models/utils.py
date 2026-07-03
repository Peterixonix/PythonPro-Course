from .base import db
from .room import Room
from .booking import Booking
from .equipment import Equipment
from sqlalchemy import func, extract
from sqlalchemy.orm import joinedload


def get_booking_statistics(start_date=None, end_date=None):
    """
    Pobierz statystyki rezerwacji.

    Returns:
        dict: Słownik ze statystykami
    """
    base_query = Booking.query.filter(Booking.status != 'cancelled')

    if start_date:
        base_query = base_query.filter(Booking.start_time >= start_date)
    if end_date:
        base_query = base_query.filter(Booking.end_time <= end_date)

    # Ogólne statystyki
    total_bookings = base_query.count()

    # Statystyki per sala
    room_stats = db.session.query(
        Room.name,
        func.count(Booking.id).label('booking_count'),
        func.sum(
            extract('epoch', Booking.end_time - Booking.start_time) /
            3600).label('total_hours')).join(Booking).filter(
                Booking.status != 'cancelled').group_by(Room.name).all()

    # Statystyki per dzień tygodnia
    weekday_stats = db.session.query(
        extract('dow', Booking.start_time).label('weekday'),
        func.count(Booking.id).label('count')).filter(
            Booking.status != 'cancelled').group_by('weekday').order_by(
                'weekday').all()

    weekdays = ['Nd', 'Pn', 'Wt', 'Śr', 'Cz', 'Pt', 'Sb']

    return {
        'total_bookings':
        total_bookings,
        'room_stats': [{
            'room': r.name,
            'bookings': r.booking_count,
            'hours': round(float(r.total_hours or 0), 1)
        } for r in room_stats],
        'weekday_stats': [{
            'day': weekdays[int(w.weekday)],
            'count': w.count
        } for w in weekday_stats]
    }


def find_available_rooms(start_time,
                         end_time,
                         min_capacity=1,
                         required_equipment=None):

    query = Room.query.options(joinedload(Room.equipment)).\
        filter(Room.is_active == True, Room.capacity >= min_capacity)

    if required_equipment:
        # Optymalizacja: pobieranie sal z odpowiednią liczbą dopasowań sprzętu
        equip_count = len(required_equipment)
        query = query.join(Room.equipment).\
            filter(Equipment.name.in_(required_equipment)).\
            group_by(Room.id).\
            having(func.count(Equipment.id) == equip_count)

    candidate_rooms = query.all()

    available = []
    for room in candidate_rooms:
        if room.is_available(start_time, end_time):
            available.append(room)

    return available
