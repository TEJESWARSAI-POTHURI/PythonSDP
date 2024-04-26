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
        subject = 'Feed Back Information'
        message = 'Thank You for sharing Feed Back with Us. \n \n \n \nComments: '+Comments
        from_email = 'saisankar3193@gmail.com'
        recipient_email = [email]

        send_mail(subject, message, from_email, recipient_email)


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

        # mail
        recipient_email = email
        subject = 'Regarding Flight Tickets'  # Set your subject here
        message_body = 'Hello, ' + '\n' + '\n' + '\n' + '\n' + '\n' + 'This is your Confirmation Mail regarding your flight tickets.\n'   # Set your email content here
        send_mail(subject,message_body,  'saisankar3193@gmail.com',[recipient_email],fail_silently=False,)


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

def bookdetails(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email = request.POST.get('email')
        destination = request.POST.get('destination')
        boarding = request.POST.get('boarding')
        persons = request.POST.get('persons')
        luggage = request.POST.get('luggage')
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate')
        passenger.objects.create(name=name,email=email,destination=destination,boarding=boarding,persons=persons,luggage=luggage,fromdate=fromdate,todate=todate)
        flight=Flight.objects.all()
        return render(request,'guestuserflight.html',{'flight':flight})
    else:
        return redirect(home)

def vifeed(request):
    feed=Feedback.objects.all()
    return render(request,'vifeed.html',{'feed':feed})