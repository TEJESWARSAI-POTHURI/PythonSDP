import string
from random import random


from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail, message,EmailMessage

from adminmodule.models import Flight


# Create your views here.
def home(request):
    return render(request,'userhomepage.html')

def feedbackform(request):
    return render(request,'feedbackform.html')
from .models import *
def feedbacksave(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        Comments = request.POST.get('Comments')
        Feedback.objects.create(name=name, email=email, Comments=Comments)
        return redirect('homeuser')
    return render(request, 'feedbackform.html')

def showbooking(request):
    flight = Flight.objects.all()
    return render(request, 'viewflight.html', {'flight': flight})

def payme(request):
    return render(request,'payme.html')

from django.core.mail import send_mail
def otp(request):

    if request.method == 'POST':
        email=request.POST.get('email')

        recipient_email = [email]
        print(f'Sent email to {recipient_email}')
        subject='Ticket Confirmation'
        message='Thank You for booking with US.'
        from_email='saisankar3193@gmail.com'

        send_mail(subject,message,from_email,recipient_email)
        print(f'Sent email to {recipient_email}')


        return redirect(thankyou)
    else:
        return render(request,'email.html')

def thankyou(request):
    return render(request,'thankyou.html')
