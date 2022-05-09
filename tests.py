import os
import tempfile

import pytest

from app import app


@pytest.fixture
def client():
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client

    os.close(db_fd)
    os.unlink(app.config['DATABASE'])


def login(client, username, password):
    return client.post('/login', data=dict(
        username=username,
        password=password
    ), follow_redirects=True)


def test_registration(client):
    resp = client.get('/')
    assert b'CLEVER BIRDS' in resp.data
    assert resp.status == '200 OK'

    resp = client.post('/signup', data=dict(
        name='name1',
        username='username1',
        password='pass123',
        email='test@example.com',
        score=0,
        avatar='alfredo',
        gender='F'
    ))

    assert b'Congrats!' in resp.data

    resp = login(client, "username1", "pass123")

    assert b'User Dashboard' in resp.data

    resp = client.get('/changeavatar')
    assert b'daisy' in resp.data
    assert b'alfredo' in resp.data
    assert b'birdy' in resp.data


def test_delete_user(client):
    test_registration(client)
    resp = client.get('/useraccount')
    assert b'Manage Account' in resp.data

    resp = client.post('/useraccount')
    assert resp.status == '200 OK'


def test_game(client):
    test_registration(client)
    resp = client.get('/playgame')
    assert resp.status == '200 OK'

    resp = client.get('/save-score/1')
    assert resp.status == '200 OK'


def test_user_documentation(client):
    resp = client.get('/about')
    assert resp.status == '200 OK'

    resp = client.get('/privacy')
    assert resp.status == '200 OK'


def test_chatbot(client):
    resp = client.get('tweety')
    assert resp.status == '200 OK'
