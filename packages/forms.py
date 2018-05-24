# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Packages
from django.contrib.admin import widgets


class NewPackageForm(UserCreationForm):
    class Meta:
        model = Packages
        fields = ('destination', 'hotelName', 'price', 'departureDate', 'duration', 'quantity')


    def __init__(self, *args, **kwargs):
        super(NewPackageForm, self).__init__(*args, **kwargs)
        self.fields['departureDate'].widget = widgets.AdminDateWidget()


class ChooseSeats(UserCreationForm):
    class Meta:
        model = Packages
        fields = 'seatsChosen'

