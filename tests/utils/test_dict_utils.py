# flake8: noqa
from helixa_app.utils.dict_utils import flatten_dict, flatten_list_to_dict, remove_nulls


def test_flatten_dict_categories():
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


def test_flatten_dict_list_input_categories():
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


def test_flatten_dict_psychographics():
    result_input_dict = {}
    test_dict = {
        "values": [
            {
                "values": [
                    {
                        "value": "Ads Paper",
                        "id": 4,
                        "pic": "/assets/img/psychographics/ico/psy_4.jpg",
                        "label": "Print Ads"
                    },
                    {
                        "value": "Ads EmergingMediaVehicles",
                        "id": 3,
                        "pic": "/assets/img/psychographics/ico/psy_3.jpg",
                        "label": "Unconventional Ads"
                    },
                ],
                "label": "Advertising",
                "ico": "flaticon-marketing",
                "id": "Adv Strategy"
            },
            {
                "values": [
                    {
                        "value": "Casual gamers",
                        "id": 51,
                        "label": "Casual Gamers"
                    }
                ],
                "label": "Gaming",
                "ico": "",
                "id": "general-gamers-segments",
                "pic": ""
            }
        ],
        "label": "Lifestyles",
        "ico": "",
        "id": "lifestyiles-cy",
        "pic": ""
    }
    flatten_result = flatten_dict(test_dict, children_key="values", result_dict=result_input_dict)
    assert flatten_result == {'lifestyiles-cy':
        {'values':
            [
                {'values':
                    [
                        {'value': 'Ads Paper', 'id': 4, 'pic': '/assets/img/psychographics/ico/psy_4.jpg',
                         'label': 'Print Ads', 'level': 4},
                        {'value': 'Ads EmergingMediaVehicles', 'id': 3,
                         'pic': '/assets/img/psychographics/ico/psy_3.jpg', 'label': 'Unconventional Ads', 'level': 4}
                    ],
                    'label': 'Advertising', 'ico': 'flaticon-marketing', 'id': 'Adv Strategy', 'level': 3
                },
                {'values':
                    [
                        {'value': 'Casual gamers', 'id': 51, 'label': 'Casual Gamers', 'level': 4}
                    ],
                    'label': 'Gaming', 'ico': '', 'id': 'general-gamers-segments', 'pic': '', 'level': 3
                }
            ],
            'label': 'Lifestyles', 'ico': '', 'id': 'lifestyiles-cy', 'pic': '', 'level': 2},
        'Adv Strategy': {'values': [
            {'value': 'Ads Paper', 'id': 4, 'pic': '/assets/img/psychographics/ico/psy_4.jpg', 'label': 'Print Ads',
             'level': 4},
            {'value': 'Ads EmergingMediaVehicles', 'id': 3, 'pic': '/assets/img/psychographics/ico/psy_3.jpg',
             'label': 'Unconventional Ads', 'level': 4}], 'label': 'Advertising', 'ico': 'flaticon-marketing',
            'id': 'Adv Strategy', 'level': 3},
        4: {'value': 'Ads Paper', 'id': 4, 'pic': '/assets/img/psychographics/ico/psy_4.jpg', 'label': 'Print Ads',
            'level': 4},
        3: {'value': 'Ads EmergingMediaVehicles', 'id': 3, 'pic': '/assets/img/psychographics/ico/psy_3.jpg',
            'label': 'Unconventional Ads', 'level': 4}, 'general-gamers-segments': {
            'values': [{'value': 'Casual gamers', 'id': 51, 'label': 'Casual Gamers', 'level': 4}], 'label': 'Gaming',
            'ico': '', 'id': 'general-gamers-segments', 'pic': '', 'level': 3},
        51: {'value': 'Casual gamers', 'id': 51, 'label': 'Casual Gamers', 'level': 4}}


def test_flatten_dict_list_input_psychographics():
    test_list = [
        {
            "values": [
                {
                    "value": "Ads Paper",
                    "id": 4,
                    "pic": "/assets/img/psychographics/ico/psy_4.jpg",
                    "label": "Print Ads"
                },
                {
                    "value": "Ads EmergingMediaVehicles",
                    "id": 3,
                    "pic": "/assets/img/psychographics/ico/psy_3.jpg",
                    "label": "Unconventional Ads"
                },
            ],
            "label": "Advertising",
            "ico": "flaticon-marketing",
            "id": "Adv Strategy"
        },
        {
            "values": [
                {
                    "value": "Casual gamers",
                    "id": 51,
                    "label": "Casual Gamers"
                }
            ],
            "label": "Gaming",
            "ico": "",
            "id": "general-gamers-segments",
            "pic": ""
        }
    ]
    flatten_result = flatten_list_to_dict(test_list, children_key="values")
    assert flatten_result == {
        "general-gamers-segments": {
            "level": 1,
            "values": [
                {
                    "level": 2,
                    "value": "Casual gamers",
                    "id": 51,
                    "label": "Casual Gamers"
                }
            ],
            "label": "Gaming",
            "ico": "",
            "id": "general-gamers-segments",
            "pic": ""
        },
        51: {
            "level": 2,
            "value": "Casual gamers",
            "id": 51,
            "label": "Casual Gamers"
        },
        "Adv Strategy": {
            "level": 1,
            "values": [
                {
                    "level": 2,
                    "value": "Ads Paper",
                    "id": 4,
                    "pic": "/assets/img/psychographics/ico/psy_4.jpg",
                    "label": "Print Ads"
                },
                {
                    "level": 2,
                    "value": "Ads EmergingMediaVehicles",
                    "id": 3,
                    "pic": "/assets/img/psychographics/ico/psy_3.jpg",
                    "label": "Unconventional Ads"
                },
            ],
            "label": "Advertising",
            "ico": "flaticon-marketing",
            "id": "Adv Strategy"
        },
        4: {
            "level": 2,
            "value": "Ads Paper",
            "id": 4,
            "pic": "/assets/img/psychographics/ico/psy_4.jpg",
            "label": "Print Ads"
        },
        3: {
            "level": 2,
            "value": "Ads EmergingMediaVehicles",
            "id": 3,
            "pic": "/assets/img/psychographics/ico/psy_3.jpg",
            "label": "Unconventional Ads"
        }
    }


def test_remove_nulls():
    test_input_obj = {
        'a': 1,
        'b': None,
        'c': {
            'a': 1,
            'b': None,
            'd': [1, 2, 3, None, ['a', 'b', None]]
        },
        'd': [
            1, 2, 3, {
                'a': 1,
                'b': None,
                'd': [1, None, 2]
            }, None
        ]
    }

    expected_output = {
        'a': 1,
        'c': {
            'a': 1,
            'd': [1, 2, 3, ['a', 'b']]
        },
        'd': [
            1, 2, 3, {
                'a': 1,
                'd': [1, 2]
            },
        ]
    }
    assert remove_nulls(test_input_obj) == expected_output
