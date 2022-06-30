import flask
from FlaskWebProject.models import User
from FlaskWebProject import create_app
import pytest

@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app()
    flask_app.testing = True

    with flask_app.test_client() as test_client:
        yield test_client

@pytest.fixture(scope='module')
def new_user():
    return User()