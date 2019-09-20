
def flatten_dict(_dictionary: dict, children_key: str, result_dict: dict, label="id") -> dict:

    if children_key not in _dictionary:
        result_dict.update({_dictionary[label]: _dictionary})
        return result_dict
    else:
        result_dict.update({_dictionary[label]: _dictionary})
        for item in _dictionary[children_key]:
            flatten_dict(item, children_key, result_dict=result_dict)
    return result_dict


def flatten_list_to_dict(_list: list, children_key: str) -> dict:
    d = {}
    for item in _list:
        d = flatten_dict(item, children_key, result_dict=d)
    return d
