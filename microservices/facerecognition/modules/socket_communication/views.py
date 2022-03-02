from . import socket_communication
from run import sio

from . import face_recognition
from . import face_training

# For testing purposes, check manually if endpoint exists
@socket_communication.route('/socketio')
def index():
        return "socketio"

# Listener for socket.io events
@sio.on('traindata')
def start_train(sid, data):
    """
    receive data create class object of face_training and start training
    """
    train = face_training()
    train.train()
    print('Training Completed')
    return {'status': 'Training Completed'}

@sio.on('stream')
def start_stream(sid, data):
    """
    receive pictures, create class object of face_recognition encode it and save them
    """
    rec = face_recognition()
    rec.format_webp(data)
    return {'status': 'ok'}

@sio.on('predict')
def start_prediction(sid, data):
    """
    receive pictures, create class object of face_recognition encode and predict if user exits
    """
    rec = face_recognition()
    picture = rec.format_login(data)
    name = rec.detect_face(picture)
    return {'status': name}
    