
def test_get_post_with(test_client, init_database, login_default_user):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/post/<int:id>' page is requested (GET)
    THEN check that the response is valid
    """

    response = test_client.get('/post/1', follow_redirects=True)
    assert response.status_code == 200
    assert b'John Smith' in response.data
    assert b'Lorem ipsum dolor sit amet' in response.data
    assert b'Proin sit amet mi ornare, ultrices augue quis, facilisis tellus.' in response.data

def test_get_post_with_anonymous_user(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/post/<int:id>' page is requested (GET) with anonymous user
    THEN check that the response is valid
    """

    response = test_client.get('/post/1', follow_redirects=True)
    assert response.status_code == 200
    assert b'Sign In' in response.data
    assert b'Username' in response.data
    assert b'Password' in response.data

def test_create_post_with_anonymous_user(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/new_post' page is requested (POST) with anonymous user
    THEN check that the response is valid
    """

    response = test_client.get('/new_post', follow_redirects=True)
    assert response.status_code == 200
    assert b'Sign In' in response.data
    assert b'Username' in response.data
    assert b'Password' in response.data

