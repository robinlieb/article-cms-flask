"""
The flask application package.
"""
import logging
from flask import Flask
from instance.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session

def register_blueprints(app):
    from FlaskWebProject.users import users_blueprint
    from FlaskWebProject.posts import posts_blueprint
    app.register_blueprint(users_blueprint)
    app.register_blueprint(posts_blueprint)

app = Flask(__name__)
app.config.from_object(Config)
# TODO: Add any logging levels and handlers with app.logger
app.logger.setLevel(logging.WARNING)
streamHander = logging.StreamHandler()
streamHander.setLevel(logging.WARNING)
app.logger.addHandler(streamHander)
Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'
register_blueprints(app)
