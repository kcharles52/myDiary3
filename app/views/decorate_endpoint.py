from flask import  jsonify, request, current_app
import jwt
from functools import wraps
import datetime



def generate_token(subject):
    """
    Generates the Authentication Token
    :return: string
    """
    print(current_app.secret_key)
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
            'iat': datetime.datetime.utcnow(),
            'sub': subject
        }
        generated_token = jwt.encode(
            payload, current_app.secret_key,
            algorithm='HS256'
        )
        return generated_token.decode('utf-8')
    except Exception as e:
        return e


@staticmethod
def decode_token(authentication_token):
    """
    Decodes the authentication token
    :param authentication_token:
    :return: integer|string
    """
    try:
        payload = jwt.decode(authentication_token, current_app.secret_key)
        return payload['sub']
    except jwt.ExpiredSignatureError:
        return 'Expired signature. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'


def protected(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth:
            return jsonify({'message': 'Token missing'})
        else:
            try:
                decoded_token = decode_token(auth)
                user_id = decoded_token[0]
                email = decoded_token[1]
                return user_id, email
            except Exception as error:
                print(error)
                return jsonify({'message': 'Invalid token'})
        return f(user_id,*args, **kwargs)
    return decorated
