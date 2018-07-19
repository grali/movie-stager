from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "{name}, {desc}".format(name=self.name, desc=self.description)

    def __unicode__(self):
        return "{name}, {desc}".format(name=self.name, desc=self.description)


class Review(models.Model):
    user = models.ManyToManyField(User)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "'{user}' added review on '{movie}'".format(user=self.user, movie=self.movie)

    def __unicode__(self):
        return "'{user}' added review on '{movie}'".format(user=self.user, movie=self.movie)
