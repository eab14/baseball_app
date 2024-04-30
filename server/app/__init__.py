from flask import Flask
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os
from app.db import init_db

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'super-secret'

jwt = JWTManager(app)

from app.routes import general_bp, user_bp
app.register_blueprint(general_bp, url_prefix='/api')
app.register_blueprint(user_bp, url_prefix='/api')

init_db(app)

if __name__ == '__main__':
    app.run(debug=True)