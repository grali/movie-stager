from django.shortcuts import render,redirect,reverse
from movies.models import Movie
from .models import Topic,TopicComment
from .forms import TopicForm
# Create your views here.

def index(request,movie_id):
	movie = Movie.objects.get(pk=movie_id)
	forum_topics = Topic.objects.filter(movie=movie)
	context = {"movie":movie,"forum_topics":forum_topics}
	return render(request,"forum/index.html",context)

def createTopic(request,movie_id):
	movie = Movie.objects.get(pk=movie_id)
	form = TopicForm()
	if request.method == "POST":
		form = TopicForm(request.POST)
		if form.is_valid():
			topic = form.save(commit=False)
			topic.movie = movie
			topic.user = request.user
			topic.save()
			return redirect(reverse("showForum",args=(movie.id,)))
		else:
			context = {"form":form}
			return render(request,"forum/newTopic.html",context)
	else:
		context = {"form":form}
		return render(request,"forum/newTopic.html",context)

def showTopic(request,topic_id):
	topic = Topic.objects.get(pk=topic_id)
	topic_comments = TopicComment.objects.filter(topic=topic)
	context = {"topic":topic,"topic_comments":topic_comments}
	return render(request,"forum/showTopic.html",context)