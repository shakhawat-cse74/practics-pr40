import email
from django.shortcuts import render
from .forms import StudentRegistration
from .models import User

# Create your views here.
def showdata(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            #save Data
            #reg = User(name=nm, email=em, password=pw)
            #reg.save()

            #update Data
            #reg = User(id=1,name=nm, email=em, password=pw)
            #reg.save()
            #delete data
            reg = User(id=1,name=nm, email=em, password=pw)
            reg.delete()
            

    else:
        fm = StudentRegistration()
    return render (request, 'enroll/registration.html', {'form':fm})
