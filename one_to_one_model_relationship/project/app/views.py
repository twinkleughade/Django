from django.shortcuts import render
from .models import *

# Create your views here.
def adhar_no1(request):
    data=Adhar.objects.all()
    print(data.values())
    # print(data.values_list())

    data=Adhar.objects.get(adhar_no=1234)
    print(data.adhar_no) 
    print(data.created_by)
    print(data.alloted_date)
    x=data.xyz # for reverse accessing
    print(x.name)
    print(x.email)
    print(x.contact)
    print(x.adhar_no)

def citizen1(request):
    data=Citizen.objects.all()
    print(data)
    print(data.values())
    print(data.values_list())

    # data=Citizen.objects.get(name='twinkle')
    data=Citizen.objects.get(id=1)
    print(data.name)
    print(data.email)
    print(data.contact)
    print(data.adhar_no)
    x=data.adhar_no # for forward accessing
    print(x.adhar_no)
    print(x.created_by)
    print(x.alloted_date)

    

