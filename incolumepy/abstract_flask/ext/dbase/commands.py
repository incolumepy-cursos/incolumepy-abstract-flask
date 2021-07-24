#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'
from .models import db


def createdb():
    """Creates database"""
    db.create_all()


def dropdb():
    """Cleans database"""
    db.drop_all()
