"""This module handle the registering of the ANSWER_APP blue_print and
 adding the adds the url rule"""
from flask import Blueprint
from app.answer.api import AnswerAPI
ANSWER_APP = Blueprint('ANSWER_APP', __name__)

ANSWER_VIEW = AnswerAPI.as_view('answer_api')
ANSWER_APP.add_url_rule('/api/v1/questions/<question_id>/answer/',
                         view_func=ANSWER_VIEW, methods=['POST', ])