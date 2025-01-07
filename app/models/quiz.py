#!usr/bin/env python3

from app.models.question import Question
from app.models.user import User
from .basemodel import BaseModel
from app.routes import db

class Quiz(BaseModel, db.Model):
    __tablename__ = 'quizzes'

    title = db.Column(db.String(40), nullable=False, unique=True)
    instructions = db.Column(db.String(255), nullable=False)
    time = db.Column(db.Integer(), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    questions = db.relationship('Question', backref='quiz', cascade='all, delete-orphan')
    quiz_owner_id = db.Column(db.String(60), db.ForeignKey('users.id'))
