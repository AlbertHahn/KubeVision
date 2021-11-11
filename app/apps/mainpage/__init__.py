from flask import Blueprint,render_template

mainpage = Blueprint('mainpage', __name__, template_folder="templates/mainpage")