from helixa_app.db.relational_db.models.models_utils import get_children_ids


def test_get_children_ids():
    test_tuple = ({
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
    })

    result = get_children_ids(test_tuple, children_key="children")
    assert result == [0, 1, 14]
