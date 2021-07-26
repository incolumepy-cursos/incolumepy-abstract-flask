#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'
from incolumepy.abstract_flask.ext.dbase.models import User
from .routes import bp
from incolumepy.abstract_flask import loginmanager


@loginmanager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


def init_app(app):
    app.register_blueprint(bp)
