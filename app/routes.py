from flask import Blueprint
from flask import render_template

# Create a Blueprint for the routes
routes_bp = Blueprint('routes', __name__)

# Define a basic route
@routes_bp.route('/')
def home():
    return render_template('home.html')
