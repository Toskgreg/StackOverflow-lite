import uuid
from flask.views import MethodView
from flask import jsonify, request, abort, make_response
from app.models import *


class AnswerAPI(MethodView):
    """This class-based view for answering a question."""

    def get(self, question_id, answer_id):
        """Method for  get answers"""
        for question in QUESTIONS:
            if question['Id'] == question_id:
                if answer_id:
                    answer_id = uuid.UUID(answer_id)
                    answers = Answer.view_all_answers()
                    for answer in ANSWERS:
                        if answer_id == answer['Id']:
                            return jsonify(answer), 200
                    return jsonify({'msg': "Answer not found "}), 404
                else:
                    answers = Question.view_all_questions()
                    if ANSWERS == []:
                        response = {
                            "msg": " There are no answers at the moment"}
                        return make_response(jsonify(response)), 200
                    return jsonify(answers), 200

    def post(self, question_id):
        '''Method for a post answer'''
        question_id = uuid.UUID(question_id)
        data = request.json
        text = data["text"]
        res = Answer.answer_question(question_id, text)
        if res == "You have successfully answered the question.":
            return jsonify({'msg': res}), 201
        return jsonify({'msg': res}), 409