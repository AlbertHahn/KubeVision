from . import home, render_template, request, redirect, url_for
from .forms import LoginForm


@home.route("/")
def show_home():

    error = request.cookies.get('session_error')

    if error == None:
        return render_template('home.html')

    return render_template('home.html', message=error)
    

"""@mainpage.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404"""