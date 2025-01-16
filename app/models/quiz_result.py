#!/usr/bin/env python
from app.routes import db
from .basemodel import BaseModel


class QuizResult(BaseModel, db.Model):
    __tablename__ = 'quiz_results'

    user_id = db.Column(db.String(60), db.ForeignKey('users.id'))
    quiz_id = db.Column(db.String(60), db.ForeignKey('quizzes.id'))
    
    score = db.Column(db.Integer(), nullable=False)

    user = db.relationship('User', back_populates='quiz_results')

