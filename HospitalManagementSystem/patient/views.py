import email
from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.views import View
from .forms import PatientForm,AddressForm,PatientFormUpdate,examinationForm
from .models import Patient
from .models import Address,Examination
from django.db.transaction import atomic
# Create your views here.


def patientShow(request,patient_id): 
    patient = Patient.objects.filter(id = patient_id)
    patient_address = Address.objects.filter(patient_address_id = patient_id)
    print(patient.values())
    print(patient_address.values())
    
    return render(request,'show_patient.html',{
            'result' : 'done',
            'patient' : patient,
            'patient_address' : patient_address
        })

class patientUpdateClass(View):
    def get(self,request,patient_id):
        patient_list = []
        
        x = Patient.objects.filter(id = patient_id)
        for i in x.values():
            temp = []
            for j in i :
                temp.append({j : i[j]})
            patient_list.append(temp)
            
            
        address_list = []
        x = Address.objects.filter(patient_address_id = patient_id)
        for i in x.values():
            temp = []
            for j in i :
                temp.append({j : i[j]})
            address_list.append(temp)

        return render(request,'update_patient.html',{
            'p_id' : patient_id,
            'patient_list' : patient_list,
            'address_list' : address_list
        })
        
    def post(self,request,patient_id):
        x = Patient.objects.filter(id = patient_id)
        form = PatientFormUpdate(request.POST)
        print('before')
        print(x.values())
        if form.is_valid():
                form2 = AddressForm(request.POST)
                
                if form2.is_valid():
                    user = Patient.objects.filter(id = patient_id).first()
                    user.full_name = form.cleaned_data['full_name']
                    user.age = form.cleaned_data['age']
                    user.national_id = form.cleaned_data['national_id']
                    user.email = form.cleaned_data['email']
                    user.phone1 = form.cleaned_data['phone1']
                    user.phone2 = form.cleaned_data['phone2']
                    user.save()
                    
                    user2 = Address.objects.filter(patient_address_id = patient_id).first()
                    user2.governorate = form2.cleaned_data['governorate']
                    user2.city = form2.cleaned_data['city']
                    user2.line_1 = form2.cleaned_data['line_1']
                    user2.line_2 = form2.cleaned_data['line_2']
                    
                    user2.save()
                    
                    print('after')
                    print(x.values())
                    return render(request,'update_patient.html',{
                'result' : 'Valid',
                'user' : user,
                'form' : form
             })
                else :
                  print(form2.errors)
            
        print(x.values())
        print(form.errors)
        return render(request,'update_patient.html', {
                'result' : 'Not Valid',
                'errors' : form.errors,
                'form' : form
            })
    
def patientDelete(request,patient_id):
    associated_Patient = Patient.objects.filter(id = patient_id).first()
    if associated_Patient is not None :
         associated_Patient.delete()
       
         return render(request,'delete_patient.html',{
            'result' : 'deleted'
        })
    else:
        return render(request,'delete_patient.html',{
            'result' : 'not found'
        })
        
class patientCreateClass(View):
    
    def get(self,request):
        form = PatientForm()
        return render(request,'create_patient.html',{
            'form':form
        })
        
    def post (self,request):
        print(Patient.objects.all())
        print(request.POST)
        # with atomic:
        form = PatientForm(request.POST)
            
        if form.is_valid():
                form2 = AddressForm(request.POST)
                
                if form2.is_valid():
                    user = form.save()
                    user2 = Address(governorate=form2.cleaned_data['governorate'],
                                city=form2.cleaned_data['city'],
                                line_1=form2.cleaned_data['line_1'],
                                line_2 = form2.cleaned_data['line_2'],
                                patient_address= Patient.objects.filter(id = request.POST.get('id')).first()
                                    )
                    user2.save()
                    
          
          
                    return render(request,'create_patient.html',{
                'result' : 'Valid',
                'user' : user,
                'form' : form
             })
                else :
                  print(form2.errors)
            
        
        print(form.errors)
        return render(request,'create_patient.html', {
                'result' : 'Not Valid',
                'errors' : form.errors,
                'form' : form
            })


def examinationShow(request,patient_id,examination_id): 
    patient = Patient.objects.filter(id = patient_id)
    patient_examination = Examination.objects.filter(patient_examination_id = patient_id)
    print(patient.values())
    print(patient_examination.values())
    
    return render(request,'show_examination.html',{
            'result' : 'done',
            'patient' : patient,
            'patient_examination' : patient_examination
        })

