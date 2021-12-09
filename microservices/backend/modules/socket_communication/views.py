from . import socket_communication
from run import sio

@socket_communication.route('/socketio')
def index():
        return "Hello"

"""@sio.on('my event')
def handle_my_custom_event(json):
    print('received json: ' + str(json))

@sio.on('stream')
def handle_my_custom_event(json):
    print('received json: ' + str(json))"""
@sio.on('my event')
def my_message(sid, data):
    print('message ', data)

"""from run import sio

@sio.on('my event')
def handle_my_custom_event(json, data):
    print('received json: ' + str(json) + str(data))

@sio.on('stream')
def handle_my_custom_event(json):
    print('received json: ' + str(json))"""