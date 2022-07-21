from glob import escape
import jwt
from requests import post
from app import app
from flask import jsonify, make_response, request
from werkzeug.security import check_password_hash
from app.routes.decorators import token_required

@app.route('/certificado')
@token_required
def certificado(current_sensor):
    response = post('127.0.0.1:5001/opensslertificate', data=current_sensor)
    if response.status_code == 200:
        return jsonify({'msg': 'autenticado', 'certificado': response.json()['certificado']}), 200
    return jsonify({'msg': 'credenciais invalidas','certificado': None}), 400

# @app.route('/teste')
# def teste():
#     return jsonify({'message': 'Hello World!'}), 200

@app.route('/token', methods=['POST'])
def token():
    auth:dict = request.get_json()
    if not auth or not auth.get('nome_sensor') or not auth.get('senha'):
        return make_response('Could not verify!', 401, {'WWW-Authenticate': 'Basic-realm= "Login required!"'})
    # User.query.filter_by(username=auth['username']).first()
    response = post('127.0.0.1:5001/sensor', json={'nome': auth.get('nome_sensor')}) # Buscar sensor no banco de dados e retornar id e senha
    
    if response.status_code != 200:
        return make_response('Could not verify sensor', response.status_code, {'WWW-Authenticate': 'Basic-realm= "No user found!"'})
    sensor = response.json()
    if check_password_hash(sensor['senha'], auth.get('senha')):
        token = jwt.encode({'public_id': sensor['id']}, app.config['SECRET_KEY'], 'HS256')
        return make_response(jsonify({'token': token}), 201)

    return make_response('Could not verify password!', 403, {'WWW-Authenticate': 'Basic-realm= "Wrong Password!"'})

