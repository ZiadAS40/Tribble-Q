#!usr/bin/env python3

from flask import request, jsonify
from app.models.quiz import Quiz
from api.v1.views import api_v1

@api_v1.route('/quiz/<quiz_id>', methods=['GET'], strict_slashes=False)
def get_quiz(quiz_id):
    """Get a quiz"""
    quiz = Quiz.objects.get_or_404(id=quiz_id)
    return jsonify(quiz.to_json())