# from app import app
# import jwt
# import werkzeug.security
# from flask import jsonify,request
# from functools import wraps

# def auth():
#     auth = request.authorization
#     if not auth or not auth.username or not auth.password:
#         return jsonify({'message': 'could not verify', 'WWW-Authenticate': 'Basic auth="Login required"'}), 401
    
#     sensor = sensor_by_id()
#     if not sensor:
#         return jsonify({'message': 'user not found', 'data': {}}), 401

    

