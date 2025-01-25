#!/usr/bin/env python3

import unittest

from app.routes import db, app

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        """Set up test environment"""
        self.app = app  # Ensure you have a testing config
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        """Tear down test environment"""
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
