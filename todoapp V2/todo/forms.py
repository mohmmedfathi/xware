from email.mime import image
from pyexpat import model
from django import forms

class Create_Student(forms.Form):
    firstname = forms.CharField(max_length=100,min_length=1)
    lastname = forms.CharField(max_length=100,min_length=1)
    subject = forms.CharField(max_length=100,min_length=1) 
    image = forms.ImageField()


    