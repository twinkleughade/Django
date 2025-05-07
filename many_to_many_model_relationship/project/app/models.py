from django.db import models

# Create your models here.

class FuelTypeModel(models.Model):
    fuel=[
        ('Diesel','Diesel'),
        ('Petrol','Petrol'),
        ('CNG','CNG'),
        ('LPG','LPG')
    ]
    fuel_name=models.CharField(max_length=255,choices=fuel)
    def __str__(self):
        return self.fuel_name
    
class CarModel(models.Model):
    car=[
        ('nexon','nexon'),
        ('Tiago','Tiago'),
        ('Swift','Swift')
    ]
    car_name=models.CharField(max_length=255,choices=car)
    fuel_name=models.ManyToManyField(FuelTypeModel,related_name="cars")
    def __str__(self):
        return self.car_name
    
