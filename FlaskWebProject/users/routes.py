from datetime import datetime
from flask import render_template, flash, redirect, request, session, url_for, current_app
from werkzeug.urls import url_parse
from instance.config import Config
from FlaskWebProject.forms import LoginForm
from flask_login import current_user, login_user, logout_user, login_required
from FlaskWebProject.models import User, Post
import msal
import uuid
from . import users_blueprint

@users_blueprint.route('/')
@users_blueprint.route('/home')
@login_required
def home():
    user = User.query.filter_by(username=current_user.username).first_or_404()
    posts = Post.query.all()
    return render_template(
        'users/index.html',
        title='Home Page',
        posts=posts
    )

@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('users.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('users.login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('users.home')
        return redirect(next_page)
    session["state"] = str(uuid.uuid4())
    redirect_url = url_for('users.authorized', _external=True, _scheme='https')
    auth_url = _build_auth_url(redirect_url=redirect_url, scopes=Config.SCOPE, state=session["state"])
    return render_template('users/login.html', title='Sign In', form=form, auth_url=auth_url)

@users_blueprint.route(Config.REDIRECT_PATH)  # Its absolute URL must match your app's redirect_uri set in AAD
def authorized():
    if request.args.get('state') != session.get("state"):
        return redirect(url_for("users.home"))  # No-OP. Goes back to Index page
    if "error" in request.args:  # Authentication/Authorization failure
        return render_template("users/auth_error.html", result=request.args)
    if request.args.get('code'):
        cache = _load_cache()
        result = _build_msal_app(cache=cache).acquire_token_by_authorization_code(
             code=request.args.get('code'),
             scopes=Config.SCOPE,
             redirect_uri=url_for('users.authorized', _external=True, _scheme='https')
         )
        if "error" in result:
            current_app.logger.warning("Recieved error trying to aquire token")
            return render_template("users/auth_error.html", result=result)
        session["user"] = result.get("id_token_claims")
        # Note: In a real app, we'd use the 'name' property from session["user"] below
        # Here, we'll use the admin username for anyone who is authenticated by MS
        user = User.query.filter_by(username="admin").first()
        login_user(user)
        _save_cache(cache)
    return redirect(url_for('users.home'))

@users_blueprint.route('/logout')
def logout():
    logout_user()
    if session.get("user"): # Used MS Login
        # Wipe out user and its token cache from session
        session.clear()
        # Also logout from your tenant's web session
        return redirect(
            Config.AUTHORITY + "/oauth2/v2.0/logout" +
            "?post_logout_redirect_uri=" + url_for("users.login", _external=True))

    return redirect(url_for('users.login'))

def _load_cache():
    cache = msal.SerializableTokenCache()
    if session.get('token_cache'):
        cache.deserialize(session['token_cache'])
    return cache

def _save_cache(cache):
    if cache.has_state_changed:
        session['token_cache'] = cache.serialize()

def _build_msal_app(cache=None, authority=None):
    return msal.ConfidentialClientApplication(
         client_id=Config.CLIENT_ID,
         client_credential=Config.CLIENT_SECRET,
         authority=authority, 
         token_cache=cache
     )

def _build_auth_url(redirect_url, authority=None, scopes=None, state=None):
    return _build_msal_app(authority=authority).get_authorization_request_url(
        scopes=scopes or [],
        state=state or str(uuid.uuid4),
        redirect_uri=redirect_url
    )
