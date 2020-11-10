import requests
import pandas as pd
import codecs
import numpy as np
import re
from bs4 import BeautifulSoup
from konlpy.tag import Twitter
from collections import Counter
from com_blacktensor.ext.db import db, openSession
from sqlalchemy import func
import json

from sqlalchemy import Column, Integer, String, Date
from com_blacktensor.cop.emo.model.emotion_kdd import EmotionKdd
from com_blacktensor.cop.emo.model.emotion_dto import EmotionDto, StockNewsDto
from com_blacktensor.cop.emo.model.emotion_dfo import EmotionDfo
from com_blacktensor.cop.emo.model.emotion_kdd import keyword

# import time
# import multiprocessing


Session = openSession()
session = Session()

class EmotionDao(EmotionDto):
    # @classmethod
    # def bulk(cls, emotion_dfo):
    #     dfo = emotion_dfo.data_pro(0, keyword)
    #     print('--------Emotion----------')
    #     print(dfo.head())
    #     session.bulk_insert_mappings(cls, dfo.to_dict(orient="records"))
    #     session.commit()
    #     session.close()

    @staticmethod
    def bulk():
        emotion_dfo = EmotionDfo()
        dfo = emotion_dfo.data_pro(keyword)
        session.bulk_insert_mappings(EmotionDto, dfo.to_dict(orient='records'))
        session.commit()
        session.close()

    @staticmethod
    def save(emotion):
        session.add(emotion)
        session.commit()

    @classmethod
    def update(cls, emotion):
        session.query(cls).filter(cls.keyword == emotion['keyword'])\
            .update({cls.no : emotion['no'],\
                cls.positive:emotion['positive'],\
                cls.pos_count:emotion['pos_count'],\
                cls.negative:emotion['negative'],\
                cls.neg_count:emotion['neg_count']})                                                        
        session.commit()

    @classmethod
    def count(cls):
        return session.query(func.count(cls.no)).one()

    # @classmethod
    # def find_insert(cls, emotion, keyword):
    #     session.query(cls).filter_by(cls.keyword == emotion['keyword']).last()\
    #         .insert({cls.no : emotion['no'],\
    #             cls.positive:emotion['positive'],\
    #             cls.pos_count:emotion['pos_count'],\
    #             cls.negative:emotion['negative'],\
    #             cls.neg_count:emotion['neg_count'],\
    #             cls.keyword:emotion['keyword']})
            # if session.query(cls).filter(cls.keyword != keyword):
            # emotion_dfo = EmotionDfo()
            # dfo = emotion_dfo.data_pro(keyword)
            # session.bulk_insert_mappings(EmotionDto, dfo.to_dict(orient='records'))
            # session.commit()
            # session.close()

        return session.query(cls).all()

    @classmethod
    def find_all(cls):
        return session.query(cls).all()

    @classmethod
    def find_x(cls, keyword):
        # session.query(cls).filter(cls.keyword != keyword).last()
        # session.query(cls).filter(cls.keyword.like('keyword'))
        session.query(cls).filter(cls.keyword != keyword)
        session.close()
        return 0

    @classmethod
    def find_y(cls, keyword):
        # session.query(cls).filter(cls.keyword != keyword).last()
        # session.query(cls).filter(cls.keyword.like('keyword'))
        session.query(cls).filter(cls.keyword == keyword)
        session.close()
        return 1

    @classmethod
    def find_like(cls, keyword):
        # session.query(cls).filter(cls.keyword.like('%'+keyword+'%'))
        session.query(cls).filter(cls.keyword.like('%'+keyword+'%'))
        print(cls.keyword)
        session.close()
        return 2

    @staticmethod
    def match(keyword):
        # session.query(emotion).filter_by(emotion.keyword.match(keyword))
        session.commit()
        session.close()
        return 3

    @staticmethod
    def test():
        print(' TEST SUCCESS !!')

class StockNewsDao(StockNewsDto):
    @staticmethod
    def bulk():
        emotion_dfo = EmotionDfo()
        df = emotion_dfo.get_df(keyword)
        session.bulk_insert_mappings(StockNewsDto, df.to_dict(orient="records"))
        session.commit()
        session.close()

    @staticmethod
    def save(emotion):
        session.add(emotion)
        session.commit()
    
    @staticmethod
    def count():
        return session.query(func.count(StockNewsDto.no)).one()

    @classmethod
    def find_all(cls):

        result = session.query(StockNewsDto).all()
        session.close()

        return result

# if __name__ == '__main__':
#     EmotionDao.bulk()