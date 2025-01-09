from django.db import models

# Create your models here.
class Student(models.Model):
    username=models.CharField(max_length=50)
    email=models.EmailField()
    detail=models.CharField(max_length=10)
    phone=models.IntegerField()
    dob=models.DateField()
    volume=models.IntegerField()
    subscribe=models.CharField(max_length=10)
    gender=models.CharField(max_length=10)
    profile_pic=models.ImageField()
    resume=models.FileField()
    password=models.CharField(max_length=10)
    

    
