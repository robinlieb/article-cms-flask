
def test_login_page(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/login' page is requested (GET)
    THEN check that the response is valid
    """

    response = test_client.get('/login')
    assert response.status_code == 200
    assert b'Sign In' in response.data
    assert b'Username' in response.data
    assert b'Password' in response.data

def test_login_logout(test_client, init_database):
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

    """
    GIVEN a Flask application configured for testing
    WHEN the '/logout' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get(
        '/logout',
        follow_redirects=True
    )

    assert response.status_code == 200
    assert b'Sign In' in response.data
    assert b'Username' in response.data
    assert b'Password' in response.data

def test_login_invalid_login(test_client, init_database):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/login' page is posted to with invalid credentials (POST)
    THEN check an error message is returned to the user
    """
    
    response = test_client.post(
        '/login',
        data=dict(username='admin', password='foo'),
        follow_redirects=True
    )

    assert response.status_code == 200
    assert b'Invalid username or password' in response.data

def test_login_already_logged_in(test_client, init_database, login_default_user):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/login' page is posted to (POST) when the user is already logged in
    THEN check the response is valid
    """

    response = test_client.post(
        '/login',
        data=dict(username='admin', password='helloworld'),
        follow_redirects=True
    )

    assert response.status_code == 200
    assert b'Logout' in response.data
    assert b'Author' in response.data
    assert b'Title' in response.data
    assert b'Subtitle' in response.data
    assert b'Create New Post' in response.data

def test_logout(test_client, init_database, login_default_user):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/logout' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get(
        '/logout',
        follow_redirects=True
    )

    assert response.status_code == 200
    assert b'Sign In' in response.data
    assert b'Username' in response.data
    assert b'Password' in response.data