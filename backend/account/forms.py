from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name=forms.CharField(max_length=30, required=False)
    last_name=forms.CharField(max_length=30, required=False)
    
    class Meta:
        model=User
        fields= ('username', 'first_name','last_name', 'email','password1','password2',)
        
    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        user.email =self.cleaned_data['email']
        if commit:
            user.save()
        return user



   