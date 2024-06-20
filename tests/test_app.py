from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_api_zero.app import app


def test_read_root():
    client = TestClient(app)

    response = client.get('/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}


def test_read_html():
    client = TestClient(app)

    response = client.get('/html')
    assert response.status_code == HTTPStatus.OK
    assert response.text.find('Olá Mundo') > 0
