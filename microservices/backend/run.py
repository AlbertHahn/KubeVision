import os
from flask import Flask
import socketio
from gevent import pywsgi

#import eventlet
#from flask_socketio import SocketIO

"""from modules import face_recognition
from modules import face_training

face_rec = face_recognition()
face_train = face_training()"""
app = Flask(__name__)

#socketio = SocketIO(app)

sio = socketio.Server(async_mode='gevent',cors_allowed_origins='*')

from modules.socket_communication.views import socket_communication
app.register_blueprint(socket_communication)


app = socketio.WSGIApp(sio, app)

"""@sio.on('my event')
def handle_my_custom_event(json, data):
    print('received json: ' + str(json) + str(data))



@sio.on('stream')
def handle_my_custom_event(json):
    print('received json: ' + str(json))"""


"""
@socketio.on('message')
def handle_my_custom_event(json, data):
    print('received json: ' + str(json) + str(data))"""

if __name__ == "__main__":
    #socketio.run(app, cors_allowed_origins='*')
    pywsgi.WSGIServer(('', 5000), app).serve_forever()




