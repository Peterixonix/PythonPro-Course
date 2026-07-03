from .base import db

room_equipment = db.Table('room_equipment',
                          db.Column('room_id', db.Integer, db.ForeignKey('rooms.id'), primary_key=True),
                          db.Column('equipment_id', db.Integer, db.ForeignKey('equipment.id'), primary_key=True))