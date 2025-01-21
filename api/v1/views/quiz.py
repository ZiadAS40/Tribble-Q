#!usr/bin/env python3

from flask import request, jsonify, redirect, url_for

from flask_login import current_user
from api.v1.views import api_v1
import json


@api_v1.route('/quiz/<string:quiz_id>', methods=['GET'], strict_slashes=False)
def get_quiz(quiz_id):
    """Get a quiz"""
    from app.models.question import Question
    list_of_questions = []
    questions = Question.query.filter_by(quiz_id=quiz_id).all()

    for question in questions:
        qu = {"tittle":question.question, "answers":question.options.split(","), "id":question.id}
        list_of_questions.append(qu)
    
    return jsonify(list_of_questions), 200

@api_v1.route('/quiz/<quiz_id>/submit', methods=['POST'], strict_slashes=False)
def submit_quiz(quiz_id):
    """Submit a quiz"""
    from app.models.question import Question
    from app.models.quiz import Quiz
    user_answers = request.headers.get('answers')
    quiz = Quiz.query.filter_by(id=quiz_id).first()
    score = 0
    for question_id, answer in json.loads(user_answers).items():
        question = Question.query.filter_by(id=question_id).first()
        if question.is_right(answer):
            score += 1


    if current_user.is_authenticated:
        from app.models.user import User
        from app.models.quiz_result import QuizResult
        user = User.query.filter_by(id=current_user.id).first()
        user_quiz = QuizResult.query.filter_by(user_id=user.id, quiz_id=quiz.id).first()
        if user_quiz:
            return jsonify({"error": "You already toke this Quiz"}), 400
        quiz_result = QuizResult(user_id=user.id, quiz_id=quiz.id, score=score)
        quiz_result.save()


    return jsonify({len(quiz.questions): score})
