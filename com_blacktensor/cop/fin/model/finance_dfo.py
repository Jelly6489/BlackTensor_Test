import csv
import pandas as pd
# # from sqlalchemy import create_engine
from com_blacktensor.ext.db import db, openSession, engine
from sqlalchemy import func
from com_blacktensor.util.file_hander import FileReader
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
        self.fileReader = FileReader()  
        self.colums = colums


    def fina_pro(self, keyword):
        print('----------Finance Testing----------')
#     def DataPro(self):
        # keyword = str(self.keyword)
        df = pd.read_csv('{}_finance.csv'.format(keyword), encoding='utf-8')

        df.rename( columns={'Unnamed: 0':'name'}, inplace=True )
        df.to_csv(keyword + '_finance.csv', encoding='utf8')
        print('-----------------fin_file------------------')
        print(df)
    fina_pro(0, keyword)

    def get_df(self, data):
        return pd.DataFrame(data, columns=self.colums)