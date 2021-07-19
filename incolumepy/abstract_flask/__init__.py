#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'
from pathlib import Path
from flask import Flask, render_template, url_for, send_from_directory


def create_app():
    app = Flask(__name__)
    # app.add_url_rule('/favicon.ico',
    #                  redirect_to=url_for('static', filename='images/favicons/favicon.ico'))

    @app.route('/')
    def home():
        title = 'Homepage'
        return render_template('index.html', title=title)

    # @app.route('/favicon.ico')
    # def favicon():
    #     ico = Path(app.root_path)
    #     return send_from_directory(ico, 'static', 'images/favicons/favicon.ico', mimetype='image/vnd.microsoft.icon')

    @app.route('/hello')
    def hello():
        return "Hello World!!"

    return app
