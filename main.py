from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS
from com_blacktensor.ext.routes import initialize_routes
from com_blacktensor.util.checker import Checker 
from com_blacktensor.util.file_handler import FileHandler as handler
from com_blacktensor.ext.db import url, db

import datetime
import time
import threading

# =============================== Emotion ===============================
from com_blacktensor.cop.emo.model.emotion_kdd import keyword
from com_blacktensor.cop.emo.model.emotion_dao import EmotionDao, StockNewsDao
from com_blacktensor.cop.emo.model.emotion_dfo import EmotionDfo
from com_blacktensor.cop.emo.model.emotion_kdd import EmotionKdd
from com_blacktensor.cop.emo.model.emotion_dto import EmotionDto, StockNewsDto
# =============================== Finance ===============================
from com_blacktensor.cop.fin.model.finance_dao import FinanceDao
from com_blacktensor.cop.fin.model.finance_dfo import FinanceDfo
from com_blacktensor.cop.fin.model.finance_dto import FinanceDto
from com_blacktensor.cop.fin.model.finance_kdd import FinanceKdd
# =============================== Stock ===============================
from com_blacktensor.cop.sto.model.stock_dao import StockDao
from com_blacktensor.cop.sto.model.stock_dfo import StockDfo
from com_blacktensor.cop.sto.model.stock_dto import StockDto
from com_blacktensor.cop.sto.model.stock_kdd import StockKdd
# =============================== Exchange ===============================
from com_blacktensor.cop.exc.model.exchange_kdd import ExchangeKdd
from com_blacktensor.cop.exc.model.exchange_dfo import ExchangeDfo
from com_blacktensor.cop.exc.model.exchange_dao import ExchangeDao
from com_blacktensor.cop.exc.model.exchange_dto import ExchangeDto
from com_blacktensor.cop.exc.model.exchange_ai import ExchangeAi
# =============================== User ===============================
from com_blacktensor.usr.model.user_dao import UserDao, ReviewDao
from com_blacktensor.usr.model.user_dfo import UserDfo
from com_blacktensor.usr.model.user_dto import UserDto, ReviewDto
# ================================== kain code =====================================
from com_blacktensor.cop.cov.status.model.status_kdd import CovidStatusKdd
from com_blacktensor.cop.cov.status.model.status_df import CovidStatusDf
from com_blacktensor.cop.cov.status.model.status_dao import CovidStatusDao
from com_blacktensor.cop.cov.status.model.status_dto import CovidStatusDto
from com_blacktensor.cop.news.covid.model.covid_news_dto import CovidNewsDto, CovidExtractionWordDto
from com_blacktensor.cop.news.economy.model.economy_dto import EconomyNewsDto, EconomyExtractionWordDto
# ==================================================================================

app = Flask(__name__)
CORS(app, resources={r'/api/*': {"origins": "*"}})
app.config['SQLALCHEMY_DATABASE_URI'] = url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
api = Api(app)

if __name__ == '__main__':
    code_df = FinanceKdd()
    # EmotionDfo.data_pro(0, keyword)
    EmotionDfo.data_pro(0, keyword)
    FinanceKdd.get_finance(0, keyword, code_df)
    ExchangeKdd.market_index_kdd(0)
    ExchangeDfo.get_ex_df(0)
    # FinanceDfo.fina_pro(keyword)
    
with app.app_context():
    db.create_all()
    # ====================== kain code ==============================
    status_count = CovidStatusDao.count()
    # ===============================================================
    emotion_count = EmotionDao.count()
    stock_new_count = StockNewsDao.count()
    stock_count = StockDao.count()
    finance_count = FinanceDao.count()
    exchange_count = ExchangeDao.count()
    # user
    user_count = UserDao.count()
    review_count = ReviewDao.count()
    print(f'***** Emotion Total Count is {emotion_count} *****')
    if emotion_count[0] == 0:
        EmotionDao.bulk()
    else :
        EmotionDao.find_keyword(keyword)

    print(f'***** StockNews Total Count is {stock_new_count} *****')
    if stock_new_count[0] == 0:
        StockNewsDao.bulk()
    else :
        StockNewsDao.find_keyword(keyword)

    print(f'***** Stock Total Count is {stock_count} *****')
    if stock_count[0] == 0:
        StockDao.bulk()
    else :
        StockDao.find_keyword(keyword)

    print(f'***** Finance Total Count is {finance_count} *****')
    if finance_count[0] == 0:
        FinanceDao.bulk()
    else :
        FinanceDao.find_keyword(keyword)

    print(f'***** Exchange Total Count is {exchange_count} *****')
    if exchange_count[0] == 0:
        ExchangeDao.bulk()

    print(f'***** Exchange Total Count is {user_count} *****')
    if user_count[0] == 0:
        UserDao.bulk()
    else:
        print("Users Data exists...")

    print(f'***** Exchange Total Count is {review_count} *****')
    if review_count[0] == 0:
        ReviewDao.bulk()
    else:
        print("Reivews Data exists...")
    # ================================ kain code =======================================
    if status_count == 0:
        endDate = datetime.date.today().strftime('%Y%m%d')
        datas = CovidStatusKdd().get_covid19_status(endDate)

        if len(datas) > 0:
            if not Checker.check_folder_path('./csv'):
                handler.crete_folder('./csv')
            
            keys = list(datas[0].keys())
            handler.save_to_csv('./csv/result_covid19_status.csv', datas, keys, 'utf-8-sig')

            df = CovidStatusDf(keys).get_dataframe(datas)
            CovidStatusDao.save_data_bulk(df)
    # ===================================================================================
initialize_routes(api) 