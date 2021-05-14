
from django.db import models

# Create your models here.
class Society(models.Model):
    name=models.CharField(max_length=30)
    

    def __str__(self):
        return self.name

class Building(models.Model):
    society=models.ForeignKey(Society,on_delete=models.CASCADE,related_name='build')
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
    


class Flat(models.Model):
    society=models.ForeignKey(Society,on_delete=models.CASCADE)
    building=models.ForeignKey(Building,on_delete=models.CASCADE,related_name='flat')
    flat_no=models.CharField(max_length=30)

    def __str__(self):
        return self.flat_no
    

    

    

    
