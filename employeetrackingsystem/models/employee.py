from django.db import models
import datetime
from django.shortcuts import render, redirect
from django.db.models import Count

GENDER=[('male', 'MALE'), ('female', 'FEMALE'),]
ORG=[('google', 'GOOGLE'), ('microsoft', 'MICROSOFT')]
# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=100)
    gender=models.CharField(max_length=10, choices=GENDER, default='male')
    jobtitle=models.CharField(max_length=100)
    organization=models.CharField(max_length=10, choices=ORG)
    dob=models.DateField(default=datetime.datetime.today)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def register(self):
        self.save()

    @staticmethod
    def get_employee_by_emailM(email='admin@microsoft.com'):
        try:
            return Employee.objects.get(email=email)
        except:
            return False
    
    @staticmethod
    def get_employee_by_emailG(email='admin@google.com'):
        try:
            return Employee.objects.get(email=email)
        except:
            return False

    def emailExists(self):
        if Employee.objects.filter(email=self.email).exists():
            return True
        return False
        
    def isExists(self):
        if Employee.objects.filter(email=self.email).filter(name__iexact=self.name).filter(dob=self.dob).filter(jobtitle__iexact=self.jobtitle).filter(organization=self.organization).filter(gender=self.gender):
            return True

        return False     