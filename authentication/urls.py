from django.urls import path,include
from . import views

urlpatterns = [
	path("login/",views.custom_login,name="login"),
	path("", include('django.contrib.auth.urls')),
]
