import logging
from flask import Blueprint
from flask_restful import Api
from com_blacktensor.resources.home import Home
from com_blacktensor.resources.stock_crow import Item, Items
from com_blacktensor.resources.user import User, Users, Auth, Access
from com_blacktensor.resources.crow import Article, Articles

home = Blueprint('home', __name__, url_prefix='/api')

api = Api(home)

def initialize_routes(api):
    
    api.add_resource(Home, '/api')

@user.errorhandler(500)
def user_api_error(e):
    logging.exception('An error occurred during user request. %s' % str(e))
    return 'An internal error occurred.', 500