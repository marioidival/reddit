import sqlalchemy as sa
from passlib.hash import sha256_crypt

from . import Base


class User(Base):
    __tablename__ = "users"

    username = sa.Column(sa.String(100, convert_unicode=True), unique=True)
    password = sa.Column(sa.String(200, convert_unicode=True))
    email = sa.Column(sa.String(200, convert_unicode=True), unique=True)

    def __init__(self, username, password, email=""):
        self.username = username
        self.email = email
        self.password = self.secured_passw(password)

    @classmethod
    def secured_passw(cls, passw):
        return sha256_crypt.encrypt(passw)

    @classmethod
    def verify_passw(cls, passw, unsecured):
        return sha256_crypt.verify(unsecured, passw)
