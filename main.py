from flask import Flask
from flask_restful import Resource, Api
from hello import HelloWorld

import datetime

from flask_cors import CORS
from com_blacktensor.ext.routes import initialize_routes
from com_blacktensor.util.checker import Checker 
from com_blacktensor.util.file_hander import FileHandler as handler
from com_blacktensor.ext.db import url, db
from com_blacktensor.resources.craw_emotion import CrawKdd, CrawDf, CrawDao, CrawDto
app = Flask(__name__)
CORS(app, resources={r'/api/*': {"origins": "*"}})

app.config['SQLALCHEMY_DATABASE_URI'] = url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
api = Api(app)
# api.add_resource(HelloWorld, '/')

# if __name__ == '__main__':
#     app.run(debug=True)

with app.app_context():
    db.create_all()

    status_count = CrawDao.count()
    
    if status_count == 0:
        # naver_news(self, maxpage, keyword, order, s_date, e_date):
        df = CrawKdd().naver_news()
        CrawDao

        if len(df) > 0:
            if not Checker.check_folder_path('./csv'):
                handler.crete_folder('./csv')
            
            keys = list(df[0].keys())
            handler.save_to_csv('./csv/result_Covid19_status.csv', df, keys, 'utf-8-sig')

            df = CrawDf(keys).get_dataframe(df)
            CrawDao.save_data_bulk(df)

initialize_routes(api)

# with app.app_context():
#     db.create_all()
#     user_count = CrawDao.count()
#     print(f'***** Users Total Count is {user_count} *****')
#     if user_count[0] == 0:
#         CrawDao.bulk()

    # cabb_count = CabbageDao.count()
    # print(f'***** Cabbages Total Count is {cabb_count} *****')
    # if cabb_count[0] == 0:
    #     CabbageDao.bulk()

# initialize_routes(api)