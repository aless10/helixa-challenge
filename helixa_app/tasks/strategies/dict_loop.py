from helixa_app.schema.schema import RequestModel


class DictLoop:
    name = "DictLoop"

    @staticmethod
    def run(input_value) -> dict:
        return get_obj_from_value(input_value)


def get_obj_from_value(input_value: RequestModel) -> dict:
    return {"result": {"id": 1, "name": "Developer"}}
