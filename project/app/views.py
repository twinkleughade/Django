from django.shortcuts import render

# Create your views here.
# from  django.shortcuts import render,redirect
# from django.http import HttpResponse, JsonResponse

# def home(request):
    # name='Guest'

    
    # return HttpResponse("<h1 style='background-color: purple; height: 50px; '>Hello</h1>")
    # return render(request,'index.html',{'name':name})  #for html web page
    # return redirect("https://www.google.com/")   #for urls
    # data={
    #     'name':'twinkle',
    #     'age':'26',
    #     'active':True,
    #     'other':None
    # }
    # return JsonResponse(data)

def  home(request):
    return render(request, 'index.html')

# def data(request):
#     print(request.methode)
#     print(request.FILES)
#     print(request.POST)


   


    

     

