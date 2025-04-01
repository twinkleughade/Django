from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse

# Create your views here.
def home(request):
    return render(request,'home.html')
def index(request):
    return redirect('http://www.google.com')
def textcontent(request):
    return HttpResponse("<h1> Hello django </h1>")
def jsres(request):
    data={'name':True, 'age':False, 'quali':None}
    return JsonResponse(data)
