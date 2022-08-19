"""HospitalManagementSystem URL Configuration

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
from django.urls import path, include
from user.views import (Login,Logout,RegisterUserView,resetpasswordView)
from patient.views import (patientShow,patientUpdateClass,patientDelete,patientCreateClass,
                           examinationShow,examinationUpdateClass,examinationDelete,examinationCreateClass)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('auth/login/' ,Login.as_view() ),
    path('auth/logout/' ,Logout.as_view() ),
    path('auth/register/' ,RegisterUserView.as_view()),
    path('auth/reset-password/' ,resetpasswordView.as_view()),
    
    path('patients/create/' ,patientCreateClass.as_view()),
    path('patients/<int:patient_id>/' ,patientShow),
    path('patients/<int:patient_id>/update/' ,patientUpdateClass.as_view()),
    path('patients/<int:patient_id>/delete/' ,patientDelete),
    
    path('patients/<int:patient_id>/examinations/create/' ,examinationCreateClass.as_view()),
    path('patients/<int:patient_id>/examinations/<int:examination_id>/' ,examinationShow),
    path('patients/<int:patient_id>/examinations/<int:examination_id>/update/' ,examinationUpdateClass.as_view()),
    path('patients/<int:patient_id>/examinations/<int:examination_id>/delete/' ,examinationDelete),
    
]
 