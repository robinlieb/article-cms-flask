from config import Config
from FlaskWebProject import app

def test_redirect_page(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/redirect' page is requested (GET)
    THEN check if redirects to home page
    """

    response = test_client.get(Config.REDIRECT_PATH)
    assert response.status_code == 302
    assert b'Redirecting' in response.data
