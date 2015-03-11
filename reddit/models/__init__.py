from datetime import datetime

import sqlalchemy as sa

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


# Index()
