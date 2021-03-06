import csv
import pandas as pd
from com_blacktensor.ext.db import db, openSession, engine
from sqlalchemy import func

from com_blacktensor.cop.sto.model.stock_kdd import StockKdd
from com_blacktensor.cop.sto.model.stock_dto import StockDto
from com_blacktensor.cop.sto.model.stock_dfo import StockDfo
from com_blacktensor.cop.emo.model.emotion_kdd import keyword

Session = openSession()
session = Session()

class StockDao(StockDto):
    @staticmethod
    def bulk():
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
        # return session.query(cls).all()
        return session.query(cls).filter(cls.keyword.like(f'%{keyword}%')).all()

    @staticmethod
    def test():
        print(' TEST SUCCESS !!')

    @classmethod
    def find_keyword(cls, keyword):
        print('==============find_update==============')
        stock = session.query(cls).filter(cls.keyword.like(f'%{keyword}%')).all()
        if stock != []:
            print('============중복 검사===========')
        if stock == []:
            print('============행복회로 가동===========')
            StockDao.bulk()

    @classmethod
    def find_by_keyword(cls, keyword):
        return session.query(cls).filter(cls.keyword.like(f'{keyword}')).all()