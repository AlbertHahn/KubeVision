from . import auth, render_template, request, url_for, redirect, session, flash
import os
from pymongo import MongoClient, errors
from werkzeug.security import generate_password_hash, check_password_hash


from .helper import successful_redirect_user, error_entry_exists

# Environmental variables for defining the endpoints
homeEndpoint = os.environ['homeEndpoint']
trainEndpoint = os.environ['trainEndpoint']
mongoEndpoint = os.environ['mongoEndpoint']

try:
    # try to instantiate a client instance
    client = MongoClient(str(mongoEndpoint))

    # print the version of MongoDB server if connection successful
    print ("server version:", client.server_info()["version"])

    # get the database_names from the MongoClient()
    database_names = client.list_database_names()

    db = client.get_database('user_db')
    records = db.register

except errors.ServerSelectionTimeoutError as err:
    # catch pymongo.errors.ServerSelectionTimeoutError
    print ("pymongo ERROR:", err)

@auth.route('/auth/login', methods=['POST'])
def login():
    """
    login function for authentication with http post
    """

    # get form variables
    user = request.form.get("username")
    password = request.form.get("password")
    user_exists = records.find_one({"name": user})

    errorMsg = "Username or Password not found!"

    if user_exists:
        hash_user_password = user_exists.get('password')

        if  check_password_hash(hash_user_password, password):
            response = redirect(homeEndpoint)
            response.set_cookie('session_user', user)
            return response
        else:
            return error_entry_exists(homeEndpoint, errorMsg)
    return error_entry_exists(homeEndpoint, errorMsg)

@auth.route('/auth/register', methods=['POST'])
def register():
    """
    register function for authentication with http post
    """
    
    # get form variables
    user = request.form.get("username")
    password = request.form.get("password")

    user_exists = records.find_one({"name": user})
    if user_exists:
        errorMsg = "Username exists!"
        return error_entry_exists(homeEndpoint, errorMsg)
    else:
        hash = generate_password_hash(password)
        insert_user = {'name': user, 'password': hash}
        records.insert_one(insert_user)

        return successful_redirect_user(homeEndpoint, user)

@auth.route('/auth/logout', methods=['GET','POST'])
def logout():
    """
    logout function for authentication with http get
    """

    if "session_user" in request.cookies:
        response = redirect(homeEndpoint)
        response.delete_cookie('session_user')
        return response
    else:
        return redirect(homeEndpoint)
