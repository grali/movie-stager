from django.shortcuts import render,redirect,reverse
from .models import Movie,Review
from forum.models import Topic
from .forms import ReviewForm

# Create your views here.

def index(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {
        "movies" : movies
    })

def createReview(request,movie_id):
	movie = Movie.objects.get(pk=movie_id)
	form = ReviewForm()
	if request.method == "POST":
		form = ReviewForm(request.POST)
		if form.is_valid():
			review = form.save(commit=False)
			review.movie = movie
			review.user = request.user
			review.save()
			return redirect(reverse("showMovie",args=(movie.id,)))
		else:
			context = {"form":form}
			return render(request,"movie/newReview.html",context)
	else:
		context = {"form":form}
		return render(request,"movie/newReview.html",context)


def showMovie(request,movie_id):
	movie = Movie.objects.get(pk=movie_id)
	if request.method == "POST":
		createReview(request,movie_id)
	movie_topics = Topic.objects.filter(movie=movie)
	movie_reviews = Review.objects.filter(movie=movie)
	if len(movie_reviews) > 3:
		latest_movie_reviews = movie_reviews[:3]
	else:
		latest_movie_reviews = movie_reviews
	if len(movie_topics) > 3:
		latest_movie_topics = movie_topics[:3]
	else:
		latest_movie_topics = movie_topics
	form = ReviewForm()
	return render(request,"movies/showMovie.html",{
		"movie":movie,
		"latest_movie_topics":latest_movie_topics,
		"latest_movie_reviews":latest_movie_reviews,
		"form":form
		})
