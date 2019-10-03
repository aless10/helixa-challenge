from helixa_app.api.v1.base_task_view import TemplateView
from helixa_app.tasks.strategies.mongo_db_query import MongoDbQuery


class MongoDbQueryView(TemplateView):
    strategy = MongoDbQuery
