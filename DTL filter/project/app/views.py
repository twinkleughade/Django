from django.shortcuts import render


# Create your views here.
def profile(request):
    about = {
        'name': 'twinkle',
        'hobbies': 'photography',
        'age':21,
        'class':'django',
        'quote':'hello everyone',
        'number':['a','b','c']   
    }
    

    # return render(request,'profile.html',about)
    return render(request,'profile.html',about)


