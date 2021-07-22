from django import forms
from django.forms import ModelForm, TextInput
from .models import City

class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name', 'city_image']
        widgets = {'name' : TextInput(attrs={'class': 'input', 'placeholder': 'City Name'})}

# will add it to views now for the prac.html page