from django.db import models

# Create your models here.
class Employee(models.Model):
    id=models.AutoField(primary_key=True)
    emo_name=models.CharField(max_length=50)
    emp_email=models.EmailField(unique=True)
    emo_joining_date=models.DateTimeField(auto_now_add=True)
    emp_updated_at=models.DateTimeField(auto_now=True)
    emp_dob = models.DateTimeField()
    emp_start_time = models.TimeField()
    emp_active = models.BooleanField()
    emp_discription = models.TextField()
    emp_pic = models.ImageField(upload_to='image/')
    emp_document = models.FileField(upload_to='file/')

class Student(models.Model):
    id=models.AutoField(primary_key=True)
    emo_name=models.CharField(max_length=50)
    emp_email=models.EmailField(unique=True)
    emo_joining_date=models.DateTimeField(auto_now_add=True)
    emp_updated_at=models.DateTimeField(auto_now=True)
    emp_dob = models.DateTimeField()
    emp_start_time = models.TimeField()
    emp_active = models.BooleanField()
    emp_discription = models.TextField()
    emp_pic = models.ImageField(upload_to='image/')
    emp_document = models.FileField(upload_to='file/')