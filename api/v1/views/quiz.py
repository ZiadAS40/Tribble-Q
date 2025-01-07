#!usr/bin/env python3

from flask import request, jsonify

from flask_login import current_user
from api.v1.views import api_v1


@api_v1.route('/quiz/<quiz_id>', methods=['GET'], strict_slashes=False)
def get_quiz(quiz_id):
    """Get a quiz"""
    from app.models.question import Question
    list_of_questions = []
    questions = Question.query.filter_by(quiz_id=quiz_id).all()

    for question in questions:
        qu = {"tittle":question.question, "answers":question.answer.split(","), "id":question.id}
        list_of_questions.append(qu)
    
    return jsonify(list_of_questions), 200

@api_v1.route('/quiz/<quiz_id>/submit', methods=['POST'], strict_slashes=False)
def submit_quiz(quiz_id):
    """Submit a quiz"""
    from app.models.question import Question
    from app.models.quiz import Quiz
    user_answers = request.json()
    quiz = Quiz.query.filter_by(id=quiz_id).first()
    score = 0
    for question_id, answer in user_answers.items():
        question = Question.query.filter_by(id=question_id).first()
        if question.is_right(answer):
            score += 1
    # update the user's quiz results
    current_user.quiz_results[quiz_id] = f"{score}/{len(quiz.questions)}"

    return jsonify({len(quiz.questions): score})
