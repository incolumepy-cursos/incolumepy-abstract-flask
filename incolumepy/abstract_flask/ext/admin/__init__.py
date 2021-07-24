#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "@britodfbr"
from flask import flash
from flask_admin import Admin
from flask_admin.actions import action
from flask_admin.contrib.sqla import ModelView, filters
from incolumepy.abstract_flask.ext.dbase import db
from incolumepy.abstract_flask.ext.dbase.models import User, Post, Comment, Category
import re

admin = Admin()


def format_mail(instance, request, user, *args, **kwargs):
    # return f"{user.email[:user.email.index('@')+1]}.."
    regex = r"(.*@)(.*)(\.\w{3}(\.\w{2})?)"
    match = re.match(regex, user.email, re.I)
    return f"{match.group(1)}..{match.group(3)}"


class UserAdmin(ModelView):
    """Interface administrativa para User"""

    column_formatters = {
        "email": format_mail,
        "birthdate": lambda i, r, u, *args, **kwargs: f"{u.birthdate:%F}",
    }
    column_list = [
        "fullname",
        "username",
        "email",
        "birthdate",
        "avatar",
        "admin",
        "outcast",
    ]
    column_searchable_list = ["fullname"]
    column_filters = [
        "superadmin",
        "admin",
        "outcast",
        filters.FilterLike(
            User.email,
            "dominio",
            options=(("presidencia", "presidência"), ("planalto", "Planalto"), ("gmail", "Gmail"))
        ),
        "email",
    ]

    @action("tornar_admin", "Alternar Admin status", "Confirma?")
    def toggle_admin_status(self, ids):
        users = User.query.filter(User.id.in_(ids)).all()
        for user in users:
            user.admin = not user.admin
        db.session.commit()
        flash(f"{len(users)} status de administrador(es) alterado(s) com sucesso!", "success")


def init_app(app):
    admin.name = "Abstract Admin"
    admin.template_mode = "bootstrap4"
    admin.init_app(app)
    admin.add_view(UserAdmin(User, db.session))
    admin.add_view(ModelView(Post, db.session))
    admin.add_view(ModelView(Comment, db.session))
    admin.add_view(ModelView(Category, db.session))
