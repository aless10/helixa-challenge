import json
from collections import namedtuple

from marshmallow import Schema, fields, post_load, post_dump

RequestModel = namedtuple("RequestModel", "value sublayer")


class RequestSchema(Schema):
    value = fields.Str(required=True, description="Value to look for")
    sublayer = fields.Str(required=False, description="Sublayer")

    @post_load
    def make_request(self, data, **kwargs):
        return RequestModel(**data)


class ResponseField(fields.Dict):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.default = {}


class ResponseSchema(Schema):
    category = ResponseField(description="Category element")
    psychographic = ResponseField(description="Psychographic element")

    @post_dump
    def to_json(self, data, **kwargs):
        return json.dumps(data)
