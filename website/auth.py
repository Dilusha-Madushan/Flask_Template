from flask import Blueprint , render_template , request , flash , redirect , url_for
from .models import User
from werkzeug.security import generate_password_hash , check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth' , __name__)

@auth.route('/login' , methods=['GET' , 'POST'])
def login():
    
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>Sign Up</p>"

@auth.route('/sign-up' , methods=['GET' , 'POST'])
def SignUp():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if(len(email)<4):
            flash("Email must be greater than 4 characters." , category='error')
        elif len(firstName)<2:
            flash("Firs Name must be greater than 4 characters." , category='error')
        elif password1!=password2:
            flash("Password is not match." , category='error')
        elif len(password1)<7:
            flash("Password must be greater than 4 characters." , category='error')
        else:
            new_user = User(email=email, password=generate_password_hash(password1 , method='sha256'), first_name=firstName)
            db.session.add(new_user)
            db.session.commit()
            flash("Account created" , category='success')
            return redirect(url_for('views.home')) 
    return render_template("sign_up.html")