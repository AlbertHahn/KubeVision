from . import socket_communication
from run import socketio

@socket_communication.route('/')
def index():
        return "Hello"

@socketio.on('my event')
def handle_my_custom_event(json):
    print('received json: ' + str(json))

@socketio.on('stream')
def handle_my_custom_event(json):
    print('received json: ' + str(json))

"""from run import sio

@sio.on('my event')
def handle_my_custom_event(json, data):
    print('received json: ' + str(json) + str(data))

@sio.on('stream')
def handle_my_custom_event(json):
    print('received json: ' + str(json))"""