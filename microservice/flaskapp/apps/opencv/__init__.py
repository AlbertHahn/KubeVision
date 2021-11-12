from flask import Blueprint, render_template, Response

opencv = Blueprint('opencv', __name__, url_prefix="/opencv")

