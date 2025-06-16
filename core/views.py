from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import *

def dashboard(request):
    if request.user.is_authenticated:
        return render(request,'core/index.html')
    else:
        return redirect('signin')


def addAttandents(request):
    if request.user.is_authenticated:
        employeeList = Employees.objects.all()
        print(employeeList)
        return render(request,'core/add_attandents.html',locals())
    else:
        return redirect('signin')