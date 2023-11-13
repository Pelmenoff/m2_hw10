from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pymongo.errors import ConnectionFailure

def get_mongodb():
    password = ""
    with open("quotes/db_key.txt", "r") as pass_file:
        password = pass_file.read()
    client = MongoClient(password, server_api=ServerApi('1'))
    client.admin.command('ismaster')
    db = client.Mongodb
    return db