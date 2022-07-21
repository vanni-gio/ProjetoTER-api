import jwt
from requests import post
from app import app
from flask import jsonify, make_response, request
from werkzeug.security import check_password_hash
from app.routes.decorators import token_required

@app.route('/certificado')
@token_required
def certificado(current_sensor):
    response = post('127.0.0.1:5001', data=current_sensor)
    return jsonify({'certificado': 'Hello World!'}), 200

@app.route('/teste')
def teste():
    return jsonify({'message': 'Hello World!'}), 200

@app.route('/token', methods=['POST'])
def token():
    auth:dict = request.get_json()
    if not auth or not auth.get('nomesensor') or not auth.get('senha'):
        return make_response('Could not verify!', 401, {'WWW-Authenticate': 'Basic-realm= "Login required!"'})
    # User.query.filter_by(username=auth['username']).first()
    sensor = {'id': 1, 'senha': 'pbkdf2:sha256:260000$XmSIHyMRs4bGAeQO$188052f7a16fc877ca4d0905c9dbec7f11b41cd150f32fa28f758fb6edba0731'} # Buscar sensor no banco de dados e retornar id e senha
    if not sensor:
        return make_response('Could not verify user, Please signup!', 401, {'WWW-Authenticate': 'Basic-realm= "No user found!"'})

    if check_password_hash(sensor.get('senha'), auth.get('senha')):
        token = jwt.encode({'public_id': sensor.get('id')}, app.config['SECRET_KEY'], 'HS256')
        return make_response(jsonify({'token': token}), 201)

    return make_response('Could not verify password!', 403, {'WWW-Authenticate': 'Basic-realm= "Wrong Password!"'})

