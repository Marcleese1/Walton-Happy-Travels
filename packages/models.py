from django.db import models
from bookings.models import BookingLine, Bookings
from django.utils import timezone
from django.db import transaction
from django.db.models import F


class Packages(models.Model):
    id = models.CharField(primary_key=True, editable=False, unique=True, max_length=150)
    destination = models.CharField(max_length=200)
    hotelName = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    price = models.IntegerField()
    quantity = models.IntegerField(default="53")
    departureDate = models.DateField(default=timezone.now)
    leavingTime = models.TimeField(default=timezone.now)
   # charge_id = models.CharField(max_length=234)


