#!/usr/bin/env python3

from tests.base import BaseTestCase
from app.models.user import User
from app.routes import db


class TestUserModel(BaseTestCase):
    def test_user_creation(self):
        """Test user creation"""
        user = User(username='testuser', email='test@example.com', password='password123')
        self.assertEqual(user.username, 'testuser')
        self.assertTrue(user.check_password('password123'))

    def test_user_email_unique(self):
        """Test that user email is unique"""
        user1 = User(username='user1', email='unique@example.com', password='password123')
        user2 = User(username='user2', email='unique@example.com', password='password123')
        db.session.add(user1)
        db.session.commit()
        db.session.add(user2)
        with self.assertRaises(Exception):
            db.session.commit()
