import logging
from flask import Blueprint
from flask_restful import Api

from com_blacktensor.resources.stock_crow import Stock
from com_blackTensor.resources.covid_status import CovidStatus
# from com_blackTensor.resources.frequency_naver_news import FrequencyNaverNews


# from com_blacktensor.resources.user import User, Users, Auth, Access
# from com_blacktensor.resources.crow import Article, Articles

home = Blueprint('home', __name__, url_prefix='/api')
covid = Blueprint('covidStatus', __name__, url_prefix='/api/covid')
# frequency = Blueprint('frequencyNaverNews', __name__, url_prefix='/api/frequency')

api = Api(covid)
# api = Api(frequency)

def initialize_routes(api):
    api.add_resource(Stock, '/api/stock')
    api.add_resource(CovidStatus, '/api/covid')
    # api.add_resource(FrequencyNaverNews, '/api/frequency')

@covid.errorhandler(500)
def user_api_error(e):
    logging.exception('An error occurred during covid request. %s' % str(e))
    return 'An internal error occurred.', 500