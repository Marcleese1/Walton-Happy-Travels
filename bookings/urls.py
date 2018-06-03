from django.urls import path

from . import views
from .views import view_bookings, EditBooking, booking_report

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('bookings_list/', view_bookings, name='bookings_list'),
    path('<int:pk>/EditBookings/', EditBooking.as_view(), name="view_bookings"),
   #path('<int:pk>/EditPackages/', EditPackage.as_view(), name="EditPackage")
    path('booking_report/', booking_report, name="bookingReport")
]