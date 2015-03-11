

def includeme(config):
    config.include(".auth", route_prefix="/auth/")
    config.include(".users", route_prefix="/user/")
