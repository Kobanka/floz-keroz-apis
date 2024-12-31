from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 


db = SQLAlchemy()
migrate = Migrate() 

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///budget.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        from .routes import bp
        app.register_blueprint(bp)
        db.create_all()  # Crée les tables

    return app




