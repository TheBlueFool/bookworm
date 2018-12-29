from flask import Flask


def create_app(test_config=None):
    """Create and configure an instance of the Bookworm application."""
    app = Flask(__name__, instance_relative_config=True)

    from bookworm.api_v0 import configure_api
    api_vzero = configure_api(app, prefix='/api/v0')

    from bookworm.resources.hello import hello_bp
    app.register_blueprint(hello_bp)

    from bookworm.resources.health import health_bp
    app.register_blueprint(health_bp)

    return app
