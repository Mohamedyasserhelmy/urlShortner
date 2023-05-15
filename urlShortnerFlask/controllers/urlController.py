from flask import Flask, Response, request, jsonify
from config import *
from models.getAll import get_all, result

# main page of backend
def index():
    return '<p> Hello world !! </p>'

# Returns the url passed from react input value form   
def post_url():
    data = request.get_json()
    return data['inputValue']

# Getting Data from Atlas mongoDB Connection
def get_data():
    conn = test_connection()
    if conn == True :  # Hence we can use our database
        return result
    else:
        return "bad request" , 400

# Creating post request to add data 
def post_data():
    required_objects = ['ios', 'android', 'web']
    data = request.get_json()

    # Check if all required objects are present in the request data
    if not all(obj in data.keys() for obj in required_objects):
        return jsonify({'error': 'Missing required objects'}), 400

    # All required objects are present, continue with processing the request
    return jsonify({'success': True}), 200