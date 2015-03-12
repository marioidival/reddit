import sqlalchemy as sa

from . import Base


class Thread(Base):

    __tablename__ = "threads"

    title = sa.Column(sa.String(100, convert_unicode=True))
    text = sa.Column(sa.String(2000), default=None)
    link = sa.Column(sa.String(1000), default=None)

    user_id = sa.Column(sa.Integer, sa.ForeignKey("users.pk"))
    subreddit_id = sa.Column(sa.Integer, sa.ForeignKey("subreddits.pk"))

    votes = sa.Column(sa.Integer, default=1)

    def __init__(self, title, text, link, user_id, subreddit_id):
        self.title = title
        self.text = text
        self.link = link
        self.user_id = user_id
        self.subreddit_ir = subreddit_id
