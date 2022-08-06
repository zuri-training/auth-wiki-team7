from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    conditions = forms.BooleanField(required=True)

    
    class Meta:
        model=User
        fields= ('username', 'email','password1','password2', 'conditions')
        
    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        user.email =self.cleaned_data['email']
        if commit:
            user.save()
        return user


   