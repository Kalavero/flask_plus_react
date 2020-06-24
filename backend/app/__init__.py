from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    app = Flask(__name__, instance_relative_config=False)

    # Load config
    app.config.from_object('config.Config')

    # Init database
    db.init_app(app)

    # Init marshmallow
    ma.init_app(app)

    with app.app_context():
        from . import routes
        db.create_all()

        return app

