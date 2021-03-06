#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'
from pathlib import Path
from flask import Flask, send_from_directory, send_file, redirect, url_for
from . import configure
from .ext import webui, dbase, cli, admin, auth
from .ext.dbase.models import loginmanager


def minimal_app():
    app = Flask(__name__)
    configure.init_app(app)
    dbase.init_app(app)
    cli.init_app(app)
    auth.init_app(app)
    return app


def create_app():
    app = minimal_app()
    admin.init_app(app)
    webui.init_app(app)

    # app.add_url_rule('/favicon.ico',
    #                  redirect_to=url_for('static', filename='images/favicons/favicon.ico'))
    @app.route("/favicon.ico")
    def favicon():
        ico = Path(app.root_path) / url_for('static', filename='images/favicons/favicon.ico').lstrip('/')
        return send_file(ico, mimetype='image/vnd.microsoft.icon')

    @app.route("/f.ico")
    def f():
        return redirect(url_for('static', filename="images/favicons/favicon.ico"))

    @app.route("/fa.ico")
    def fa():
        ico = Path(app.root_path) / url_for('static', filename='images/favicons/favicon.ico').lstrip('/')
        return send_file(ico, mimetype='image/vnd.microsoft.icon')

    @app.route("/fav.ico")
    def fav():
        ico = Path(app.root_path) / 'static/images/favicons/favicon.ico'
        return send_file(ico, mimetype='image/vnd.microsoft.icon')

    @app.route('/favi.ico')
    def favi():
        return send_from_directory(app.root_path, path="images/favicons", filename="favicon.ico", mimetype='image/vnd.microsoft.icon')

    @app.route("/favic.ico")
    def favic():
        return url_for('static', filename='images/favicons/favicon.ico')

    @app.route('/hello')
    def hello():
        return "Hello World!!"

    return app
