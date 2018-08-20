from flask import Blueprint
from app.question.api import QUESTIONAPI

QUESTION_APP = Blueprint('QUESTION_APP', __name__)

QUESTION_VIEW = QUESTIONAPI.as_view('question_api')
QUESTION_APP.add_url_rule('/api/v1/questions/', defaults={'question_id': None},
                      view_func=QUESTION_VIEW, methods=['GET', ])

QUESTION_APP.add_url_rule('/api/v1/questions/<question_id>', view_func=QUESTION_VIEW,
                      methods=['GET', ])