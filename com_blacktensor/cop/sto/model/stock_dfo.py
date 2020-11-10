import csv
import pandas as pd
# # from sqlalchemy import create_engine
from com_blacktensor.ext.db import db, openSession, engine
from sqlalchemy import func
from com_blacktensor.util.file_handler import FileHandler
from com_blacktensor.cop.emo.model.emotion_kdd import keyword
# from com_blacktensor.ext.routes import Resource

class StockDfo(object):
    def __init__(self):
        self.fileHandler = FileHandler()  
        # self.colums = colums

    # def get_df(self, data):
    #     return pd.DataFrame(data, columns=self.colums)


    def get_df(self, keyword):
        # file = open('{}.csv'.format(keyword), 'r', encoding='utf-8-sig')

        df = pd.read_csv('{}_data.csv'.format(keyword), index_col=[0], encoding='utf-8-sig')
        # C:/Users/Admin/VscProject/BlackTensor_Test/
        # df = df.drop(['1', '2', '3', '4', '5', '9', '10', '319', '320', '324',
        # '325', '326', '327', '328'], axis = 1, inplace = True)
        # DF = df[:-1]
        # df = df.drop([df.index[0], df.index[1], df.index[2], df.index[3], df.index[4], df.index[5], 
        # df.index[6], df.index[214], df.index[215], df.index[216],
        # df.index[217], df.index[218], df.index[219]])
        # df.drop(df.columns[0, 1, 2, 3, 4, 5, 6, 214, 215, 216, 217, 218, 219], axis = 1, inplace = True)
        df.drop(df.tail(7).index, inplace=True)
        df.drop(df.head(7).index, inplace=True)
        df = df.reset_index(drop=True)

        # news_df.rename( columns={'Unnamed: 0':'name'}, inplace=True )
        df.to_csv(keyword + '_data.csv', encoding='utf-8-sig')
        print('-----------------get_df------------------')
        print(df)
        return df
        # return pd.DataFrame(data, columns=self.colums)
    get_df(0, keyword)