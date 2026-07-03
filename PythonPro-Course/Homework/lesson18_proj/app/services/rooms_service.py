from ..db import db
import re

from ..models import Room


def create_room_vadilator(name, capacity, floor, description, is_active,
                          hourly_rate):
    if hourly_rate < 1:
        raise ValueError("Hourly rate must be positive")
    if Room.query.filter(name == name.title()):
        raise ValueError(f"Name {name} is already used.")


def create_room(name, capacity, floor, description, is_active, hourly_rate):
    create_room_vadilator(name, capacity, floor, description, is_active,
                          hourly_rate)
    room = Room(name=name.title(),
                capacity=capacity,
                floor=floor,
                description=description,
                is_active=is_active,
                hourly_rate=hourly_rate)
    db.session.add(room)
    db.session.commit()


def get_rooms_all():
    return Room.query.all()


def get_room_by_id(id: int):
    return Room.query.get(id)
