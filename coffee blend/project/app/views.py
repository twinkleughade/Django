from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request,'home.html')

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def menu(request):
    return render(request,'menu.html')

def service(request):
    return render(request,'service.html')

def login(request):
    return render(request,'login.html')
