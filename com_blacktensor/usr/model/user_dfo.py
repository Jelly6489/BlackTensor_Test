import csv
import pandas as pd
from pandas import Series, DataFrame
import numpy as np
from com_blacktensor.ext.db import db, openSession, engine
from sqlalchemy import func
from com_blacktensor.util.file_handler import FileHandler
# from run import search

class UserDfo(object):
    def __init__(self):
        self.fileHandler = FileHandler() 

    def create(self):
        print('============Test1==========')
        df = pd.DataFrame(
            {
                'email': 'aaaaaa@naver.com',
                'name': 'bbbbb',
                'password': 'ccc56123',
                'type': 'a',
                'gender': 'M',
                'age': 20
            }, index=[0]
        )
        print(df)
        return df

    def get_mypage(self):
        print('=========mypage==========')
        df = pd.DataFrame(
            {
                "name": 'test111',
                "money": 123,
                "type": 'sdas',
                "date": '2020-10-10',
                "price": 123,
                "cnt": 123
            }, index=[0]
        )
        print(df)
        return df