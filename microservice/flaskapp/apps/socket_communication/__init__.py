from flask import Blueprint

socket_communication = Blueprint('socket_communication', __name__)

from . import views