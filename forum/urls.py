from django.urls import path
from . import views

urlpatterns = [
	path("<movie_id>",views.index,name="showForum"),
]