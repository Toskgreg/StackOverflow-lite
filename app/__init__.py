'''This module instanciates a flask object and creates the app'''
from flask import Flask, jsonify
from config import configuration

app = Flask(__name__)


def create_app(configuration_name):
    '''creates the app and registers Blue prints'''
    app.config.from_object(configuration[configuration_name])
    from app.question.views import QUESTION_APP
    from app.answer.views import ANSWER_APP
    from app.comment.views import COMMENT_APP
    from app.upvote.views import UPVOTE_APP
    from app.downvote.views import DOWNVOTE_APP
   
    # register_blueprint
    app.register_blueprint(QUESTION_APP)
    app.register_blueprint(ANSWER_APP)
    app.register_blueprint(COMMENT_APP)
    app.register_blueprint(DOWNVOTE_APP)
    app.register_blueprint(UPVOTE_APP)





    return app