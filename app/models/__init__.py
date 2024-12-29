#!usr/bin/env python3

from run import app
from flask_mongoengine import MongoEngine

db = MongoEngine(app)