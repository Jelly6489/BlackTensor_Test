import logging
from flask import Blueprint
from flask_restful import Api

from com_blacktensor.cop.emo.resource.emotion import Emotion
# from com_blacktensor.resources.craw_emotion import Craw
# from com_blackTensor.resources.covid_status import CovidStatus
# from com_blackTensor.resources.frequency_naver_news import FrequencyNaverNews


# from com_blacktensor.resources.user import User, Users, Auth, Access
# from com_blacktensor.resources.crow import Article, Articles

emotion = Blueprint('emotion', __name__, url_prefix='/api/emotion')
# covid = Blueprint('covidStatus', __name__, url_prefix='/api/covid')
# frequency = Blueprint('frequencyNaverNews', __name__, url_prefix='/api/frequency')

api = Api(emotion)
# api = Api(frequency)

def initialize_routes(api):
    api.add_resource(Emotion, '/api/emotion')
    # api.add_resource(CovidStatus, '/api/covid')
    # api.add_resource(FrequencyNaverNews, '/api/frequency')

@emotion.errorhandler(500)
def user_api_error(e):
    logging.exception('An error occurred during emotion request. %s' % str(e))
    return 'An internal error occurred.', 500