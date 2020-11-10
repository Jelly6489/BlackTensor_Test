from flask import request
from flask_restful import Resource, reqparse
from flask import jsonify

from com_blacktensor.cop.emo.model.emotion_dao import EmotionDao, StockNewsDao
from com_blacktensor.cop.emo.model.emotion_dfo import EmotionDfo
from com_blacktensor.cop.emo.model.emotion_kdd import EmotionKdd
from com_blacktensor.cop.emo.model.emotion_dto import EmotionVo
from com_blacktensor.cop.emo.model.emotion_dto import EmotionDto
# ============================================================
# ==================                     =====================
# ==================      Resourcing     =====================
# ==================                     =====================
# ============================================================
class Emotion(Resource):
    def __init__(self):
        self.dao = EmotionDao()

    def get(self):
        result = self.dao.find_all()
        return jsonify([item.json for item in result])
        # return jsonify(result)


class StockNews(Resource):
    def __init__(self):
        self. dao = StockNewsDao()

    def get(self):
        result = self.dao.find_all()
        return jsonify([item.json for item in result])
        # return jsonify(result)

# if __name__ == "__main__":
#     ck = EmotionKdd()
#     cd = EmotionDf()
#     cd.data_pro()
#     # c_dto = EmotionDto()
    
#     EmotionDao.bulk() # class

# parser = reqparse.RequestParser()
# parser.add_argument('no', type = int, required = True,
#                             help='This field should be a userId')
# parser.add_argument('positive', type = str, required = True,
#                             help='This field should be a positive')
# parser.add_argument('pos_count', type = int, required = True,
#                             help='This field should be a pos_count')
# parser.add_argument('negative', type = str, required = True,
#                             help='This field should be a negative')
# parser.add_argument('neg_count', type = int, required = True,
#                             help='This field should be a neg_count')
# parser.add_argument('stock', type = str, required = True,
#                             help='This field should be a stock')

# class Emotion(Resource):
#     @staticmethod
#     def post():
#         args = parser.parse_args()
#         emotion = EmotionVo()
#         emotion.stock_name = args.stock_name
#         emotion.positive = args.positive
#         emotion.negative = args.negative
#         # service.assign(emotion)
#         print("Predicted emotion")

# parser = reqparse.RequestParser() 

# class Emotion(Resource):
#     @staticmethod
#     def post():
#         print(f'[ User Signup Resource Enter ] ')
#         body = request.get_json()
#         emotion = EmotionDao(**body)
#         EmotionDao.save(emotion)
#         emotion_id = emotion.no
        
#         return {'emotionId': str(emotion_id)}, 200 

#     @staticmethod
#     def get(emotionId: str):
#         try:
#             print(f'User ID is {emotionId} ')
#             emotion = EmotionDao.find_one(emotionId)
#             if emotion:
#                 return json.dumps(emotion.json()), 200
#         except Exception as e:
#             return {'message': 'Emotion not found'}, 404

# class Emotions(Resource):
            
#     @staticmethod
#     def post():
#         print(f'[ Emotion Bulk Resource Enter ] ')
#         EmotionDao.bulk()
#     @staticmethod
#     def get():
#         print(f'[ Emotion List Resource Enter ] ')
#         data = EmotionDao.find_all()
#         return json.dumps(data), 200