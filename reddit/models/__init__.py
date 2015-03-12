from datetime import datetime

import sqlalchemy as sa

from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.orm import scoped_session, sessionmaker

from zope.sqlalchemy import ZopeTransactionExtension


DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))


class MyBase(object):

    query = DBSession.query_property()

    @declared_attr
    def pk(cls):
        return sa.Column(sa.Integer, primary_key=True)

    @declared_attr
    def created_at(cls):
        return sa.Column(sa.DateTime, default=datetime.utcnow)

    @declared_attr
    def updated_at(cls):
        return sa.Column(sa.DateTime, onupdate=datetime.utcnow)


Base = declarative_base(cls=MyBase)


def save_instance(request, instance):
    try:
        request.db.add(instance)
        request.db.flush()
        return {"success": True}
    except IntegrityError as e:
        # Get email, username
        key_error = e.message.split(' ')[-1].split('.')[-1]
        msg = "{0} already exists".format(key_error.title())



# Index()
