from django.contrib import admin
from .models import Adhar,Citizen

# Register your models here.
@admin.register(Adhar)
class AdharAdmin(admin.ModelAdmin):
    list_display=['adhar_no','created_by','alloted_date']

@admin.register(Citizen)
class CitizenAdmin(admin.ModelAdmin):
    list_display=['name','email','contact','adhar_no']