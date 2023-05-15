from flask import Flask, Response, request
from controllers.urlController import *
from flask_restful import Api, Resource, reqparse
from flask import Blueprint
from flask_cors import CORS
from api.apiHandler import ApiHandler

app = Flask(__name__)

CORS(app)
api = Api(app)

#api.add_resource(ApiHandler, '/flask')
blueprint = Blueprint('blueprint',__name__)

# index blueprint    
blueprint.route('/', methods=['GET'])(index)

#The listener for React frontend
blueprint.route('/submitUrl', methods=['POST'])(post_url)

# GET All the data 
blueprint.route('/shortlinks', methods=['GET'])(get_data)
# POST data 
blueprint.route('/shortlinks', methods=['POST'])(post_data)

app.register_blueprint(blueprint)