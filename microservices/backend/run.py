import os
from flask import Flask, render_template
import socketio

from flask_uwsgi_websocket import GeventWebSocket

from modules import face_recognition
from modules import face_training

face_rec = face_recognition()
face_train = face_training()

websocket = GeventWebSocket()

app = Flask(__name__)


websocket.init_app(app)

clients = []

# sample websocket endpoing
@websocket.route('/echo')
def echo(ws):
    clients.append(ws)
    while True:
        msg = ws.receive()
        ws.send(msg)


"""sio = socketio.Server(async_mode='gevent_uwsgi',cors_allowed_origins='*')

app = socketio.WSGIApp(sio, app)

@sio.on('my event')
def handle_my_custom_event(json, data):
    print('received json: ' + str(json) + str(data))

@sio.on('stream')
def handle_my_custom_event(json):
    print('received json: ' + str(json))"""


if __name__ == "__main__":
    app.run(host='0.0.0.0')




