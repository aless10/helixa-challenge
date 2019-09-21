from typing import Optional

from helixa_app.schema.file_schema import categories, psychographics, FileInfo
from helixa_app.schema.schema import RequestModel


class DictLoop:
    name = "DictLoop"

    @staticmethod
    def run(input_value) -> dict:
        return get_obj_from_value(input_value)


def get_obj_from_value(request_model: RequestModel) -> dict:
    category_val = get_value(categories, request_model.value)
    psychographics_val = get_value(psychographics, request_model.value)
    return {"category": category_val, "psychographics": psychographics_val}


def get_value(file_info_obj: FileInfo, value: str) -> Optional[dict]:
    for item in file_info_obj.values():
        if item[file_info_obj.label] == value:
            return item
