from FlaskWebProject.models import User
from FlaskWebProject import app
import pytest

@pytest.fixture(scope='module')
def test_client():
    flask_app = app
    flask_app.testing = True

    with flask_app.test_client() as test_client:
        yield test_client

@pytest.fixture(scope='module')
def new_user():
    return User()