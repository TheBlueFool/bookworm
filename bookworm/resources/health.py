from flask import Blueprint

health_bp = Blueprint("health", __name__)


@health_bp.route('/health')
def health_status():
    return 'OK'

# def configure_health(app, api):
#     api.add_resource(health_status, '/health')
#     app.register_blueprint(health_bp)
