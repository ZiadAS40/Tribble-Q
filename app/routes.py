#!/usr/bin/env python3

from flask import Blueprint
from flask import render_template

routes_bp = Blueprint('routes', __name__)


@routes_bp.route('/')
def home():
    return render_template('home.html')
