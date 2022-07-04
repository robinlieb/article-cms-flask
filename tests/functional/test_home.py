
def test_home_page(test_client, init_database, login_default_user):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """

    response = test_client.get('/', follow_redirects=True)
    assert response.status_code == 200
    assert b'admin' in response.data
    assert b'Logout' in response.data
    assert b'Author' in response.data
    assert b'Title' in response.data
    assert b'Subtitle' in response.data
    assert b'Create New Post' in response.data

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
    assert b'Username' in response.data
    assert b'Password' in response.data