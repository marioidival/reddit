from __future__ import unicode_literals

from pyramid.view import view_config
from pyramid.security import remember, forget
from pyramid.httpexceptions import exception_response, HTTPFound

from reddit.models import save_instance
from reddit.models.users import User
from reddit.forms.auth import LoginForm, RegisterForm


@view_config(route_name="reddit:auth:login", renderer="json")
def login(request):

    loginf = LoginForm(request.params)

    if loginf.validate():
        user = User.query.filter_by(username=loginf.username.data).one()

        if user and User.verify_passw(user.password, loginf.password.data):
            headers = remember(request, str(user.pk))
            response = request.response
            response.headerlist.extend(headers)

            return {"success": True}
        else:
            return {"success": False, "msg": "username or password invalid"}

    return {"success": False, "loginf": loginf.errors}


@view_config(route_name="reddit:auth:logout", renderer="json")
def logout(request):
    headers = forget(request)
    response = request.response
    response.headerlist.extend(headers)
    return {"success": True}


@view_config(route_name="reddit:auth:register", renderer="json")
def register(request):

    registerf = RegisterForm(request.params)

    if registerf.validate():
        delattr(registerf, "confirm")

        user = User(**registerf.data)

        save_instance(request, user)

    return {"success": False, "registerf": registerf.errors}
