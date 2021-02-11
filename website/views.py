#place where users can navigate to other than login as it requires authentication 

from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")