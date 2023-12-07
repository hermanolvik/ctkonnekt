from app import db
from flask_login import UserMixin
from datetime import datetime

"""
This module contains the model of the application, which is created with the help of
SQLAlchemy, which provides object-relational mapping for Flask.
"""


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(1000), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    family_name = db.Column(db.String(50), nullable=False)

    # Table relationships for easy access
    posts = db.relationship('Post', backref='author', lazy=True)
    comments = db.relationship('Comment', backref='author', lazy=True)
    liked_posts = db.relationship('Post', secondary=likes, lazy='subquery',
                                  backref=db.backref('likers', lazy=True))


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    comments = db.relationship('Comment', backref='post', lazy=True, cascade="all, delete-orphan")

    # String representation for debug purposes
    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


# An association table to accommodate 'likes'
likes = db.Table('likes',
                 db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
                 db.Column('post_id', db.Integer, db.ForeignKey('post.id'), primary_key=True)
                 )


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)

    # String representation for debug purposes
    def __repr__(self):
        return f"Comment('{self.content}', '{self.date_posted}')"
