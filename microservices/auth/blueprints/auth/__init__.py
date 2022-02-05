from flask import Blueprint, render_template, request, url_for, redirect, session, flash

auth = Blueprint('auth', __name__)