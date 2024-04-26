from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
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
        if username=='admin' and password=='admin':
            name1 = 'admin'
            a2 = {'name1': name1}
            return render(request, 'adminhomepage.html', a2)
        elif Register.objects.filter(username=username,password=password).exists():
           Login.objects.create(username=username, password=password)
           name1 = username
           a2 = {'name1': name1}
           return render(request, 'userhomepage.html', a2)
        return HttpResponse("User Name or Password is Incorrect")
    return render(request, 'loginpage.html')

@login_required(login_url='login')
def adminhome(request):
    name1 = 'admin'
    a2 = {'name1': name1}
    return render(request, 'adminhomepage.html', a2)



def phonepay(request):
    img1 = {'pp': '/static/img.png'}
    return render(request, 'phonepay.html', img1)



def customer(request):
    return render(request,'customercare.html')




#@login_required(login_url='login')

def payment(request):
    return render(request,'payment.html')
from django.http import HttpResponse
import qrcode
from io import BytesIO
'''
def netbank(request):
    data = "https://www.phonepe.com/"
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color='blue', back_color='white')

    # Saving the image to a BytesIO object
    buffer = BytesIO()
    qr_img.save(buffer, format='PNG')
    buffer.seek(0)

    # Creating an HttpResponse object with the image content
    response = HttpResponse(buffer.getvalue(), content_type='image/png')

    return response

'''


def social(request):
    return render(request,'socialmedia.html')

def offers(request):
    return render(request,'offers.html')

def tickets(request):
    return render(request,'ticket.html')

# views.py
from django.shortcuts import render

def my_view(request):
    # Set session data
    request.session['username'] = 'john'

    # Access session data
    username = request.session.get('username')

    # Your view logic here
    return render(request, 'template_name.html', {'username': username})


from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('home')  # Assuming 'home' is the name of your homepage URL pattern
