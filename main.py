from flask import Flask
from flask_restful import Resource, Api
from hello import HelloWorld

import datetime

from flask_cors import CORS
from com_blacktensor.ext.routes import initialize_routes
from com_blacktensor.util.checker import Checker 
from com_blacktensor.util.file_handler import FileHandler as handler
from com_blacktensor.ext.db import url, db

from com_blacktensor.cop.emo.model.emotion_kdd import keyword
#Emotion
from com_blacktensor.cop.emo.model.emotion_dao import EmotionDao, StockNewsDao
from com_blacktensor.cop.emo.model.emotion_dfo import EmotionDfo
from com_blacktensor.cop.emo.model.emotion_kdd import EmotionKdd
from com_blacktensor.cop.emo.model.emotion_dto import EmotionDto, StockNewsDto
# Finance
from com_blacktensor.cop.fin.model.finance_dao import FinanceDao
from com_blacktensor.cop.fin.model.finance_dfo import FinanceDfo
from com_blacktensor.cop.fin.model.finance_dto import FinanceDto
from com_blacktensor.cop.fin.model.finance_kdd import FinanceKdd
# Stock
from com_blacktensor.cop.sto.model.stock_dao import StockDao
from com_blacktensor.cop.sto.model.stock_dfo import StockDfo
from com_blacktensor.cop.sto.model.stock_dto import StockDto
from com_blacktensor.cop.sto.model.stock_kdd import StockKdd

from com_blacktensor.cop.emo.model import emotion_dfo

from com_blacktensor.ext.db import db, openSession

Session = openSession()
session = Session()

print(f'========================= START 1 ==============================')
EmotionDao.test()
# 
# EmotionDfo.data_pro(0, keyword)
# 
app = Flask(__name__)
CORS(app, resources={r'/api/*': {"origins": "*"}})

print(f'========================= START 2 ==============================')
EmotionDao.test()

app.config['SQLALCHEMY_DATABASE_URI'] = url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
api = Api(app)

if __name__ == '__main__':
    code_df = FinanceKdd()
    EmotionDfo.data_pro(0, keyword)
    EmotionDfo.data_pro(0, keyword)
    FinanceKdd.get_finance(0, keyword, code_df)
    # FinanceDfo.fina_pro(keyword)
    

print(f'========================= START 3 ==============================')
EmotionDao.test()

with app.app_context():
    db.create_all()
    # emotion_find = EmotionDao.find(EmotionDao, keyword)
    emotion_count = EmotionDao.count()
    stock_new_count = StockNewsDao.count()
    stock_count = StockDao.count()
    finance_count = FinanceDao.count()
    print(f'***** Emotion Total Count is {emotion_count} *****')
    if emotion_count[0] == 0:
        EmotionDao.bulk()
        # if emotion_find == 0:
            # EmotionDao.find_insert()
        # session.query(emotion).filter(emotion.keyword == keyword).last()\
        #     .insert({EmotionDao.no : emotion['no'],\
        #         EmotionDao.positive:emotion['positive'],\
        #         EmotionDao.pos_count:emotion['pos_count'],\
        #         EmotionDao.negative:emotion['negative'],\
        #         EmotionDao.neg_count:emotion['neg_count'],\
        #         EmotionDao.keyword:emotion['keyword']})

    print(f'***** StockNews Total Count is {stock_new_count} *****')
    if stock_new_count[0] == 0:
        StockNewsDao.bulk()

    print(f'***** Stock Total Count is {stock_count} *****')
    if stock_count[0] == 0:
        StockDao.bulk()

    print(f'***** Finance Total Count is {finance_count} *****')
    if finance_count[0] == 0:
        FinanceDao.bulk()

initialize_routes(api)