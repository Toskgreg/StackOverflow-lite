"""This module handles the class RequestApi and its post method"""
import uuid
from flask.views import MethodView
from flask import jsonify, request, abort, make_response
from app.models import *


class COMMENTAPI(MethodView):
    """This class-based view for requesting a ride."""

    def post(self, question_id, answer_id):
        '''Method for a post request'''
        question_id = uuid.UUID(question_id)
        answer_id = uuid.UUID(answer_id)
        data = request.json
        text1 = data["text1"]
        res = Comment.comment_on_answer(question_id, answer_id, text1)
        if res == "You have successfully commented on the answer.":
            return jsonify({'msg': res}), 201
        return jsonify({'msg': res}), 409
