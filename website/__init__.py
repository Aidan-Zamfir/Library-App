from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from os import path

db = SQLAlchemy() #initialize database
DB_NAME = "database.db"

def create_app():

    #initialize application
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '123' # yes I know
    #connect to databse
    app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    #check if databse already exists, if not: create it
    from .models import User, Book
    with app.app_context():
        if not path.exists("website/" + DB_NAME):
            db.create_all()

    #login manager
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id)) #'get' looks for primary key (checks db)

    return app
