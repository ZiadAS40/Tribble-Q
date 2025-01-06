#!usr/bin/env python3

from flask import request, jsonify
from app.models.quiz import Quiz
from flask_login import current_user
from api.v1.views import api_v1


@api_v1.route('/quiz/<quiz_id>', methods=['GET'], strict_slashes=False)
def get_quiz(quiz_id):
    """Get a quiz"""
    quiz = Quiz.query.filter_by(id=quiz_id).first()
    return jsonify(quiz.to_json())

@api_v1.route('/quiz/<quiz_id>/submit', methods=['POST'], strict_slashes=False)
def submit_quiz(quiz_id):
    """Submit a quiz"""
    user_answers = request.json()
    # get the quiz and calculate the score
    quiz = Quiz.query.filter_by(id=quiz_id).first()
    score = quiz.calculate_score(user_answers)
    # update the user's quiz results
    current_user.quiz_results[quiz_id] = quiz.score

    return jsonify({len(quiz.questions): score})
