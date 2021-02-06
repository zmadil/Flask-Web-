from flask import Flask

def create_app():
    app = Flask(__name__)                                                           #Initialize
    app.config['SECRET_KEY']= 'abcdefgh'                                            #Need this line for all applications


    return app