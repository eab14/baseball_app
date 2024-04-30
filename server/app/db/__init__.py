from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask import current_app
import os

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')

engine = create_engine(DATABASE_URL, echo=True, pool_size=20, max_overflow=0)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
db = SQLAlchemy()

def init_db(app):
    db.init_app(app)
    with app.app_context():
        from app.models import User
        Base.metadata.create_all(bind=engine)