#!/usr/bin/env python3

import os
from datetime import timedelta
import secrets

class Config:
    """Base configuration."""
    HOST = 'localhost'
    PORT = 5000
    SECRET_KEY = os.environ.get('SECRET_KEY', secrets.token_hex(16))
    JSONIFY_PRETTYPRINT_REGULAR = True
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)
    MONGODB_SETTINGS = {
        'db': 'quiz_app_db',
        'host': 'localhost',
        'port': 27017
    }

class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True

class TestingConfig(Config):
    """Testing configuration."""
    TESTING = True
    MONGODB_SETTINGS = {
        'db': 'quiz_app_test_db',
        'host': 'localhost',
        'port': 27017
    }

class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False
