from flask import request, make_response
from flask_restful import Resource, reqparse
from flask import jsonify
import json

from com_blacktensor.cop.sto.model.stock_dao import StockDao
from com_blacktensor.cop.sto.model.stock_dfo import StockDfo
from com_blacktensor.cop.sto.model.stock_kdd import StockKdd
from com_blacktensor.cop.sto.model.stock_dto import StockVo
from com_blacktensor.cop.sto.model.stock_dto import StockDto

# ============================================================
# ==================                     =====================
# ==================      Resourcing     =====================
# ==================                     =====================
# ============================================================

class Stock(Resource):
    def __init__(self):
        self.dao = StockDao()

    def get(self):
        result = self.dao.find_all()
        # result = json.dumps(result, ensure_ascii=False)

        # res = make_response(result)
        # # with open('result.json', 'w', encoding='utf-8') as f:
        #     # json.dumps(result, f, ensure_ascii=False)
        # res = json.dumps(result)
        # results = json.loads(res)
        # # return jsonify([item.json for item in result])
        # # return jsonify(json.dumps(str(result)))
        # return jsonify(res)
        # return jsonify(str(result))
        return jsonify([item.json for item in result])

# parser = reqparse.RequestParser()
# parser.add_argument('date', type = int, required = True,
#                             help='This field should be a date')
# parser.add_argument('close', type = str, required = True,
#                             help='This field should be a close')
# parser.add_argument('volume', type = int, required = True,
#                             help='This field should be a volume')
# parser.add_argument('keyword', type = str, required = True,
#                             help='This field should be a keyword')


# class Stock(Resource):
#     @staticmethod
#     def post():
#         args = parser.parse_args()
#         stock = StockVo()
#         stock.date = args.date
#         stock.close = args.close
#         stock.volume = args.volume
#         stock.keyword = args.keyword
#         # service.assign(finance)
#         print("Predicted finance")

# ==================================================================

# parser = reqparse.RequestParser() 

# class Stock(Resource):
#     @staticmethod
#     def post():
#         print(f'[ User Signup Resource Enter ] ')
#         body = request.get_json()
#         stock = StockDao(**body)
#         StockDao.save(stock)
#         stock_id = stock.no
        
#         return {'stockId': str(stock_id)}, 200 

#     @staticmethod
#     def get(stockId: str):
#         try:
#             print(f'User ID is {stockId} ')
#             stock = StockDao.find_one(stockId)
#             if stock:
#                 return json.dumps(stock.json()), 200
#         except Exception as e:
#             return {'message': 'Stock not found'}, 404

# class Stocks(Resource):
            
#     @staticmethod
#     def post():
#         print(f'[ Stock Bulk Resource Enter ] ')
#         StockDao.bulk()
#     @staticmethod
#     def get():
#         print(f'[ Stock List Resource Enter ] ')
#         data = StockDao.find_all()
#         return json.dumps(data), 200