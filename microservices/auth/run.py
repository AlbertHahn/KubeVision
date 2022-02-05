from flask import Flask, render_template, request, url_for, redirect, session
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from blueprints.auth.auth import auth
app.register_blueprint(auth)


if __name__ == "__main__":
  app.run(host="0.0.0.0",debug=True)