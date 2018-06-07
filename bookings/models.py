from django.db import models
import uuid
from django.utils import timezone
from payments.models import Payment
import datetime

#MODEL FOR HOLDING BOOKING INFORMATION
class Bookings(models.Model):

    user = models.ForeignKey('users.Customer', verbose_name='Customer', on_delete=models.CASCADE, default=True,
                             related_name='bookings')
    id = models.IntegerField(primary_key=True, unique=True, editable=False)
    BookingId = models.UUIDField(default=uuid.uuid4, editable=False)
    bookingDate = models.DateTimeField(default=timezone.now)
    bookingType = models.CharField(blank=False, max_length=50)
    bookingPayment = models.PositiveIntegerField('Payment')
    bookingDeposit = models.PositiveIntegerField('Payment', default=0)
    seatsChosen = models.PositiveIntegerField(default=1)


#MODEL FOR HOLDING BOOKING LINE INFORMATION
class BookingLine(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    BookingLineId = models.UUIDField(default=uuid.uuid4, editable=False)
    departure = models.ForeignKey('packages.Packages', verbose_name='departureDate',
                                  on_delete=models.CASCADE,
                                  default=True, related_name='Packages')


#MODEL FOR HOLDING TRIP INFORMATION
class Trip(models.Model):
    tripId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    destination = models.CharField(max_length=200)
    duration = models.TextField(max_length=100)
    price = models.PositiveIntegerField()
    totalCost = models.PositiveIntegerField(default=0)
    hotelName = models.CharField(max_length=100)
