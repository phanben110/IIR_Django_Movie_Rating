# ratings/forms.py
from django import forms
from .models import Rating
from .models import User, Movie


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['user_id', 'movie_id', 'rating']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['user_age', 'user_name']

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['movie_name']
