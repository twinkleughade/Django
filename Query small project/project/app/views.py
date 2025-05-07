from django.shortcuts import render
from .models import Student

# Create your views here.
def landing(request):
    return render(request,'landing.html')

def first(request):
    data=Student.objects.all()[0:5]
    return render(request,'table.html',{'data':data})

def asc(request):
    data=Student.objects.order_by('name')
    return render(request,'table.html',{'data':data})

def last_5(request):
    data=Student.objects.order_by('-name')[0:5]
    return render(request,'table.html',{'data':data})

def desc(request):
    data=Student.objects.order_by('-name')
    return render(request,'table.html',{'data':data})

def all(request):
    data=Student.objects.all()
    return render(request,'table.html',{'data':data})







