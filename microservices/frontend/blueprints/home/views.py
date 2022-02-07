from . import home, render_template, request, redirect, url_for
import os

loginEndpoint = os.environ['loginEndpoint']
registerEndpoint = os.environ['registerEndpoint']

authObj = {'login':loginEndpoint, 'register':registerEndpoint}

@home.route("/")
def show_home():
    if "session_error" not in request.cookies:
        return render_template('home.html', authObj=authObj)
    else:
        error = request.cookies.get('session_error')
        return render_template('home.html', message=error, authObj=authObj)

@home.route("/register")
def show_register():
    if "session_error" not in request.cookies:
        return render_template('register.html', authObj=authObj)
    else:
        error = request.cookies.get('session_error')
        return render_template('register.html', message=error, authObj=authObj)


@home.route("/profile")
def show_profile():
    if "session_user" not in request.cookies:
        return render_template('home.html', authObj=authObj)
    else:
        name = request.cookies.get('session_user')
        return render_template('profile.html', message=name)
