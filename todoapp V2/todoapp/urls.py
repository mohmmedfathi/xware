"""todoapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path
from todo import views
from django.conf.urls.static import static
from django.conf import settings
"""
def create_task(request):
    return HttpResponse("create task")
def update_task(request):
    return HttpResponse("update task")
def delete_task(request):
    return HttpResponse("delete task")
def retrieve_task(request):
    return HttpResponse("retrieve task")

def create_user(request):
    return HttpResponse("create user")
def update_user(request):
    return HttpResponse("update user")
def delete_user(request):
    return HttpResponse("delete user")
def retrieve_user(request):
    return HttpResponse("retrieve user")
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('todo/',views.Create_task_view.as_view()),
    path('todo/update',views.update_task ),
    path('todo/delete',views.delete_task),
    path('todo/retrieve',views.retrieve_task),
    
    path('user/list',views.list_users),
    path('user/create',views.CreateUserView.as_view()),
    path('user/update',views.update_user),
    path('user/delete',views.delete_user),
    path('user/retrieve',views.retrieve_user),
    path('user/login',views.Login.as_view()),
    path('user/logout',views.Logout.as_view()),
]

# to access media file
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

