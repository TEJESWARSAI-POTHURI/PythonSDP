from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import *


def home(request):
    return render(request,'home.html')
def search(request):
    return render(request,'searchflightresult.html')


def hello1(request):
    return HttpResponse("<center>Welcome to TTM Homepage</center>")

def flights(request):
    return render(request,'Flights.html')
def ticks(request):
    return render (request,'booktickets.html')

def login(request):
    return render(request,'loginpage.html')
def reg(request):
    return render(request,'registerPage.html')
def regfun(request):
    if(request.method=='POST'):
        name=request.POST.get('name')
        email=request.POST.get('email')
        phonenumber=request.POST.get('phonenummber')
        password=request.POST.get('password')

        if Register.objects.filter(email=email).exists():
            return HttpResponse("email already exists ")
        Register.objects.create(name=name,email=email,phonenumber=phonenumber,password=password)
        return redirect('home')
    return render(request,'registerpage')


def customer(request):
    return render(request,'customercare.html')


