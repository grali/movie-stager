from django.db import models
from django.contrib.auth.models import User
from movies.models import Movie

# Create your models here.

class Topic(models.Model):
	movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	title = models.CharField(max_length=150)
	content = models.TextField()
	created_at = models.DateTimeField(auto_now=True)
	updated_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "{} - {} - {}".format(self.movie.name,self.user,self.title)
