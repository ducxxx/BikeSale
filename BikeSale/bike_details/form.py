from dataclasses import field
from django import forms
from .models import BikeDetail

class BikeDetailForm(forms.ModelForm):
    class Meta:
        model = BikeDetail
        fields = ['date_of_manufacture', 'bike_color', 'bike_engine', 'height', 'weight', 'integrated_technology', 'price']
        date_of_manufacture = forms.DateField(widget=forms.widgets.DateInput(format="%m/%d/%y"))