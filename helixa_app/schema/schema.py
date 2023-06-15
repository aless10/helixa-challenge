import json
from collections import namedtuple

from marshmallow import Schema, fields, post_load, post_dump, pre_dump

from helixa_app.utils.dict_utils import remove_nulls

RequestModel = namedtuple("RequestModel", "value sublayer")


class RequestSchema(Schema):
    value = fields.Str(required=True, description="Value to look for")
    sublayer = fields.Str(required=False, description="Sublayer")

    @post_load
    def make_request(self, data, **kwargs):  # pylint: disable=unused-argument
        return RequestModel(**data)


def _set_key(obj: Schema, key: str, data: dict) -> dict:
    if key in data:
        setattr(obj, key, fields.List(fields.Dict))
    return data


def _set_key_to_none(key: str, data: dict) -> dict:
    if key not in data:
        data[key] = None
    return data


class CategoryAtomSchema(Schema):
    name = fields.Str()
    id = fields.Integer()
    level = fields.Integer()
    pic = fields.Str()
    type = fields.Str()
    l1 = fields.Int(allow_none=True)
    l2 = fields.Int(allow_none=True)
    l3 = fields.Int(allow_none=True)
    l4 = fields.Int(allow_none=True)
    l5 = fields.Int(allow_none=True)

    @pre_dump
    def check_for_children(self, data, **kwargs):  # pylint: disable=unused-argument
        return _set_key(self, "children", data)


class CategorySchema(CategoryAtomSchema):
    children = fields.List(fields.Nested(CategoryAtomSchema))
    ico = fields.Str()

    @pre_dump
    def set_children_to_none(self, data, **kwargs):  # pylint: disable=unused-argument
        return _set_key_to_none("children", data)


class PsychoAtomId(fields.Field):

    def _serialize(self, value, attr, obj, **kwargs):
        """
        Since the id field of psycho objects can be an int or a string, we want to return the value without checking
        its type
        """
        try:
            value = int(value)
        except ValueError:
            pass
        return value


class PsychoAtomSchema(Schema):
    value = fields.Str()
    id = PsychoAtomId()
    label = fields.Str()
    pic = fields.Str()

    @pre_dump
    def check_for_values(self, data, **kwargs):  # pylint: disable=unused-argument
        return _set_key(self, "values", data)


class PsychographicsSchema(PsychoAtomSchema):
    values = fields.List(fields.Nested(PsychoAtomSchema))
    ico = fields.Str(allow_none=True)
    sources = fields.List(fields.Nested(fields.Dict))

    @pre_dump
    def set_values_to_none(self, data, **kwargs):  # pylint: disable=unused-argument
        return _set_key_to_none("values", data)


class ResponseSchema(Schema):
    category = fields.List(fields.Nested(CategorySchema), description="Category elements")
    psychographics = fields.List(fields.Nested(PsychographicsSchema), description="Psychographic elements")
    category_sublayer = fields.List(fields.Nested(CategorySchema), description="Category filtered element")
    psychographics_sublayer = fields.List(fields.Nested(PsychographicsSchema),
                                          description="Psychographic filtered element")

    @post_dump
    def to_json(self, data, **kwargs):  # pylint: disable=unused-argument
        cleaned_data = remove_nulls(data)
        return json.dumps(cleaned_data)
