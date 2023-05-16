from flask import Flask, Response, request
from controllers.urlController import *
from flask_restful import Api, Resource, reqparse
from flask import Blueprint
from flask_cors import CORS


app = Flask(__name__)

CORS(app)


#api.add_resource(ApiHandler, '/flask')
blueprint = Blueprint('blueprint',__name__)

# index blueprint    
blueprint.route('/', methods=['GET'])(index)

#returning the new shortened link to react app 
blueprint.route('/getlink', methods=['GET'])(send_link_to_react)

#The listener for React frontend
blueprint.route('/submitUrl', methods=['POST'])(post_url)

# The reason of this endpoint is to redirect the user from short url to original url 
blueprint.route('/<string:slug>', methods=['GET'])(redirect_to_original_url)

# GET All the data 
blueprint.route('/shortlinks', methods=['GET'])(get_data)

# POST data 
blueprint.route('/shortlinks', methods=['POST'])(post_data)

# Update Data
blueprint.route('/shortlinks/<string:slug>', methods=['PUT'])(update_data)

# Get One Entry 
blueprint.route('/shortlinks/<string:slug>', methods=['GET'])(get_url)

app.register_blueprint(blueprint)