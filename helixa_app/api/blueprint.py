from flask import Blueprint

from helixa_app.api.v1.db_query_view import DbQueryView
from helixa_app.api.v1.dict_loop_view import DictLoopView
from helixa_app.api.v1.mongo_db_query_view import MongoDbQueryView
from helixa_app.api.v1.status import Status

v1 = Blueprint('api_v1', __name__, url_prefix='/api/v1')

v1.add_url_rule('/status', view_func=Status.as_view('get-status'))
v1.add_url_rule('/tasks/dict-loop/', view_func=DictLoopView.as_view('dict-loop'))
v1.add_url_rule('/tasks/db-query/', view_func=DbQueryView.as_view('db-query'))
v1.add_url_rule('/tasks/mongo-db-query/', view_func=MongoDbQueryView.as_view('mongo-db-query'))
