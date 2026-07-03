from flask import Blueprint, render_template, jsonify
from app.services import dashboard_service as ds
dashboard_bp = Blueprint('dashboard', __name__)
@dashboard_bp.route('/dashboard')
def dashboard():
    stats, upcoming, top_users, room_utilization = ds.get_dashboard_summary()
    return render_template(
        'dashboard.html',
        stats=stats,
        upcoming=upcoming,
        top_users=top_users,
        room_utilization=room_utilization
    )
@dashboard_bp.route('/api/dashboard/stats')
def api_stats():
    return jsonify(ds.get_dashboard_api_stats())
