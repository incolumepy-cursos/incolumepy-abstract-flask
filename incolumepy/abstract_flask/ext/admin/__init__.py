#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "@britodfbr"
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from incolumepy.abstract_flask.ext.dbase import db
from incolumepy.abstract_flask.ext.dbase.models import User

admin = Admin()


def init_app(app):
    admin.name = "Abstract Admin"
    admin.template_mode = "bootstrap4"
    admin.init_app(app)
    admin.add_view(ModelView(User, db.session))

