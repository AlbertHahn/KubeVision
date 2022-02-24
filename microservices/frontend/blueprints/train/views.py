from flask.helpers import url_for
from werkzeug.utils import redirect
from . import train, render_template, request, session
import os

websocketServer = os.environ['websocketServer']
homeEndpoint = os.environ['homeEndpoint']

socketioEndpoints = {'websocketServer':websocketServer, 'homeEndpoint':homeEndpoint}

@train.route("/train")
def train_home():

    if "session_user" not in request.cookies:
        return redirect(url_for("home.show_home"))
    else:
        name = request.cookies.get('session_user')
        return render_template('train.html', message=name, socketioEndpoints=socketioEndpoints)

@train.route("/facelogin")
def face_login():
    return render_template('facelogin.html', socketioEndpoints=socketioEndpoints)

    

"""@mainpage.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404"""