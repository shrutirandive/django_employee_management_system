from django.shortcuts import render, redirect
from django.db.models import Count
from django.views import View

from employeetrackingsystem.models.employee import Employee
from employeetrackingsystem.middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator

#View

def showg(request):
    employee=Employee.objects.filter(organization='google')
    totalcountG=Employee.objects.filter(organization='google').count()
    nameG=Employee.objects.values_list('organization', flat=True).get(pk=1)
    d={'employee':employee, 'totalcountG':totalcountG, 'nameG':nameG}
    return render(request, 'detailsg.html', d)

def showm(request):
    employee=Employee.objects.filter(organization='microsoft')
    totalcountM=Employee.objects.filter(organization='microsoft').count()
    nameM=Employee.objects.values_list('organization', flat=True).get(pk=2)
    d={'employee':employee, 'totalcountM':totalcountM, 'nameM':nameM}
    return render(request, 'detailsm.html', d)

