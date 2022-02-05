from flask.helpers import url_for
from werkzeug.utils import redirect
from . import train, render_template, request, session

@train.route("/train")
def train_home():
    name = request.cookies.get('session_user')
    
    #if name == None:
    #    return redirect(url_for("home.show_home"))

    #return render_template('train.html', message=name)

    if "session_user" not in request.cookies:
        return redirect(url_for("home.show_home"))
    else:
        return render_template('train.html', message=name)

    

"""@mainpage.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404"""