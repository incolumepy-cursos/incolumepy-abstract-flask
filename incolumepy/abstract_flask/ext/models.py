#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "@britodfbr"
import datetime as dt
from incolumepy.abstract_flask.ext.dbase import db, bc


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
     "media": "",
     "user_id": "4"},
    {"id": "1",
     "title": "Aniversário",
     "date_published": "2021-7-5 14:15",
     "date_updated": "2021-7-5 14:15",
     "content": "Meu aniversário",
     "media": "",
     "user_id": "3"},
    {"id": "1",
     "title": "Parabéns",
     "date_published": "2021-7-5 14:15",
     "date_updated": "2021-7-5 14:15",
     "content": "Meu aniversário",
     "media": "",
     "user_id": "2"},
    {"id": "1",
     "title": "Parabéns",
     "date_published": "2021-7-5 14:15",
     "date_updated": "2021-7-5 14:15",
     "content": "Meu aniversário",
     "media": "",
     "user_id": "1"},

]


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(150), nullable=False)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(160), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    birthdate = db.Column(db.DateTime(), nullable=False)
    avatar = db.Column(db.String(20), nullable=False, default="user_color.svg")
    admin = db.Column(db.Boolean(), nullable=False, default=False)
    outcast = db.Column(db.Boolean(), nullable=False, default=False)   # pária(outcast)/banido(banished)
    posts = db.relationship("Post", backref="author", lazy=True)
    comments = db.relationship("Comment", backref="comment", lazy=True)

    def __init__(
        self, fullname, username, email, avatar, birthdate, password, **kwargs
    ):
        password = bc.generate_password_hash(self.password).decode("utf-8")
        super().__init__(password=password, **kwargs)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

    def count_posts(self):
        ...

    def count_comments(self):
        ...


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
        return f"Post('{self.title}', '{self.posted}')"


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
