from flask import Flask
from flask_restful import Resource, Api
from hello import HelloWorld

import datetime

from flask_cors import CORS
from com_blacktensor.ext.routes import initialize_routes
from com_blacktensor.util.checker import Checker 
from com_blacktensor.util.file_handler import FileHandler as handler
from com_blacktensor.ext.db import url, db
# from com_blacktensor.resources.craw_emotion import CrawKdd, CrawDf, CrawDao, CrawDto
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
print(f'========================= START 1 ==============================')
EmotionDao.test()

app = Flask(__name__)
CORS(app, resources={r'/api/*': {"origins": "*"}})

print(f'========================= START 2 ==============================')
EmotionDao.test()

app.config['SQLALCHEMY_DATABASE_URI'] = url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
api = Api(app)

print(f'========================= START 3 ==============================')
EmotionDao.test()

with app.app_context():
    db.create_all()
    emotion_count = EmotionDao.count()
    print(f'***** Users Total Count is {emotion_count} *****')
    if emotion_count[0] == 0:
        EmotionDao.bulk()

    # cabb_count = CabbageDao.count()
    # print(f'***** Cabbages Total Count is {cabb_count} *****')
    # if cabb_count[0] == 0:
    #     CabbageDao.bulk()

initialize_routes(api)

# with app.app_context():
#     db.create_all()

#     status_count = EmotionDao.count()
#     print('========================oK0====================')
#     if status_count == 0:
#         endDate = datetime.date.today().strftime('%Y%m%d')
#         datas = EmotionDfo().data_pro(keyword)
#         print('========================oK1====================')
#         if len(datas) > 0:
#             # if not Checker.check_folder_path('./csv'):
#                 # handler.crete_folder('./csv')
            
#             keys = list(datas[0].keys())
#             handler.save_to_csv('./csv/result_Covid19_status.csv', datas, keys, 'utf-8-sig')
#             print('========================oK2====================')
#             # df = EmotionDfo(keys).get_dataframe(datas)
#             df = EmotionDfo.data_pro(datas)
#             EmotionDao.bulk(df)

# initialize_routes(api)

print(f'========================= START 4 ==============================')
# EmotionDao.bulk(df)
# FinanceDao.bulk(FinanceDfo)
# StockDao.bulk(StockDfo)
# api.add_resource(HelloWorld, '/')

'''
with app.app_context():
    db.create_all()

    status_count = EmotionDao.count()
    
    if status_count == 0:
        endDate = datetime.date.today().strftime('%Y%m%d')
        datas = EmotionKdd().get_covid19_status(endDate)

        if len(datas) > 0:
            if not Checker.check_folder_path('./csv'):
                handler.crete_folder('./csv')
            
            keys = list(datas[0].keys())
            handler.save_to_csv('./csv/result_Covid19_status.csv', datas, keys, 'utf-8-sig')

            df = EmotionDfo(keys).get_dataframe(datas)
            EmotionDao.save_data_bulk(df)

initialize_routes(api)
'''
# with app.app_context():
#     db.create_all()

#     status_count = CrawDao.count()
    
#     if status_count == 0:
#         # naver_news(self, maxpage, keyword, order, s_date, e_date):
#         df = CrawKdd().naver_news()
#         CrawDao

#         if len(df) > 0:
#             if not Checker.check_folder_path('./csv'):
#                 handler.crete_folder('./csv')
            
#             keys = list(df[0].keys())
#             handler.save_to_csv('./csv/result_Covid19_status.csv', df, keys, 'utf-8-sig')

#             df = CrawDf(keys).get_dataframe(df)
#             CrawDao.save_data_bulk(df)

# initialize_routes(api)

# with app.app_context():
#     db.create_all()
#     user_count = CrawDao.count()
#     print(f'***** Users Total Count is {user_count} *****')
#     if user_count[0] == 0:
#         CrawDao.bulk()

    # cabb_count = CabbageDao.count()
    # print(f'***** Cabbages Total Count is {cabb_count} *****')
    # if cabb_count[0] == 0:
    #     CabbageDao.bulk()

# initialize_routes(api)
    