import logging.config
import os
import sys
from logging.handlers import TimedRotatingFileHandler

from flask import Flask

from student import api
from student.extensions import db, migrate
from student.middleware.restplus import api

def create_app(
        config=None,
        environment=os.environ.get(
            'FLASK_ENV',
            'development'),
        cli=True):
    """Application factory, used to create application
    """

    app = Flask('student')
    app.config['JWT_SECRET_KEY'] = os.environ.get(
        'JWT_SECRET_KEY', 'alien_secret')
    configure_app(app, environment)
    configure_extensions(app, cli)
    register_blueprints(app)

    return app



def configure_app(app, environment):
    """set configuration for application
    """
    if environment == 'testing':
        app.config.from_object('student.config.test')
    elif environment == 'production':
        app.config.from_object('student.config.prod')
    else:
        app.config.from_object('student.config.dev')


def configure_extensions(app, cli):
    """configure flask extensions
    """
    db.init_app(app)

    if cli is True:
        migrate.init_app(app, db)


def register_blueprints(app=None):
    """register all blueprints for application
    """
    app.register_blueprint(api.blueprint)