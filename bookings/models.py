from django.db import models
import uuid
from django.utils import timezone
from payments.models import Payment
#from users.models import Customer


class Bookings(models.Model):

    userId = models.ForeignKey('Customer', blank=False, on_delete=models.CASCADE)
    #customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    BookingId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bookingDate = models.DateTimeField(default=timezone.now)
    bookingType = models.CharField(blank=False, max_length=50)
    bookingPayment = models.CharField('Payment', max_length=30)
    bookingDeposit = models.CharField('Payment', max_length=30)


class BookingLine(models.Model):
    BookingLineId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    departureDate = models.DateTimeField(timezone.now())
    arrivalDate = models.DateTimeField(timezone.now())


class Trip(models.Model):
    tripId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    destination = models.CharField(max_length=200)
    duration = models.TextField(BookingLine.departureDate - BookingLine.arrivalDate)
    price = models.CharField(max_length=10)
    totalCost = models.CharField(price)
    hotelName = models.CharField(max_length=100)
