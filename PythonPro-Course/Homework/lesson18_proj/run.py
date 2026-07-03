"""
Główny plik uruchamiający aplikację.
"""
from dotenv import load_dotenv
load_dotenv(override=True)
from sqlalchemy import inspect
import random
from datetime import datetime, timedelta, timezone

from app import create_app
from app.models import Booking, Equipment, Room, User
from app.db import db

app = create_app()

# Surowe dane wejściowe
EQUIPMENT_DATA = [
    {
        "name": "Projektor",
        "icon": "projector"
    },
    {
        "name": "Tablica",
        "icon": "chalkboard"
    },
    {
        "name": "Wideokonferencja",
        "icon": "video"
    },
    {
        "name": "Klimatyzacja",
        "icon": "snowflake"
    },
    {
        "name": "Nagłośnienie",
        "icon": "volume-up"
    },
]

ROOMS_DATA = [
    {
        "name": "Sala A1",
        "capacity": 10,
        "floor": 1,
        "description": "Mała sala do spotkań zespołowych",
        "hourly_rate": 50,
        "equipment_names": ["Tablica", "Klimatyzacja"]
    },
    {
        "name": "Sala B2",
        "capacity": 20,
        "floor": 2,
        "description": "Średnia sala z projektorem",
        "hourly_rate": 80,
        "equipment_names": ["Projektor", "Wideokonferencja", "Klimatyzacja"]
    },
    {
        "name":
        "Sala Konferencyjna",
        "capacity":
        50,
        "floor":
        3,
        "description":
        "Duża sala na prezentacje",
        "hourly_rate":
        150,
        "equipment_names": [
            "Projektor", "Tablica", "Wideokonferencja", "Klimatyzacja",
            "Nagłośnienie"
        ]
    },
    {
        "name": "Pokój Kreatywny",
        "capacity": 8,
        "floor": 1,
        "description": "Sala do burzy mózgów z tablicami",
        "hourly_rate": 60,
        "equipment_names": ["Tablica"]
    },
]

USERS_DATA = [
    {
        "name": "Jan Kowalski",
        "email": "jan@firma.pl",
        "department": "IT",
        "is_admin": False
    },
    {
        "name": "Anna Nowak",
        "email": "anna@firma.pl",
        "department": "HR",
        "is_admin": False
    },
    {
        "name": "Piotr Wiśniewski",
        "email": "piotr@firma.pl",
        "department": "Marketing",
        "is_admin": False
    },
    {
        "name": "Maria Dąbrowska",
        "email": "maria@firma.pl",
        "department": "IT",
        "is_admin": True
    },
]

BOOKING_TITLES = [
    "Spotkanie zespołu",
    "Code review",
    "Prezentacja projektu",
    "Rozmowa rekrutacyjna",
    "Szkolenie",
    "Planning sprint",
    "Retrospektywa",
    "Demo dla klienta",
]


def seed_database():
    """Wypełnia bazę przykładowymi danymi."""
    with app.app_context():
        if User.query.first():
            return

        # Wczytywanie wyposażenia
        equipments_map = {}
        for eq_data in EQUIPMENT_DATA:
            eq = Equipment(name=eq_data["name"], icon=eq_data["icon"])
            db.session.add(eq)
            equipments_map[eq_data["name"]] = eq

        db.session.commit()

        # Wczytywanie sal i mapowanie relacji
        rooms = []
        for room_data in ROOMS_DATA:
            room = Room(name=room_data["name"],
                        capacity=room_data["capacity"],
                        floor=room_data["floor"],
                        description=room_data["description"],
                        hourly_rate=room_data["hourly_rate"])
            # Powiązanie sprzętu na podstawie słownika
            room.equipment = [
                equipments_map[name] for name in room_data["equipment_names"]
            ]
            db.session.add(room)
            rooms.append(room)

        # Wczytywanie użytkowników
        users = []
        for user_data in USERS_DATA:
            user = User(**user_data)
            db.session.add(user)
            users.append(user)

        db.session.commit()

        # Generowanie rezerwacji
        now = datetime.now(timezone.utc).replace(minute=0,
                                                 second=0,
                                                 microsecond=0)

        for _ in range(20):
            room = random.choice(rooms)
            user = random.choice(users)

            days_offset = random.randint(0, 14)
            hour = random.randint(9, 16)
            duration = random.choice([1, 2, 3])

            start = now + timedelta(days=days_offset, hours=hour - now.hour)
            end = start + timedelta(hours=duration)

            if room.is_available(start, end):
                booking = Booking(room_id=room.id,
                                  user_id=user.id,
                                  title=random.choice(BOOKING_TITLES),
                                  start_time=start,
                                  end_time=end,
                                  attendees_count=random.randint(
                                      2, room.capacity),
                                  applied_hourly_rate=room.hourly_rate)
                db.session.add(booking)

        db.session.commit()


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        if User.query.count() == 0:
            print("Baza pusta - uruchamiam seed.")
            seed_database()
        else:
            print("Dane już istnieją - pomijam seed.")
        print("Users:", User.query.count())
        print("Rooms:", Room.query.count())
        print("Bookings:", Booking.query.count())
        print("Equipment:", Equipment.query.count())
    app.run(debug=True, port=5000)

