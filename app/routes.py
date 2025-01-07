#!/usr/bin/env python3

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user
from datetime import timedelta
from flask_cors import CORS
from flask import render_template
import os
import secrets




app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://ziad4036:ltstore@localhost/tripple_q'
app.config['SECRET_KEY'] =  os.environ.get('SECRET_KEY', secrets.token_hex(16))
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(days=30)
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}}, supports_credentials=True)

db = SQLAlchemy()
db.init_app(app)

login_manager = LoginManager(app)


@login_manager.user_loader
def load_user(user_id):
    """implement the session manager"""
    from .models.user import User
    return User.query.filter_by(id=user_id).first()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/categories')
def cate():
    return render_template('cate.html')

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

@app.route('/quiz/english')
def en():
    from app.models.quiz import Quiz
    if current_user.is_anonymous:
        return render_template('login.html')
    quiz = Quiz.query.filter_by().first()
    return render_template('english.html', quiz_id=quiz.id, user_id=current_user.id)

from .auth import auth
from api.v1.views import api_v1

app.register_blueprint(auth, url_prefix='/')
app.register_blueprint(api_v1, url_prefix='/api/v1')