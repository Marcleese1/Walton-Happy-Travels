# users/urls.py
from django.urls import path
from . import views
from .views import edit, delete_account

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('editdetails/', edit, name='editdetails'),
    path('delete_user/', delete_account, name='deleteUser')
]