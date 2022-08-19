from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views import View
from django.contrib.auth import authenticate,login,logout
from .forms import User_Register_Model_Form,User_Reset_Model_Form
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
# Create your views here.
class Logout(View):
    def get (self,request):
        logout(request)
        return render(request,'login.html')

class Login(View):
    def get (self,request):
        return render(request,'login.html')
    
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




class RegisterUserView(View):
    
    def get(self,request):
        form = User_Register_Model_Form()
        return render(request,'create_user.html',{
            'form':form
        })
        

    def post (self,request):
        form = User_Register_Model_Form(request.POST)
        
        if form.is_valid():
            user = form.save()

            return render(request,'create_user.html',{
                'result' : 'Valid',
                'user' : user,
                'form' : form
            })
            
        else:
            return render(request,'create_user.html', {
                'result' : 'Not Valid',
                'errors' : form.errors,
                'form' : form
            })



class resetpasswordView(View):
    def get(self,request):
        form = User_Reset_Model_Form()
        return render(request,'reset_password.html',{
            'form' : form
        })
        
    def post(self,request):
        
        associated_user = User.objects.filter(username = request.POST.get('username')).first()
        if associated_user is not None :
            associated_user.set_password(request.POST.get('password'))
            associated_user.save()
            
           # return redirect('change_password')
            print(User.objects.values())
            return render(request,'reset_password_done.html',{
            'process' : True
            })
        print(User.objects.values())
        return render(request,'reset_password_done.html',{
            'process' : False
            })
     
        
            