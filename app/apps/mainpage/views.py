from . import mainpage, render_template

@mainpage.route("/")
def home():
    return render_template('index.html')

@mainpage.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404