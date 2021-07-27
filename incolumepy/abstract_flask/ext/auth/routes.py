#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "@britodfbr"
from flask import Blueprint, render_template, url_for, redirect, flash, request
from flask_login import current_user, logout_user, login_user
from incolumepy.abstract_flask.ext.dbase.models import User
from incolumepy.abstract_flask.ext.dbase import db
from incolumepy.abstract_flask.ext.auth.forms import RegisterForm, LoginForm
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
        flash(f'Conta "{form.email.data}" criada com sucesso!', "success")
        return redirect(url_for("auth.login"))
    return render_template("register.html", form=form, title="Register")


@bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("webui.home"))
    form = LoginForm()
    if form.validate_on_submit():
        print(form.password.data, form.email.data)
        user = User.query.filter_by(email=form.email.data).first()
        print(user)
        if user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            flash("Login with success", 'success')
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('webui.home'))
        else:
            flash('Please check your user or password', 'danger')
    return render_template("login.html", form=form, title="Login")


@bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.home"))
