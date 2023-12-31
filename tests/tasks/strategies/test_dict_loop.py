from argparse import Namespace

from helixa_app.tasks.strategies.dict_loop import get_value

MockInfo = Namespace(label="name", values=lambda: [{"id": 1, "level": 1,
                                                    "children": [{"level": 2, "name": "test", "id": 2},
                                                                 {"level": 2, "name": "test_2", "id": 3,
                                                                  "children": [
                                                                      {"id": 4, "name": "test_4", "level": 3},
                                                                      {"level": 3, "name": "t_5", "id": 5}
                                                                  ]}],
                                                    "name": "root"},
                                                   {"id": 2, "name": "test", "level": 2},
                                                   {"level": 2, "name": "test_2", "id": 3},
                                                   {"id": 4, "name": "test_4", "level": 3},
                                                   {"level": 3, "name": "t_5", "id": 5}
                                                   ])


def test_get_value():
    test_value = "test"
    assert get_value(MockInfo, test_value) == [{"id": 4, "name": "test_4", "level": 3}]


def test_get_value_not_found():
    test_value = "test_not_found"
    assert get_value(MockInfo, test_value) == []
