from django.shortcuts import render,redirect,reverse
from movies.models import Movie
from .models import Topic,TopicComment
from .forms import TopicForm,TopicCommentForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request,movie_id):
	movie = Movie.objects.get(pk=movie_id)
	forum_topics = Topic.objects.filter(movie=movie)
	context = {"movie":movie,"forum_topics":forum_topics}
	return render(request,"forum/index.html",context)

@login_required
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

@login_required
def editTopic(request,topic_id):
	topic = Topic.objects.get(pk=topic_id)
	form = TopicForm()
	context = {"form":form,"topic":topic}
	if request.method == "POST":
		form = TopicForm(request.POST,instance=topic)
		if form.is_valid():
			topic = form.save(commit=False)
			topic.save()
			return redirect(reverse("showTopic",args=(topic.id,)))
		else:
			return render(request,"forum/editTopic.html",context)
	else:
		return render(request,"forum/editTopic.html",context)

@login_required
def deleteTopic(request,topic_id):
	topic = Topic.objects.get(pk=topic_id)
	if topic.user == request.user:
		topic.delete()
	return redirect(reverse("showForum",args=(topic.movie.id,)))

@login_required
def createTopicComment(request,topic_id):
	topic = Topic.objects.get(pk=topic_id)
	form = TopicCommentForm()
	if request.method == "POST":
		form = TopicCommentForm(request.POST)
		if form.is_valid():
			topicComment = form.save(commit=False)
			topicComment.topic = topic
			topicComment.user = request.user
			topicComment.save()
			print("nice")
			return redirect(reverse("showTopic",args=(topic.id,)))
		else:
			context = {"form":form,"topic":topic}
			return render(request,"forum/createComment.html",context)
	else:
		return redirect(reverse("showTopic",args=(topic.id,)))


def showTopic(request,topic_id):
	topic = Topic.objects.get(pk=topic_id)
	form = TopicCommentForm()
	topic_comments = TopicComment.objects.filter(topic=topic)
	context = {"topic":topic,"topic_comments":topic_comments,"form":form}
	return render(request,"forum/showTopic.html",context)