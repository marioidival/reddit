

def includeme(config):

    config.add_route('home', '/')

    config.include(".auth", route_prefix="/auth/")
    config.include(".users", route_prefix="/user/")
    config.include(".subreddits", route_prefix="/r/")
