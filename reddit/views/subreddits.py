from __future__ import unicode_literals

from pyramid.view import view_config
from pyramid.url import route_url
from pyramid.httpexceptions import HTTPFound

from reddit.models import save_instance
from reddit.models.subreddits import SubReddit
from reddit.forms.subreddits import SubRedditForm


@view_config(route_name="reddit:subreddit:create", renderer="json")
def subreddit_create(request):

    subredditf = SubRedditForm(request.params)

    if subredditf.validate():

        new_subreddit = SubReddit(
            subredditf.name.data,
            subredditf.description.data,
            request.authenticated_userid
        )

        save_instance(request, new_subreddit)

        next = route_url(
            "reddit:subreddit:subreddit",
            request,
            subreddit=new_subreddit.name,
        )

        return HTTPFound(location=next)
    else:
        return {"success": False, "subreddif": subreddif.errors}


@view_config(
    route_name="reddit:subreddit:subreddit",
    renderer="templates/subreddit/index.html"
)
def subreddit(request):
    return {}
