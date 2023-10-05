import os 
from flask import Flask
from . import db
from . import auth

def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY = 'mikey',
        DATABASE_HOST = os.environ.get('FLASK_DATABASE_HOST'),
        DATABASE_USER = os.environ.get('FLASK_DATABASE_USER'),
        DATABASE_PASSWORD=os.environ.get('FLASK_DATABASE_PASSWORD'),
        DATABASE = os.environ.get('FLASK_DATABASE')
    )
    
    db.init_app(app)
    app.register_blueprint(auth.bp)
    
    return app



