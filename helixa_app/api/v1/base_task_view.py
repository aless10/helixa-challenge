from flask.views import MethodView

from helixa_app.cache.cache_utils import cache
from helixa_app.tasks.task_executor import TaskExecutor


class BaseTask(MethodView):
    strategy = None

    @cache
    def post(self):
        executor = TaskExecutor(strategy=self.strategy)
        executor.execute()
        return executor.make_response()


class TemplateView(BaseTask):

    def post(self):
        return super().post()
