from django.urls import path

from . import views
from .views import view_bookings

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('view_bookings/', view_bookings, name='bookings_list')
]