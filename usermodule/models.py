from django.db import models

# Create your models here.
class Feedback(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    Comments=models.CharField(max_length=100)
    class meta:
        db_table="Feedback" #To show the table name to the user
'''
class Flight(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    destination=models.CharField(max_length=100)
    boardingpoint=models.CharField(max_length=100)
    numberofpersons=models.CharField(max_length=100)
    weight=models.CharField(max_length=100)

    class meta:
        db_table="Passenger_details" #to know the user details 
'''
