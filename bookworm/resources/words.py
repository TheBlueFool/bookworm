from flask import Blueprint
from flask_restful import Resource, abort

from .data import words_full_list

words_bp = Blueprint('words_bp', __name__)


def abort_if_todo_doesnt_exist(word_target):
    if word_target not in words_full_list:
        abort(404, message="Word {} doesn't exist".format(word_target))


class WordSimple(Resource):
    def get(self, word_target):
        return {word_target: words_full_list[word_target]}

    # def put(self, play_id):
    #     plays[play_id] = request.form['data']
    #     return {play_id: plays[play_id]}


def configure_words(app, api):
    api.add_resource(WordSimple, '/words/<string:word_target>')
    app.register_blueprint(words_bp)
