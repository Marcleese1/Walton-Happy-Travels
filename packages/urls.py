from django.urls import path

from . import views
from. import models
from .models import Packages
from .views import ChooseSeats, EditPackage, checkout, payment_form, Delete_Booking, Delete_package

#URLS FOR PACKAGE APP
urlpatterns = [
    path('', views.ViewPackages.as_view(), name='viewpackages'),
    path('checkout/', checkout, name="checkout"),
    path('payment_form/', payment_form, name="payment"),
    path('PackageCreateView/', views.PackageCreateView.as_view(), name="package_new"),
    path('<int:pk>/ChooseSeats/', ChooseSeats.as_view(), name="chooseSeats"),
    path('<int:pk>/EditPackages/', EditPackage.as_view(), name="EditPackage"),
    path('<int:pk>/delete_booking/', Delete_Booking.as_view(), name="delete_booking"),
    path('<int:pk>/delete_package/', Delete_package.as_view(), name='DeletePackage')
]