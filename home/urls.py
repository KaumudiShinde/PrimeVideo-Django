from django.urls import path
from . import views

urlpatterns = [

    path(
        "",
        views.home,
        name="home"
    ),

    path(
        "movies/",
        views.movies,
        name="movies"
    ),

    path(
        "movie/<int:movie_id>/",
        views.movie_detail,
        name="movie_detail"
    ),

    path(
        "add-movie/",
        views.add_movie,
        name="add_movie"
    ),

    path(
        "edit-movie/<int:movie_id>/",
        views.edit_movie,
        name="edit_movie"
    ),

    path(
        "delete-movie/<int:movie_id>/",
        views.delete_movie,
        name="delete_movie"
    ),

    path(
        "genre/<str:genre_name>/",
        views.genre_movies,
        name="genre_movies"
    ),
    path(
    "manage-movies/",
    views.manage_movies,
    name="manage_movies"
),
]