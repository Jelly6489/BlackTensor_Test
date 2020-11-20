from flask import Flask, render_template, request
from flask_restful import Resource, Api
from main import app
from flask import jsonify
import pandas as pd
from com_blacktensor.cop.emo.resource.emotion import Emotion
# import flask_cors CORS, cross_origin
from flask_cors import CORS

# CORS(app, resources={r'*': {'origins': ['https://192.168.0.10:8080/api/access', 'http://192.168.0.10:8080']}})
app.run(host='192.168.0.10', port='8080', debug=True)
# app.run(host='127.0.0.1', port='8080', debug=True)
# '''
# app = Flask(__name__)
# api = Api(app)
# @app.route('/')
# def main_get(num=None):
#     return render_template(num=num)
# if __name__ == "__main__":
#     app.run(host='192.168.0.10', port='8080', debug=True)
    # return render_template('####.html', num=num)

# @app.route('/api/stock/emotion/', method = ['GET', 'POST'])
# def stock_name():
#     if request.method == 'GET':
#         args_dict = request.args.to.dict()
#         keyword = request.args.get('keyword')
#         print('==========keyword============')
#         print(keyword)
#         print('==========request.form============')
#         print(request.form)


#     # return render_template('.jsx', keyword = keyword)
#     return render_template(keyword = keyword)
#     # return 0
# if __name__ == "__main__":
#     app.run(host='192.168.0.10', port='8080', debug=True)
# '''
########## 파일 업로드 ###########

# url = 'http://your_url'
# files = {'file': open('myfile.test', 'rb')}
# r = requests.post(url, files=files)


# print('================Search Test1===================')
# app = Flask(__name__)
# @app.route('/api/access', methods = ["POST", "OPTIONS"])
# def search():
#     # email = request.form["email"]
#     # name = request.form["name"]
#     # password = request.form["password"]
#     # type = request.form["type"]
#     # gender = request.form["gender"]
#     # age = request.form["age"]
#     # msg = []
#     # email = request.form.get("email")
#     # msg.append(email)
#     # name = request.form.get("name")
#     # password = request.form.get("password")
#     # type = request.form.get("type")
#     # gender = request.form.get("gender")
#     # age = request.form.get("age")
#     # email = request.json
#     # name = request.json
#     # password = request.json
#     # type = request.json
#     # gender = request.json
#     # age = request.json
#     data = request.json
#     body = request.get_json()
#     print('type(body): ', type(body))
#     print('body: ', body)
#     # user = UserDto(**body)
#     # email1 = request.args("email")
#     # email2 = request.form("email")
#     data1 = request.form.to_dict(flat=False)
#     print(data)
#     print('===========data==========')
#     print(body)
#     # print(email1)
#     # print(email2)
#     # df = pd.DataFrame(data)
    
#     return jsonify(data)
# if __name__ == "__main__":
#     app.run(host='192.168.0.10', port='8080', debug=True)

'''
@app.route('/api/emotion', method = ['POST', 'GET'])
def stock_name(num=None):
    if request.method == 'POST':
        # temp = request.form['num']
        pass
    elif request.method == 'GET':
        temp = request.args.get('num')
        # temp = str(temp)
        temp1 = request.args.get('keyword')
        print('Ok!')
        # return render_template('####.html', num=temp, keyword=temp1)

if __name__ == '__main__':
  app.run(host='192.168.0.10', port='8080', debug=True)  
'''

'''
app = Flask(__name__)
api = Api(app)
 
class Rest(Resource):
    def get(self):
        return {'rest': '한국 !'}
        # return Emotion()
    def post(self):
        return {'rest': 'post success !'}
api.add_resource(Rest, '/api')
 
if __name__ == '__main__':
    app.run(host='192.168.0.10', port='8080', debug=True)
'''
'''
app = Flask(__name__)
api = Api(app)


@app.route('/test')
def test():
    if request.method == 'Post':
    return {'test' : 'test Success!'}
def get():
    return {'get' : 'get Success!'}
def post():
    return {'post' : 'post Success!'}

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8080)
'''

'''
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world!'

if __name__ == 'main':
    app.run(host='192.168.0.10', port='8080', debug=True)

'''