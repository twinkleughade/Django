from django.shortcuts import render
from .models import FuelTypeModel,CarModel

# Create your views here.

def fueltype(request):
    all_data=FuelTypeModel.objects.all()
    print(all_data)

def cartype(request):
    # forward access(carmodel + fueltypemodel)
    car=CarModel.objects.get(car_name='Swift')
    fuel_types=car.fuel_name.all()

    for fuel in fuel_types:
        print(fuel.fuel_name)

   # reverse access (fueltypemode - carmodel)
   # fuel_name=models.manytomanyfield
    fuel=FuelTypeModel.objects.get(fuel_name='Petrol')
    cars_using_petrol=fuel.cars.all()

    for car in cars_using_petrol:
        print(car.car_name)
        



