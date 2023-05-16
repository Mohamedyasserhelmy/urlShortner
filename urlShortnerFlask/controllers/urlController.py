from flask import Flask, Response, request, jsonify, redirect
from config import *
from models.getAll import get_all, result
from models.findurl import find_url
from models.inserturl import insert_url
from models.updateurl import update_url
from controllers.slugGenerator import generate_code
from controllers.redirectUrl import create_short_url
SHORT_LINK = None
# main page of backend
def index():
    return '<p> Hello world !! </p>'

# Returns the url passed from react input value form   
def post_url():
    global SHORT_LINK
    data = request.get_json()
    client_long_url =  data['inputValue']
    short_url_payload = create_short_url(client_long_url)
    status = insert_url(short_url_payload)
    new_shortened_url = request.host_url + short_url_payload['slug']
    SHORT_LINK = new_shortened_url
   
    return jsonify({"message" : status.json()['insertedId']}) , 201

# sending link to react app 
def send_link_to_react():
    return {"message": SHORT_LINK} , 200
    
# Redirecting to the original website     
def redirect_to_original_url(slug):
    redirected_url = get_url(slug)
    original_website = redirected_url[0]['message']
    return redirect(original_website , code=302)

# Getting Data from Atlas mongoDB Connection
def get_data():
    return result 
# Creating post request to add data 
def post_data():
    required_objects = ['ios', 'android', 'web', 'slug']
    
    # adding slug to request 
    data = request.get_json()
    data['slug'] = generate_code()
    
    # Check if all required objects are present in the request data
    if not all(obj in data.keys() for obj in required_objects):
        return jsonify({'error': 'Missing required objects'}), 400

    # All required objects are present, continue with processing the request
    # insert data into database 
    insertion_response = insert_url(jsonify(data).get_json())
    if (insertion_response.status_code != 201):
        return jsonify({'Error': 'Invalid arguments'})
    
    return jsonify({'success': True}), 201

# Handling PUT request 
def update_data(slug):
    data = find_url(slug).json() 
    
    # data Not found because of wrong slug
    if (data['document'] == None):
        return jsonify({'error': 'invalid Slug !!'}), 404
    
    # if we found the data successfully then we can update our entries 
    # NOTE : we can update only web, ios and android objects only
    if('slug'in request.get_json()):
        return  jsonify({'error': 'Cannot update slug'}), 400
    update_url(slug, request.get_json())
    
    return jsonify({'success': True}), 200


def get_url(slug):
    found_url = find_url(slug).json()
    
    # Url Not found
    if (found_url['document'] == None):
        return jsonify({'error': 'invalid Slug !!'}), 404
    
    # TODO : replace it with web link
    return {"message" : found_url['document']['web']}, 200 