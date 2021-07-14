from django.shortcuts import render
# from django.shortcuts import render
import requests
from .models import City
# Create your views here.


def index(request):

    

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=685feed5f1bd934d26f395f2e68fbd7f'


    cities = City.objects.all()

    weather_data = []
    for city in cities:
        r = requests.get(url.format(city)).json()

        city_weather = {
            'city': city.name,
            'temp': r['main']['temp'],
            'description':r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
            'time': r['dt'],
            'sunset': r['sys']['sunset'],
        }
     
        weather_data.append(city_weather)


    # print(city_weather)
    print(weather_data)
    context = {
        'weather_data': weather_data,
        'first_row': weather_data[:4],
        'sec_row': weather_data[4:8],
        'thrid_row': weather_data[8:12],

        }

    return render(request, 'app/index.html', context)