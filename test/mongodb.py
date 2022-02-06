#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# import the MongoClient class
from pymongo import MongoClient, errors

# global variables for MongoDB host (default port is 27017)
DOMAIN = '0.0.0.0'
PORT = 27017

# use a try-except indentation to catch MongoClient() errors
try:
    # try to instantiate a client instance
    #client = MongoClient("mongodb://localhost:27017/",
    #username="admin", password="password")

    client = MongoClient("mongodb://admin:password@localhost:27017/")

    # print the version of MongoDB server if connection successful
    print ("server version:", client.server_info()["version"])

    # get the database_names from the MongoClient()
    database_names = client.list_database_names()

    mydb = client["mydatabase"]
    mycol = mydb["customers"]

    #mydict = { "name": "John", "address": "Highway 37" }

    #x = mycol.insert_one(mydict)
    x = mycol.find_one()

    print(x)

except errors.ServerSelectionTimeoutError as err:
    # set the client and DB name list to 'None' and `[]` if exception
    client = None
    database_names = []

    # catch pymongo.errors.ServerSelectionTimeoutError
    print ("pymongo ERROR:", err)

print ("\ndatabases:", database_names)