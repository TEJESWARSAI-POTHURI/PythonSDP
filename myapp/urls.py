# myapp/urls.py
from django.urls import path
from .views import *


urlpatterns = [
    path('',home,name='home'),
    path('search/',search,name='search'),
    path('searchflights/',flights,name='search'),

    path('login/',login,name='login'),
    path('register/',reg,name='register'),
    path('regfun/',regfun,name='regfun'),
    path('customer/',customer,name='customer'),
    path('pay',payment,name='payment'),
    path('loginfun',loginfun,name='loginfun'),
    path('social',social,name='social'),
    path('phonepay',phonepay,name='phonepay'),
   # path('netbank',netbank,name='netbank')
    path('offers',offers,name='offers'),
    path('tickets',tickets,name='tickets'),
    path('logout/', logout_view, name='logout'),
    path('adminhome/',adminhome,name='adminhome'),

    ]