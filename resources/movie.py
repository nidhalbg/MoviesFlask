from flask import Blueprint, Response, request, jsonify
from database.models import Movie

movies = Blueprint('movies', __name__)

@movies.route('/movies')
def get_movies():
    movies = Movie.objects().to_json()
    return Response(movies, mimetype="application/json", status=200)

@movies.route('/movies', methods=['POST'])
def add_movie():
    body = request.get_json()
    movie = Movie(**body).save()
    return jsonify(movie), 200

@movies.route('/movies/<id>', methods=['PUT'])
def update_movie(id):
    body = request.get_json()
    #Movie.objects.get(id=id).update(**body)
    movie = Movie.objects.get(id=id).update(**body)

    return jsonify({"message": "success", "movie": movie}), 200

@movies.route('/movies/<id>', methods=['DELETE'])
def delete_movie(id):
    movie = Movie.objects.get(id=id).delete()
    return jsonify({'done': 'done'}), 200

@movies.route('/movies/<id>')
def get_movie(id):
    movie = Movie.objects.get(id=id).to_json()
    return Response(movie, mimetype="application/json", status=200)