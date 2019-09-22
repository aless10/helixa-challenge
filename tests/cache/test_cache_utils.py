from argparse import Namespace

from helixa_app.api.v1.base_task_view import TemplateView
from helixa_app.cache.cache_utils import build_key_from_request


MockStrategy = Namespace(name="mock_strategy")


class MockView(TemplateView):
    strategy = MockStrategy


def test_build_key_from_request():
    request_body = {"key_1": "value_1", "key_2": "value_2", "key_3": None}
    view = MockView()
    args = (view,)
    key_result = build_key_from_request(request_body, *args)
    assert isinstance(key_result, str)
    assert key_result == '922f53fb794d125090f29cf0b48a206d'
