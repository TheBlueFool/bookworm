from flask import Blueprint
from flask_restful import Resource, abort

from resources.data import plays_full_list

plays_bp = Blueprint('api', __name__)


def abort_if_todo_doesnt_exist(play_id):
    if play_id not in plays_full_list:
        abort(404, message="Todo {} doesn't exist".format(play_id))


class PlaySimple(Resource):
    def get(self, play_id):
        return {play_id: plays_full_list[play_id]}

    # def put(self, play_id):
    #     plays[play_id] = request.form['data']
    #     return {play_id: plays[play_id]}


def configure_plays(app, api):
    api.add_resource(PlaySimple, '/plays/<string:play_id>')
    app.register_blueprint(plays_bp)
