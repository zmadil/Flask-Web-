from flask import Flask

def create_app():
    app = Flask(__name__)                                                           #Initialize
    app.config['SECRET_KEY']= 'abcdefgh'                                            #Need this line for all applications


    from .views import views                                                     #Import Blueprint
    from .auth import auth



    app.register_blueprint(views, url_prefix='/')                                  #Registring our blueprint
    app.register_blueprint(auth, url_prefix='/')



    return app