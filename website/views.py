from flask import Blueprint, render_template
from flask_login import login_required, current_user


views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("index.html")

@views.route('/library')
@login_required
def library():
    return render_template("library.html")

@views.route('/new_user')
def new_user():
    return render_template("new_user.html")