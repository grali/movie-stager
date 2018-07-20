from django import forms

from .models import Movie, Review


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = [
            "name",
            "description"
        ]


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            "rating",
            "description"
        ]
