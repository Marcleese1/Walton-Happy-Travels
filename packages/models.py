from django.db import models


class Packages(models.Model):
    destination = models.CharField(max_length=200)
    hotelName = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    price = models.IntegerField()
    Quantity = models.IntegerField(default="53")