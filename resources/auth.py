from flask import Response, request, jsonify, make_response, json
from flask_jwt_extended import create_access_token
from database.models import User
from flask_restful import Resource
import datetime

class SignupApi(Resource):
    def post(self):
        body = request.get_json()
        user = User(**body)
        user.hash_password()
        user.save()
        id = user.id
        res = json.dumps({'message': 'success', 'user': user})
        return Response(res, status=200, mimetype='application/json')
        #return make_response(jsonify({'message': 'success', 'id': str(id), 'user': user}), 200)
    
class LoginApi(Resource):
    def post(self):
        body = request.get_json()
        user = User.objects.get(email=body.get('email'))
        authorized = user.check_password(body.get('password'))
        if not authorized:
            return {'error': 'Email or password invalid'}, 401

        expires = datetime.timedelta(days=7)
        access_token = create_access_token(identity=str(user.id), expires_delta=expires)
        return {'token': access_token}, 200