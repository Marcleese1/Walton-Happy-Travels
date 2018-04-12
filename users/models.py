from django.contrib.auth.models import AbstractUser
from django.db import models


class Customer(AbstractUser):
    email = models.EmailField(blank=False, unique=True)
    FirstName = models.CharField(blank=True, max_length=255)
    LastName = models.CharField(blank=True, max_length=255)
    Address_Line_1 = models.CharField(blank=True, max_length=255)
    Address_Line_2 = models.CharField(blank=True, max_length=255)
    town = models.CharField(blank=True, max_length=50)
    postCode = models.CharField(blank=True,max_length=8)
    PhoneNumber = models.CharField(blank=True, max_length=15)
    homePhone = models.CharField(blank=True,max_length=15)

    def __str__(self):
        return self.email


class Staff(AbstractUser):
    FirstName = models.CharField(blank=True, max_length=255)
    LastName = models.CharField(blank=True, max_length=255)
