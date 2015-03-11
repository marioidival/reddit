from pyramid.config import Configurator
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


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine

    config = Configurator(settings=settings)

    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_renderer(".html", "pyramid_jinja2.renderer_factory")
    config.add_request_method(sessiondb, "db", reify=True)


    config.add_route('home', '/')

    config.include(".routes")
    config.scan()
    return config.make_wsgi_app()
