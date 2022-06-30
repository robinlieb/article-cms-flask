from FlaskWebProject.views import _build_msal_app, _build_auth_url
from urllib import parse

def test_build_msal_app():
    """
    GIVEN a authority url
    WHEN a msal app is created
    THEN check if authority is set correctly
    """
    authority = "https://login.microsoftonline.com/common"
    authorization_endpoint = "https://login.microsoftonline.com/common/oauth2/v2.0/authorize"
    device_authorization_endpoint = "https://login.microsoftonline.com/common/oauth2/v2.0/devicecode"
    token_endpoint = "https://login.microsoftonline.com/common/oauth2/v2.0/token"

    app = _build_msal_app(authority=authority)

    assert app.authority.authorization_endpoint == authorization_endpoint
    assert app.authority.device_authorization_endpoint == device_authorization_endpoint
    assert app.authority.token_endpoint == token_endpoint

def test_build_auth_url():
    """
    GIVEN a authority and redirect url
    WHEN an auth url is created
    THEN check if auth url contains quoted redirect url
    """
    authority = "https://login.microsoftonline.com/common"
    redirect_url = "https://test.com/authorized"
    redirect_url_quoted = "https%3A%2F%2Ftest.com%2Fauthorized"

    auth_url = _build_auth_url(redirect_url=redirect_url, authority=authority)

    assert redirect_url_quoted in auth_url