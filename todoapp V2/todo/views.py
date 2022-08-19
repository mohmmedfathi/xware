from asyncio import FastChildWatcher
import email
from email.policy import HTTP
from http.client import HTTPResponse
import imp
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from .forms import Create_Student as Create_User_Form, Create_User_Model_Form
from .task_form import Create_task
from .models import User
from .models import tasks
from django.views.decorators.http import require_http_methods,require_GET,require_POST
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.

class CreateUserView(View):
    def get(self,request):
        form = Create_User_Model_Form()
        return render(request,'todo/create_user.html',{
            'form':form
        })
        
       # if request.session.has_key('username'):

    def post (self,request):
        form = Create_User_Model_Form(request.POST)
        if form.is_valid():
            user = form.save()
            """
            user = User.objects.create_user(
                username = form.cleaned_data['username'],
                email = form.cleaned_data['email'],
                
                password = form.cleaned_data['password']
            )
            """
            
            return render(request,'todo/create_user.html',{
                'result' : 'Valid',
                'user' : user,
                'form' : form
            })
        else:
            return render(request,'todo/create_user.html', {
                'result' : 'Not Valid',
                'errors' : form.errors,
                'form' : form
            })


class Create_task_view(View):
    
    def get(self,request):
        return render (request,'todo/create_task.html')
    
    def post(self,request):
        form = Create_task(request.POST)
        if form.is_valid():
             
             task = tasks(
                 name = form.cleaned_data['name'],
                 describtion = form.cleaned_data['describtion'],
                 created_date =  form.cleaned_data['created_date'],
                 finished_date = form.cleaned_data['finished_date'],
                 task_note =form.cleaned_data['task_note']
             )
             task.save()
             return render(request,'todo/create_task.html',{
                'result' : 'Valid',
                'Validated_name' : task.name,
                'Validated_describtion' : task.describtion,
                'Validated_created_date' : task.created_date,
                'Validated_finished_date' : task.finished_date,
                'Validated_task_note' : task.task_note,
            })
        else:
               return render(request,'todo/create_task.html', {
                'result' : 'Not Valid',
            })
             
         
        
def update_task(request):
    if not request.user.is_authenticated:
        return HttpResponse('You are forbidden from updating Users')
    last_id_not_found = True
    new_id_not_found = True
    x = tasks.objects.filter(id = request.GET.get('id')).first()
    before_id = 0
    newid = 0
    if x is not None :
        before_id = x.id
        if 'newid' in request.GET:
            newid = request.GET.get('newid')
            x.id = newid
            last_id_not_found = False
            new_id_not_found = False
            
    return render(request,'update_task.html',{
            'last_id_not_found' : last_id_not_found,
            'new_id_not_found' : new_id_not_found,
            'before_id' : before_id,
            'newid' : newid
        })
        

    
def delete_task(request):
    
    x = tasks.objects.filter(id = request.GET.get('id')).first()
    if x is not None:
        x.delete()
        return render(request,'delete_task.html',{
            'result' : 'deleted'
        })
    else:
        return render(request,'delete_task.html',{
            'result' : 'not found'
        })
        
def retrieve_task(request):
    
    user = tasks.objects.filter(id=request.GET.get('id')).first()
    # print(user)
    if user ==None:
        return HttpResponse("user not found")
    else: 
     return render(request,'todo/retUser.html',{
        'is_found' : True,
        'user' : user
     })

def list_users(request):
    if not request.user.is_authenticated:
        return HttpResponse('You are forbidden from listing Users')
    first_time = True
    if 'Horry'  in request.COOKIES:
        first_time = False
    users = User.objects.all()
    user_list = []
    for user in users:
        user_list.append({
            'u_name' : user.username,
            'u_lastname' : user.email,
            'u_subject' : user.password
        })
    
    response = render (request,'todo/list_users.html',{
        'users' : user_list,
        'first_time': first_time
    })
    response.set_cookie('Horry' , 'Hallo')
    return response

        


def update_user(request):
    if not request.user.is_authenticated:
        return HttpResponse('You are forbidden from updating Users')
    last_id_not_found = True
    new_id_not_found = True
    x = User.objects.filter(id = request.GET.get('id')).first()
    before_id = 0
    newid = 0
    if x is not None :
        before_id = x.id
        if 'newid' in request.GET:
            newid = request.GET.get('newid')
            x.id = newid
            last_id_not_found = False
            new_id_not_found = False
    x.save()   
    return render(request,'update_user.html',{
            'last_id_not_found' : last_id_not_found,
            'new_id_not_found' : new_id_not_found,
            'before_id' : before_id,
            'newid' : newid
        })
    
    
            
        
def delete_user(request):
    
    if not request.user.is_authenticated:
        return HttpResponse('You are forbidden from deleting Users')
    x = User.objects.filter(id = request.GET.get('id')).first()
    if x is not None:
        x.delete()
        return render(request,'index.html',{
            'result' : 'deleted'
        })
    else:
        return render(request,'index.html',{
            'result' : 'not found'
        })


def retrieve_user(request):
    if not request.user.is_authenticated:
        return HttpResponse('You are forbidden from retrieving Users')
    user = User.objects.filter(id=request.GET.get('id')).first()
    # print(user)
    if user ==None:
        return HttpResponse("user not found")
    else: 
     return render(request,'todo/retUser.html',{
        'is_found' : True,
        'user' : user
     })

       
class Logout(View):
    def get (self,request):
        logout(request)
        return render(request,'login.html')

class Login(View):
    def get (self,request):
        all = User.objects.values()
        print (all)
        return render(request,'login.html',{'all_v' : all})
    
    def post(self,request):
        
        user = authenticate(
            username = request.POST['username'],
            password = request.POST['password']
        )
        if user is not None:
            login(request,user)
            return render(request,'login.html',{
                'logged' : True
            })
        return render(request,'login.html',{
                'error' : 'Username or password is wrong'
            })
    
    