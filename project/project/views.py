from  django.shortcuts import render,redirect
from django.http import HttpResponse

def home(request):
    x=10
    y=10
    
    return HttpResponse("<h1 style='background-color: aquamarine; height: 50px; '>Hello</h1>")