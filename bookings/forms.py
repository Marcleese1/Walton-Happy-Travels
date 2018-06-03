# bookings/forms.py
import datetime
from django import forms
from.models import Bookings
from packages.models import Packages


class BookingsChangeFormAdmin(forms.ModelForm):
    class Meta:
        model = Bookings
        fields = ('user', 'bookingDate', 'bookingPayment', 'bookingType', 'bookingDeposit', 'seatsChosen' )


class EditBookingForm(forms.ModelForm):
    class Meta:
        model = Bookings
        fields = ('seatsChosen', )


class ChooseSeatsForm(forms.ModelForm):
    class Meta:
        model = Bookings
        fields = ('seatsChosen', )


class GenerateReport(forms.ModelForm):
    Start = forms.DateField(widget=forms.SelectDateWidget, initial=datetime.date.today())
    End = forms.DateField(widget=forms.SelectDateWidget, initial=datetime.date.today())

    class Meta:
        model = Bookings
        fields = ('bookingDate', )
