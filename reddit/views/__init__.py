from pyramid.response import Response
from pyramid.view import view_config

from reddit.forms.auth import LoginForm, RegisterForm


@view_config(route_name='home', renderer='templates/base.html')
def my_view(request):
    return {
        'loginf': LoginForm(),
        'registerf': RegisterForm()
    }
