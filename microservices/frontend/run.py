import os
from flask import Flask



app = Flask(__name__)

from apps.mainpage.views import mainpage
app.register_blueprint(mainpage)



if __name__ == "__main__":
    app.run(host='0.0.0.0',cors_allowed_origins='*')




