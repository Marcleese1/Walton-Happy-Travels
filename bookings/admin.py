from django.contrib import admin

from . import models


class Booking(admin.ModelAdmin):
    model = models.Bookings


class BookingLine(admin.ModelAdmin):
    model=models.BookingLine


admin.site.register(models.Bookings)
admin.site.register(models.BookingLine)