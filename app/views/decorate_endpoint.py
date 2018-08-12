from flask import  jsonify, request, current_app
import jwt
from functools import wraps
import datetime



def generate_token(subject):
    """
    Generates the Authentication Token
    :return: string
    """

    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
            'iat': datetime.datetime.utcnow(),
            'sub': subject
        }
        generated_token = jwt.encode(
            payload, 'kato123456',
            algorithm='HS256'
        )

        return generated_token.decode('utf-8')
    except Exception as e:
        return e



def decode_token(authentication_token):
    """
    Decodes the authentication token
    :param authentication_token:
    :return: integer|string
    """
    try:
        payload = jwt.decode(authentication_token, 'kato123456')
        return payload['sub']
    except jwt.ExpiredSignatureError:
        return 'Expired signature. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'


def protected(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.headers['Authorization']
        if not auth:
            return jsonify({'message': 'Token missing'})
        else:
            try:
                user = decode_token(auth)
            except Exception as error:
                print(error)
                return jsonify({'message': 'Invalid token'})
        return f(user,*args, **kwargs)
    return decorated
