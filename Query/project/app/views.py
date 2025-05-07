from django.shortcuts import render
from .models import Student

# Create your views here.

def student(request):
    all_data=Student.objects.all()
    # print(all_data)
    # print(all_data.values())
    # print(all_data.values_list())
    all_data=Student.objects.all()[0]  #indexing   
    print(all_data)
    all_data=Student.objects.all()[:2]  #slice
    print(all_data)
    # all_data=Student.objects.all()[-1]  #slice  # it not support negative indexing
    # print(all_data)
    all_data=Student.objects.all().reverse()  #slice
    print(all_data)
    # all_data=Student.objects.all().order_by('stu_name')  #order by
    # print(all_data)
    # all_data=Student.objects.all().order_by('-stu_name') #ascending order by 
    # print(all_data)
    # all_data=Student.objects.all().order_by('-id') 
    # print(all_data)
    # all_data=Student.objects.all().order_by('id')  
    # print(all_data)
    # all_data=Student.objects.filter(stu_name='twinkle',stu_email='twinklethakre1998@gmail.com')  #used for filtering multiple  
    # print(all_data)
    # all_data=Student.objects.filter(stu_name='ria')  # empty 
    # print(all_data)
    # all_data=Student.objects.exclude(stu_name='twinkle')    #it exclude that name
    # print(all_data)
    # all_data=Student.objects.get(stu_name='ria')  #for single 
    # print(all_data)
    # all_data=Student.objects.get(stu_name='twinkle')  #for single 
    # print(all_data)
    # all_data=Student.objects.first()  #for first object
    # print(all_data)
    # all_data=Student.objects.last()  #for last object 
    # print(all_data)
    # all_data=Student.objects.create(stu_name='pooja',stu_email='pooja@gmail.com',stu_contact=1234567890,stu_city='indore')  #for create data 
    # print(all_data)
    #crude operation
    # data=Student.objects.first()   # for read
    # data.delete()   #for delete
    # data.update(stu_name='twinkle',stu_email='twinkle@gmail.com',stu_contact=1234567890,stu_city='bhopal') #for update
    # data.stu_name='twinky'
    # data.stu_email='twinky@gmail.com'
    # data.save()


    

   



