from django.db import models
from django.contrib.auth.models import User


class Atandents(models.Model):
    name = models.CharField(max_length=250)
    date = models.CharField(max_length=250)
    entry = models.CharField(max_length=250,null=True,blank=True)
    out = models.CharField(max_length=250,blank=True, null=True)
    total_hour = models.IntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.category
    
class Employees(models.Model):
    name = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    position = models.CharField(max_length=250)
    hourlyrate = models.FloatField()


    def __str__(self):
        return self.name
    
