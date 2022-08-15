from django import forms

class Create_task(forms.Form):
   
    name = forms.CharField(max_length=50)
    describtion = forms.CharField(max_length=100)
    created_date =  forms.DateTimeField()
    finished_date = forms.DateTimeField()
    task_note = forms.CharField() 
    