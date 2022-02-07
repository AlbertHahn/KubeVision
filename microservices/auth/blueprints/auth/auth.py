from . import auth, render_template, request, url_for, redirect, session, flash
import os
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash


from .helper import successful_redirect_user, error_entry_exists

homeEndpoint = os.environ['homeEndpoint']
trainEndpoint = os.environ['trainEndpoint']
profileEndpoint = os.environ['profileEndpoint']
mongoEndpoint = os.environ['mongoEndpoint']

# try to instantiate a client instance
#client = MongoClient("mongodb://admin:password@mongodbservice:27017/?authSource=admin")
client = MongoClient(str(mongoEndpoint))

# print the version of MongoDB server if connection successful
print ("server version:", client.server_info()["version"])

# get the database_names from the MongoClient()
database_names = client.list_database_names()

db = client.get_database('total_records')
records = db.register

@auth.route('/auth/login', methods=['GET', 'POST'])
def login():

    user = request.form.get("fullname")
    password = request.form.get("password1")
    user_exists = records.find_one({"name": user})

    errorMsg = "Username or Password not found!"

    if user_exists:
        hash_user_password = user_exists.get('password')

        if  check_password_hash(hash_user_password, password):
            response = redirect(profileEndpoint)
            response.set_cookie('session_user', user)
            return response
        else:
            return error_entry_exists(homeEndpoint, errorMsg)
    return error_entry_exists(homeEndpoint, errorMsg)

@auth.route('/auth/register', methods=['GET', 'POST'])
def register():

    user = request.form.get("fullname")
    password = request.form.get("password1")

    user_exists = records.find_one({"name": user})
    if user_exists:
        errorMsg = "Username exists!"
        return error_entry_exists(homeEndpoint, errorMsg)
    else:
        hash = generate_password_hash(password)
        insert_user = {'name': user, 'password': hash}
        records.insert_one(insert_user)

        return successful_redirect_user(profileEndpoint, user)

@auth.route('/auth/logout', methods=['GET', 'POST'])
def logout():

    if "session_user" in request.cookies:
        response = redirect(homeEndpoint)
        response.delete_cookie('session_user')
        return response
    else:
        return redirect(homeEndpoint)
