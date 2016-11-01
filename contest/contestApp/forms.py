from django import forms
from .models import Picture, Vote
from django.contrib.admin import widgets

class PictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ['created', 'url', 'description']

class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        fields = ['foto', 'email']
