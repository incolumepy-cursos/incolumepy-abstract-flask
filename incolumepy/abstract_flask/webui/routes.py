#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'
from pathlib import Path
from markdown import markdown
from flask import Blueprint, render_template, current_app

bp = Blueprint('webui', __name__)


@bp.route('/')
def home():
    title = 'Homepage'
    return render_template('index.html', title=title)


@bp.route('/about.html')
def about():
    title = "About"
    readme = Path(current_app.root_path[:current_app.root_path.index('incolumepy', 50)]).joinpath('README.md')
    content = markdown(readme.read_text())
    return render_template('about.html', title=title, content=content)
