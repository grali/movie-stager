from django import forms

from .models import Movie, Review


<<<<<<< HEAD
=======
class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = [
            "name",
            "description"
        ]

>>>>>>> 589b4ade64b2070fbe8e573739e0b57fdd7f67a4

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            "rating",
            "description"
        ]
