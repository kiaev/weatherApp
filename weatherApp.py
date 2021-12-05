import requests;
import datetime;

getCurrentYear = str(datetime.datetime.now().year)
getCurrentMonth = str(datetime.datetime.now().month)
getYesterday = str(datetime.datetime.now().day -1) 
print(getCurrentYear,getCurrentMonth,getYesterday)
getLocation = (requests.get("https://www.metaweather.com/api/location/2123260/"+getCurrentYear+"/"+getCurrentMonth+"/"+getYesterday+"/")).text
print (getLocation)

