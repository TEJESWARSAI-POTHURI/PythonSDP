from django.db import models

# Create your models here.


class Sankar(models.Model):
    FirstName=models.CharField(max_length=100)
   # LastName=models.CharField(max_length=100)
    email=models.EmailField(primary_key=True)
   # DOB=models.DateField
    password=models.CharField(max_length=100)
    phonenumber=models.IntegerField()
  #
   # Gender = [
  #      ('male', 'Male'),
  #      ('female', 'Female'),
   #     ('other', 'Other'),
    #]
    #Gender = models.CharField(max_length=20, choices=Gender)
    #'''

    class Meta:
        db_table="Sankar" #To show the table name to the user
