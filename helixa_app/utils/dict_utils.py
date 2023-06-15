
def flatten_dict(_dictionary: dict, children_key: str, result_dict: dict, level: int = 1, label="id") -> dict:

    level += 1
    if children_key not in _dictionary:
        _dictionary["level"] = _dictionary.get("level", level)
        result_dict.update({_dictionary[label]: _dictionary})
        return result_dict
    else:
        _dictionary["level"] = _dictionary.get("level", level)
        result_dict.update({_dictionary[label]: _dictionary})
        for item in _dictionary[children_key]:
            flatten_dict(item, children_key, result_dict=result_dict, level=level)
    return result_dict


def flatten_list_to_dict(_list: list, children_key: str) -> dict:
    d = {}
    for item in _list:
        level = 0
        d = flatten_dict(item, children_key, result_dict=d, level=level)
    return d


def remove_nulls(obj):
    if isinstance(obj, dict):
        obj = {k: remove_nulls(v) for k, v in obj.items() if v is not None}

    if isinstance(obj, list):
        obj = [remove_nulls(i) for i in obj if i is not None]

    return obj
