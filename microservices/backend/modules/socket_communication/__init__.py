from flask import Blueprint
from ..opencv import face_recognition
from ..opencv import face_training

socket_communication = Blueprint('socket_communication', __name__)

from . import views