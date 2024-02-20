
from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    dob = models.CharField(max_length=10)
    password = models.CharField(max_length=100)  # Consider using Django's built-in User model for authentication
    repassword = models.CharField(max_length=100)  # Assuming this is for password confirmation
    mobile = models.CharField(max_length=10)  # Assuming Indian phone numbers, change accordingly
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    def __str__(self):
        return self.first_name  # or any other meaningful representation

    class Meta:
        db_table = "User"  # To specify the table name
