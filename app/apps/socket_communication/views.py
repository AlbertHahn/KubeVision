from . import socket_communication
from app import socketio

@socket_communication.route('/')
def index():
        return "Hello"

@socketio.on('my event')
def handle_my_custom_event(json):
    print('received json: ' + str(json))

@socketio.on('stream')
def handle_my_custom_event(json):
    print('received json: ' + str(json))