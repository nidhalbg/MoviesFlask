from flask import Response, request, jsonify, json
from database.models import Movie, User
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource


class MoviesApi(Resource):
    @jwt_required
    def get(self):
        movies = Movie.objects().to_json()
        return Response(movies, mimetype="application/json", status=200)

    @jwt_required
    def post(self):
        user_id = get_jwt_identity()
        user = User.objects.get(id=user_id)

        body = request.get_json()
        movie = Movie(**body, added_by=user).save()

        user.update(push__movies=movie)
        user.save()

        return Response(movie.to_json(), mimetype="application/json", status=200)

class MovieApi(Resource):
    @jwt_required
    def put(self, id):
        user_id = get_jwt_identity()
        movie = Movie.objects.get(id=id, added_by=user_id)
        body = request.get_json()
        movie = Movie.objects.get(id=id).update(**body)
        return Response(json.dumps({"message": "success"}), mimetype="application/json", status=200)

    @jwt_required
    def delete(self, id):
        user_id = get_jwt_identity()
        movie = Movie.objects.get(id=id, added_by=user_id)
        movie.delete()
        return '', 200

    def get(self, id):
        movies = Movie.objects.get(id=id).to_json()
        return Response(movies, mimetype="application/json", status=200)