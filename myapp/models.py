from django.db import models

# Create your models here.
class Register(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(primary_key=True)
    phonenumber=models.IntegerField(max_length=10)
    password=models.CharField(max_length=100)

    class meta:
        db_table = "Register"