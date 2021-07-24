#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "@britodfbr"
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from incolumepy.abstract_flask.ext.dbase import db
from incolumepy.abstract_flask.ext.dbase.models import User, Post, Comment, Category

admin = Admin()


class UserAdmin(ModelView):
    """Interface administrativa para User"""


def init_app(app):
    admin.name = "Abstract Admin"
    admin.template_mode = "bootstrap4"
    admin.init_app(app)
    admin.add_view(UserAdmin(User, db.session))
    admin.add_view(ModelView(Post, db.session))
    admin.add_view(ModelView(Comment, db.session))
    admin.add_view(ModelView(Category, db.session))
