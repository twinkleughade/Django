from django.db import models


# Create your models here.
class Adhar(models.Model):
    adhar_no=models.IntegerField(unique=True)
    created_by=models.CharField(max_length=50)
    alloted_date=models.DateTimeField()

    def __str__(self):
        return str(self.adhar_no)

class Citizen(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField()
    contact=models.IntegerField(unique=True)
    adhar_no=models.OneToOneField(Adhar,on_delete=models.PROTECT,to_field='adhar_no',related_name='xyz')
    # adhar_no=models.OneToOneField(Adhar,on_delete=models.CASCADE)


    def __str__(self):
        # return str(self.name)
        return self.name +' '+ str(self.adhar_no)
    

        
