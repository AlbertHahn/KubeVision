import os
from flask import Flask
import socketio
from gevent import pywsgi

# Create Flask app and Socketio server Instance
app = Flask(__name__)
sio = socketio.Server(async_mode='gevent',cors_allowed_origins='*')

# Import the SocketIo Blueprints and register them in the Flask app
from modules.socket_communication.views import socket_communication
app.register_blueprint(socket_communication)

# Wrap Flask app to WSGI-SocketServer
app = socketio.WSGIApp(sio, app)

if __name__ == "__main__":
    pywsgi.WSGIServer(('', 5000), app).serve_forever()




