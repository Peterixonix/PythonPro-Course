from .booking import bookings_bp
from .rooms import rooms_bp
from .dashboard import dashboard_bp
from .equipment import equipment_bp
from .debug import debug_bp
from .notifications import notifications_bp
from .reports import reports_bp
BLUEPRINTS = [
    bookings_bp,
    rooms_bp,
    dashboard_bp,
    equipment_bp,
    debug_bp,
    notifications_bp,
    reports_bp,]