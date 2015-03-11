


def includeme(config):

    config.add_route("reddit:auth:login", "login/")
    config.add_route("reddit:auth:logout", "logout/")
    config.add_route("reddit:auth:register", "register/")
