from django import forms
from django.contrib.auth.models import User
from .models import Movie


class RegisterForm(forms.ModelForm):

    password = forms.CharField(
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = [
            'name',
            'genre',
            'releaseYear',
            'rating',
            'duration',
            'director',
            'cast',
            'description',
            'bannerUrl',
            'trailer'
        ]