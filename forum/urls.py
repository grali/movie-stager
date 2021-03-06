from django.urls import path
from . import views

urlpatterns = [
	path("<movie_id>",views.index,name="showForum"),
	path("<movie_id>/create",views.createTopic,name="createTopic"),
	path("<topic_id>/edit",views.editTopic,name="editTopic"),
	path("<topic_id>/topic",views.showTopic,name="showTopic"),
	path("<topic_id>/topic/createComment",views.createTopicComment,name="createComment"),
	path("<topic_id>/topic/delete",views.deleteTopic,name="deleteTopic"),
]