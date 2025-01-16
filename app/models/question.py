#!usr/bin/env python3

from app.routes import db
import uuid
from .basemodel import BaseModel


class Question(BaseModel, db.Model):
    """Question class"""
    __tablename__ = 'questions'

    question = db.Column(db.String(255), nullable=False)
    options = db.Column(db.String(1024), nullable=False)
    answer = db.Column(db.String(255), nullable=False)
    number = db.Column(db.Integer(), nullable=False)
    category = db.Column(db.String(40), nullable=False)
    quiz_id = db.Column(db.String(255), db.ForeignKey('quizzes.id'))

    def is_right(self, answer):
        """Check if the answer is correct"""
        return self.answer == answer
