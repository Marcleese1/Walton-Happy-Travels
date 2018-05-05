from django.urls import path

from . import views
from .views import edit

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('password_change_form', edit, name='registration/password_change_form')
]