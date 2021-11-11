import os
from flask import Flask
from flask_socketio import SocketIO

socketio = SocketIO(cors_allowed_origins='*')

def create_app():
    # create the app
    app = Flask(__name__)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    socketio.init_app(app)

    from apps.mainpage.views import mainpage
    app.register_blueprint(mainpage)

    from apps.socket_communication.views import socket_communication
    app.register_blueprint(socket_communication)

    from apps.opencv.views import opencv
    app.register_blueprint(opencv)

    return app


if __name__ == "__main__":
    socketio.run(create_app)


