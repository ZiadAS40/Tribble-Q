#!/usr/bin/env python3
"""User model module"""

from flask_login import UserMixin
from .basemodel import BaseModel
from werkzeug.security import generate_password_hash, check_password_hash
from app.routes import db



class User(UserMixin, BaseModel,db.Model):
    __tablename__ = 'users'

    username = db.Column(db.String(40), nullable=False, unique=True)
    email = db.Column(db.String(40), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    quiz_results = db.Column(db.String(255), nullable=True)
    role = db.Column(db.String(40), nullable=False, default='student')
    active = db.Column(db.Boolean(), default=True)


    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        self.set_password(kwargs['password'])

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def set_password(self, password):
        self.password = generate_password_hash(password)
