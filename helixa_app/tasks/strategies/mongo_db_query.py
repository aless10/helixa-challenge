import logging

from flask import current_app

from helixa_app.db.mongo_db.repository import get_from_request
from helixa_app.db.mongo_db.session import context_db
from helixa_app.schema.schema import RequestModel
from helixa_app.tasks.strategies.base_strategy import BaseStrategy

log = logging.getLogger(__name__)


class MongoDbQuery(BaseStrategy):  # pylint: disable=too-few-public-methods
    name = "MongoDbQuery"

    @staticmethod
    def run(input_value: RequestModel) -> dict:
        with context_db(current_app.config["MONGO_DB_CONNECTION_URI"]) as db:
            return get_from_request(db, input_value)
