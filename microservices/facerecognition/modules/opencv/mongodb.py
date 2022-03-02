from pymongo import MongoClient, errors
import os
mongoEndpoint = os.environ['mongoEndpoint']

class mongodb:

    def __init__(self):
        self
    
    def erstablish_connnection(self):
        """
        Pymongo function to establish a connection to a MongoDB-Server
        try to receive db and return as object
        """

        try:
            client = MongoClient(mongoEndpoint)

            # print the version of MongoDB server if connection successful
            print ("server version:", client.server_info()["version"])
            db = client.get_database('user_db')

            return db.register  

        except errors.ServerSelectionTimeoutError as err:
            # catch pymongo.errors.ServerSelectionTimeoutError
            print ("pymongo ERROR:", err)#

            return err

             
     

