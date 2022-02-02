from . import socket_communication
from run import sio

from . import face_recognition
from . import face_training

@socket_communication.route('/socketio')
def index():
        return "Hello"

@sio.on('traindata')
def my_message(sid, data):
    train = face_training()
    train.train()
    print('message ', data)

@sio.on('stream')
def handle_my_custom_event(sid, data):
    rec = face_recognition()
    rec.encode_webp(data)
    return {'status': 'ok'}

@sio.on('predict')
def predicted_or_not(sid, data):
    rec = face_recognition()
    rec.detect_face(rec.encode_login(data))
    