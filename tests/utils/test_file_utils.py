import os

from helixa_app.utils.file_utils import load_json_from_file


def test_json_to_dict():
    test_json_file = os.path.join(os.path.dirname(__file__), "json_file.json")
    dict_result = load_json_from_file(test_json_file)
    assert isinstance(dict_result, list)
