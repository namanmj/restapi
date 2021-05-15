
from django.db import models
from django.db.models.fields import AutoField

# Create your models here.
class Society(models.Model):
    id = AutoField(primary_key=True,editable=False)
    name=models.CharField(max_length=30)
    

    def __str__(self):
        return self.name

class Building(models.Model):
    id = AutoField(primary_key=True,editable=False)
    society=models.ForeignKey(Society,on_delete=models.CASCADE,related_name='build')
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
    


class Flat(models.Model):
    id = AutoField(primary_key=True,editable=False)
    society=models.ForeignKey(Society,on_delete=models.CASCADE)
    building=models.ForeignKey(Building,on_delete=models.CASCADE,related_name='flat')
    flat_no=models.CharField(max_length=30)

    def __str__(self):
        return self.flat_no
    

    

    

    
