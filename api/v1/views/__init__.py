#!/usr/bin/env python3
from flask import Blueprint

api_v1 = Blueprint('api_v1', __name__)

from api.v1.views.quiz import *