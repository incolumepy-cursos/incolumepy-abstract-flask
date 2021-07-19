#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'
from flask import Blueprint, render_template

bp = Blueprint('webui', __name__)


@bp.route('/')
def home():
    title = 'Homepage'
    return render_template('index.html', title=title)