class examinationUpdateClass(View):
    def get(self,request,patient_id,examination_id):
        patient_list = []
        
        x = Patient.objects.filter(id = patient_id)
        for i in x.values():
            temp = []
            for j in i :
                temp.append({j : i[j]})
            patient_list.append(temp)
            
            
        examination_list = []
        x = Examination.objects.filter(patient_examination_id = examination_id)
        for i in x.values():
            temp = []
            for j in i :
                temp.append({j : i[j]})
            examination_list.append(temp)

        return render(request,'update_examination.html',{
            'p_id' : patient_id,
            'e_id' : examination_id,
            'patient_list' : patient_list,
            'address_list' : examination_list
        })
        
    def post(self,request,patient_id,examination_id):
        x = Patient.objects.filter(id = patient_id)
        form = examinationForm(request.POST)
        print('before')
        print(x.values())
        if form.is_valid():
                
                    user = Examination.objects.filter(id = patient_id).first()
                    print('--------------------')
                    print (Examination.objects.filter(id = patient_id).values())
                    user.diagnosis = form.cleaned_data['diagnosis']
                    user.treatment = form.cleaned_data['treatment']
                    user.examination_date = form.cleaned_data['examination_date']
                    user.save()
                    
                    print('after')
                    print(x.values())
                    print('--------------------')
                    print (Examination.objects.filter(id = patient_id).values())
                    return render(request,'update_examination.html',{
                'result' : 'Valid',
                'user' : user,
                'form' : form
             })
            
        print(x.values())
        print(form.errors)
        return render(request,'update_examination.html', {
                'result' : 'Not Valid',
                'errors' : form.errors,
                'form' : form
            })
    
def examinationDelete(request,patient_id,examination_id):
    associated_Patient = Patient.objects.filter(id = patient_id).first()
    associated_examination = Examination.objects.filter(id = examination_id).first()
    if associated_examination is not None :
         associated_examination.delete()
       
         return render(request,'delete_examination.html',{
            'result' : 'deleted'
        })
    else:
        return render(request,'delete_examination.html',{
            'result' : 'not found'
        })
    
class examinationCreateClass(View):
    
    def get(self,request,patient_id):
        form = examinationForm()
        return render(request,'create_examination.html',{
            'form':form
        })
        
    def post (self,request,patient_id):
        print(Patient.objects.all())
        print(request.POST)
        form = examinationForm(request.POST)
            
        if form.is_valid():
                user = Examination(diagnosis=form.cleaned_data['diagnosis'],
                                treatment=form.cleaned_data['treatment'],
                                examination_date=form.cleaned_data['examination_date'],
                               patient_examination = Patient.objects.filter(id = patient_id).first()
                                    )
                user.save()
          
                return render(request,'create_examination.html',{
                'result' : 'Valid',
                'user' : user,
                'form' : form
             })
        else :
            print(form.errors)
            return render(request,'create_examination.html', {
                'result' : 'Not Valid',
                'errors' : form.errors,
                'form' : form
            })
            

class HomePage(View):
    def get(self,request):
        return render(request,'home_page.html')
    
    def post(self,request):
        lookup = request.POST.get('lookup')
        val = request.POST.get('val')
        patient_list = []
        lookup = str(lookup)
        val = str(val)
        print(lookup)
        print(val)
        print('--------------------')
        print(Patient.objects.filter(full_name = val).first())
        if lookup == 'full_name':
            try:
                x = Patient.objects.filter( full_name= val)
                dummy = x[0]
            except IndexError:
                return render(request,'home_page.html',{
              'faild' : 'value not found!'
          })
                
        elif lookup=='national_id':
            try :
              x = Patient.objects.filter( national_id= val)
              dummy = x[0]
            except IndexError:
                return render(request,'home_page.html',{
              'faild' : 'value not found!'
          })
                
        elif lookup =='email':
            try:
                x = Patient.objects.filter( email= val)
                dummy = x[0]
            except IndexError:
                return render(request,'home_page.html',{
              'faild' : 'value not found!'
          })
                
        elif lookup == 'phone1':
            try :
                x = Patient.objects.filter( phone1= val)
                dummy = x[0]
            except :
                return render(request,'home_page.html',{
              'faild' : 'value not found!'
          })
                
        else:
             return render(request,'home_page.html',{
              'faild' : 'search field wrong !'
          })
        
            
        for i in x.values():
            temp = []
            for j in i :
                temp.append({j : i[j]})
            patient_list.append(temp)
            
        address_list = []
        y = Address.objects.filter(patient_address_id = x[0].id)
        for i in y.values():
            temp = []
            for j in i :
                temp.append({j : i[j]})
            address_list.append(temp)

        examination_list = []
        z = Examination.objects.filter(patient_examination_id = x[0].id)
        for i in z.values():
            temp = []
            for j in i :
                temp.append({j : i[j]})
            examination_list.append(temp)
            
        return render(request,'home_page.html',{
            'p_id' : x[0].id,
            'patient_list' : patient_list,
            'address_list' : address_list,
            'examination_list' : examination_list
        })