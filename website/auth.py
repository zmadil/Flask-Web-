from flask import Blueprint, render_template, flash, request     #We import request to get the information that was sent in the form

auth = Blueprint('auth', __name__)

@auth.route('/login', methods= ['GET','POST'])
def login():
    return render_template("login.html")
    

@auth.route('/logout')
def logout():
    return "<p>Logout </p>"

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
            flash ('Account created', category='success')
            

    return render_template("sign_up.html")
