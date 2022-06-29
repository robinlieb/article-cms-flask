from FlaskWebProject.models import User

def test_user_check_password(new_user):
    """
    GIVEN a user model
    WHEN a password of a User is set
    THEN check if the password is set correctly
    """

    new_user.set_password("Test")
    
    assert True == new_user.check_password("Test")
