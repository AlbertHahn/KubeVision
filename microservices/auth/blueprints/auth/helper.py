from . import auth, render_template, request, url_for, redirect, session, flash


def successful_redirect_user(endpoint, user):
    response = redirect(endpoint)
    response.set_cookie('session_user', user)
    return response

def error_entry_exists():
    endpoint = 'http://localhost:5000'
    errorMsg = "Username Already Exists!"

    response = redirect(endpoint)
    response.set_cookie('session_error', errorMsg)
    return response