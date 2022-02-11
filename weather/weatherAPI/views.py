from django.shortcuts import render
import requests
from .models import Location
from .forms import LocationForm


def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=608a07f8eeb3a2ddd6c39ba4693e4127'
    cities = Location.objects.all()
    if request.method == 'POST':
        form = LocationForm(request.POST)
        for c in cities:
            print(c)
        form.save()

    form = LocationForm()
    weather_data = []
    for city in cities:
        city_weather = requests.get(url.format(city)).json()
        weather = {
            'city': city,
            'temperature': city_weather['main']['temp'],
            'description': city_weather['weather'][0]['description'],
            'icon': city_weather['weather'][0]['icon']
        }
        
        weather_data.append(weather)
        
    context = {'weather_data': weather_data, 'form': form}

    #print(city_weather)
    return render(request, 'weatherAPI/index.html', context)
