import re
import logging

from helixa_app.schema.file_schema import categories, psychographics, FileInfo
from helixa_app.schema.schema import RequestModel

log = logging.getLogger(__name__)


class DictLoop:  # pylint: disable=too-few-public-methods
    name = "DictLoop"

    @staticmethod
    def run(input_value) -> dict:
        return get_obj_from_value(input_value)


def get_obj_from_value(request_model: RequestModel) -> dict:
    category_val = get_value(categories, request_model.value)
    psychographics_val = get_value(psychographics, request_model.value)
    return {"category": category_val, "psychographics": psychographics_val,
            "category_sublayer": {}, "psychographics_sublayer": {}}


def get_value(file_info_obj: FileInfo, value: str) -> list:
    log.info("Getting value %s from %s", value, file_info_obj)
    match_items = []
    level = 0
    for item in file_info_obj.values():
        if re.search(f".*{value}.*", item[file_info_obj.label]) and item.get("level") > level:
            match_items.append(item)
            level += 1
    return match_items
