from . import socket_communication
from run import sio

from . import face_recognition
from . import face_training


@socket_communication.route('/socketio')
def index():
        return "Hello"

@sio.on('traindata')
def my_message(sid, data):
    face_training.train(face_training())
    print('message ', data)

@sio.on('stream')
def handle_my_custom_event(sid, data):
    #img, dirname, counter = face_recognition.encode_webp(face_recognition(), data)
    #face_recognition.detect_face(face_recognition(), img, dirname, counter)
    face_recognition.encode_webp(face_recognition(), data)

@sio.on('predict')
def predicted_or_not(sid, data):
    face_recognition.detect_face(face_recognition(), face_recognition.encode_login(face_recognition(), data))
    