from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse

# Create your views here.
def home(request):
    # data={'name':'twinkle', 'age':26, 'quali':'Mtech'}
    data=[{'name':'twinkle', 'age':26, 'quali':'Mtech'},{'name':'twink', 'age':26, 'quali':'Btech'}]
    user={'name':'twi','city':'bhopal'}
    # return render(request,'home.html', data)
    # return render(request,'home.html', {'key1':data})
    return render(request,'home.html',{'key1':user, 'key2':data})
  
def index(request):
    return redirect('http://www.google.com')
def textcontent(request):
    return HttpResponse("<h1> Hello django </h1>")
def jsres(request):
    data={'name':True, 'age':False, 'quali':None}
    return JsonResponse(data)
