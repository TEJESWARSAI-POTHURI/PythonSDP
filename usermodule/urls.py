from .views import *
from django.urls import path

urlpatterns = [
    path('', home, name='homeuser'),
    path('feedback/', feedbackform, name='feedback'),
    path('feedbacksave/', feedbacksave, name='feedbacksave'),
    path('showbooking/',showbooking,name='showbooking'),
    path('payme',payme,name='payme'),
    path('otp',otp,name='otp'),
    path('book/',bookdetails,name='book'),
    path('viewfeed',vifeed,name='vifeed'),
    path('thanlyou',thankyou,name='thankyou'),
    ]