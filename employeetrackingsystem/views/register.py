import requests
import json
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect

from django.views import View

from employeetrackingsystem.models.employee import Employee

# Create your views here.
class Register(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        postData=request.POST
        name=postData.get('name')
        gender=postData.get('gender')
        jobtitle=postData.get('jobtitle')
        organization=postData.get('organization')
        dob=postData.get('dob')
        email=postData.get('email')
        password=postData.get('password')

        #validation
        value={
            'name':name,
            'gender':gender,
            'jobtitle':jobtitle,
            'organization':organization,
            'dob':dob,
            'email':email,
            'password':password
        }
        error_message=None
        
        #creation of objects
        employee=Employee(name=name, gender=gender, jobtitle=jobtitle, organization=organization, dob=dob,email=email, password=
        password)
        error_message=self.validateEmployee(employee)

        if not error_message:
            print(name, gender, jobtitle, organization, dob, email, password)
            employee.password=make_password(employee.password)
            employee.register()
            return redirect('/')

        else:
            data={
                'error':error_message,
                'values':value
            }
            return render(request, 'register.html', data)

    def validateEmployee(self, employee):
        error_message=None
        if(not employee.name):
            error_message="name required"
        elif(not employee.gender):
            error_message="gender required"
        elif(not employee.jobtitle):
            error_message="jobtitle required"
        elif(not employee.organization):
            error_message="organization required"
        elif(not employee.email):
            error_message="email required"
        elif(not employee.dob):
            error_message="dob required"
        elif(employee.dob>"2002-01-01"):
            error_message="invalid age"
        elif(not employee.password):
            error_message="password required"


        elif employee.isExists():
            error_message="same employee, employee already registered"

        return error_message

