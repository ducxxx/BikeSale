from dataclasses import field
from django import forms
import re
from .models import Users
class CreateUserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['id', 'birthday', 'age', 'address', 'username', 'password', 'last_name', 'first_name']
        birthday = forms.DateField(widget=forms.widgets.DateInput(format="%m/%d/%y"))
        password = forms.CharField(max_length=20, widget=forms.PasswordInput)
        

class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['birthday', 'age', 'address', 'username', 'password', 'last_name', 'first_name']
        birthday = forms.DateField(widget=forms.widgets.DateInput(format="%m/%d/%y"))
        password = forms.CharField(max_length=20, widget=forms.PasswordInput)