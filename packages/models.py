from django.db import models
from bookings.models import BookingLine, Bookings
from django.utils import timezone


class Packages(models.Model):
    id = models.IntegerField(primary_key=True, editable=False, unique=True)
    destination = models.CharField(max_length=200)
    hotelName = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    price = models.IntegerField()
    quantity = models.IntegerField(default="53")
    departureDate = models.DateTimeField(default=timezone.now)

