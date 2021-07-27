#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'
import datetime as dt
from flask_login import UserMixin
from . import db, loginmanager, bc


@loginmanager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(150), nullable=False)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(160), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    birthdate = db.Column(db.DateTime(), nullable=False)
    avatar = db.Column(db.String(20), nullable=False, default="user_color.svg")
    admin = db.Column(db.Boolean(), nullable=False, default=False)
    superadmin = db.Column(db.Boolean(), nullable=False, default=False)
    outcast = db.Column(db.Boolean(), nullable=False, default=False)   # pária(outcast)/banido(banished)
    posts = db.relationship("Post", backref="author", lazy=True)
    comments = db.relationship("Comment", backref="comment", lazy=True)

    @property
    def password(self):
        raise AttributeError('password not readable')

    @password.setter
    def password(self, pwd):
        self.password = bc.generate_password_hash(pwd).decode('utf-8')

    def check_password(self, pwd):
        return bc.check_password_hash(self.password, pwd)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.avatar}')"

    def count_posts(self):
        ...

    def count_comments(self):
        ...


# class Group(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(150), nullable=False)
#     users = db.relationship("User", backref="users", lazy=True)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_published = db.Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    date_updated = db.Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    media = db.Column(db.String(), default='')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    posts = db.relationship('Comment', backref='post', lazy=True)

    def __repr__(self):
        return f"Post('{self.title}', '{self.posted}')"


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_published = db.Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    date_updated = db.Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)

    def __repr__(self):
        return f"Comment('{self.title}', '{self.posted}')"


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)

    def __repr__(self):
        return f"Category('{self.name}')"

users = [
    {"id": 1,
     "fullname": "Ricardo Brito do Nascimento",
     "username": "britodfbr",
     "email": "britodfbr+1@gmail.com",
     "password": "123",
     "avatar": "user_color.svg",
     "admin": True,
     "outcast": False},
    {"id": 2,
     "fullname": "Eliana Brito",
     "username": "elianabrito",
     "email": "britodfbr+2@gmail.com",
     "password": "123",
     "avatar": "user_color.svg",
     "admin": False,
     "outcast": False},
    {"id": 3,
     "fullname": "Ana Brito",
     "username": "anabrito",
     "email": "britodfbr+3@gmail.com",
     "password": "123",
     "avatar": "user_color.svg",
     "admin": False,
     "outcast": False},
    {"id": 4,
     "fullname": "Ada Brito",
     "username": "adabrito",
     "email": "britodfbr+4@gmail.com",
     "password": "123",
     "avatar": "user_color.svg",
     "admin": False,
     "outcast": False},
]
posts = [
    {"id": "1",
     "title": "Parabéns",
     "date_published": "2021-7-5 14:15",
     "date_updated": "2021-7-5 14:15",
     "content": "Meu aniversário",
     "media": "lamp-600.jpg",
     "user_id": "4"},
    {"id": "2",
     "title": "Aniversário",
     "date_published": "2021-7-5 14:15",
     "date_updated": "2021-7-5 14:15",
     "content": "Meu aniversário",
     "media": "tulips-600.jpg",
     "user_id": "3"},
    {"id": "3",
     "title": "Parabéns",
     "date_published": "2021-7-5 14:15",
     "date_updated": "2021-7-5 14:15",
     "content": "Meu aniversário",
     "media": "tulips-600.jpg",
     "user_id": "2"},
    {"id": "4",
     "title": "Parabéns",
     "date_published": "2021-7-5 14:15",
     "date_updated": "2021-7-5 14:15",
     "content": "Meu aniversário",
     "media": "dew-600.jpg",
     "user_id": "1"},
    {"id": 5,
     "title": "Just a Standard Format Post",
     "content": "Lorem ipsum Sed eiusmod esse aliqua sed incididunt aliqua incididunt mollit id et sit proident dolor"
                " nulla sed commodo est ad minim elit reprehenderit nisi officia aute incididunt velit sint in aliqua"
                " cillum in consequat consequat in culpa in anim.",
     "date_published": "2021-7-22 15:38",
     "date_updated": "2021-7-22 15:38",
     "media": "woodcraft-600.jpg",
     "user_id": "2"
     },
    {"id": 6,
     "title": "Using Repetition and Patterns in Photography",
     "content": "Lorem ipsum Sed eiusmod esse aliqua sed incididunt aliqua incididunt mollit id et sit proident dolor"
                " nulla sed commodo est ad minim elit reprehenderit nisi officia aute incididunt velit sint in aliqua"
                " cillum in consequat consequat in culpa in anim.",
     "date_published": "2020-10-22 15:38",
     "date_updated": "2021-7-22 15:38",
     "media": "woodcraft-600.jpg",
     "user_id": 2},
]
