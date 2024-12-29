#!/usr/bin/env python3

from config import DevelopmentConfig, TestingConfig, ProductionConfig
import os
from flask import Blueprint, Flask
from flask_cors import CORS
import os
from config import DevelopmentConfig, TestingConfig, ProductionConfig



def create_app(config_class=DevelopmentConfig):
    """
    Create and configure the Flask application.
    """
    app = Flask(__name__, template_folder='app/templates', static_folder='app/static')
    app.config.from_object(config_class)

    from api.v1.views import api_v1
    from app.routes import routes_bp

    app.register_blueprint(routes_bp)
    app.register_blueprint(api_v1)

    return app


env = os.environ.get('FLASK_ENV', 'development')
if env == 'production':
    app = create_app(ProductionConfig)
elif env == 'testing':
    app = create_app(TestingConfig)
else:
    app = create_app(DevelopmentConfig)

if __name__ == "__main__":
    app.run()