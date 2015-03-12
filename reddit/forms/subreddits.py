from __future__ import unicode_literals

from wtforms import ValidationError
from wtforms.form import Form
from wtforms.fields import StringField, TextAreaField
from wtforms.validators import Required, Optional

from reddit.models.subreddits import SubReddit


def check_subreddit_name(form, field):
    subreddit = SubReddit.query.filter_by(name=field.data).first()

    if subreddit:
        raise ValidationError(
            "{} already exists!".format(subreddit.name.title())
        )


class SubRedditForm(Form):

    name = StringField("Community", [Required(), check_subreddit_name])
    description = TextAreaField("Description", [Optional()])
