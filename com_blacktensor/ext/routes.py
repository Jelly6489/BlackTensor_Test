import logging
from flask import Blueprint
from flask_restful import Api

from com_blacktensor.cop.emo.resource.emotion import Emotion, StockNews
from com_blacktensor.cop.fin.resource.finance import Finance
from com_blacktensor.cop.sto.resource.stock import Stock
from com_blacktensor.cop.exc.resource.exchange import Exchange
from com_blacktensor.usr.resource.user import User, Users
from com_blacktensor.usr.resource.review import Review, Reviews
from com_blacktensor.usr.resource.login import Login

# from com_blacktensor.cop.emo.model.emotion_kdd import keyword
# =============================================================================================
# ===================================== kain code =============================================
# =============================================================================================
from com_blacktensor.cop.cov.status.resources.status import CovidStatus
from com_blacktensor.cop.cov.board.resources.covid_board import CovidBoard
from com_blacktensor.cop.cov.board.resources.covid_board import CovidBoard
from com_blacktensor.cop.news.covid.resources.covid_news import CovideNews
from com_blacktensor.cop.news.economy.resources.economy_news import EconomyNews
from com_blacktensor.cop.cov.status.resources.status_arr import CovidStatusToArray

covid = Blueprint('covidStatus', __name__, url_prefix='/api/status/covid')
board = Blueprint('covidBoard', __name__, url_prefix='/api/board/covid')
covid_arr = Blueprint('CovidStatusToArray', __name__, url_prefix='/api/status/arr/covid')
covid_news = Blueprint('FrequencyNaverNews', __name__, url_prefix='/api/news/covid')
economy_news = Blueprint('FrequencyNaverNews', __name__, url_prefix='/api/news/economy')
# =============================================================================================
# =============================================================================================
# =============================================================================================

stock = Blueprint("stock", __name__, url_prefix='/api/stock/stock')
finance = Blueprint('finance', __name__, url_prefix='/api/stock/finance')
emotion = Blueprint('emotion', __name__, url_prefix='/api/stock/emotion')
stock_news = Blueprint('stock_news', __name__, url_prefix='/api/stock/mainNews')
exchange = Blueprint('exchange', __name__, url_prefix='/api/stock/exchange')
user = Blueprint('user', __name__, url_prefix='/api/access')
login = Blueprint('user', __name__, url_prefix='/api/login')
review = Blueprint('review', __name__, url_prefix='/api/mypage')
# =============================================================================================
# ===================================== kain code =============================================
# =============================================================================================
api = Api(covid)
api = Api(covid_news)
api = Api(board)
api = Api(economy_news)
api = Api(covid_arr)
# =============================================================================================
# =============================================================================================
# =============================================================================================
api = Api(stock)
api = Api(finance)
api = Api(emotion)
api = Api(stock_news)
api = Api(exchange)
api = Api(user)
api = Api(login)
api = Api(review)

def initialize_routes(api):
    api.add_resource(Stock, f'/api/stock/stock/<keyword>')
    api.add_resource(Finance, f'/api/stock/finance/<keyword>')
    api.add_resource(Emotion, f'/api/stock/emotion/<keyword>')
    api.add_resource(StockNews, f'/api/stock/mainNews/<keyword>')
    api.add_resource(Exchange, '/api/stock/exchange')
    api.add_resource(User, '/api/access', '/api/access/<user_id>')
    api.add_resource(Login, '/api/login')
    api.add_resource(Review, '/api/mypage', '/api/mypage/<name>')
    

# =============================================================================================
# ===================================== kain code =============================================
# =============================================================================================
    api.add_resource(CovidStatus, '/api/status/covid')
    api.add_resource(CovideNews, '/api/news/covid')
    api.add_resource(CovidBoard, '/api/board/covid')
    api.add_resource(EconomyNews, '/api/news/economy')
    api.add_resource(CovidStatusToArray, '/api/status/arr/covid')
# =============================================================================================
# =============================================================================================
# =============================================================================================

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

@stock_news.errorhandler(500)
def stock_news_api_error(e):
    logging.exception('An error occurred during emotion request. %s' % str(e))
    return 'An internal error occurred.', 500

@exchange.errorhandler(500)
def exchange_api_error(e):
    logging.exception('An error occurred during emotion request. %s' % str(e))
    return 'An internal error occurred.', 500

@user.errorhandler(500)
def user_api_error(e):
    logging.exception('An error occurred during user request. %s' % str(e))
    return 'An internal error occurred.', 500

@login.errorhandler(500)
def review_api_error(e):
    logging.exception('An error occurred during user request. %s' % str(e))
    return 'An internal error occurred.', 500

# =============================================================================================
# ===================================== kain code =============================================
# =============================================================================================
@covid.errorhandler(500)
def user_api_error(e):
    logging.exception('An error occurred during covid request. %s' % str(e))
    return 'An internal error occurred.', 500

@covid_news.errorhandler(500)
def frequency_api_error(e):
    logging.exception('An error occurred during frequency request. %s' % str(e))
    return 'An internal error occurred.', 500

@board.errorhandler(500)
def board_api_error(e):
    logging.exception('An error occurred during board request. %s' % str(e))
    return 'An internal error occurred.', 500

@economy_news.errorhandler(500)
def economy_news_api_error(e):
    logging.exception('An error occurred during board request. %s' % str(e))
    return 'An internal error occurred.', 500

@covid_arr.errorhandler(500)
def covid_arr_api_error(e):
    logging.exception('An error occurred during board request. %s' % str(e))
    return 'An internal error occurred.', 500
# =============================================================================================
# =============================================================================================
# =============================================================================================