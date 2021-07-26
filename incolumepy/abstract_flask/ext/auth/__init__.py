#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'
from incolumepy.abstract_flask.ext.dbase.models import User
from .routes import bp


def init_app(app):
    app.register_blueprint(bp)
