import requests
import pandas as pd
import codecs
import numpy as np
import re
from flask import request
from bs4 import BeautifulSoup
from konlpy.tag import Twitter
from collections import Counter
from flask_restful import Resource, reqparse
from com_blacktensor.ext.db import db, openSession, engine
from sqlalchemy import func
import json

from sqlalchemy import Column, Integer, String, Date

from com_blacktensor.cop.fin.model.finance_dao import FinanceDao
from com_blacktensor.cop.fin.model.finance_dfo import FinanceDfo
from com_blacktensor.cop.fin.model.finance_kdd import FinanceKdd
from com_blacktensor.cop.fin.model.finance_dto import FinanceVo

# ============================================================
# ==================                     =====================
# ==================      Resourcing     =====================
# ==================                     =====================
# ============================================================

# parser = reqparse.RequestParser()
# parser.add_argument('no', type = int, required = True,
#                             help='This field should be a no')
# parser.add_argument('name', type = str, required = True,
#                             help='This field should be a name')
# parser.add_argument('f_2015_12', type = int, required = True,
#                             help='This field should be a f_2015_12')
# parser.add_argument('f_2016_12', type = str, required = True,
#                             help='This field should be a f_2016_12')
# parser.add_argument('f_2017_12', type = int, required = True,
#                             help='This field should be a f_2017_12')
# parser.add_argument('f_2018_12', type = str, required = True,
#                             help='This field should be a f_2018_12')
# parser.add_argument('f_2019_12', type = str, required = True,
#                             help='This field should be a f_2019_12')
# parser.add_argument('f_2020_12', type = int, required = True,
#                             help='This field should be a f_2020_12')
# parser.add_argument('f_2021_12', type = str, required = True,
#                             help='This field should be a f_2021_12')
# parser.add_argument('f_2022_12', type = str, required = True,
#                             help='This field should be a f_2022_12')
# parser.add_argument('keyword', type = str, required = True,
#                             help='This field should be a keyword')

# class Finance(Resource):
#     @staticmethod
#     def post():
#         args = parser.parse_args()
#         finance = FinanceVo()
#         finance.no = args.no
#         finance.name = args.name
#         finance.f_2015_12 = args.f_2015_12
#         finance.f_2016_12 = args.f_2016_12
#         finance.f_2017_12 = args.f_2017_12
#         finance.f_2018_12 = args.f_2018_12
#         finance.f_2019_12 = args.f_2019_12
#         finance.f_2020_12 = args.f_2020_12
#         finance.f_2021_12 = args.f_2021_12
#         finance.f_2022_12 = args.f_2022_12
#         finance.keyword = args.keyword
#         # service.assign(finance)
#         print("Predicted finance")

parser = reqparse.RequestParser() 

class Finance(Resource):
    @staticmethod
    def post():
        print(f'[ User Signup Resource Enter ] ')
        body = request.get_json()
        finance = FinanceDao(**body)
        FinanceDao.save(finance)
        finance_id = finance.no
        
        return {'financeId': str(finance_id)}, 200 

    @staticmethod
    def get(financeId: str):
        try:
            print(f'User ID is {financeId} ')
            finance = FinanceDao.find_one(financeId)
            if finance:
                return json.dumps(finance.json()), 200
        except Exception as e:
            return {'message': 'Finance not found'}, 404

class Finances(Resource):
    @staticmethod
    def post():
        print(f'[ Finance Bulk Resource Enter ] ')
        FinanceDao.bulk()
    @staticmethod
    def get():
        print(f'[ Finance List Resource Enter ] ')
        data = FinanceDao.find_all()
        return json.dumps(data), 200