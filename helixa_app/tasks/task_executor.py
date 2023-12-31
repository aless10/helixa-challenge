import logging

from flask import request, Response
from marshmallow import ValidationError
from werkzeug.exceptions import BadRequest, InternalServerError

from helixa_app.schema.schema import RequestSchema, ResponseSchema

log = logging.getLogger(__name__)


class TaskExecutor:

    def __init__(self, strategy):
        if strategy is None:
            raise Exception("You must implement a strategy")
        self.strategy = strategy
        self._result = None
        self._status_code = None

    def execute(self):
        request_body = request.get_json(force=True)
        log.info("Running task %s with body %s", self.strategy.name, request_body)
        try:
            request_model = RequestSchema().load(request_body)
        except ValidationError as e:
            log.error('Failed Schema Validation: %s', e)
            self._status_code = BadRequest.code
        except Exception as e:
            log.error('Error while validating schema: %s', e)
            self._status_code = InternalServerError.code
        else:
            try:
                self._result = self.strategy.run(request_model)
                log.info("Task result: %s", self._result)
                self._status_code = 200
            except Exception:
                log.exception("Exception occurred in task")
                self._status_code = InternalServerError.code

    def make_response(self):
        response_schema_result = ResponseSchema().dump(self._result)
        return Response(response_schema_result, status=self._status_code, mimetype='application/json')
