import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.models import User
from dotenv import load_dotenv
import os

load_dotenv()

db = SQLAlchemy()
from app.models import *

def create_app():

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    return app

def seed_database():

    app = create_app()

    with app.app_context():

        db.drop_all()
        db.create_all()

        with open('data/users.json', 'r') as f:
            data = json.load(f)

        for user_data in data:
            first_name = user_data['first_name']
            last_name = user_data['last_name']
            password = user_data['password']
            email = user_data['email']

            user = User(first_name=first_name, last_name=last_name, password=password, email=email)
            db.session.add(user)

        db.session.commit()

        print('\n')
        print('- - - [ Users ] Table Seeded')
        print('- - - [ Database ] Seeded')
        print('\n')

if __name__ == "__main__":
    seed_database()