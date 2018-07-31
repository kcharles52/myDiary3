from flask import Blueprint, jsonify, make_response

users = Blueprint('users',__name__)


@users.route('/api/v1/auth/signup', methods=['POST'])
def register_user():
    pass


@users.route('/api/v1/auth/login', methods=['POST'])
def login_user():
    pass

