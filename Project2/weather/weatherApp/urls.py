from django.urls import path
from .views import WeatherViewSet
urlpatterns = [
    path('',WeatherViewSet)
]