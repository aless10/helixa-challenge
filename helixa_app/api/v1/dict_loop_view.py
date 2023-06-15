from helixa_app.api.v1.base_task_view import TemplateView
from helixa_app.tasks.strategies.dict_loop import DictLoop


class DictLoopView(TemplateView):
    strategy = DictLoop
