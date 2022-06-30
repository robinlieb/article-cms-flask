
def test_get_post_with_anonymous_user(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/post/<int:id>' page is requested (GET) with anonymous user
    THEN check that the response is valid
    """

    response = test_client.get('/post/1')
    assert response.status_code == 302
    assert b'login' in response.data

def test_create_post_with_anonymous_user(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/new_post' page is requested (POST) with anonymous user
    THEN check that the response is valid
    """

    response = test_client.get('/new_post')
    assert response.status_code == 302
    assert b'login' in response.data

