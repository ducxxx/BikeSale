from distutils.command.upload import upload
from tkinter import Image
from django.db import models

# Create your models here.
class Bike(models.Model):
    bikename = models.CharField(max_length=30)
    bikecode = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    image1 = models.ImageField(upload_to='files/covers')
    image2 = models.ImageField(upload_to='files/covers')
    image3 = models.ImageField(upload_to='files/covers')