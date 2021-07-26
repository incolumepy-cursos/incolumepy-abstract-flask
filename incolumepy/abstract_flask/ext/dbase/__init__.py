#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt


bc = Bcrypt()
loginmanager = LoginManager()
db = SQLAlchemy()
migrate = Migrate()


def init_app(app):
    db.init_app(app)
    migrate.init_app(app, db)
    bc.init_app(app)
    loginmanager.init_app(app)
