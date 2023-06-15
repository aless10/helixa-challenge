from helixa_app.db.relational_db.repository import get_from_request
from helixa_app.schema.schema import RequestModel


def test_get_from_request(local_session):
    test_request = RequestModel(value="test_children_", sublayer="test_parent_1")
    result = get_from_request(local_session, test_request)
    assert result == {
        'category': [
            {'id': 2, 'name': 'test_children_1', 'level': '2', 'children': [], 'pic': None, 'type': None, 'l1': None,
             'l2': None, 'l3': None, 'l4': None, 'l5': None},
            {'id': 3, 'name': 'test_children_2', 'level': '2', 'children': [], 'pic': None, 'type': None, 'l1': None,
             'l2': None, 'l3': None, 'l4': None, 'l5': None}],
        'psychographics': [],
        'category_sublayer': [
            {'id': 2, 'name': 'test_children_1', 'level': '2', 'children': [], 'pic': None, 'type': None, 'l1': None,
             'l2': None, 'l3': None, 'l4': None, 'l5': None},
            {'id': 3, 'name': 'test_children_2', 'level': '2', 'children': [], 'pic': None, 'type': None, 'l1': None,
             'l2': None, 'l3': None, 'l4': None, 'l5': None}],
        'psychographics_sublayer': []}
