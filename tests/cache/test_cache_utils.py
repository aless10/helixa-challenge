from helixa_app.cache.cache_utils import build_key_from_request
from helixa_app.tasks.strategies.base_strategy import BaseStrategy


def test_build_key_from_request():
    request_body = {"key_1": "value_1", "key_2": "value_2", "key_3": None}
    strategy = BaseStrategy()
    strategy.name = "test"
    args = (strategy,)
    key_result = build_key_from_request(request_body, *args)
    assert isinstance(key_result, str)
    assert key_result == 'a80834fc49e649f6998a04daeabc9f9c'
