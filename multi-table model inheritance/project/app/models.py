from django.db import models

# Create your models here.

class BaseField(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=255)
    contact=models.IntegerField()
    def __str__(self):
        return self.name
    
    
class Student(BaseField):
    course=models.CharField(max_length=50)
    roll_no=models.IntegerField()
    def __str__(self):
        return self.name
    

class Employee(BaseField):
    department=models.CharField(max_length=20)
    emp_id=models.IntegerField()
    salary=models.IntegerField()
    def __str__(self):
        return self.name

class Client(BaseField):
    project=models.CharField(max_length=100)
    billing_status=models.IntegerField()
    def __str__(self):
        return self.name



