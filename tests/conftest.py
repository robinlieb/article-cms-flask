import flask
from FlaskWebProject.models import User, Post
from FlaskWebProject import create_app, db
from instance.config import TestConfig
import pytest

@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app(TestConfig)

    with flask_app.test_client() as test_client:
        with flask_app.app_context():
            yield test_client

@pytest.fixture(scope='module')
def init_database(test_client):

    db.create_all()

    user = User()
    user.username = "admin"
    user.password_hash = 'pbkdf2:sha256:260000$p1hn7qX6mzriQDYs$5859d3d329d33d7c88c9f568aec82cef54c2cbdfa04674994cb3f91d1ed036e2'
    db.session.add(user)

    db.session.commit()

    yield

    db.drop_all()

@pytest.fixture(scope='function')
def login_default_user(test_client):
    test_client.post(
        '/login',
        data=dict(username='admin', password='helloworld'),
        follow_redirects=True
    )

    yield

    test_client.get('/logout', follow_redirects=True)

@pytest.fixture(scope='module')
def new_user():
    return User()