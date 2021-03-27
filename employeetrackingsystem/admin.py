from django.contrib import admin
from .models.employee import Employee
# Register your models here.
class AdminEmployee(admin.ModelAdmin):
    list_display=['name', 'organization','gender', 'dob','jobtitle','email']

admin.site.register(Employee, AdminEmployee)