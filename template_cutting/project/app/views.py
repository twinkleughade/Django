from django.shortcuts import render
from .models import student

# Create your views here.
def base(request):
    return render(request,'landing.html')
def home(request):
    return render(request,'home.html')
def home1(request,pk):
    userdata=student.objects.get(id=pk)
    userdata={
        "id":userdata.id,
        "name":userdata.stu_name,
        "contact":userdata.stu_contact,
        "email":userdata.stu_email,
        "des":userdata.stu_des,
        "dob":userdata.stu_dob,
        "edu":userdata.stu_edu,
        "gender":userdata.stu_gender,
        "image":userdata.Stu_image,
        "document":userdata.stu_document,
        "pass":userdata.stu_pass, 
    }
    return render(request,'home.html',{'userdata':userdata})
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
    resume=request.FILES.get('resume')
    password=request.POST.get('password')
    cpassword=request.POST.get('cpassword')

    print(username,email,detail,phone,dob,subscribe,gender,password,cpassword,profile_pic,resume)

    user=student.objects.filter(stu_email=email)
    if user:
        msg="Email already exist"
        return render(request,'registration.html',{'key':msg})
    else:
        if password==cpassword:
            student.objects.create(stu_name=username,stu_email=email,stu_des=detail,stu_contact=phone,stu_dob=dob,stu_edu=subscribe,stu_gender=gender,Stu_image=profile_pic,stu_document=resume,stu_pass=password)
            msg="Registration done"
            return render(request,'login.html',{'key1':msg})
        else:
            msg1="password and confirm password not matched"
            return render(request,'registration.html',{'key':msg1})


    # student.objects.create(stu_name=username,stu_email=email,stu_des=detail,stu_contact=phone,stu_dob=dob,stu_edu=subscribe,stu_gender=gender,Stu_image=profile_pic,stu_document=resume,stu_pass=password)

def logindata(request):
    if request.method=='POST':
        email=request.POST.get('email')
        passw=request.POST.get('password')
        user=student.objects.filter(stu_email=email)
        if user:
            userdata=student.objects.get(stu_email=email)
            print(userdata.stu_name)
            print(userdata.stu_email)
            pass1=userdata.stu_pass
            if passw==pass1:
                dmsg="Welcome to Dashboard"
                userdata={
                    "id":userdata.id,
                    "name":userdata.stu_name,
                    "contact":userdata.stu_contact,
                    "email":userdata.stu_email,
                    "des":userdata.stu_des,
                    "dob":userdata.stu_dob,
                    "edu":userdata.stu_edu,
                    "gender":userdata.stu_gender,
                    "image":userdata.Stu_image,
                    "document":userdata.stu_document,
                    "pass":userdata.stu_pass,                   
                }
                return render(request,'dashboard.html',{"userdata":userdata})
            else:
                msg="email and password not matched"
                return render(request,'login.html',{'msg':msg,'email':email})
        else:
            msg="email not registered"
            return render(request,'login.html')
    else:
        return render(request,'login.html')




   