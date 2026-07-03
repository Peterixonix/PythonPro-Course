from flask import Flask, jsonify
from sqlalchemy import event, text
from .db import db
from .routes import BLUEPRINTS
from .models import Room, Booking, Equipment, User
from .routes.debug import QueryStats
from config import Config
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    for bp in BLUEPRINTS:
        app.register_blueprint(bp)
    with app.app_context():
        @event.listens_for(db.engine, "before_cursor_execute")
        def count_queries(conn, cursor, statement, parameters, context, executemany):
            QueryStats.query_count += 1
        @app.route("/test-db")
        def test_db():
            try:
                db.session.execute(text("SELECT 1"))
                return jsonify({"message": "Połączenie OK!"})
            except Exception as e:
                return jsonify({
                    "message": "Błąd połączenia z bazą",
                    "error": str(e)
                }), 500
        db.create_all()
    return app
