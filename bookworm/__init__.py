import os

from flask import Flask
from flask_restful import reqparse, abort, Api, Resource


def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    api_v0 = Api(app, prefix='/api/v0')

    from bookworm.resources.hello import hello_bp
    app.register_blueprint(hello_bp)

    from bookworm.resources.health import health_bp
    app.register_blueprint(health_bp)

    from bookworm.resources.plays import configure_plays
    configure_plays(app, api_v0)

    from bookworm.resources.health_api import configure_health
    configure_health(app, api_v0)

    from bookworm.resources.words import configure_words
    configure_words(app, api_v0)



    # apply the blueprints to the app
    # from bookworm import hello
    # app.register_blueprint(hello.bp)
    # app.register_blueprint(blog.bp)

    # make url_for('index') == url_for('blog.index')
    # in another app, you might define a separate main index here with
    # app.route, while giving the blog blueprint a url_prefix, but for
    # the tutorial the blog will be the main index

    return app
