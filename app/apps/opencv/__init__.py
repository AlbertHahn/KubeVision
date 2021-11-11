from flask import Blueprint

opencv = Blueprint('opencv', __name__)

from . import views