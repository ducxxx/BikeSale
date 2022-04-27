from django.db import models

from home.models import Bike

# Create your models here.
class BikeDetail(models.Model):
    bikecode = models.ForeignKey(Bike, on_delete=models.CASCADE)
    date_of_manufacture = models.DateField()
    bike_color = models.CharField(max_length=30)
    bike_engine = models.CharField(max_length=128)
    height = models.IntegerField()
    weight = models.IntegerField()
    integrated_technology = models.CharField(max_length=20)
    price = models.IntegerField()