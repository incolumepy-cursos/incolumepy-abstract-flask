#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'
from flask_wtf import FlaskForm
from incolumepy.abstract_flask.ext.dbase.models import User
from wtforms import StringField, PasswordField, SubmitField, DateTimeField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


class RegisterForm(FlaskForm):
    fullname = StringField("Fullname", validators=[DataRequired()])
    username = StringField(
        "Username", validators=[DataRequired(), Length(min=8, max=30)]
    )
    email = StringField("Email", validators=[DataRequired(), Email()])
    email_confirm = StringField("Email", validators=[DataRequired(), Email(), EqualTo("email")])
    password = PasswordField("Password", validators=[DataRequired()])
    password_confirm = PasswordField(
        "Confirm Password", validators=[DataRequired(), EqualTo("password")]
    )
    birthdate = DateTimeField("birthdate", format="%Y-%m-%d", validators=[])
    submit = SubmitField('Sign Up')

    def validate_username(self, field):
        user = User.query.filter_by(username=field.data).first()
        if user:
            raise ValidationError(f'alrady exist <<{field.data}>>, choice another')

    def validate_email(self, field):
        user = User.query.filter_by(email=field.data).first()
        if user:
            raise ValidationError(f'alrady exist <<{field.data}>>, choice another')


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')
