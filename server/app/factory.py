from flask import Flask

from .configurations import Config
from .extensions import db


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    from app.extensions import cors
    cors.init_app(app)

    # Set up database
    db.init_app(app)

    # imports api_s
    # from api.users_api import api as users_api

    # register api_s
    # app.register_blueprint(users_api)


    # Create tables
    with app.app_context():
        db.create_all()
        return app