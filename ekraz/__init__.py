#!/usr/bin/env python3
"""
"""
# install library
from flask import Flask
from dotenv import load_dotenv

# python standard library
import os

# project module
from .mysql import profil_db


load_dotenv()


def launch():

    app = Flask(__name__)
    
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.environ.get('USERNAME')}:{os.environ.get('PASSWORD')}/{os.environ.get('PROFILBASE')}"
    app.config['SQLALCHEMY_BINDS'] = {
        'auth': f"postgresql://{os.environ.get('USERNAME')}:{os.environ.get('PASSWORD')}/{os.environ.get('USERBASE')}"
    }

    profil_db.init_app(app)

    # call all database

    from .url import endpoint

    app.register_blueprint(endpoint)

    from .profil import (
        Permission,
        Profil,
        Entreprise,
        Experience,
        Formation,
        Language,
        Abonnement
    )

    with app.app_context():
        db.create_all()
    
    return app
