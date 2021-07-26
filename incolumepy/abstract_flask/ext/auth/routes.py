#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "@britodfbr"
from flask import Blueprint, render_template, url_for, redirect, flash
from flask_login import current_user, logout_user
from incolumepy.abstract_flask.ext.dbase.models import User
from incolumepy.abstract_flask.ext.dbase import db
from incolumepy.abstract_flask.ext.auth.forms import RegisterForm
bp = Blueprint("auth", __name__, template_folder="templates")


@bp.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("webui.home"))
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(
            fullname=form.fullname.data,
            username=form.username.data,
            email=form.email.data,
            password=form.password.data,
            birthdate=form.birthdate.data,
        )
        db.session.add(user)
        db.session.commit()
        # flash(f'Conta "{form.email.data}" criada com sucesso!', "success")
        return redirect(url_for("users.login"))
    return render_template("register.html", form=form, title="Register")


@bp.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html", title="Login")


@bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.home"))
