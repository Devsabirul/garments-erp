from datetime import datetime
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import *

def dashboard(request):
    if request.user.is_authenticated:
        return render(request,'core/index.html')
    else:
        return redirect('signin')


def addAttandents(request):
    if not request.user.is_authenticated:
        return redirect('signin')

    employeeList = Employees.objects.all()
    error = None
    success = None

    if request.method == "POST":
        employee_id = request.POST.get('employee_id')
        date = request.POST.get('date')
        entry = request.POST.get('entry')
        out = request.POST.get('out')
        total_hour = request.POST.get('total_hour')

        try:
            employee = Employees.objects.get(id=employee_id)
        except Employees.DoesNotExist:
            return render(request, 'core/add_attandents.html', {
                'employeeList': employeeList,
                'error': 'Invalid employee selected.'
            })

        # Optional: Use employee.name if you still need name in a separate field
        name = employee.name

        if Atandents.objects.filter(employee=employee, date=date).exists():
            error = "Attendance for this employee and date already exists."
        else:
            attandent = Atandents(
                name=name,
                employee=employee,
                date=date,
                entry=entry,
                out=out,
                total_hour=total_hour,
                author=request.user,
            )
            attandent.save()
            success = "Attendance saved successfully."

    return render(request, 'core/add_attandents.html', {
        'employeeList': employeeList,
        'error': error,
        'success': success
    })

    
def attandentsReport(request):
     if request.user.is_authenticated:
        attandentsReport = Atandents.objects.order_by("-id")
        return render(request,'core/attandents_report.html',locals())
     else:
        return redirect('signin')

def viewattandentsreport(request):
    if not request.user.is_authenticated:
        return redirect('signin')

    attandent_id = request.GET.get('id')
    date_str = request.GET.get('date')

    if not attandent_id or not date_str:
        return render(request, 'core/error.html', {'message': 'Missing id or date parameter'})

    try:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        return render(request, 'core/error.html', {'message': 'Invalid date format'})

    year = date_obj.year

    # Filter attendance records by employee ID and year (using startswith on CharField)
    records = Atandents.objects.filter(
        employee__id=attandent_id,
        date__startswith=f"{year}-"
    ).order_by('date')

    # Sum total hours
    total_hours = sum(rec.total_hour for rec in records if rec.total_hour)

    # Optional: sanitize empty fields
    for rec in records:
        rec.entry = rec.entry or ''
        rec.out = rec.out or ''
        rec.total_hour = rec.total_hour or 0

    context = {
        'attandentsReport': records,
        'total_hours': total_hours
    }

    return render(request, 'core/view_report.html', context)

    
def addProducts(request):
    if not request.user.is_authenticated:
        return redirect('signin')

    companyList = Companies.objects.all()
    error = None
    success = None

    if request.method == "POST":
        date = request.POST.get('date')
        art = request.POST.get('art')
        piz = request.POST.get('piz')
        price = request.POST.get('price')
        delivery_date = request.POST.get('delivery_date')
        company_name_str = request.POST.get('company_name')

        try:
            company_instance = Companies.objects.get(name=company_name_str)
        except Companies.DoesNotExist:
            error = f"Company '{company_name_str}' does not exist."
            return render(request, 'core/add_products.html', {
                'companyList': companyList,
                'error': error,
                'success': success
            })

        product = Products.objects.create(
            date=date,
            art=art,
            piz=piz,
            price=price,
            delivery_date=delivery_date,
            company_name=company_instance
        )
        product.save()
        success = "Product added successfully."

    return render(request, 'core/add_products.html', {
        'companyList': companyList,
        'error': error,
        'success': success
    })


def productsReport(request):
    if not request.user.is_authenticated:
        return redirect('signin')
        
        
    productsList = Products.objects.all()

    return render(request, 'core/product_report.html',locals())