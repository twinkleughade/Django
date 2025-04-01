from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def app3(request):
    return HttpResponse('<h1 style="color: blue; font-size:100px;"> hello django </h1>')
