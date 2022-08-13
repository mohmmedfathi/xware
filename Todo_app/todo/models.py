import email
from operator import mod
from pyexpat import model

from django.db import models

# Create your models here.
class User (models.Model):
    name= models.CharField(max_length=90)
    email=models.EmailField(max_length=90)
    age=models.IntegerField()

class Tasks (models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name= models.CharField(max_length=90)
    description= models.CharField(max_length=200)
    created_date= models.DateTimeField(auto_created=True)
    finished_date= models.CharField(max_length=40)
    task_notes= models.CharField(max_length=90)

