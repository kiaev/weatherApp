from django.shortcuts import  render
from weatherApp.models import Weather
import requests
import json
import datetime




def WeatherViewSet(request):
    
    YESTERDAY = (datetime.datetime.now()- datetime.timedelta(days=1))
    YEAR_BEFORE = str((YESTERDAY.year) - 1)
    YEAR_CURRENT = str(YESTERDAY.year)
    MONTH = str(YESTERDAY.month)
    DAY = str(YESTERDAY.day)
    CITY_NAME = "St.Petersburg"
    HOST = "https://www.metaweather.com/api/location/2123260/"
    YEARS = [YEAR_CURRENT,YEAR_BEFORE]

    req1 = (json.loads((requests.get(HOST+YEAR_CURRENT+"/"+MONTH+"/"+DAY+"/")).text)[0])    
    req2 = (json.loads((requests.get(HOST+YEAR_BEFORE+"/"+MONTH+"/"+DAY+"/")).text)[0]) 
    req_data = Weather(
        CityName = CITY_NAME,
        Date = req1['applicable_date'],
        Temperature = req1['the_temp'],
        MaxTemperature = req1['max_temp'],
        MinTemperature = req1['min_temp'],
        Humidity = req1['humidity'],
        Date_YEAR_BEFORE = req2['applicable_date'],
        Temperature_YEAR_BEFORE = req2['the_temp'],
        MaxTemperature_YEAR_BEFORE = req2['max_temp'],
        MinTemperature_YEAR_BEFORE = req2['min_temp'],
        Humidity_YEAR_BEFORE = req2['humidity']  
        )
    req_data.save()
    queryset = Weather.objects.all().last()
    
    return render (request, 'weatherApp/index.html', context={'all_queryset' : queryset})

