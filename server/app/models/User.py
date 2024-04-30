from app.db import db
import bcrypt
from datetime import datetime
from flask import jsonify
from flask_jwt_extended import create_access_token, decode_token

class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.LargeBinary, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

    def __init__(self, first_name, last_name, password, email):
        self.first_name= first_name
        self.last_name= last_name
        self.email = email
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(rounds=10))
        self.date_created = datetime.now()

    @staticmethod
    def verify_password(input_password, hashed_password):
        input_password_bytes = input_password.encode('utf-8')
        return bcrypt.checkpw(input_password_bytes, hashed_password)
    
    def generate_auth_token(self):
        return create_access_token(identity=self.email)
    
    @staticmethod
    def verify_auth_token(token):
        try:
            data = decode_token(token)
            return User.query.get(data['identity'])
        except:
            return None