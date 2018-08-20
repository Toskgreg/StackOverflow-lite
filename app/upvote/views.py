"""This module handle the registering of the UPVOTE_APP blue_print and
 adding the adds the url rule"""
from flask import Blueprint
from app.upvote.api import Up
UPVOTE_APP = Blueprint('UPVOTE_APP', __name__)

UPVOTE_VIEW = Up.as_view('upvote_api')
UPVOTE_APP.add_url_rule('/api/v1/questions/<question_id>/<answer_id>/upvote',
                        view_func=UPVOTE_VIEW, methods=['POST', ])