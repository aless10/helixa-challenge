import json

from sqlalchemy import TypeDecorator, String


class JsonBlob(TypeDecorator):

    impl = String

    def process_bind_param(self, value, dialect):
        return json.dumps(value)

    def process_result_value(self, value, dialect):
        return json.loads(value)


def get_children_ids(children: tuple, children_key: str) -> list:
    ids = []
    for child in children:
        ids.append(child.get("id"))
        grand_children = child.get(children_key)
        if grand_children is not None:
            ids.extend(get_children_ids(grand_children, children_key=children_key))
    return ids
