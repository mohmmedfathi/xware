from django import forms

class create_user(forms.Form):
        user_name=forms.CharField(max_length=200,required=True,min_length=1)
        user_email=forms.EmailField(max_length=200,required=True,min_length=1)
        user_age=forms.IntegerField()