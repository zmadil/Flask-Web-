from . import db
from flask import Blueprint, render_template, flash, request, redirect, url_for     #We import request to get the information that was sent in the form
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)

@auth.route('/login', methods= ['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)
    

@auth.route('/logout')
@login_required                                                                                     #So User can not access this logout unless he is logged in
def logout():
    logout_user
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods= ['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email= request.form.get('email')
        firstName= request.form.get('firstName')
        password1= request.form.get('password1')
        password2= request.form.get('password2')

        if len(email) <4:
            flash ('Email greater than 4 letters', category = 'error')
        elif len(firstName) <2:
            flash ('first name greater than 2',category = 'error')
        elif password1 != password2 :
            flash ('passwords don\'t match', category = 'error')
        else:
            new_user = User(email=email, firstName=firstName, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))                                                  #Imported redirect. Views is directory and home is function
            

    return render_template("sign_up.html")
