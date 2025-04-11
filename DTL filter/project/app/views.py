from django.shortcuts import render


# Create your views here.
def profile(request):
    about = {
        'name': 'twinkle',
        'hobbies': ['photography', 'scabbooking', 'painting'],
        'age':21,
        'class':'django',
        'quote':'hello everyone',
        'name':'saboo',
        'number':['a','b','c'],   
    }
    

    return render(request,'profile.html',about)

