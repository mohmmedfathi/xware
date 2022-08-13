from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import User
from .forms import create_user as create_user_form


# Create your views here.
def create_todo(request):
    # return HttpResponse('created')
    return render(request,'todo/create_todo.html')

def update_todo(request):
    
    return HttpResponse('updated')
  
def delete_todo(request):

    return HttpResponse('deleted')
    
def retrieve_todo(request: HttpRequest):
    
    return HttpResponse('retrieved')

def check_todo(request):
    return HttpResponse('check')

def create_user(request):
    print(request)
    if request.method=='GET':
        return render(request,'todo/create_user.html')
    else:
        form=create_user_form(request.POST)
        if form.is_valid():
            user = User(
            name=form.cleaned_data['user_name'],
            email=form.cleaned_data['user_email'],
            age=form.cleaned_data['user_age']
            )
            user.save()
            return HttpResponse('created')
        else:
            print(form.errors)
            return HttpResponse('not created')

def update_user(request):
    
    return HttpResponse('updated')
  
def delete_user(request):

    return HttpResponse('deleted')
    
def retrieve_user(request: HttpRequest):
    
    return HttpResponse('retrieved')