import csv
import pandas as pd
# # from sqlalchemy import create_engine
from com_blacktensor.ext.db import db, openSession, engine
from sqlalchemy import func
from com_blacktensor.util.file_handler import FileHandler
# from com_blacktensor.ext.routes import Resource

class StockDfo(object):
    def __init__(self):
        self.fileHandler = FileHandler()  
        # self.colums = colums

    # def get_df(self, data):
    #     return pd.DataFrame(data, columns=self.colums)


    def get_df(self, keyword):
        # file = open('{}.csv'.format(keyword), 'r', encoding='utf-8-sig')

        news_df = pd.read_csv('{}_data.csv'.format(keyword), index_col=[0], encoding='utf-8-sig')
        # C:/Users/Admin/VscProject/BlackTensor_Test/

        news_df.rename( columns={'Unnamed: 0':'name'}, inplace=True )
        news_df.to_csv(keyword + '_data.csv', encoding='utf-8-sig')
        print('-----------------get_df------------------')
        print(news_df)
        return news_df
        # return pd.DataFrame(data, columns=self.colums)