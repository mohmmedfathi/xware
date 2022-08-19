from asyncio import FastChildWatcher
from django.db import models

# Create your models here.
Gender = [
	('male' , 'male'),
 	('female', 'female'),
  	('other' , 'other')
]
class Patient(models.Model):
    #patient_id = models.IntegerField(models.AutoField(_("")))
    id = models.IntegerField(primary_key=True, null = False)
    full_name = models.CharField(max_length=100,null = False)
    age = models.IntegerField(null = False)
    national_id = models.IntegerField(null = False)
    email = models.EmailField(max_length=100)
    phone1 = models.IntegerField(null = False) 
    phone2 = models.IntegerField()
    gender = models.CharField(null = False,choices = Gender,max_length=20)
    
    
class Address(models.Model):
    patient_address = models.ForeignKey(Patient,on_delete=models.CASCADE)
    governorate = models.CharField(max_length=100,null = False)
    city = models.CharField(max_length=100,null = False)
    line_1 = models.CharField(max_length=100,null = False)
    line_2 = models.CharField(max_length=100,null = False)
    
class Examination(models.Model):
    patient_examination = models.ForeignKey(Patient,on_delete=models.CASCADE)
    diagnosis = models.CharField(max_length=100,null = False)
    treatment = models.CharField(max_length=100,null = False)
    examination_date = models.DateTimeField(null = False)
