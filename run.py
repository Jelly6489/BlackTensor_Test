from flask import Flask, render_template, request
from flask_restful import Resource, Api
from main import app
from com_blacktensor.cop.emo.resource.emotion import Emotion
app.run(host='192.168.0.10', port='8080', debug=True)
# app.run(host='127.0.0.1', port='8080', debug=True)

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