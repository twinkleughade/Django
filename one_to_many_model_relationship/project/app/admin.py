from django.contrib import admin
from .models import Department,Student

# Register your models here.

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display=['dep_name','dep_des','dep_hod']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['stu_name','stu_email','stu_contact','stu_dep']

# from.models import *
# admin.site.register(Department)
# admin.site.register(Student)