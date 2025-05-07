from django.db import models

# Create your models here.
class student(models.Model):
    stu_name=models.CharField(max_length=50)
    stu_email=models.EmailField()
    stu_des=models.CharField(max_length=201)
    stu_contact=models.IntegerField()
    stu_dob=models.DateField()
    stu_edu=models.CharField(max_length=50)
    stu_gender=models.CharField(max_length=50)
    stu_image=models.ImageField(upload_to='image/')
    stu_document=models.FileField(upload_to='file/')
    stu_pass=models.CharField(max_length=50)
