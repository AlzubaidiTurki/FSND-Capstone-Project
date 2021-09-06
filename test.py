import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
import math
from app import app
from models import setup_db, Servant, Master


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = app
        self.client = self.app.test_client
        self.DB_HOST = os.getenv('DB_HOST', '127.0.0.1:5432')  
        self.DB_USER = os.getenv('DB_USER', 'postgres')  
        self.DB_PASSWORD = os.getenv('DB_PASSWORD', 'postgres')  
        self.DB_NAME = os.getenv('DB_NAME', 'fate')  
        self.DB_PATH = 'postgresql://{}:{}@{}/{}'.format(self.DB_USER, self.DB_PASSWORD, self.DB_HOST, self.DB_NAME)
        setup_db(self.app)

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()
    
    def tearDown(self):
        pass

    def test_valid_get_index(self):
        res = self.client().get('/')
        self.assertEqual(res.status_code, 200)
        # Since all other endpoints require premessions, please refer to the postman workspace.

if __name__ == "__main__":
    unittest.main()