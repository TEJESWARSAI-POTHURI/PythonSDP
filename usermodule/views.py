import string
from random import random

from django.core.mail import send_mail
from django.shortcuts import render, redirect

from django.core.mail import send_mail

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

def otp(request):

    if request.method == 'POST':
        email=request.POST.get('email')
        # mail
        recipient_email = email
        subject = 'Regarding Flight Tickets'  # Set your subject here
        message_body = 'Hello, ' + '\n' + '\n' + '\n' + '\n' + '\n' + 'This is your Confirmation Mail regarding your flight tickets.\n'   # Set your email content here
        send_mail(subject,message_body,  'saisankar3193@gmail.com',[recipient_email],fail_silently=False,)
        return redirect(thankyou)
    else:
        return render(request,'email.html')

def thankyou(request):
    return render(request,'thankyou.html')
