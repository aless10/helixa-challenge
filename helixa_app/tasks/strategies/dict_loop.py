import re
import logging

from helixa_app.schema.file_schema import categories, psychographics, FileInfo
from helixa_app.schema.schema import RequestModel
from helixa_app.tasks.strategies.base_strategy import BaseStrategy

log = logging.getLogger(__name__)


class DictLoop(BaseStrategy):  # pylint: disable=too-few-public-methods
    name = "DictLoop"

    @staticmethod
    def run(input_value: RequestModel) -> dict:
        return get_obj_from_value(input_value)


def get_obj_from_value(request_model: RequestModel) -> dict:
    category_val = get_value(categories, request_model.value)
    psychographics_val = get_value(psychographics, request_model.value)
    psycho_sublayer = psychographics.filter_from_value(request_model.sublayer)
    cat_sublayer = categories.filter_from_value(request_model.sublayer)
    psycho_sublayer_val = get_value(psycho_sublayer, request_model.value)
    cat_sublayer_val = get_value(cat_sublayer, request_model.value)
    return {"category": category_val, "psychographics": psychographics_val,
            "category_sublayer": cat_sublayer_val, "psychographics_sublayer": psycho_sublayer_val}


def get_value(file_info_obj: FileInfo, value: str) -> list:
    log.info("Getting value %s from %s", value, file_info_obj)
    match_items = []
    level = 0
    for item in file_info_obj.values():
        if re.search(f".*{value.lower()}.*", item[file_info_obj.label].lower()):
            item_level = item.get("level", 0)
            if item_level > level:
                match_items = []
                level = item_level
            elif item_level < level:
                continue
            match_items.append(item)
    return match_items
