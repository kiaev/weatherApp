import requests
import datetime
import json

getCurrentYear = str(datetime.datetime.now().year)
getCurrentMonth = str(datetime.datetime.now().month)
getYesterday = str(datetime.datetime.now().day -1) 
print(getCurrentYear,getCurrentMonth,getYesterday)

getWeatherParse = requests.get("https://www.metaweather.com/api/location/2123260/"+getCurrentYear+"/"+getCurrentMonth+"/"+getYesterday+"/")
weatherParametrList = (json.dumps(getWeatherParse.json(), sort_keys=True, indent=4))




"""
getLocation = ((requests.get("https://www.metaweather.com/api/location/2123260/"+getCurrentYear+"/"+getCurrentMonth+"/"+getYesterday+"/")).text).split(",")
print (getLocation)

for element in getLocation:
    print(element)
"""
