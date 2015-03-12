import sqlalchemy as sa

from . import Base


class SubReddit(Base):

    __tablename__ = "subreddits"

    name = sa.Column(sa.String(100, convert_unicode=True), unique=True)
    description = sa.Column(sa.String(2500, convert_unicode=True))

    admin_id = sa.Column(sa.Integer, sa.ForeignKey("users.pk"))

    threads = sa.orm.relationship(
        "Thread", backref="subreddit", lazy="dynamic"
    )

    def __init__(self, name, description, admin_id):
        self.name = name
        self.description = description
        self.admin_id = admin_id
