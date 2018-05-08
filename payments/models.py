from django.db import models
from django.utils import timezone


class Payment(models.Model):
    date_paid = models.DateTimeField(default=timezone.now)
    Deposit = models.BooleanField(default=False)
    Deposit_Amount = models.IntegerField(blank=True, null=True)

