#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'
import click
from incolumepy.abstract_flask.ext.dbase.commands import create_db, drop_db


def init_app(app):
    # add multiple commands in a bulk
    for command in [create_db, drop_db]:
        app.cli.add_command(app.cli.command()(command))
