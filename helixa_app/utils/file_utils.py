import json
from typing import Union


def load_json_from_file(filename: str) -> Union[list, dict]:
    with open(filename) as f:
        return json.load(f)
