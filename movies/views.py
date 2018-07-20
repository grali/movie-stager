from django.shortcuts import render
from .models import Movie,Review
from forum.models import Topic

# Create your views here.

def index(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {
        "movies" : movies
    })

def showMovie(request,movie_id):
	movie = Movie.objects.get(pk=movie_id)
	movie_topics = Topic.objects.filter(movie=movie)
	movie_reviews = Review.objects.filter(movie=movie)
	return render(request,"movies/showMovie.html",{
		"movie":movie,
		"movie_topics":movie_topics,
		"movie_reviews":movie_reviews
		})