from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')

def new1(request):
    print(request.method)
    print(request.POST)  #for text content from  home.html
    print(request.FILES) #for binary content from home.html

    name=request.POST.get('fname')
    image=request.FILES.get('image')

    print(name,image)