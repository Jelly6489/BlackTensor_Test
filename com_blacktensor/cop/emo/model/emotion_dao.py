import requests
import pandas as pd
import codecs
import numpy as np
import re
from bs4 import BeautifulSoup
from konlpy.tag import Twitter
from collections import Counter
from com_blacktensor.ext.db import db, openSession, engine
from sqlalchemy import func
import json

from sqlalchemy import Column, Integer, String, Date
from com_blacktensor.cop.emo.model.emotion_dto import EmotionDto, StockNewsDto
# import time
# import multiprocessing


Session = openSession()
session = Session()

class EmotionDao(EmotionDto):
    @classmethod
    def bulk(cls, emotion_dfo):
        dfo = emotion_dfo.create()
        print(dfo.head())
        session.bulk_insert_mappings(cls, dfo.to_dict(orient="records"))
        session.commit()
        session.close()

    @staticmethod
    def save(emotion):
        session.add(emotion)
        session.commit()
    
    @staticmethod
    def count(cls):
        return session.query(func.count(cls.no)).one()

    @classmethod
    def find_all(cls):

        result = session.query(EmotionDto).all()
        session.close()

        return result

class StockNewsDao(StockNewsDto):
    @staticmethod
    def bulk(datas):
        session.bulk_insert_mappings(StockNewsDto, datas.to_dict(orient="records"))
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