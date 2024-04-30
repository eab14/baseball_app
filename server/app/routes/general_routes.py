from flask import jsonify
from . import general_bp

@general_bp.route('/status', methods=['GET'])
def index():
    return jsonify({ 'database' : "Postgres" })