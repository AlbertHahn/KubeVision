from . import home, render_template

@home.route("/home")
def show_home():
    return render_template('home.html')

"""@mainpage.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404"""