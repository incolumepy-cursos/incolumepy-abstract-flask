#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "@britodfbr"
from incolumepy.abstract_flask.ext.dbase import db, bc
from incolumepy.abstract_flask.ext.posts.models import Post


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(150), nullable=False)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    avatar = db.Column(db.String(20), nullable=False, default="user_color.svg")
    birthdate = db.Column(db.Datetime(), nullable=False)
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship("Post", backref="author", lazy=True)

    def __init__(
        self, fullname, username, email, avatar, birthdate, password, **kwargs
    ):
        password = bc.generate_password_hash(self.password).decode("utf-8")
        super().__init__(password=password, **kwargs)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"
