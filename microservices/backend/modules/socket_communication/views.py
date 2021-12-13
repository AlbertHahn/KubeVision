from . import socket_communication
from run import sio

from . import face_recognition


@socket_communication.route('/socketio')
def index():
        return "Hello"

@sio.on('my event')
def my_message(sid, data):
    print('message ', data)

@sio.on('stream')
def handle_my_custom_event(sid, data):
    print('received stream: ' + data)
    face_recognition.detect_face(face_recognition(),face_recognition.encode_webp(data))
    

"""from run import sio

@sio.on('my event')
def handle_my_custom_event(json, data):
    print('received json: ' + str(json) + str(data))

@sio.on('stream')
def handle_my_custom_event(json):
    print('received json: ' + str(json))"""