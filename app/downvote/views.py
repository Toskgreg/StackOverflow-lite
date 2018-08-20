"""This module handle the registering of the REQUES_APP blue_print and
 adding the adds the url rule"""
from flask import Blueprint
from app.downvote.api import DOWNVOTEAPI
DOWNVOTE_APP = Blueprint('DOWNVOTE_APP', __name__)

DOWNVOTE_VIEW = DOWNVOTEAPI.as_view('downvote_api')
DOWNVOTE_APP.add_url_rule(
    '/api/v1/questions/<question_id>/<answer_id>/downvote',
    view_func=DOWNVOTE_VIEW,
    methods=[
        'POST',
    ])