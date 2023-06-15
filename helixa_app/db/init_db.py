import logging

from helixa_app.db.mongo_db.repository import populate_mongo_db_from_object
from helixa_app.db.relational_db.repository import populate_db_from_object
from helixa_app.db.relational_db.session import create_db as create_relational_db

log = logging.getLogger(__name__)


def init_db(config_obj, categories, psychographics):
    log.info("Init db")
    create_relational_db(config_obj.DATABASE_CONNECTION_URI)
    populate_db_from_object(categories, config_obj.DATABASE_CONNECTION_URI)
    populate_db_from_object(psychographics, config_obj.DATABASE_CONNECTION_URI)
    populate_mongo_db_from_object(categories, config_obj.MONGO_DB_CONNECTION_URI)
    populate_mongo_db_from_object(psychographics, config_obj.MONGO_DB_CONNECTION_URI)
