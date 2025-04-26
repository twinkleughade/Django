from django.contrib import admin

# Register your models here.

# from.models import *
from.models import Student, Employee, Client, BaseField

admin.site.register(BaseField)
admin.site.register(Student)
admin.site.register(Employee)
admin.site.register(Client)



