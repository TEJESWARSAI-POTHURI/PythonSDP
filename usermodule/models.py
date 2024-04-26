from django.db import models

# Create your models here.
class Feedback(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    Comments=models.CharField(max_length=100)
    class meta:
        db_table="Feedback" #To show the table name to the user

class passenger(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    destination=models.CharField(max_length=100)
    boarding=models.CharField(max_length=100)
    persons=models.CharField(max_length=100)
    luggage=models.CharField(max_length=100)
    fromdate=models.CharField(max_length=100)
    todate=models.CharField(max_length=100)


    class meta:
        db_table="passenger" #to know the user details

