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
        if request.method == "POST":
            name = request.POST.get('name')
            date = request.POST.get('date')
            entry = request.POST.get('entry')
            out = request.POST.get('out')
            total_hour = request.POST.get('total_hour')
            attandent = Atandents(name=name,date=date,entry=entry,out=out,total_hour=total_hour,author=request.user)
            attandent.save()
            print(name)
        else:
            print("problem")
        return render(request,'core/add_attandents.html',locals())
    else:
        return redirect('signin')
    
def attandentsReport(request):
     if request.user.is_authenticated:
        attandentsReport = Atandents.objects.order_by("-id")
        return render(request,'core/attandents_report.html',locals())
     else:
        return redirect('signin')

def viewattandentsreport(request):
     if request.user.is_authenticated:
        attandentsReport = Atandents.objects.order_by("-id")
        return render(request,'core/view_report.html',locals())
     else:
        return redirect('signin')

    
