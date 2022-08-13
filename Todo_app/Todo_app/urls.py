"""Todo_app URL Configuration

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
from django.contrib import admin
from django.urls import path
from todo.views import *

urlpatterns = [
        path('admin/', admin.site.urls),
        path('todo/',create_todo),
        path('todo/update/',update_todo),
        path('todo/check/',check_todo),
        path('todo/delete/',delete_todo),
        path('todo/retrieve/',retrieve_todo),
        path('user/', create_user),
        path('user/update/',update_user),
        path('user/delete/',delete_user),
        path('user/retrieve/',retrieve_user),
        

]
