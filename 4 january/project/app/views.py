from django.shortcuts import render
def home(request):
    return render(request,'home.html')

# Create your views here.

def data(request):
    print(request.method)
    print(request.FILES)
    print(request.POST)


    name = request.POST.get('username')
    email = request.POST.get('email')
    detail = request.POST.get('detail')
    phone = request.POST.get('phone')
    age = request.POST.get('age')
    volume = request.POST.get('volume')
    subscribe = request.POST.getlist('subscribe')
    gender = request.POST.get('gender')
    dob = request.POST.get('dob')
    password = request.POST.get('password')
    cpassword = request.POST.get('cpassword')
    profile_pic = request.FILES.get('profile-pic')
    resume = request.FILES.get('resume')

    print(name)
    print(email)
    print(detail)
    print(phone)
    print(age)
    print(volume)
    print(subscribe)
    print(gender)
    print(dob)
    print(profile_pic)
    print(resume)
    print(password)
    print(cpassword)