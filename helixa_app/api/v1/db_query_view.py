from helixa_app.api.v1.base_task_view import TemplateView
from helixa_app.tasks.strategies.db_query import DbQuery


class DbQueryView(TemplateView):
    strategy = DbQuery
