#!/usr/bin/env python3

from tests.base import BaseTestCase
from app.models.quiz import Quiz

class TestQuizModel(BaseTestCase):
    def test_quiz_creation(self):
        """Test quiz creation"""
        quiz = Quiz(title='Sample Quiz', instructions='Follow the instructions', time=30, description='A sample quiz', cate='General')
        self.assertEqual(quiz.title, 'Sample Quiz')
        self.assertEqual(quiz.time, 30)
