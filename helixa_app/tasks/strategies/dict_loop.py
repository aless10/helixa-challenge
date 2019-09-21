from helixa_app.schema.file_schema import categories, psychographics
from helixa_app.schema.schema import RequestModel


class DictLoop:
    name = "DictLoop"

    @staticmethod
    def run(input_value) -> dict:
        return get_obj_from_value(input_value)


def get_obj_from_value(request_model: RequestModel) -> dict:
    result = {"category": None, "psychographics": None}
    for value in categories.values():
        if value[categories.label] == request_model.value:
            result["category"] = value

    for value in psychographics.values():
        if value[psychographics.label] == request_model.value:
            result["psychographics"] = value

    return result
