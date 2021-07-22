#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'
from pathlib import Path
from flask import Flask, url_for, send_from_directory
from .ext import webui


def minimal_app():
    app = Flask(__name__)
    return app


def create_app():
    app = minimal_app()
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
