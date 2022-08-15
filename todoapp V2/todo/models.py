from distutils.command.upload import upload
from email.mime import image
from pydoc import describe
from django.db import models

# Create your models here.
class User(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.EmailField(max_length=100)
    subject = models.IntegerField()
    image = models.ImageField(null = True,upload_to = 'media/')
    
class tasks(models.Model):
    user_task = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    describtion = models.CharField(max_length=100)
    created_date =  models.DateTimeField(auto_created=True)
    finished_date = models.DateTimeField()
    task_note = models.TextField()
