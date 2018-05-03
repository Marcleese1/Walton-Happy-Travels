from django.db import models


class Payment(models.Model):
    date_paid = models.DateTimeField()
    Deposit = models.BooleanField(default=False)
    Deposit_Amount = models.IntegerField(blank=True, null=True)

