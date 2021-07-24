#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'
from pathlib import Path
from markdown import markdown
from flask import Blueprint, render_template, current_app, request
from incolumepy.abstract_flask.ext.models import posts, users
bp = Blueprint('webui', __name__)


@bp.route('/')
def home():
    title = 'Homepage'
    return render_template('index.html', title=title, posts=posts)


@bp.route("/post/<int:post_id>")
def post(post_id):
    title = 'Post'
    post = posts[post_id - 1]
    return render_template("post.html", title=title, post=post)


@bp.route('/about.html')
def about():
    title = "About"
    readme = Path(current_app.root_path[:current_app.root_path.index('incolumepy', 50)]).joinpath('README.md')
    content = markdown(readme.read_text())
    return render_template('about.html', title=title, content=content)


@bp.route('/styles.html')
def styles():
    return render_template('generic_page.html', title='Styles', content='')


@bp.route('/contact.html')
def contact():
    return render_template('generic_page.html', title='Contact', content='')


@bp.route('/category.html')
def category():
    cat = request.args.get('category')
    return render_template('generic_page.html', title=f'Category :: {cat}', content=cat)


@bp.route('/page')
def generic_page():
    title = request.args.get('title')
    return render_template('generic_page.html', title=f'{title}', content=title)

