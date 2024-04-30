from flask import Blueprint, request, jsonify
from app.models.User import User
from flask_jwt_extended import jwt_required, get_jwt_identity
from . import user_bp

@user_bp.route('/users', methods=['GET'])
def get_all_users():
    page = request.args.get('page', 1, type=int)
    per_page = 5

    users = User.query.paginate(page=page, per_page=per_page, error_out=False)
    user_list = [{'id': user.id, 'email': user.email, 'first_name': user.first_name, 'last_name': user.last_name} for user in users.items]

    return jsonify({
        'users': user_list,
        'total_users': users.total,
        'current_page': users.page,
        'total_pages': users.pages
    })

@user_bp.route('/users/login', methods=['POST'])
def login():
    data = request.json
    if 'email' not in data or 'password' not in data:
        return jsonify({'message': 'Missing email or password'}), 400

    user = User.query.filter_by(email=data['email']).first()

    if not user:
        return jsonify({'message': 'Invalid email or password'}), 401

    if not user.verify_password(data['password'], user.password):
        return jsonify({'message': 'Invalid email or password'}), 401

    token = user.generate_auth_token()
    return jsonify({'access_token': token}), 200

@user_bp.route('/users/verify', methods=['GET'])
@jwt_required()
def verify():
    email = get_jwt_identity()
    current_user = User.query.filter_by(email=email).first()
    return jsonify({'email': current_user.email}), 200