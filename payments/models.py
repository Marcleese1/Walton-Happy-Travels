from django.db import models


class Payment(models.Model):
    cardNumber = models.TextField(max_length=19)
    expiry = models.DateField(max_length=5)
    security_Code = models.TextField(max_length=4)
    Deposit = models.BooleanField(default=False)


