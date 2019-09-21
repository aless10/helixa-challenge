import json
from collections import namedtuple

from marshmallow import Schema, fields, post_load, post_dump, pre_dump

from helixa_app.utils.dict_utils import remove_nulls

RequestModel = namedtuple("RequestModel", "value sublayer")


class RequestSchema(Schema):
    value = fields.Str(required=True, description="Value to look for")
    sublayer = fields.Str(required=False, description="Sublayer")

    @post_load
    def make_request(self, data, **kwargs):
        return RequestModel(**data)


class CategoryAtomSchema(Schema):
    name = fields.Str()
    id = fields.Integer()
    level = fields.Integer()

    @pre_dump
    def add_levels_fields(self, data, **kwargs):
        pass


class CategorySchema(CategoryAtomSchema):
    children = fields.List(fields.Nested(CategoryAtomSchema))
    ico = fields.Str()


class PyschoAtomId(fields.Field):

    def _serialize(self, value, attr, obj, **kwargs):
        try:
            value = int(value)
        except ValueError:
            pass
        return value


class PsychoAtomSchema(Schema):
    value = fields.Str()
    id = PyschoAtomId()
    label = fields.Str()
    pic = fields.Str()

    @pre_dump
    def check_for_values(self, data, **kwargs):
        if "values" in data:
            setattr(self, "values", fields.List(fields.Dict))
        return data


class PsychographicsSchema(PsychoAtomSchema):
    values = fields.List(fields.Nested(PsychoAtomSchema))
    ico = fields.Str(allow_none=True)

    @pre_dump
    def set_values_to_none(self, data, **kwargs):
        if "values" not in data:
            data['values'] = None
        return data


class ResponseSchema(Schema):
    category = fields.List(fields.Nested(CategorySchema), description="Category elements")
    psychographics = fields.List(fields.Nested(PsychographicsSchema), description="Psychographic elements")
    category_sublayer = fields.List(fields.Dict, description="Category filtered element")
    psychographics_sublayer = fields.List(fields.Dict, description="Psychographic filtered element")

    @post_dump
    def to_json(self, data, **kwargs):
        cleaned_data = remove_nulls(data)
        return json.dumps(cleaned_data)
