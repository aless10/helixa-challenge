from flask import url_for


def test_dict_loop_invalid_body(client):
    body = {"value": None, "sublevel": None}
    response = client.post(url_for('api_v1.dict-loop'), json=body)
    assert response.status_code == 400
