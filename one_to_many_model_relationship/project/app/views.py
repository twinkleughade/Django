from django.shortcuts import render
from .models import Student,Department


# Create your views here.
def student(request):
    all_data=Student.objects.all()
    print(all_data)
    print(all_data.values())
    print(all_data.values_list())

    data=Student.objects.get(stu_name='twinkle')
    print(data.stu_name)
    print(data.stu_email)
    print(data.stu_contact)
    print(data.stu_dep)
    print(data.stu_dep.dep_name)
    print(data.stu_dep.dep_des)
    print(data.stu_dep.dep_hod)

def department(request):
    all_data=Department.objects.all()
    print(all_data)
    print(all_data.values())
    print(all_data.values_list())

    data=Department.objects.get(dep_name='python')
    print(data.Students)
    all_student=data.Students.all()
    print(all_student)
    



