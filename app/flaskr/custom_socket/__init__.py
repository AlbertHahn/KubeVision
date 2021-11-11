from flask import Blueprint

custom_socket = Blueprint('main', __name__)

from . import custom_socket