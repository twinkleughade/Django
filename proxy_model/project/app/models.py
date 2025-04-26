from django.db import models

# Create your models here.
class BaseInfo(models.Model):
    name=models.CharField(max_length=50)
    dob=models.DateField()
    address=models.CharField()
    branch=models.CharField()
    fees=models.IntegerField()

    class Meta:
        db_table='Student'
        ordering=['id']
        # ordering=['name']
        # ordering=['-name']
        verbose_name="My Custom Model"                      # it show s in last 
        # verbose_name_plural="My Custom Model"             #not for s



class ProxyBaseInfo(BaseInfo):
    class Meta:
        proxy=True
        ordering=['name']
        verbose_name="Myproxymodel"

        
