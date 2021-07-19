#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'
import click
from .commands import dropdb, createdb


def init_app(app):
    # add multiple commands in a bulk
    for command in [createdb, dropdb]:
        app.cli.add_command(app.cli.command()(command))

    # add a single command
    @app.cli.command()
    @click.option('--username', '-u', help='Username to login')
    @click.option('--email', '-e', help='A valid email address')
    @click.option('--password', '-p', help='Password to login')
    @click.option('--avatar', '-a', default=None, help='Image to avatar user')
    def add_user(username, email, password, avatar):
        """Adds a new user to the database"""
        return create_user(username, email, password, avatar)
