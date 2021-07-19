#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "@britodfbr"
from incolumepy.abstract_flask import create_app
app = create_app()

if __name__ == '__main__':
    app.run()
