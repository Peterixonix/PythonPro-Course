from .base import db, Base
from .booking import Booking
from .associations import room_equipment


class Room(Base):
    """Model sali konferencyjnej."""
    __tablename__ = 'rooms'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    floor = db.Column(db.Integer, default=0)
    description = db.Column(db.Text)
    is_active = db.Column(db.Boolean, default=True)
    hourly_rate = db.Column(db.Numeric(10, 2), default=0)

    bookings = db.relationship('Booking',
                               backref='room',
                               lazy='dynamic',
                               cascade='all, delete-orphan')

    equipment = db.relationship('Equipment',
                                secondary=room_equipment,
                                lazy='subquery',
                                backref=db.backref('rooms', lazy=True))

    def __repr__(self):
        return f'<Room {self.name} (cap: {self.capacity})>'

    def to_dict(self, include_equipment=True):
        data = super().to_dict()
        if include_equipment:
            data['equipment'] = [e.name for e in self.equipment]
        return data

    def is_available(self, start_time, end_time, exclude_booking_id=None):
        """
        Sprawdza, czy sala jest dostępna w podanym przedziale czasowym.
        
        Args:
            start_time: Początek rezerwacji (datetime)
            end_time: Koniec rezerwacji (datetime)
            exclude_booking_id: ID rezerwacji do pominięcia (przy edycji)
        
        Returns:
            bool: True jeśli sala jest dostępna
        """
        query = Booking.query.filter(
            Booking.room_id == self.id,
            Booking.status != 'cancelled',
            # Sprawdzenie nakładania się przedziałów czasowych
            Booking.start_time < end_time,
            Booking.end_time > start_time)

        if exclude_booking_id:
            query = query.filter(Booking.id != exclude_booking_id)

        return query.count() == 0
