
from django.db import models

class Register(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    class Meta:
        db_table = "Register"

class Login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    class Meta:
        db_table = "Login"



class ChillMODEL(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    destination=models.CharField(max_length=100)
    boardingpoint=models.CharField(max_length=100)
    numberofpersons=models.CharField(max_length=100)
    weight=models.CharField(max_length=100)

    class meta:
        db_table="Passenger_details" #to know the user details

