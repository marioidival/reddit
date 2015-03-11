from pyramid.config import Configurator
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from sqlalchemy import engine_from_config

from .models import (
    DBSession,
    Base,
    )


def sessiondb(request):
    """Return session of SQLAlchemy"""
    session = DBSession()

    def cleanup(request):
        """Callback to close session if transaction finish without errors"""
        session.close()

    # Add callback on request
    request.add_finished_callback(cleanup)

    return session


def username(request):
    """Add username of user in request"""

    from .models.users import User
    user = request.db.query(User).get(request.authenticated_userid)

    if user:
        return user.username


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine

    authe_fact = AuthTktAuthenticationPolicy("myredditkey")
    autho_fact = ACLAuthorizationPolicy()

    config = Configurator(
        settings=settings,
        authentication_policy=authe_fact,
        authorization_policy=autho_fact
    )

    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_renderer(".html", "pyramid_jinja2.renderer_factory")

    config.add_request_method(sessiondb, "db", reify=True)
    config.add_request_method(username, "user", reify=True)

    config.include(".routes")
    config.scan()

    return config.make_wsgi_app()
