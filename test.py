import unittest
import uuid
from flask import json
from test_data import*
from app import create_app
from app.models import *


class TestBase(unittest.TestCase):
    """ Base class for all test classes """
    app = create_app('TESTING')
    app.app_context().push()
    client = app.test_client()


class TestQuestion(TestBase):
    """ Defines tests for the view methods of for questions """

    def setUp(self):
        pass

    def test_question_creation(self):
        """Test API can create a question (POST request)"""
        response = self.client.post('api/v1/questions/',
                                    content_type='application/json',
                                    data=json.dumps(post_question1))

        self.assertEqual(response.status_code, 201)
        

    def test_api_can_view_all_questions(self):
        """Test QUESTIONAPI can view all (GET request)."""
        response = self.client.post('api/v1/questions/',
                                    content_type='application/json',
                                    data=json.dumps(post_question1))

        self.assertEqual(response.status_code, 201)
        response = self.client.get('api/v1/questions/')
        self.assertEqual(response.status_code, 200)
        self.assertIn("title", str(response.data))

    def test_api_can_get_question_by_id(self):
        """Test API can fetch a single question by using it's id."""
        # post data
        response = self.client.post('api/v1/questions/',
                                    content_type='application/json',
                                    data=json.dumps(post_question1))
        self.assertEqual(response.status_code, 201)
        response = self.client.get('api/v1/questions/')
        self.assertEqual(response.status_code, 200)

        results = json.loads(response.data.decode())
        for question in results:
            result = self.client.get(
                'api/v1/questions/{}'.format(question['Id']))
            self.assertEqual(result.status_code, 200)
            self.assertIn(question['Id'], str(result.data))

    def test_api_can_answer_question_with_id(self):
        """Test API can fetch a single question by using it's id."""
        # post data
        response = self.client.post('api/v1/questions/',
                                    content_type='application/json',
                                    data=json.dumps(post_question1))

        self.assertEqual(response.status_code, 201)
        response = self.client.get('api/v1/questions/')
        self.assertEqual(response.status_code, 200)

        results = json.loads(response.data.decode())

        for question in results:
            response = self.client.post('api/v1/questions/{}/answer/'
                                        .format(question['Id']),
                                        content_type='application/json',
                                        data=json.dumps(post_answer))
            self.assertEqual(response.status_code, 201)
            self.assertIn(
                "You have successfully answered the question.",
                str(response.data))


if __name__ == '__main__':
    unittest.main()
