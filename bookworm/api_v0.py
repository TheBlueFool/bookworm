from flask_restful import Api


def configure_api(app, prefix):
    api = Api(app, prefix=prefix)

    from bookworm.resources.plays import configure_plays
    configure_plays(app, api)

    from bookworm.resources.health_api import configure_health
    configure_health(app, api)

    from bookworm.resources.words import configure_words
    configure_words(app, api)

    return api
