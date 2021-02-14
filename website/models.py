from . import db
from flask_login import UserMixin                                       # A flask module which helps the users log in

from SQLAlchemy.sql import func                                         #to get date and time



class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text= db.Column(db.String(100000))
    date= db.Column(db.DateTime(timezone=True), default= func.now())    #TO automatically get date and time
    user_id= db.Column(db.Integer, db.ForeignKey('user.id'))            #user.id has to be lower case for foreign key. Getting this value from User Class and ID field. Always have this on children



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email= db.Column(db.String(100), unique=True)
    password= db.Column(db.String(100))
    firstName= db.Column(db.String(100))
    lastName=db.Column(db.String(100))
    secretAnswer=db.Column(db.String(100))
    notes= db.relationship('Note')                                      #Establishing foregin key relation with line 12. Need capital for 'Note'