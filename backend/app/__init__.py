from flask import Flask
from flask_cors import CORS
from app.db import db
from app.routes.job_routes import job_bp
from app.routes.auth_routes import auth_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')  # Charge la config
    CORS(app)

    db.init_app(app)
    app.register_blueprint(job_bp)
    app.register_blueprint(auth_bp)

    return app
