from datetime import datetime, timezone
from .base import Base, db
class Notification(Base):
    __tablename__ = "notifications"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    message = db.Column(db.Text, nullable=False)
    is_read = db.Column(db.Boolean, default=False, nullable=False)
    created_at = db.Column(
        db.DateTime,
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )
    user = db.relationship("User", backref=db.backref("notifications", lazy="dynamic"))
    def __repr__(self):
        return f"<Notification user_id={self.user_id} read={self.is_read}>"