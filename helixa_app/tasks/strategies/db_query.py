import logging

from flask import current_app

from helixa_app.db.repository import get_from_request
from helixa_app.db.session import context_session
from helixa_app.schema.schema import RequestModel
from helixa_app.tasks.strategies.base_strategy import BaseStrategy

log = logging.getLogger(__name__)


class DbQuery(BaseStrategy):  # pylint: disable=too-few-public-methods
    name = "DbQuery"

    @staticmethod
    def run(input_value: RequestModel) -> dict:
        with context_session(current_app.config["DATABASE_CONNECTION_URI"]) as session:
            return get_from_request(session, input_value)
