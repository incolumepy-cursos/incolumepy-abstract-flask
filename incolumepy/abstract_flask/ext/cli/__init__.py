#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'
import click
from incolumepy.abstract_flask.ext.dbase.commands import createdb, dropdb


def init_app(app):
    # add multiple commands in a bulk
    for command in [createdb, dropdb]:
        app.cli.add_command(app.cli.command()(command))
