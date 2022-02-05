from flask import Blueprint, render_template, request, redirect, url_for

home = Blueprint('home', __name__, template_folder="templates")