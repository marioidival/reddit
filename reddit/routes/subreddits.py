

def includeme(config):

    config.add_route("reddit:subreddit:create", "create/")
    config.add_route("reddit:subreddit:delete", "delete/")
    config.add_route("reddit:subreddit:subreddit", "{subreddit}")
