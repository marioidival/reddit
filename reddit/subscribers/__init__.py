from pyramid.events import subscriber, BeforeRender

from reddit.models.subreddits import SubReddit
from reddit.forms.auth import LoginForm, RegisterForm
from reddit.forms.subreddits import SubRedditForm



@subscriber(BeforeRender)
def subreddits(event):
    subreddits_names = [subreddit.name for subreddit in SubReddit.query.all()]

    event.update(subreddits=subreddits_names)
    event.update(loginf=LoginForm())
    event.update(registerf=RegisterForm())
    event.update(subredditf=SubRedditForm())
