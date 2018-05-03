from django.contrib import admin

from . import models


class Booking(admin.ModelAdmin):
    model = models.Bookings


admin.site.register(models.Bookings)
