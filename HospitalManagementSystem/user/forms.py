from dataclasses import fields
from email.mime import image
from pyexpat import model
from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class User_Register_Model_Form(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['username','email','password']
    
    def clean(self):
        cleaned_data = super().clean()
        cleaned_data['password'] = make_password(
            cleaned_data['password']
        )
        return cleaned_data
    

class User_Reset_Model_Form(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['username','password']
    
    
        