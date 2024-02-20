

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
    if request.method=='POST':
        FirstName=request.POST.get('FirstName')
        email=request.POST.get('email')
        dob=request.POST.get('DOB')
        password=request.POST.get('password')
        repassword = request.POST.get('repassword')
        mobile=request.POST.get('mobile')
        gender=request.POST.get('Gender')

        if User.objects.filter(email=email).exists():
            return HttpResponse("Email already registered. Choose a different email.")

        User.objects.create(first_name=FirstName,  email=email,dob=dob, password=password, repassword=repassword, mobile=mobile,gender=gender )
        return redirect('home')
    return render(request,'registerpage.html')


def customer(request):
    return render(request,'customercare.html')



