import eventlet
import socketio

def create_socketio_server(app, port):

    sio = socketio.Server()

    @sio.event
    def connect(sid, environ):
        print(sid, 'connected')


    @sio.event
    def disconnect(sid):
        print(sid, 'disconnected')

    eventlet.wsgi.server(eventlet.listen(('', port)), app)