from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=["GET", "POST"])
def login():
    data = request.form
    print(data)
    return render_template('login.html', boolean=True) #can add variubale name to pass in varibale to that page (and then access it in login.html)

@auth.route('/logout')
def logout():
    return "<p>Logout<p>"

@auth.route('sign-up', methods=["GET", "POST"])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        userName = request.form.get('userName')
        password = request.form.get('password')

        if len(email) < 4:
            flash("email too short", category='error')
        elif len(userName) < 6:
            flash("username too short", category='error')
        elif len(password) < 7:
            flash("pass too short", category='error')
        else:
            flash('created', category='succes')

    return render_template('sign_up.html')

