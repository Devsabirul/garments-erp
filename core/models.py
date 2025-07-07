from django.db import models
from django.contrib.auth.models import User



    
class Employees(models.Model):
    name = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    position = models.CharField(max_length=250)
    hourlyrate = models.FloatField()


    def __str__(self):
        return self.name
    
class Atandents(models.Model):
    name = models.CharField(max_length=250)
    date = models.CharField(max_length=250)
    entry = models.CharField(max_length=250,null=True,blank=True)
    out = models.CharField(max_length=250,blank=True, null=True)
    total_hour = models.IntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    employee = models.ForeignKey(Employees,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.name
    
class Companies(models.Model):
    name = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    phone_num= models.CharField(max_length=300)

    def __str__(self):
        return self.name
    
class Products(models.Model):
    date = models.CharField(max_length=250)
    art = models.CharField(max_length=250)
    piz = models.IntegerField()
    price = models.FloatField()
    delivery_date = models.CharField(max_length=250,null=True,blank=True)
    delivery_completed_date = models.CharField(max_length=250,null=True,blank=True)
    company_name =  models.ForeignKey(Companies,on_delete=models.CASCADE)
    status = models.CharField(max_length=250,null=True,blank=True)

    def __str__(self):
        return self.art
    
