# #!/usr/bin/env python3

# from config import DevelopmentConfig, ProductionConfig
# import os
# from flask import Blueprint, Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_cors import CORS
# import os

# # db = SQLAlchemy()

# def create_app(config_class=DevelopmentConfig):
#     """
#     Create and configure the Flask application.
#     """
#     app = Flask(__name__, template_folder='app/templates', static_folder='app/static')
#     app.config.from_object(config_class)

#     from app.routes import routes_bp
#     from app.auth import auth

#     app.register_blueprint(routes_bp)
#     app.register_blueprint(auth)

#     return app



# env = os.environ.get('FLASK_ENV', 'development')
# if env == 'production':
#     app = create_app(ProductionConfig)
# else:
#     app = create_app(DevelopmentConfig)

# db = SQLAlchemy(app)
from app.routes import app
if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)