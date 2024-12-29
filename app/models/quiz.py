#!usr/bin/env python3

from app.models import db

class Quiz(db.Document):
    """Quiz class"""
    title = db.StringField(required=True, unique=True)
    instructions = db.ListField(db.StringField(), required=True)
    time = db.IntField(required=True)
    description = db.StringField(required=True)
    questions = db.ListField(db.EmbeddedDocumentField('Question'))
    queiz_owner = db.ReferenceField('User')
