from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

def app4(request):
    # data={'name':True,'age':False,'quali':None}
    data={'name':'twinkle','age':26,'quali':'BE'}
    return JsonResponse(data)

