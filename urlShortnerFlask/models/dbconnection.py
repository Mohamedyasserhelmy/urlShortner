from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://admin:7pkTlnFO1yPB9tOv@cluster0.chfdekv.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    db = client.get_database('short_urls')
    collection = db['urlcollection']
    data_cursor = collection.find({})
    for document in data_cursor:
        print (document)
except Exception as e:
    print(e)