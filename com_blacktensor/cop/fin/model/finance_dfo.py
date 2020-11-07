import csv
import pandas as pd
import os
from pathlib import Path
# # from sqlalchemy import create_engine
from com_blacktensor.ext.db import db, openSession, engine
from sqlalchemy import func
from com_blacktensor.util.file_handler import FileHandler
from com_blacktensor.cop.emo.model.emotion_kdd import keyword
# from com_blacktensor.ext.routes import Resource

class FinanceDfo(object):
    def __init__(self, colums):
        # self.ck = CrawKdd()
        # this = self.ck
        # self.keyword = this.keyword
        # fk = FinanceKdd()
        ####
        # self.fk = FinanceKdd()
        # this = self.fk
        # self.keyword = this.keyword
        self.fileHandler = FileHandler()
        self.data = os.path.join(os.path.abspath(os.path.dirname(__file__))+'\\data')
        self.colums = colums
        self.odf = None


    def fina_pro(self, keyword):
        train = keyword + '_finance.csv'
        # this = self.fileHandler
        # this.handler = self.new_model(train)
        # my_folder = 'C:/Users/Admin/VscProject/BlackTensor_Test/'
        print('----------FinanceDfo----------')
#     def DataPro(self):
        # keyword = str(self.keyword)
        df = pd.read_csv('{}_finance.csv'.format(keyword), index_col=[0], encoding='utf-8')
        # C:/Users/Admin/VscProject/BlackTensor_Test/

        df.rename( columns={'Unnamed: 0':'name'}, inplace=True )
        df.to_csv(keyword + '_finance.csv', encoding='utf-8')
        print('-----------------fin_file------------------')
        print(df)
        return df
    # fina_pro(0, keyword)

    # def get_df(self, data):
    #     return pd.DataFrame(data, columns=self.colums)

    # fina_pro(0, keyword)

    # def create(self):
    #     train = keyword + '_finance.csv'
    #     this = self.fileHandler
    #     this.handler = self.new_model(train)

    #     self.odf = pd.DataFrame()

    # def new_model(self, payload) -> object:
    #     this = self.fileHandler
    #     this.data = self.data
    #     this.fname = payload
    #     print(f'{self.data}')
    #     print(f'{this.fname}')
    #     return pd.read_csv(Path(self.data, this.fname))

    # @staticmethod
    # def create_train(this) -> object:
    #     return this.train

# if __name__ == '__main__':
#     # FinanceKdd.get_finance(0, keyword, code_df)
#     FinanceDfo.fina_pro()