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
        
    @classmethod
    def ask_question(cls, question_title, question_description):
        """A method for asking a question"""
        cls.data = {}
        cls.data = collections.OrderedDict()
        if cls.question_already_exists(question_title, question_description):
            return "question already exists"
        else:
            cls.data['Id'] = uuid.uuid1()
            cls.data['date_created'] = dt.utcnow()
            cls.data['date_modified'] = dt.utcnow()
            cls.data['question_title'] = question_title
            cls.data['question_description'] = question_description
            cls.data['answers'] = ANSWERS

            QUESTIONS.append(cls.data)
            return "Your question has been successfully asked."