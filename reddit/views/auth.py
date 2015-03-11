from __future__ import unicode_literals

import transaction
from sqlalchemy.exc import IntegrityError

from pyramid.view import view_config
from pyramid.security import remember, forget
from pyramid.httpexceptions import exception_response

from reddit.models.users import User
from reddit.forms.auth import LoginForm, RegisterForm


@view_config(route_name="reddit:auth:login", renderer="json")
def login(request):

    loginf = LoginForm(request.params)

    if loginf.validate():
        user = User.query.filter_by(username=loginf.username.data).one()

        if user and User.verify_passw(user.password, loginf.password.data):
            headers = remember(request, str(user.pk))
            return HTTPFound(request.referrer, headers=headers)
        else:
            return {"success": False, "loginf": ["message of error"]}

    return {"success": False, "loginf": loginf.errors}



@view_config(route_name="reddit:auth:logout", renderer="json")
def logout(request):
    pass


@view_config(route_name="reddit:auth:register", renderer="json")
def register(request):

    registerf = RegisterForm(request.params)

    if registerf.validate():
        delattr(registerf, "confirm")

        user = User(**registerf.data)
        try:
            request.db.add(user)
            request.db.flush()

            return {"success": True}
        except IntegrityError as e:
            # Get email, username
            key_error = e.message.split(' ')[-1].split('.')[-1]
            msg = "{0} already exists".format(key_error.title())

            return {"success": False, "msg": msg}

    return {"success": False, "registerf": registerf.errors}
