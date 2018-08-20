'''This module instanciates a flask object and creates the app'''
from flask import Flask, jsonify
from config import configuration

app = Flask(__name__)


def create_app(configuration_name):
    '''creates the app and registers Blue prints'''
    app.config.from_object(configuration[configuration_name])
    from app.question.views import QUESTION_APP







    
    # register_blueprint
    app.register_blueprint(QUESTION_APP)




    return app