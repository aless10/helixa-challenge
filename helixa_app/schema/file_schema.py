import os

from helixa_app.utils.dict_utils import flatten_list_to_dict
from helixa_app.utils.file_utils import load_json_from_file


class FileInfo:

    children_key = None
    filename = None
    label = None

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


class CategoriesInfo(FileInfo):
    children_key = "children"
    filename = os.path.join(os.path.dirname(__file__), "..", "..", "categories.json")
    label = "name"


class PsychographicsInfo(FileInfo):
    children_key = "values"
    filename = os.path.join(os.path.dirname(__file__), "..", "..", "psychographics.json")
    label = "label"


categories = CategoriesInfo.load_from_file()
psychographics = PsychographicsInfo.load_from_file()
