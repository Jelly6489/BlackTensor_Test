from flask import request, make_response
from flask_restful import Resource, reqparse
from flask import jsonify
import json

from com_blacktensor.cop.sto.model.stock_dao import StockDao
from com_blacktensor.cop.sto.model.stock_dfo import StockDfo
from com_blacktensor.cop.sto.model.stock_kdd import StockKdd
from com_blacktensor.cop.sto.model.stock_dto import StockVo
from com_blacktensor.cop.sto.model.stock_dto import StockDto

from com_blacktensor.cop.emo.model.emotion_kdd import keyword

# ============================================================
# ==================                     =====================
# ==================      Resourcing     =====================
# ==================                     =====================
# ============================================================

class Stock(Resource):
    def __init__(self):
        self.dao = StockDao()
        self.df = StockDfo()

    def get(self):
        result = self.dao.find_all()
        return jsonify([item.json for item in result])