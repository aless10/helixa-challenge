import os

from helixa_app.db.relational_db.models.category import Category
from helixa_app.db.relational_db.models.psychographic import Psychographic
from helixa_app.utils.dict_utils import flatten_list_to_dict
from helixa_app.utils.file_utils import load_json_from_file


class FileInfo:

    children_key = None
    filename = None
    label = None
    db_table = None

    def __init__(self, content):
        self.info = flatten_list_to_dict(content, self.children_key)

    @classmethod
    def load_from_file(cls) -> 'FileInfo':
        info_from_file = load_json_from_file(cls.filename)
        return cls(info_from_file)

    def filter_from_value(self, value: str) -> 'FileInfo':
        for v in self.info.values():
            if v[self.label] == value:
                return self.__class__([v])
        return self.__class__([])

    def values(self):
        return self.info.values()

    def items(self):
        return self.info.items()


class CategoriesInfo(FileInfo):
    children_key = "children"
    filename = os.path.join(os.path.dirname(__file__), "..", "..", "categories.json")
    label = "name"
    db_table = Category


class PsychographicsInfo(FileInfo):
    children_key = "values"
    filename = os.path.join(os.path.dirname(__file__), "..", "..", "psychographics.json")
    label = "label"
    db_table = Psychographic


categories = CategoriesInfo.load_from_file()
psychographics = PsychographicsInfo.load_from_file()
