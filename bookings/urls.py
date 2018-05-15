from django.urls import path

from . import views
#

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('<int:pk>/', views.BookingDetailView.as_view(), name='booking_detail' ),
    path('bookings_list/', views.BookingListView.as_view(), name='bookings_list')
]