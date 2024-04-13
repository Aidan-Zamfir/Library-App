from . import db #from current package (website folder) import db (found in init.py)
from flask_login import UserMixin
from datetime import datetime

#Database models: 2 models -> User and Book, 1 table -> link many-to-many


user_book = db.Table('user_book',
    db.Column('id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('book_id', db.Integer, db.ForeignKey("book.book_id"), primary_key=True)
)

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column("id", db.Integer, primary_key=True)
    user_name = db.Column("user_name", db.String(300), unique=True, nullable=False)
    email = db.Column("email", db.String(150), unique=True, nullable=False)
    password = db.Column("password", db.String(300), nullable=False)
    books = db.relationship('Book', secondary=user_book, backref='id')

    def __repr__(self):
        return f"user: {self.id, self.user_name, self.email, self.password}"

class Book(db.Model):
    __tablename__ = 'book'

    book_id = db.Column('book_id', db.Integer, primary_key=True)
    pages_read = db.Column("pages_read", db.Integer)
    time_read = db.Column("reading_time", db.Integer)
    date = db.Column("date", db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f" book: {self.book_id, self.pages_read, self.time_read, self.date}"
