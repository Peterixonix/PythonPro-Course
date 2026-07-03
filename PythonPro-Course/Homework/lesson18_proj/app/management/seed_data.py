from app import create_app
from ..db import db
from app.models import User, Room, Equipment, Booking
from datetime import datetime, timedelta
import random

app = create_app()

EQUIPMENT_DATA = [
    ("Projektor", "projector"),
    ("Tablica", "chalkboard"),
    ("Wideokonferencja", "video"),
    ("Klimatyzacja", "snowflake"),
    ("Nagłośnienie", "volume-up"),
]

ROOM_DATA = [
    (
        "Sala A1",
        10,
        1,
        "Mała sala do spotkań zespołowych",
        50,
        ["Tablica", "Klimatyzacja"],
    ),
    (
        "Sala B2",
        20,
        2,
        "Średnia sala z projektorem",
        80,
        ["Projektor", "Wideokonferencja", "Klimatyzacja"],
    ),
    (
        "Sala Konferencyjna",
        50,
        3,
        "Duża sala na prezentacje",
        150,
        [
            "Projektor",
            "Tablica",
            "Wideokonferencja",
            "Klimatyzacja",
            "Nagłośnienie",
        ],
    ),
    (
        "Pokój Kreatywny",
        8,
        1,
        "Sala do burzy mózgów z tablicami",
        60,
        ["Tablica"],
    ),
]

USER_DATA = [
    ("Jan Kowalski", "jan@firma.pl", "IT", False),
    ("Anna Nowak", "anna@firma.pl", "HR", False),
    ("Piotr Wiśniewski", "piotr@firma.pl", "Marketing", False),
    ("Maria Dąbrowska", "maria@firma.pl", "IT", True),
]


def seed_database():
    with app.app_context():

        if User.query.first():
            print("Baza już zawiera dane. Pomijam seeding.")
            return

        print("Tworzenie przykładowych danych...")

        # Wyposażenie
        equipment_map = {}

        for name, icon in EQUIPMENT_DATA:
            equipment = Equipment(name=name, icon=icon)
            equipment_map[name] = equipment
            db.session.add(equipment)

        # Sale
        rooms = []

        for (name, capacity, floor, description, hourly_rate,
             equipment_names) in ROOM_DATA:

            room = Room(
                name=name,
                capacity=capacity,
                floor=floor,
                description=description,
                hourly_rate=hourly_rate,
            )

            room.equipment = [
                equipment_map[equipment_name]
                for equipment_name in equipment_names
            ]

            rooms.append(room)
            db.session.add(room)

        # Użytkownicy
        users = []

        for name, email, department, is_admin in USER_DATA:
            user = User(
                name=name,
                email=email,
                department=department,
                is_admin=is_admin,
            )

            users.append(user)
            db.session.add(user)

        # Rezerwacje
        titles = [
            "Spotkanie zespołu",
            "Code review",
            "Prezentacja projektu",
            "Rozmowa rekrutacyjna",
            "Szkolenie",
            "Planning sprint",
            "Retrospektywa",
            "Demo dla klienta",
        ]

        now = datetime.now().replace(
            minute=0,
            second=0,
            microsecond=0,
        )

        for _ in range(20):
            room = random.choice(rooms)
            user = random.choice(users)

            start = now + timedelta(
                days=random.randint(0, 14),
                hours=random.randint(9, 16) - now.hour,
            )

            end = start + timedelta(hours=random.choice([1, 2, 3]))

            if room.is_available(start, end):
                db.session.add(
                    Booking(
                        room=room,
                        user=user,
                        title=random.choice(titles),
                        start_time=start,
                        end_time=end,
                        attendees_count=random.randint(
                            2,
                            room.capacity,
                        ),
                    ))

        db.session.commit()
        print("Seed zakończony.")
        print("Users:", User.query.count())
        print("Rooms:", Room.query.count())
        print("Bookings:", Booking.query.count())
        print("Equipment:", Equipment.query.count())
