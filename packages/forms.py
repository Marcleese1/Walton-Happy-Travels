# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Packages
from django.contrib.admin import widgets
from bookings.models import Bookings


class NewPackageForm(UserCreationForm):
    class Meta:
        model = Packages
        fields = ('destination', 'hotelName', 'price', 'departureDate', 'leavingTime', 'duration', 'quantity', 'type')

    def __init__(self, *args, **kwargs):
        super(NewPackageForm, self).__init__(*args, **kwargs)
        self.fields['departureDate'].widget = widgets.AdminDateWidget()


class ChooseSeatsForm(forms.ModelForm):
    class Meta:
        model = Bookings
        fields = ('seatsChosen', )


class EditPackageForm(forms.ModelForm):
    class Meta:
        model=Packages
        fields=('quantity', 'price',)


