from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views


urlpatterns = [
    path("movies/", views.MovieList.as_view()),
    path("movies/create/", views.MovieCreate.as_view()),
    path("movies/create_function/", views.movie_create),
    path("movies/<int:id>/", views.MovieDetail.as_view()),
    path("users/register/", views.register),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'), #esta ruta no acepta GET, pues paso username y password
]