from . import db #from current package (website folder) import db (found in init.py)
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    user_name = db.Column(db.String(150))
    user_pass = db.Column(db.String(150))
    library = db.relationship('Library') #capital
    book = db.relationship('Book') #capital

class Library(db.Model):
    book_id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(150))
    total_time = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id')) #lowercase when reference class name (table in db)
    book = db.relationship('Book') #capital

class Book():
    book_id = db.Column(db.Integer, db.ForeignKey('library.book_id')) #lowercase
    pages_read = db.Column(db.Integer)
    time_read = db.Column(db.Integer)
    date = db.Column(db.DateTime(timezone=False), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id')) #lowercase
