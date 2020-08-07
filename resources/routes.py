from .movie import MoviesApi, MovieApi
from .auth import SignupApi, LoginApi

def initialize_routes(api):
   api.add_resource(MoviesApi, '/movies')
   api.add_resource(MovieApi, '/movies/<id>')

   api.add_resource(SignupApi, '/auth/signup')
   api.add_resource(LoginApi, '/auth/login')