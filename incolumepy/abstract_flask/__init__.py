#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'

import configure
from flask import Flask
from .ext import webui, dbase, cli, users, posts


def minimal_app(*args, **kwargs):
    app = Flask(__name__, *args, **kwargs)
    configure.init_app(app)
    dbase.init_app(app)
    cli.init_app(app)
    return app


def create_app(*args, **kwargs):
    app = minimal_app(*args, **kwargs)
    webui.init_app(app)

    # app.add_url_rule('/favicon.ico',
    #                  redirect_to=url_for('static', filename='images/favicons/favicon.ico'))

    # @app.route('/favicon.ico')
    # def favicon():
    #     ico = Path(app.root_path)
    #     return send_from_directory(ico, 'static', 'images/favicons/favicon.ico', mimetype='image/vnd.microsoft.icon')

    @app.route('/hello')
    def hello():
        return "Hello World!!"

    return app
