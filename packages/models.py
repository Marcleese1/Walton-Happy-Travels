from django.db import models
from bookings.models import BookingLine, Bookings
#from django.utils import timezone


class Packages(models.Model):
    destination = models.CharField(max_length=200)
    hotelName = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    price = models.IntegerField()
    Quantity = models.ForeignKey('bookings.Bookings', on_delete=models.CASCADE)
    departure = models.ForeignKey('bookings.BookingLine', verbose_name='BookingLine', on_delete=models.CASCADE,
                                  default=True, related_name='Packages')
