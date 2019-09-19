import datetime
import logging
import os
import uuid
from logging.config import fileConfig

from flask import Flask, g, request, make_response, jsonify

from helixa_app.api import blueprint
from helixa_app.api.swagger import swaggerui_blueprint

log = logging.getLogger(__name__)


def register_blueprint(flask_app, blueprints=()):
    for flask_blueprint in blueprints:
        flask_app.register_blueprint(flask_blueprint)


def register_error_handlers(flask_app):
    def handle_400_error(_error):
        """Return a http 400 error to client"""
        return make_response(jsonify({'error': 'Misunderstood'}), 400)

    def handle_401_error(_error):
        """Return a http 401 error to client"""
        return make_response(jsonify({'error': 'Unauthorised'}), 401)

    def handle_404_error(_error):
        """Return a http 404 error to client"""
        return make_response(jsonify({'error': 'Not found'}), 404)

    def handle_500_error(_error):
        """Return a http 500 error to client"""
        return make_response(jsonify({'error': 'Server error'}), 500)


def register_request_callbacks(flask_app):
    def begin_request():
        g.start = datetime.datetime.now()
        g.x_request_id = request.headers.get('X-Request-ID', uuid.uuid4())
        flask_app.logger.info(
            "Received a new request x_request_id[%s] body[%s] method[%s] endpoint[%s]",
            g.x_request_id,
            request.json,
            request.method,
            request.path
        )

    def end_request(response):
        request.direct_passthrough = False
        duration = datetime.datetime.now() - g.start
        log.info(
            'PERF x_request_id[%s] time[%s] method[%s] endpoint[%s] status[%s]',
            g.x_request_id,
            duration,
            request.method,
            request.path,
            response.status
        )
        log.debug('RESPONSE x_request_id[%s]', g.x_request_id)
        response.headers['X-Request-ID'] = g.x_request_id
        response.headers['X-Time-Elapsed'] = duration
        return response

    flask_app.before_request(begin_request)
    flask_app.after_request(end_request)


def setup_logging(configuration):
    fileConfig(configuration.LOG_CONF, defaults=os.environ)


def create_app(config_obj):
    app = Flask('helixa_app')
    app.config.from_object(config_obj)
    register_request_callbacks(app)
    register_blueprint(app, blueprints=(swaggerui_blueprint, blueprint.v1,))
    # app.register_blueprint(swaggerui_blueprint, url_prefix=swaggerui_blueprint.url_prefix)
    setup_logging(config_obj)
    return app
