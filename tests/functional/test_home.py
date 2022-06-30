
def test_home_page(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/login' page is requested (GET)
    THEN check that the response is valid
    """

    response = test_client.get('/login')
    assert response.status_code == 200
    assert b'Sign In' in response.data
