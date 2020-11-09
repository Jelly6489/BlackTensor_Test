import csv
import pandas as pd
# # from sqlalchemy import create_engine
from com_blacktensor.ext.db import db, openSession, engine
from sqlalchemy import func
# from com_blacktensor.ext.routes import Resource

from com_blacktensor.cop.sto.model.stock_dto import StockDto
from com_blacktensor.cop.sto.model.stock_dfo import StockDfo
from com_blacktensor.cop.sto.model.stock_kdd import StockKdd
from com_blacktensor.cop.emo.model.emotion_kdd import keyword

Session = openSession()
session = Session()

class StockDao(StockDto):
    # @classmethod
    # def bulk(cls, stock_dfo):
    #     dfo = stock_dfo.get_df(0, data)
    #     print('---------StockDao------------')
    #     print(f'[ StockDao ] {dfo.head()}')
    #     print(dfo.head())
    #     session.bulk_insert_mappings(cls, dfo.to_dict(orient="records"))
    #     session.commit()
    #     session.close()
    #     # Session = openSession()
    #     # session = Session()
    #     # stock_df = StockDf()
    #     # df = stock_df.hook()
    #     # print(df.head())
    #     # session.bulk_insert_mappings(StockDto, df.to_dict(orient='records'))
    #     # session.commit()
    #     # session.close()
    # #
    # # @staticmethod
    # # def bulk(datas):

    # #     session.bulk_insert_mappings(StockDto, datas.to_dict(orient='records'))

    # #     session.commit()
    # #     session.close()

    # #
    # @staticmethod
    # def save(stock):
    #     session.add(stock)
    #     session.commit()
    
    # @classmethod
    # def count(cls):
    #     return session.query(func.count(cls.date)).one()

    # @classmethod
    # def find_all(cls):

    #     result = session.query(StockDto).all()
    #     session.close()

    #     return result

    @staticmethod
    def bulk():
        # emotion_dfo = EmotionDfo()
        # dfo = emotion_dfo.data_pro(keyword)
        # session.bulk_insert_mappings(EmotionDto, dfo.to_dict(orient='records'))
        stock_dfo = StockDfo()
        dfo = stock_dfo.get_df(keyword)
        session.bulk_insert_mappings(StockDto, dfo.to_dict(orient='records'))
        session.commit()
        session.close()

    @staticmethod
    def save(emotion):
        session.add(emotion)
        session.commit()

    @classmethod
    def count(cls):
        return session.query(func.count(cls.date)).one()

    @classmethod
    def find_all(cls):
        return session.query(cls).all()

    @staticmethod
    def test():
        print(' TEST SUCCESS !!')

# if __name__ == '__main__':
#     StockDao.bulk()

# ===========================================================================

    # @staticmethod
    # def count():
    #     return session.query(func.count(StockDto.date)).one()

    # @staticmethod
    # def save(stock):
    #     new_stock = StockDto(date = stock['date'],
    #                        keyword = stock['keyword'],
    #                        close = stock['close'],
    #                        volume = stock['volume'])
    #     session.add(new_stock)
    #     session.commit()


