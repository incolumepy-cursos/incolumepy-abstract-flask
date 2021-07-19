#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'
from incolumepy.abstract_flask.ext.dbase import db


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
