import os

from flask import Flask 

from .extensions import db
from .routes import main

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
    # postgresql://leshan_psql_user:wI4ogRNzK7XS2CQB6yeBGCeaKefqwe5b@dpg-d4avto3uibrs73fdp6jg-a.oregon-postgres.render.com/leshan_psql

    db.init_app(app)

    app.register_blueprint(main)

    return app