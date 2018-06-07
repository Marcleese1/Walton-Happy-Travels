from django.contrib import admin

from . import models


#displays bookings on admin page
class Booking(admin.ModelAdmin):
    model = models.Bookings


#displays booking line on admin page
class BookingLine(admin.ModelAdmin):
    model=models.BookingLine


#displays the Trip on the admin page
class Trip(admin.ModelAdmin):
    model=models.Trip


admin.site.register(models.Bookings)
admin.site.register(models.BookingLine)
admin.site.register(models.Trip)