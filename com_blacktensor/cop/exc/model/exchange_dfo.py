import requests
import pandas as pd
import codecs
import numpy as np
import re
from bs4 import BeautifulSoup
from konlpy.tag import Twitter
from collections import Counter
from com_blacktensor.util.file_handler import FileHandler
# from sqlalchemy import Column, Integer, String, Date
# # from sqlalchemy import create_engine

# # ============================================================
# # ==================                     =====================
# # ==================    Preprocessing    =====================
# # ==================                     =====================
# # ============================================================
my_folder = '/c/Users/Admin/VscProject/BlackTensor_Test/csv'
class ExchangeDfo(object):
    def __init__(self):
        print('-----------ExchangeDfo--------------')
        self.fileHandler = FileHandler()

    def get_ex_df(self):
    
        df = pd.read_csv('exchange_index.csv', encoding='utf-8-sig')
        
        df.rename( columns={'Unnamed: 0':'date', '미국 USD':'usd', '일본 JPY':'jpy',\
        '유럽연합 EUR' : 'eur', '중국 CNY' : 'cny'}, inplace=True )
        df = df.sort_values(by=['date'], ascending=True)
        df.drop(df.head(2893).index, inplace=True)
        df = df.reset_index(drop=True)
        df.to_csv('./csv/exchange_index.csv', encoding='utf-8-sig')
        print('-----------------Ex_get_df------------------')
        print(df)
        print(type(df))
        return df
        # return pd.DataFrame(data, columns=self.colums)
    get_ex_df(0)

    # def get_csv(self, keyword):
    #     df = pd.read_csv('./csv/{}_data.csv'.format(keyword), index_col=[0], encoding='utf-8-sig')
    #     # df = df.reset_index(drop=True)
    #     # df = df.values.tolist()
    #     # df = df.to_json('./csv/{}_data.csv'.format(keyword), orient='table')
    #     # df.drop(df.tail(6).index, inplace=True)
    #     # df.drop(df.head(8).index, inplace=True)
    #     # df = df.reset_index(drop=True)

    #     # news_df.rename( columns={'Unnamed: 0':'name'}, inplace=True )
    #     # df.to_csv('./csv/'+keyword + '_data.csv', encoding='utf-8-sig')
    #     # df.to_csv('./csv/{}_data.csv', encoding='utf-8-sig')
    #     print('-----------------Ex_get_csv------------------')
    #     print(df)
    #     print(type(df))
    #     return df