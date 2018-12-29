from flask import Blueprint

from flask_restful import Resource, abort


health_api_bp = Blueprint("health_api", __name__)


class HealthSimple(Resource):
    def get(self):
        return 'OK'

def health_status():
    return 'OK'

def configure_health(app, api):
    api.add_resource(HealthSimple, '/health')
    app.register_blueprint(health_api_bp)
