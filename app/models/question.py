#!usr/bin/env python3

from app.models import db

class Question(db.EmbeddedDocument):
    """Question class"""
    question = db.StringField(required=True)
    options = db.ListField(db.StringField(), required=True)
    answer = db.StringField(required=True)
    number = db.IntField(required=True)
    category = db.StringField(required=True)
    meta = {
        'indexes': [
            'question',
        ]
    }

