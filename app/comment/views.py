"""This module handle the registering of the COMMENT_APP blue_print and
 adding the adds the url rule"""
from flask import Blueprint
from app.comment.api import COMMENTAPI
COMMENT_APP = Blueprint('COMMENT_APP', __name__)

COMMENT_VIEW = COMMENTAPI.as_view('comment_api')
COMMENT_APP.add_url_rule('/api/v1/questions/<question_id>/<answer_id>/comment',
                         view_func=COMMENT_VIEW, methods=['POST', ])