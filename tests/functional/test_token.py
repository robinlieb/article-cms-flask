def test_get_token(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/getToken' page is requested (GET)
    THEN check that the response is valid
    """

    response = test_client.get('/getToken', follow_redirects=True)
    assert response.status_code == 200
    assert b'Sign In' in response.data
    assert b'Username' in response.data
    assert b'Password' in response.data