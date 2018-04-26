from django.db import models
import uuid
from django.utils import timezone
from payments.models import Payment
#from users.models import Customer


class Bookings(models.Model):

    #customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    BookingId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bookingDate = models.DateTimeField(default=timezone.now)
    bookingType = models.CharField(blank=False, max_length=50)
    bookingPayment = models.CharField('Payment', max_length=30)
    bookingDeposit = models.CharField('Payment', max_length=30)
