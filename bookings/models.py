from django.db import models
import uuid


class Bookings:
    userID = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    BookingId = models.UUIDField(primary_key=True, Default=uuid.uuid4,editable=False)
