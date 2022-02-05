from requests.sessions import Session
from . import auth, render_template, request, url_for, redirect, session, flash
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash

from .helper import successful_redirect_user, error_entry_exists

DOMAIN = '0.0.0.0'
PORT = 27017

# try to instantiate a client instance
client = MongoClient("mongodb://localhost:27017/",
username="admin", password="password")

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

    user_data = records.find_one({"user": user})
    hash_user_password = records.find_one({"password": password})
    
    check_password_hash(hash_user_password, password)

    if user_data and check_password_hash:
 
        response = redirect('http://localhost:5000/train')
        response.set_cookie('session_user', user)
        return response

@auth.route('/auth/register', methods=['GET', 'POST'])
def register():

    user = request.form.get("fullname")
    password = request.form.get("password1")

    user_exists = records.find_one({"name": user})
    if user_exists:
        return error_entry_exists()
    else:
        hash = generate_password_hash(password)
        insert_user = {'name': user, 'password': hash}
        records.insert_one(insert_user)

        return successful_redirect_user('http://localhost:5000/train', user)

@auth.route('/logout', methods=['GET', 'POST'])
def logout():

    if "session_user" in request.cookies:
        response = redirect('http://localhost:5000/')
        response.delete_cookie('session_user')
        return response
    else:
        return redirect('http://localhost:5000/')



"""
        user = request.form.get("fullname")
        email = request.form.get("email")
        
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        
        user_found = records.find_one({"name": user})
        email_found = records.find_one({"email": email})
        if user_found:
            message = 'There already is a user by that name'
            return render_template('index.html', message=message)
        if email_found:
            message = 'This email already exists in database'
            return render_template('index.html', message=message)
        if password1 != password2:
            message = 'Passwords should match!'
            return render_template('index.html', message=message)
        else:
            hashed = bcrypt.hashpw(password2.encode('utf-8'), bcrypt.gensalt())
            user_input = {'name': user, 'email': email, 'password': hashed}
            records.insert_one(user_input)
            
            user_data = records.find_one({"email": email})
            new_email = user_data['email']
"""
