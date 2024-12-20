#!/usr/bin/env python3
from flask import Flask

def create_app():
    app = Flask(__name__)

    # Configuration settings can be added here
    app.config.from_mapping(
        SECRET_KEY='your_secret_key',
        DATABASE='your_database_path'
    )

    # Register blueprints and routes 
    from .routes import routes_bp
    from api.v1.views import api_v1
    app.register_blueprint(routes_bp)
    app.register_blueprint(api_v1)

    return app