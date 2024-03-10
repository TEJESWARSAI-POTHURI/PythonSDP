from django.core.mail import send_mail
from django.shortcuts import render, redirect

from django.core.mail import send_mail
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