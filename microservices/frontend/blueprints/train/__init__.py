from flask import Blueprint, render_template, request, session

train = Blueprint('train', __name__, template_folder="templates")