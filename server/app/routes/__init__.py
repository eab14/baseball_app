from flask import Blueprint

general_bp = Blueprint('general', __name__)
user_bp = Blueprint('user', __name__)

from .general_routes import general_bp
from .user_routes import user_bp