from pymongo import MongoClient
import os
mongoEndpoint = os.environ['mongoEndpoint']

class mongodb:

    def __init__(self):
        self
    
    def erstablish_connnection(self):
        client = MongoClient(mongoEndpoint)

        # print the version of MongoDB server if connection successful
        print ("server version:", client.server_info()["version"])

        # get the database_names from the MongoClient()
        database_names = client.list_database_names()

        print(database_names)

        db = client.get_database('total_records')

        #for document in db.register.find():
        #    print(document) # iterate the cursor


        return db.register   
     