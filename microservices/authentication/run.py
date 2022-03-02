from flask import Flask, render_template, request, url_for, redirect, session
from config import Config

# Create Flask App and get config
app = Flask(__name__)
app.config.from_object(Config)

# Import the blueprints and register them in the Flask app
from blueprints.auth.auth import auth
app.register_blueprint(auth)


if __name__ == "__main__":
  app.run(host="0.0.0.0",cors_allowed_origins='*')