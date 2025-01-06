# #!/usr/bin/env python3

# import os
# from datetime import timedelta
# import secrets
# from flask_sqlalchemy import SQLAlchemy


# class Config:
#     """Base configuration."""
#     HOST = 'localhost'
#     PORT = 5000
#     SECRET_KEY = os.environ.get('SECRET_KEY', secrets.token_hex(16))
#     JSONIFY_PRETTYPRINT_REGULAR = True
#     JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
#     JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)
#     SQLALCHEMY_DATABASE_URI = 'sqlite:///tripple_q.db'
#     SQLALCHEMY_DATABASE_URI = 'mysql://ziad4036:ltstore@localhost/tripple_q'

# class DevelopmentConfig(Config):
#     """Development configuration."""
#     DEBUG = True

# class ProductionConfig(Config):
#     """Production configuration."""
#     DEBUG = False
