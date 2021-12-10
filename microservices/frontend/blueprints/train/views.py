from . import train, render_template

@train.route("/train")
def train_home():
    return render_template('train.html')

"""@mainpage.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404"""