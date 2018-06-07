# users/urls.py
from django.urls import path
from . import views
from .views import edit, delete_account, change_password, SignUp

#URLS FOR THE USER APP
urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('editdetails/', edit, name='editdetails'),
    path('delete_user/', delete_account, name='deleteUser'),
    path('password/', change_password, name='changepassword')
]