from . import db #from current package (website folder) import db (found in init.py)
from flask_login import UserMixin
from datetime import datetime

user_book = db.Table('user_book',
    db.Column('user_id', db.Integer, db.ForeignKey('user.user_id'), primary_key=True),
    db.Column('book_id', db.Integer, db.ForeignKey("book.book_id"), primary_key=True)
)

class User(db.Model, UserMixin):
    user_id = db.Column("user_id", db.Integer, primary_key=True)
    user_name = db.Column("user_name", db.String(300), unique=True, nullable=False)
    email = db.Column("email", db.String(150), unique=True, nullable=False)
    # password = db.Column("password", db.String(300), nullable=False)
    books = db.relationship('Book', secondary=user_book, backref='user_id')

class Book(db.Model):
    book_id = db.Column('book_id', db.Integer, primary_key=True)
    pages_read = db.Column("pages_read", db.Integer)
    time_read = db.Column("reading_time", db.Integer)
    date = db.Column("date", db.DateTime, nullable=False, default=datetime.utcnow)
    # user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)


# class Library(db.Model): #not m-t-m
#     book_id = db.Column("book_id", db.Integer, primary_key=True)
#     book_name = db.Column("book_name", db.String(150))
#     total_time = db.Column("reading_time", db.Integer)


#add to libaray byt searching for values in book & user: then inset the data

# time spent reading & date data into graphical rep of reading history
# for USER, get every LOG on DATE