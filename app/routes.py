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

@app.route('/quiz/<string:quiz_id>')
def quiz(quiz_id):
    if current_user.is_anonymous:
        return render_template('login.html')
    return render_template('quiz.html', quiz_id=quiz_id, user_id=current_user.id)

@app.route('/quiz/english')
def en():
    from app.models.quiz import Quiz
    from app.models.user import User
    quizzes_en = []
    quizzes = Quiz.query.filter_by(cate="en").all()

    for quiz in quizzes:
        q = {}
        success_threshold = 0.5
        q["title"] = quiz.title
        all_users = User.query.all()
        all_users_with_quiz = [
            user for user in all_users
            if user.quiz_results is not None and str(quiz.id) in user.quiz_results
        ]
        acc = 0
        acc_l = 0
        for user in all_users_with_quiz:
            if user.quiz_results is not None:
                results = user.quiz_results
        
                acc += int(results.split(":")[1].split("/")[0])
                acc_l += int(results.split(":")[1].split("/")[1])

                
        q["avg_score"] = round((acc / acc_l * 100 if acc_l > 0 else 0), 1)


        suc_users = [
            user for user in all_users_with_quiz
            if user.quiz_results and len(user.quiz_results.split(":")) > 1
            for quiz_result in user.quiz_results.split(",")
            if len(quiz_result.split(":")) > 1
            for result in [quiz_result.split(":")[1]]
            if len(result.split("/")) == 2
            for u, a in [(int(result.split("/")[0]), int(result.split("/")[1]))]
            if u / a > success_threshold
        ]

        q["suc_users"] = len(suc_users)
        q["users_with_quiz"] = len(all_users_with_quiz)
        q["success_rate"] = round((len(suc_users) / len(all_users_with_quiz) * 100 if len(all_users_with_quiz) > 0 else 0), 1)
        q["time"] = quiz.time
        q["id"] = quiz.id
        q["cate"] = quiz.cate
        q["num_of_questions"] = len(quiz.questions)

        quizzes_en.append(q)

    if current_user.is_anonymous:
        return render_template('login.html')

    return render_template('english.html', quizzes=quizzes_en)

from .auth import auth
from api.v1.views import api_v1

app.register_blueprint(auth, url_prefix='/')
app.register_blueprint(api_v1, url_prefix='/api/v1')