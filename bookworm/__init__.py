import os

from flask import Flask
from flask_restful import reqparse, abort, Api, Resource


def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    api = Api(app)
    app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY='dev',
        # store the database in the instance folder
        # DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    # if test_config is None:
    #     # load the instance config, if it exists, when not testing
    #     app.config.from_pyfile('config.py', silent=True)
    # else:
    #     # load the test config if passed in
    #     app.config.update(test_config)

    # # ensure the instance folder exists
    # try:
    #     os.makedirs(app.instance_path)
    # except OSError:
    #     pass

    from bookworm.resources.hello import hello_bp
    app.register_blueprint(hello_bp)

    # from bookworm.resources import todo
    # todo.configure_todo(app, api)

    from bookworm.resources.health import health_bp
    app.register_blueprint(health_bp)

    from bookworm.resources.plays import configure_plays
    configure_plays(app, api)
    # apply the blueprints to the app
    # from bookworm import hello
    # app.register_blueprint(hello.bp)
    # app.register_blueprint(blog.bp)

    # make url_for('index') == url_for('blog.index')
    # in another app, you might define a separate main index here with
    # app.route, while giving the blog blueprint a url_prefix, but for
    # the tutorial the blog will be the main index

    return app


