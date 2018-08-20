"""This module contains classes Question,Answer,Upvote,Downvote,comments and their methods"""
import uuid
import collections
from datetime import datetime as dt
from flask import jsonify, request, abort, make_response
QUESTIONS = []



class Question(object):
    ''' A Questions class'''

    def __init__(
            self,
            question_id,
            question_title,
            date_created,
            date_modified,
            question_description,
            answers):
        ''' Initializes the question object'''
        self.question_id = question_id
        self.question_title = question_title
        self.date_created = dt.utcnow()
        self.date_modified = dt.utcnow()
        self.question_description = question_description
        self.answers = ANSWERS

    @classmethod
    def question_already_exists(cls, question_title, question_description):
        """A method to check if the same question already exists """
        for question in QUESTIONS:
            if question['question_title'] == question_title and question['question_description'] == \
                    question_description:
                return True
        return False

    @classmethod
    def view_all_questions(cls):
        """ Return all the questions asked on the forum."""
        return QUESTIONS
