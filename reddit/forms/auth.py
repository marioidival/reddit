from __future__ import unicode_literals

from wtforms.form import Form
from wtforms.fields import StringField, PasswordField
from wtforms.validators import Required, EqualTo, Email, Optional


class LoginForm(Form):

    username = StringField("Username", [Required()])
    password = PasswordField("Password", [Required()])


class RegisterForm(Form):
    username = StringField('Username', [Required()])
    email = StringField('Email address', [Optional(), Email()])
    password = PasswordField('Password', [Required()])
    confirm = PasswordField('Repeat Password', [
        Required(),
        EqualTo('password', message='Passwords must match')
    ])
