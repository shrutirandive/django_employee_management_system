from django.shortcuts import render, redirect

from django.views import View

from employeetrackingsystem.models.employee import Employee
def main(request):
    return render(request, 'main.html')