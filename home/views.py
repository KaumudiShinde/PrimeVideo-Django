from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Movie
from .forms import MovieForm


@login_required
def home(request):
    movies = Movie.objects.all()

    return render(request, "home.html", {
        "movies": movies
    })


@login_required
def movies(request):

    search = request.GET.get("search", "")
    genre = request.GET.get("genre", "")

    movies = Movie.objects.all()

    if search:
        movies = movies.filter(
            name__icontains=search
        )

    if genre:
        movies = movies.filter(
            genre__icontains=genre
        )

    genres = Movie.objects.values_list(
        "genre",
        flat=True
    ).distinct()

    return render(request, "movies.html", {
        "movies": movies,
        "search": search,
        "genres": genres,
        "selected_genre": genre
    })


@login_required
def movie_detail(request, movie_id):

    movie = get_object_or_404(Movie, id=movie_id)

    return render(request, "movie_detail.html", {
        "movie": movie
    })


@login_required
def add_movie(request):

    if not request.user.is_staff:
        return redirect("home")

    if request.method == "POST":

        form = MovieForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("manage_movies")

    else:
        form = MovieForm()

    return render(request, "add_movie.html", {
        "form": form
    })


@login_required
def edit_movie(request, movie_id):

    if not request.user.is_staff:
        return redirect("home")

    movie = get_object_or_404(Movie, id=movie_id)

    if request.method == "POST":

        form = MovieForm(
            request.POST,
            instance=movie
        )

        if form.is_valid():
            form.save()
            return redirect("manage_movies")

    else:
        form = MovieForm(instance=movie)

    return render(request, "edit_movie.html", {
        "form": form,
        "movie": movie
    })


@login_required
def delete_movie(request, movie_id):

    if not request.user.is_staff:
        return redirect("home")

    movie = get_object_or_404(Movie, id=movie_id)

    if request.method == "POST":

        movie.delete()
        return redirect("manage_movies")

    return render(request, "delete_movie.html", {
        "movie": movie
    })

@login_required
def genre_movies(request, genre_name):

    movies = Movie.objects.filter(
        genre__icontains=genre_name
    )

    return render(request, "movies.html", {
        "movies": movies
    })



@login_required
def manage_movies(request):

    if not request.user.is_staff:
        return redirect("home")

    movies = Movie.objects.all()

    return render(request, "manage_movies.html", {
        "movies": movies
    })


