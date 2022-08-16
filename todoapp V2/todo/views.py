from asyncio import FastChildWatcher
import email
from email.policy import HTTP
from http.client import HTTPResponse
import imp
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from .forms import Create_Student as Create_User_Form
from .task_form import Create_task
from .models import User
from .models import tasks
from django.views.decorators.http import require_http_methods,require_GET,require_POST
# Create your views here.

def create_user(request):
 if request.session.has_key('username'):
    if request.method =='GET':
        return render(request,'todo/create_user.html')
    else :
        form = Create_User_Form(request.POST,request.FILES)
        if form.is_valid():
            user = User(
                firstname = form.cleaned_data['firstname'],
                lastname = form.cleaned_data['lastname'],
                subject = form.cleaned_data['subject'],
                image = form.cleaned_data['image']
            )
            user.save()
            print(user.image.url)
            return render(request,'todo/create_user.html',{
                'result' : 'Valid',
                'Validated_firstname' : user.firstname,
                'Validated_lastname' : user.lastname,
                'Validated_subject' : user.subject,
                'user' : user
            })
        else:
            print(form.errors)
            return render(request,'todo/create_user.html', {
                'result' : 'Not Valid',
            })
 else:
     return HttpResponse("متستعبطش يايـــوزر واعمل تسجيل دخول")
            
def create_task(request):
     if request.method =='GET':
         return render (request,'todo/create_task.html')
     else:
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
    
    first_time = True
    if 'Horry'  in request.COOKIES:
        first_time = False
    users = User.objects.all()
    user_list = []
    for user in users:
        user_list.append({
            'u_name' : user.firstname,
            'u_lastname' : user.lastname,
            'u_subject' : user.subject
        })
    
    response = render (request,'todo/list_users.html',{
        'users' : user_list,
        'first_time': first_time
    })
    response.set_cookie('Horry' , 'Hallo')
    return response

        


def update_user(request):
    
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
    user = User.objects.filter(id=request.GET.get('id')).first()
    # print(user)
    if user ==None:
        return HttpResponse("user not found")
    else: 
     return render(request,'todo/retUser.html',{
        'is_found' : True,
        'user' : user
     })

def login(request):
    if request.method =='POST':
        
        request.session['username'] = request.POST['username']
        request.session['password'] = request.POST['password']
        return render(request,'login.html' ,{
            'logged' : True
        })
    else:
        return render(request,'login.html')
            
  
       

def logout(request):
    try:
      del request.session['username']
      del request.session['password']
    except:
      pass
    return HttpResponse("<strong>You are logged out.</strong>")
    