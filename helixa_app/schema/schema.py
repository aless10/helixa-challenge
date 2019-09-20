from collections import namedtuple

from marshmallow import Schema, fields, post_load

RequestModel = namedtuple("RequestModel", "value sublayer")


class RequestSchema(Schema):
    value = fields.Str(required=True, description="Value to look for")
    sublayer = fields.Str(required=False, description="Sublayer")

    @post_load
    def make_request(self, data, **kwargs):
        return RequestModel(**data)


class ResponseSchema(Schema):
    result = fields.Dict(required=True, description="Value to look for", allow_none=True)
