from django.shortcuts import render
# from django.shortcuts import render
import requests
from app.models import City
from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
from .forms import CityForm
from django.urls import reverse
from django.contrib import messages


def index(request):

    

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=685feed5f1bd934d26f395f2e68fbd7f'


    cities = City.objects.all()

    weather_data = []
    for city in cities:
        r = requests.get(url.format(city)).json()

        city_weather = {
            'city': city.name,
            'main_image': city.city_image,
            'temp': r['main']['temp'],
            'description':r['weather'][0]['description'],
            # 'icon': r['weather'][0]['icon'],
            'time': r['dt'],
            'sunset': r['sys']['sunset'],
            'country': r['sys']['country']
        }
     
        weather_data.append(city_weather)
        # to render out the image it will be 
        # weather_data.city_image


    # print(city_weather)
    print(weather_data)
    context = {
        'weather_data': weather_data,
        'first_row': weather_data[:4],
        'sec_row': weather_data[4:8],
        'thrid_row': weather_data[8:12],
        'fourth_row': weather_data[12:16],
        'fifth_row': weather_data[16:20],

        }

    return render(request, 'app/index.html', context)



def SearchResultsView(request):
    
    if request.method == "POST":
        searched = request.POST['searched']
        # prints to test
        # print(searched)
        # not case senstive
        looking_city = City.objects.filter(name__icontains=searched)
        # print(looking_city)
        # why are we using the variable name because that is the name we gave it in models.py
        return render(request, 'app/search.html', {'looking_city': looking_city, 'searched': searched, 'main': main})
        


    return render(request, 'app/search.html', {'looking_city': looking_city, 'searched': searched})


# you always need three things with django views urls and a template

def prac(request):
    if request.method == 'POST':
        # print(request.POST)
        form = CityForm(request.POST)
        if form.is_valid():
            
            form.save()
            # some sort of action needs to be performed here
            # (1) save data
            # (2) send an email ####
            # (3) return search result
            # (4) upload a file
            return HttpResponseRedirect(reverse('correct'))
        else:
            messages.add_message(request, messages.INFO, 'We already have this city! Return to Homepage to view')
    else:
        form = CityForm()
        
    # return HttpResponseRedirect(reverse('correct')) 

    form = CityForm()
    context = {'form': form}
    return render(request, 'weather/prac.html', context)