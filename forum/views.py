from django.shortcuts import render
from movies.models import Movie
from .models import Topic
# Create your views here.

def index(request,movie_id):
	movie = Movie.objects.get(pk=movie_id)
	forum_topics = Topic.objects.filter(movie=movie)
	context = {"movie":movie,"forum_topics":forum_topics}
	return render(request,"forum/index.html",context)