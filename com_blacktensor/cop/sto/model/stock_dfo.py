import csv
import pandas as pd
import numpy as np
from com_blacktensor.ext.db import db, openSession, engine
from sqlalchemy import func
from com_blacktensor.util.file_handler import FileHandler
from com_blacktensor.cop.emo.model.emotion_kdd import keyword

class StockDfo(object):
    def __init__(self):
        self.fileHandler = FileHandler()  

    def get_df(self, keyword):
        df = pd.read_csv('{}_data.csv'.format(keyword), index_col=[0], encoding='utf-8-sig')
        # df.drop(df.head(12).index, inplace=True)
        df = df.reset_index(drop=True)

        # news_df.rename( columns={'Unnamed: 0':'name'}, inplace=True )
        # df.to_csv(keyword + '_data.csv', encoding='utf-8-sig')
        df.to_csv('./csv/{}_data.csv'.format(keyword), encoding='utf-8-sig')
        print('-----------------get_df------------------')
        print(df)
        print(type(df))
        return df
        # return pd.DataFrame(data, columns=self.colums)
    get_df(0, keyword)
