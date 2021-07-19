#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'
import datetime as dt
from incolumepy.abstract_flask.ext.dbase import db


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_published = db.Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    date_updated = db.Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.posted}')"
