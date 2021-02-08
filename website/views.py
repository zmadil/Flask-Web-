#place where users can navigate to other than login as it requires authentication 

from flask import Blueprint

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return "<h1> Test </h1>"