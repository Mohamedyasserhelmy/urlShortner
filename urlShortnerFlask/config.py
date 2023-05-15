from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


def test_connection():
    uri = "mongodb+srv://admin:7pkTlnFO1yPB9tOv@cluster0.chfdekv.mongodb.net/?retryWrites=true&w=majority"
    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))
    test = False
    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        test = True
    except Exception as e:
        print(e)
    client.close()    
    return test    

