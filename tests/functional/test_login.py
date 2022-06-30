
def test_login_page_with_anonymous_user(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET) with anonymous user
    THEN check that the response is valid
    """

    response = test_client.get('/')
    assert response.status_code == 302
    assert b'login' in response.data
