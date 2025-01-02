from flask import Flask
from flask_sqlalchemy import SQLAlchemy
<<<<<<< HEAD
from flask_migrate import Migrate 


db = SQLAlchemy()
migrate = Migrate() 

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///budget.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
=======
from flask_migrate import Migrate
from app.config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    # Load configuration from Config class
    app.config.from_object(Config)
>>>>>>> upstream/main

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        from .routes import bp
        app.register_blueprint(bp)
<<<<<<< HEAD
        db.create_all()  # Crée les tables

    return app




=======
        db.create_all()  # Create tables

    return app
>>>>>>> upstream/main
