from django.shortcuts import render, redirect
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
from django.shortcuts import render, get_object_or_404



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
        'sixth_row': weather_data[20:24],
        'seventh_row': weather_data[24:28],
        'eight_row': weather_data[28:32], 
        'tenth_row': weather_data[36:40], 

    }

    return render(request, 'app/index.html', context)



def SearchResultsView(request):
    
    context = {}
    return render(request, 'app/search.html', context)


# you always need three things with django views urls and a template

def prac(request):
    if request.method == 'POST':
        # this was taken from the docs
        # becaise we are also looking for a file git
        form = CityForm(request.POST, request.FILES)
        data = request.POST
        img = request.FILES.get('image')

        new_city = City.objects.create(
            name=data['name'],
            city_image=img,
        )
             # form.save()
            # some sort of action needs to be performed here
            # (1) save data
            # (2) send an email ####
            # (3) return search result
            # (4) upload a file
        return HttpResponseRedirect(reverse('search'))
        # else:
        #     messages.add_message(request, messages.INFO, 'We already have this city! Return to Homepage to view')
    # else:
    #     form = CityForm()
        
   

    form = CityForm()
    context = {'form': form}
    return render(request, 'app/prac.html', context)



