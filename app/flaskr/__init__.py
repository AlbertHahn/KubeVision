import os
import socketio
import eventlet

from flask_socketio import SocketIO

from flask import Flask, render_template, Response

socketio = SocketIO(cors_allowed_origins="*")

def create_app(test_config=None):
    # create and configure the app
    #sio = socketio.Server()
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import face
    app.register_blueprint(face.bp)

    from .custom_socket import custom_socket
    app.register_blueprint(custom_socket)

    @app.route('/')
    def index():
        return render_template('index.html')

    socketio.init_app(app, cors_allowed_origins="*")

    return app
