from django.urls import path

from . import views
from .views import view_bookings, editbooking

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('view_bookings/', view_bookings, name='bookings_list'),
    path('editbookings/', editbooking, name='editbookings')
]