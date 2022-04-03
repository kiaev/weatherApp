from django.db import models

class Weather(models.Model):

    CityName = models.CharField('CityName', max_length=255)

    Date = models.CharField(max_length=255)

    Temperature = models.CharField(max_length=255)

    MaxTemperature = models.CharField(max_length=255)

    MinTemperature = models.CharField(max_length=255)

    Humidity = models.CharField(max_length=255)

    Date_YEAR_BEFORE = models.CharField(max_length=255)

    Temperature_YEAR_BEFORE = models.CharField(max_length=255)

    MaxTemperature_YEAR_BEFORE = models.CharField(max_length=255)

    MinTemperature_YEAR_BEFORE = models.CharField(max_length=255)

    Humidity_YEAR_BEFORE = models.CharField(max_length=255)

    def __str__(self):
        return '{}'.format(self.title)
