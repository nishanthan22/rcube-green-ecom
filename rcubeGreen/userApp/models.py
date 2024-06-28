from django.db import models
from django.contrib.auth.models import User


class RegisterUser(User):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='male')


# class LoginUser(User):
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=100)
