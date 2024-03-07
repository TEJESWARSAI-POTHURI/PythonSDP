# myapp/urls.py
from django.urls import path
from .views import *


urlpatterns = [
    path('',home,name='home'),
    path('search/',search,name='search'),
    path('searchflights/',flights,name='search'),
    path('book/',ticks,name='book'),
    path('login/',login,name='login'),
    path('register/',reg,name='register'),
    path('regfun/',regfun,name='regfun'),
    path('customer/',customer,name='customer'),
    path('pay',payment,name='payment'),
    path('loginfun',loginfun,name='loginfun'),
    ]