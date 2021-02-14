from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path                                                                 #For database
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME= "database.db "


def create_app():
    app = Flask(__name__)                                                           #Initialize
    app.config['SECRET_KEY']= 'abcdefgh'                                            #Need this line for all applications
    app.config['SQLALCHEMY_DATABASE_URI']= f'sqlite:///{DB_NAME}'
    db.init_app(app)                                                                #Telling flask that this app will be used for our database


    from .views import views                                                     #Import Blueprint
    from .auth import auth



    app.register_blueprint(views, url_prefix='/')                                  #Registring our blueprint
    app.register_blueprint(auth, url_prefix='/')


   from .models import User, Note

    create_database(app)


    return app

def create_database(app):
    if not path.exists('website'+ DB_NAME):
        db.create_all(app=app) 
        print('Created Database!')