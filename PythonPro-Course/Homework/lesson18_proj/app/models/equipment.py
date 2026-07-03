from .base import db, Base


class Equipment(Base):
    """Model wyposażenia sali (projektor, tablica, wideokonferencja itp.)."""
    __tablename__ = 'equipment'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    icon = db.Column(db.String(50))  # np. "projector", "whiteboard"

    def __repr__(self):
        return f'<Equipment {self.name}>'
