from datetime import datetime
from decimal import Decimal
from ..db import db
class Base(db.Model):
    __abstract__ = True
    def to_dict(self, exclude=None):
        exclude = exclude or set()
        data = {}
        for col in self.__table__.columns:
            if col.name in exclude:
                continue
            value = getattr(self, col.name)
            if isinstance(value, datetime):
                value = value.isoformat()
            elif isinstance(value, Decimal):
                value = float(value)
            data[col.name] = value
        return data
