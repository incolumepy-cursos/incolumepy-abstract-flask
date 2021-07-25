#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'
from flask_login import LoginManager
from incolumepy.abstract_flask.ext.dbase.models import User
from .routes import bp
loginmanager = LoginManager()


@loginmanager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


def init_app(app):
    loginmanager.init_app(app)
    app.register_blueprint(bp)

