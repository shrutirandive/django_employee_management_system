from django.shortcuts import render, redirect

from django.views import View

from employeetrackingsystem.models.employee import Employee
def navbar(request):
    return render(request, 'navbar.html')