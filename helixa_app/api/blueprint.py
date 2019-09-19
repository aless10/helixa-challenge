from flask import Blueprint

from helixa_app.api.v1.status import Status

v1 = Blueprint('api_v1', __name__, url_prefix='/api/v1')

v1.add_url_rule('/status', view_func=Status.as_view('get-status'))

