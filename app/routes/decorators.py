

# Authentication decorator
from functools import wraps
from app import app
from flask import jsonify, make_response, request
import jwt


def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        # ensure the jwt-token is passed with the headers
        print(request.headers)
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token: # throw error if no token provided
            return make_response(jsonify({"message": "A valid token is missing!"}), 401)
        try:
           # decode the token to obtain user public_id
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            print(data['public_id'])
            # User.query.filter_by(public_id=data['public_id']).first()
            current_user = {'id': data['public_id'], 'senha': '12345'} # buscar sensor pelo id publico
        except:
            return make_response(jsonify({"message": "Invalid token!"}), 401)
         # Return the user information attached to the token
        return f(current_user, *args, **kwargs)
    return decorator