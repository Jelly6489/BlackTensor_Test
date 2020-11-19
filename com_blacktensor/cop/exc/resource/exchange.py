import requests
import pandas as pd
import codecs
import numpy as np
import re
from flask import request
from flask_restful import Resource, reqparse
from flask import jsonify

from com_blacktensor.cop.exc.model.exchange_kdd import ExchangeKdd
from com_blacktensor.cop.exc.model.exchange_dao import ExchangeDao
from com_blacktensor.cop.exc.model.exchange_dfo import ExchangeDfo
from com_blacktensor.cop.exc.model.exchange_dto import ExchangeDto
from com_blacktensor.cop.emo.model.emotion_kdd import keyword

# ============================================================
# ==================                     =====================
# ==================      Resourcing     =====================
# ==================                     =====================
# ============================================================
class Exchange(Resource):
    def __init__(self):
        self.dao = ExchangeDao()

    def get(self):
        print('================Exchange1================')
        result = self.dao.find_all()
        print('================Exchange2================')
        # url = 'http://192.168.0.10:8080/api/stock/lstm_usd'
        # files = {'file': open('./ai_data/{}_LSTM_USD.png'.format(keyword), 'rb')}
        # r = requests.post(url, files=files)
        return jsonify([item.json for item in result])
 