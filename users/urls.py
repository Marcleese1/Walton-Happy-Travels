# users/urls.py
from django.urls import path
from . import views
from .views import edit, delete_user

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('editdetails/', edit, name='editdetails'),
    path('user_delete', delete_user, name="user_delete")
]