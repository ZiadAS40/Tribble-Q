#!/usr/bin/env python3
"""User model module"""

from flask_login import UserMixin
from mongoengine import Document, StringField, EmailField, BooleanField
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import db


class User(db.Document, UserMixin):
    """User class"""
    username = StringField(required=True, uinque=True)
    email = EmailField(required=True, unique=True)
    password = StringField(required=True, min_length=6, max_length=100)
    role = StringField(required=True, choices=['instructor', 'student'])
    active = BooleanField(default=True)
    
    def set_password(self, password):
        """Set password"""
        self.password = generate_password_hash(password)

    def check_password(self, password):
        """Check password"""
        return check_password_hash(self.password, password)

    def __init__(self, username, email, password, role, active=True):
        """Constructor"""
        self.username = username
        self.email = email
        self.set_password(password)
        self.role = role
        self.active = active
