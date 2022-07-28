from django import forms
from . models import *
from django.forms import ModelForm, widgets




class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [ 'content']