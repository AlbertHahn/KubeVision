import os
from flask import Flask
#from flask_socketio import SocketIO
import socketio



"""def create_app():
    # create the app
    app = Flask(__name__)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    #socketio.init_app(app)

    #from apps.mainpage.views import mainpage
    #app.register_blueprint(mainpage)

    #from apps.socket_communication.views import socket_communication
    #app.register_blueprint(socket_communication)

    #from apps.opencv.views import opencv
    #app.register_blueprint(opencv)


    return app"""
#socketio = SocketIO(cors_allowed_origins='*')

app = Flask(__name__)

from apps.mainpage.views import mainpage
app.register_blueprint(mainpage)


#socketio.init_app(app)

#sio = socketio.Server(async_mode='gevent_uwsgi',cors_allowed_origins='*')

#from apps.socket_communication.views import socket_communication
#app.register_blueprint(socket_communication)


#app = socketio.WSGIApp(sio, app)




if __name__ == "__main__":
    #socketio.run(app)
    #app = create_app()
    app.run(host='0.0.0.0')




