from dataclasses import field
from django import forms
from .models import Bike

class BikeForm(forms.ModelForm):
    class Meta:
        model = Bike
        fields = ['bikename', 'bikecode', 'type', 'description', 'image1', 'image2', 'image3']