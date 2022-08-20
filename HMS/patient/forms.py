from dataclasses import fields
from email.mime import image
from pyexpat import model
from django import forms
from .models import Address, Patient
 
class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = "__all__" 
        
class PatientFormUpdate(forms.Form):
    full_name = forms.CharField(max_length=100 ,required=True)
    age = forms.DecimalField(max_digits=3,required=True)
    national_id = forms.DecimalField(max_digits=15, required=True)
    email = forms.EmailField(max_length=100)
    phone1 = forms.DecimalField(max_digits=15,required=True)
    phone2 = forms.DecimalField(max_digits=15,required=True)
    
class AddressForm(forms.Form):
        governorate=forms.CharField(max_length=100,required=True,min_length=1)
        city= forms.CharField(max_length=100,required=True,min_length=1)
        line_1=forms.CharField(max_length=100,required=True,min_length=1)
        line_2 = forms.CharField(max_length=100,required=True,min_length=1)

class examinationForm(forms.Form):
    diagnosis = forms.CharField(max_length=100,required= True)
    treatment = forms.CharField(max_length=100,required = False)
    examination_date= forms.DateTimeField(required=True)
