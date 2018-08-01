#imports
from flask import Blueprint, jsonify, request, make_response
import re
from ..models.user_model import UsersModel

#create a blueprint
users = Blueprint('users',__name__)


@users.route('/api/v1/auth/signup', methods=['POST'])
def register_user():
    #get user data from request
    user_registration_data = request.get_json()

    #check if data has been passed into URL
    if not user_registration_data:
        return jsonify({'Message': 'All fields are required'}), 400

    name = user_registration_data['name']
    email = str(user_registration_data['email']).strip()
    password = str(user_registration_data['password']).strip()

    if not name or name == "" or name == type(int) or len(name) < 3:
        return jsonify({'status':'Fail','message': 'Invalid name'}), 400

    if not re.match(r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+$)", email):
        return make_response(jsonify({
            "status": "Fail",
            "message": "Enter valid email"}), 400)
    if not password or password == "" or len(password) < 5:
        return jsonify({ 'status':'Fail','message': 'A stronger password  is required'}), 400

    new_user = UsersModel(name, email, password)
    UsersModel.insert_user(new_user)

    return jsonify({'status':'success', 'message': 'User {} has been registered'.format(name)}), 201


@users.route('/api/v1/auth/login', methods=['POST'])
def login_user():
    pass

