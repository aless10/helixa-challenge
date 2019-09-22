from unittest import mock

from flask import url_for

from tests.conftest import raise_exception


@mock.patch("helixa_app.cache.cache_utils.call_redis")
@mock.patch("helixa_app.tasks.strategies.dict_loop.get_obj_from_value")
def test_dict_loop_valid_body(mock_get_obj, mock_redis, client):
    mock_redis.return_value = None
    test_return_value = {'psychographics': [{
        "values": [
            {
                "value": "Ads Paper",
                "id": 4,
                "pic": "/assets/img/psychographics/ico/psy_4.jpg",
                "label": "Print Ads"
            },
        ],
        "label": "Advertising",
        "ico": "flaticon-marketing",
        "id": "test_value"
    }], 'category': []}

    mock_get_obj.return_value = test_return_value
    body = {"value": "test", "sublayer": "test_sublevel"}
    response = client.post(url_for('api_v1.dict-loop'), json=body)
    assert response.status_code == 200
    assert response.json == test_return_value


@mock.patch("helixa_app.cache.cache_utils.call_redis")
def test_dict_loop_invalid_body(mock_redis, client):
    mock_redis.return_value = None
    body = {"value": None, "sublayer": None}
    response = client.post(url_for('api_v1.dict-loop'), json=body)
    assert response.status_code == 400


@mock.patch("helixa_app.cache.cache_utils.call_redis")
@mock.patch("helixa_app.tasks.task_executor.RequestSchema.load")
def test_dict_loop_server_error(mock_load, mock_redis, client):
    mock_redis.return_value = None
    mock_load.side_effect = raise_exception
    body = {"value": "value_1", "sublayer": "sublayer_1"}
    response = client.post(url_for('api_v1.dict-loop'), json=body)
    assert response.status_code == 500
