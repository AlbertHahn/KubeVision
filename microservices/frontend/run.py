import os
from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from blueprints.train.views import train
app.register_blueprint(train)

from blueprints.home.views import home
app.register_blueprint(home)



if __name__ == "__main__":
    app.run(host='0.0.0.0', cors_allowed_origins='*', debug=True)




