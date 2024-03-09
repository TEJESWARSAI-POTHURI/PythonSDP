

from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import *
from django.views.decorators.csrf import csrf_exempt

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
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')

        if Register.objects.filter(email=email).exists():
            return HttpResponse("Email already registered. Choose a different email.")
        Register.objects.create(username=username,  email=email,password=password)
        return render(request, 'loginpage.html')
    return render(request,'loginpage.html')



def loginfun(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if Register.objects.filter(username=username,password=password).exists():
           Login.objects.create(username=username, password=password)
           return render(request,'home.html')
        return HttpResponse("User Name or Password is Incorrect")
    return render(request, 'loginpage.html')





def customer(request):
    return render(request,'customercare.html')
def payment(request):
    return render(request,'payment.html')

def social(request):
    return render(request,'socialmedia.html')



