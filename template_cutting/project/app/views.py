from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request,'landing.html')
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def service(request):
    return render(request,'service.html')
def registration(request):
    return render(request,'registration.html')
def login(request):
    return render(request,'login.html')
def register(request):
    print('register page')
    print(request.GET)
    print(request.POST)
    print(request.FILES)
    username=request.POST.get('username')
    email=request.POST.get('email')
    detail=request.POST.get('detail')
    phone=request.POST.get('phone')
    dob=request.POST.get('dob')
    subscribe=request.POST.getlist('subscribe')
    gender=request.POST.get('gender')
    profile_pic=request.FILES.get('profile-pic')
    resume=request.POST.get('resume')
    password=request.POST.get('password')
    cpassword=request.POST.get('cpassword')

    print(username,email,detail,phone,dob,subscribe,gender,password,cpassword,profile_pic,resume)