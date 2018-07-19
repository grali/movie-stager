from django.shortcuts import render,redirect
from django.contrib.auth.views import login
# Create your views here.

def custom_login(request,**kwargs):
	if request.user.is_authenticated:
		return redirect("/")
	else:
		return login(request)