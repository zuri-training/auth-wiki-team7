from logging import PlaceHolder
from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    
    class Meta:
        model=User
        fields= ('username', 'email','password1','password2')

        
    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        user.email =self.cleaned_data['email']
        if commit:
            user.save()
        return user

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({'class': 'input sp-input', 'placeholder': 'Username', 'id': 'username'})
        self.fields['email'].widget.attrs.update({'class': 'input sp-input', 'placeholder': 'Email', 'id': 'email'})
        self.fields['password1'].widget.attrs.update({'class': 'input sp-input', 'placeholder': 'Password', 'id': 'password'})
        self.fields['password2'].widget.attrs.update({'class': 'input sp-input', 'placeholder': 'Repeat Password', 'id': 'password2'})

