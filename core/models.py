from django.db import models

# Create your models here.
class Flat(models.Model):
    flat_no=models.CharField(max_length=30)

    def __str__(self):
        return self.flat_no
    
class Building(models.Model):
    name=models.CharField(max_length=30)
    flat=models.ManyToManyField(Flat)
    

    def __str__(self):
        return self.name
    
class Society(models.Model):
    name=models.CharField(max_length=30)
    building=models.ManyToManyField(Building)

    def __str__(self):
        return self.name
    
