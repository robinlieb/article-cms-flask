
def test_login_page_with_anonymous_user(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET) with anonymous user
    THEN check that the response is valid
    """

    response = test_client.get('/', follow_redirects=True)
    assert response.status_code == 200
    print(response.data)
    assert b'Sign In' in response.data

def test_login(test_client, init_database):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/login' page is requested (POST) with known user
    THEN check that the response is valid
    """

    response = test_client.post(
        '/login',
        data=dict(username='admin', password='helloworld'),
        follow_redirects=True
    )

    assert response.status_code == 200
    assert b'Logout' in response.data