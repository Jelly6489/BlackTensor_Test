from typing import List
from flask import request
from flask_restful import Resource, reqparse
from flask import jsonify
from com_sba_api.ext.db import db, openSession, engine
from pathlib import Path
from sqlalchemy import func
from dataclasses import dataclass
import json
import pandas as pd
import os
import numpy as np
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

@dataclass
class FileReader:
    # def __init__(self, context, fname, train, test, id, label):
        # self.__context = context # - 1ea default access, -2ea private access
    
    # 3.7부터 간소화되서 dataclass 데코 후, key: value 형식으로 써도 됨(lombok 형식)
    context : str = ''
    fname : str = ''
    train : object = None
    test : object = None
    id : str = ''
    label : str = ''

    # -> 반환값에 할당되어야 하는 형식을 할당
    def new_file(self) -> str: 
        return os.path.join(self.context, self.fname)

    def csv_to_dframe(self) -> object:
        return pd.read_csv(self.new_file(), encoding='UTF-8', thousands=',')

    def xls_to_dframe(self, header, usecols) -> object:
        print(f'PANDAS VERSION: {pd.__version__}')
        return pd.read_excel(self.new_file(), header=header, usecols=usecols)

    def json_load(self):
        return json.load(open(self.new_file(), encoding='UTF-8'))

class CabbageDef(object):
    def __init__(self):
        self.fileReader = FileReader()
        self.data = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data')
        self.df = None

    def new_train(self, payload) -> object:
        this = self.fileReader
        this.data = self.data
        this.fname = payload
        print(f'{self.data}')
        print(f'{this.fname}')
        return pd.read_csv(Path(self.data, this.fname))

    def new(self):
        this = self.fileReader
        price_data = 'price_data.csv'
        this.train = self.new_train(price_data)
        print(this.train.columns)
        '''
        Index(['year', 'avgTemp', 'minTemp', 'maxTemp', 'rainFall', 'avgPrice'], dtype='object')
        '''
        self.df = pd.DataFrame(
            {
                'year' : this.train.year,
                'avg_temp' : this.train.avgTemp,
                'min_temp' : this.train.minTemp,
                'max_temp' : this.train.maxTemp,
                'rain_fall' : this.train.rainFall,
                'avg_price' : this.train.avgPrice
            }
        )
        return self.df


config = {
    'user' : 'root',
    'password' : 'root',
    'host' : '127.0.0.1',
    'port' : '3306',
    'database' : 'com_sba_api'
}
charset = {'utf8' : 'utf8'}
url = f"mysql+mysqlconnector://{config['user']}:{config}"

