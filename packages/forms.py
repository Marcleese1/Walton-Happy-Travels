# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Packages


class NewPackageForm(UserCreationForm):
    class Meta:
        model = Packages
        fields = ('destination', 'hotelName', 'price', 'duration')

