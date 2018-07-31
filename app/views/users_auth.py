#imports
from flask import Blueprint, jsonify, request, make_response
import re
from passlib.hash import sha256_crypt
import jwt
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token, get_jwt_identity)
import datetime
from functools import wraps
from ..models.user_model import UsersModel

#create a blueprint
users = Blueprint('users',__name__)


def protected(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth:
            return jsonify({'message': 'Token missing'})
        else:
            try:
                jwt.decode(auth, 'charles123', algorithms=['HS256'])
            except Exception as error:
                print(error)
                return jsonify({'message': 'Invalid token'})
        return f(*args, **kwargs)
    return decorated


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

    #hash the password
    hashed_password = sha256_crypt.encrypt(password)
    new_user = UsersModel(name, email, hashed_password)
    new_user.insert_user()

    return jsonify({'status':'success', 'message': 'User {} has been registered'.format(name)}), 201


@users.route('/api/v1/auth/login', methods=['POST'])
def login_user():

    # getting user login data
    user_login_data = request.get_json()

    #check if returned user data is empty
    if not user_login_data:
        return jsonify({'Message': 'All fields are required'}), 400

    email = str(user_login_data.get('email')).strip()
    password = str(user_login_data.get('password')).strip()

    if not email or email == "":
        return jsonify({'Message': 'email is required'}), 400

    if not password or password == "":
        return jsonify({'Message': 'password  is required'}), 400

    loggedin_user = UsersModel.fetch_user(email)

    submited_password = sha256_crypt.encrypt(password)
    stored_password = loggedin_user[3]

    if sha256_crypt.verify(submited_password,stored_password):
        token = jwt.encode({"email": email, 'exp': datetime.datetime.utcnow()
        + datetime.timedelta(minutes=20)}, 'charles123')
        return jsonify(token.decode('utf-8'))

    return jsonify({"Message": "Welcome {}. You are logged in".format(loggedin_user[1])}), 200
