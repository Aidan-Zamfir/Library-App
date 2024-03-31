from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html', text='testing') #can add variubale name to pass in varibale to that page (and then access it in login.html)

@auth.route('/logout')
def logout():
    return "<p>Logout<p>"

@auth.route('sign-up')
def sign_up():
    return render_template('sign_up.html')

