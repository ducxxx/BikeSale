from enum import auto
from statistics import mode
from tkinter import Widget
from django.db import models, migrations
from django import forms

# Create your models here.
class Users(models.Model):
    birthday = models.DateField()
    age = models.IntegerField()
    address = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    role = models.IntegerField()