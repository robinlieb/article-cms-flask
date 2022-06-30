"""
The flask application package.
"""
import logging
from flask import Flask
from instance.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session

db = SQLAlchemy()
login = LoginManager()
login.login_view = 'users.login'

def create_app(config_class=Config):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_class)
    app.logger.setLevel(logging.WARNING)
    streamHander = logging.StreamHandler()
    streamHander.setLevel(logging.WARNING)
    app.logger.addHandler(streamHander)
    Session(app)
    initialize_extensions(app)
    register_blueprints(app)
    return app

def initialize_extensions(app):
    db.init_app(app)
    login.init_app(app)

def register_blueprints(app):
    from FlaskWebProject.users import users_blueprint
    from FlaskWebProject.posts import posts_blueprint
    app.register_blueprint(users_blueprint)
    app.register_blueprint(posts_blueprint)
