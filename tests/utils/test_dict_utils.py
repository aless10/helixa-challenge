from helixa_app.utils.dict_utils import flatten_dict, flatten_list_to_dict


def test_flatten_dict():
    result_input_dict = {}
    test_dict = {
        "id": -3,
        "name": "Influencers",
        "level": 1,
        "children": [
            {
                "l1": -3,
                "level": 2,
                "id": 13,
                "name": "Singers & Bands",
                "children": [
                    {
                        "l1": -3,
                        "l2": 13,
                        "level": 3,
                        "id": 14,
                        "name": "Classical Music"
                    },
                ]
            },
            {
                "l1": -3,
                "level": 2,
                "id": 12,
                "name": "Actors and Directors"
            },
        ]
    }
    flatten_result = flatten_dict(test_dict, children_key="children", result_dict=result_input_dict)
    assert flatten_result == {
        -3: {
            "id": -3,
            "name": "Influencers",
            "level": 1,
            "children": [
                {
                    "l1": -3,
                    "level": 2,
                    "id": 13,
                    "name": "Singers & Bands",
                    "children": [
                        {
                            "l1": -3,
                            "l2": 13,
                            "level": 3,
                            "id": 14,
                            "name": "Classical Music"
                        },
                    ]
                },
                {
                    "l1": -3,
                    "level": 2,
                    "id": 12,
                    "name": "Actors and Directors"
                },
            ]
        },
        13: {
            "l1": -3,
            "level": 2,
            "id": 13,
            "name": "Singers & Bands",
            "children": [
                {
                    "l1": -3,
                    "l2": 13,
                    "level": 3,
                    "id": 14,
                    "name": "Classical Music"
                },
            ]
        },
        12: {
            "l1": -3,
            "level": 2,
            "id": 12,
            "name": "Actors and Directors"
        },
        14: {
            "l1": -3,
            "l2": 13,
            "level": 3,
            "id": 14,
            "name": "Classical Music",
        },

    }


def test_flatten_dict_list_input():
    test_list = [{
        "l1": -3,
        "l2": 13,
        "level": 3,
        "id": 0,
        "name": "Classical Music"
    }, {
        "l1": -3,
        "l2": 13,
        "level": 3,
        "id": 1,
        "name": "Classical Music",
        "children": [
            {
                "l1": -3,
                "l2": 13,
                "level": 3,
                "id": 14,
                "name": "Classical Music"
            },
        ]
    }]
    assert flatten_list_to_dict(test_list, children_key="children") == {0: {"l1": -3,
                                                                            "l2": 13,
                                                                            "level": 3,
                                                                            "id": 0,
                                                                            "name": "Classical Music"
                                                                            },
                                                                        1: {
                                                                            "l1": -3,
                                                                            "l2": 13,
                                                                            "level": 3,
                                                                            "id": 1,
                                                                            "name": "Classical Music",
                                                                            "children": [
                                                                                {
                                                                                    "l1": -3,
                                                                                    "l2": 13,
                                                                                    "level": 3,
                                                                                    "id": 14,
                                                                                    "name": "Classical Music"
                                                                                },
                                                                            ]},
                                                                        14: {
                                                                            "l1": -3,
                                                                            "l2": 13,
                                                                            "level": 3,
                                                                            "id": 14,
                                                                            "name": "Classical Music"}
                                                                        }
