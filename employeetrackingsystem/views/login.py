import requests
import json
from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect, HttpResponseRedirect

from django.views import View

from employeetrackingsystem.models.employee import Employee

#create views
class Login(View):
    return_url=None
    def get(self, request):
        Login.return_url=request.GET.get('return_url')
        return render(request, 'login.html')

    def post(self, request):
        email=request.POST.get('email')
        password=request.POST.get('password')
    #MICROSOFT
        if(email=='admin@microsoft.com'):
            employeeM=Employee.get_employee_by_emailM(email)
            error_message=None
            if employeeM:
                flag=check_password(password, employeeM.password)
                if flag:
                    request.session['employee']=employeeM.id

                    if Login.return_url:
                        return HttpResponseRedirect(Login.return_url)
                    else:
                        Login.return_url=None
                        return redirect('showm')
                else:
                    error_message="email or password invalid"
                    
            else:
                error_message="email or password invalid"
    #GOOGLE
        elif(email=="admin@google.com"):
            employeeG=Employee.get_employee_by_emailG(email)
            error_message=None
            if employeeG:
                flag=check_password(password, employeeG.password)
                if flag:
                    request.session['employee']=employeeG.id

                    if Login.return_url:
                        return HttpResponseRedirect(Login.return_url)
                    else:
                        Login.return_url=None
                        return redirect('showg')
                else:
                    error_message="email or password invalid"
                    
            else:
                error_message="email or password invalid"
        
        else:
            error_message="invalid"
            return render(request, 'login.html', {'error':error_message})

        print(email, password)
        return render(request, 'login.html', {'error':error_message})

#LOGOUT
def logout(request):
    request.session.clear()
    return redirect('login')