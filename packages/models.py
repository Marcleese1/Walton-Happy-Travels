from django.db import models
from bookings.models import BookingLine, Bookings
from django.utils import timezone
from django.db import transaction
from django.db.models import F


#MODEL TO STORE PACKAGE INFORMATION
class Packages(models.Model):
    id = models.IntegerField(primary_key=True, editable=False, unique=True)
    destination = models.CharField(max_length=200)
    hotelName = models.CharField(max_length=100)
    duration = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField(default="53")
    departureDate = models.DateField(default=timezone.now)
    leavingTime = models.TimeField(default=timezone.now)
    type = models.CharField(max_length=100, default="Coach")


