import logging
from flask import Blueprint
from flask_restful import Api

from com_blacktensor.cop.emo.resource.emotion import Emotion
from com_blacktensor.cop.fin.resource.finance import Finance
from com_blacktensor.cop.sto.resource.stock import Stock
# from com_blacktensor.resources.craw_emotion import Craw
# from com_blackTensor.resources.covid_status import CovidStatus
# from com_blackTensor.resources.frequency_naver_news import FrequencyNaverNews


# from com_blacktensor.resources.user import User, Users, Auth, Access
# from com_blacktensor.resources.crow import Article, Articles
stock = Blueprint('stock', __name__, url_prefix='/api/stock')
finance = Blueprint('finance', __name__, url_prefix='/api/finance')
emotion = Blueprint('emotion', __name__, url_prefix='/api/emotion')
# covid = Blueprint('covidStatus', __name__, url_prefix='/api/covid')
# frequency = Blueprint('frequencyNaverNews', __name__, url_prefix='/api/frequency')

api = Api(emotion)
# api = Api(frequency)

def initialize_routes(api):
    api.add_resource(Stock, '/api/stock')
    api.add_resource(Finance, '/api/finance')
    api.add_resource(Emotion, '/api/emotion')


@stock.errorhandler(500)
def stock_api_error(e):
    logging.exception('An error occurred during emotion request. %s' % str(e))
    return 'An internal error occurred.', 500

@finance.errorhandler(500)
def finance_api_error(e):
    logging.exception('An error occurred during emotion request. %s' % str(e))
    return 'An internal error occurred.', 500

@emotion.errorhandler(500)
def emotion_api_error(e):
    logging.exception('An error occurred during emotion request. %s' % str(e))
    return 'An internal error occurred.', 500