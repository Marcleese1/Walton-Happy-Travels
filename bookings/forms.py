# bookings/forms.py
import datetime
from django import forms
from.models import Bookings
from packages.models import Packages


#form for showing the bookings in view booking
class BookingsChangeFormAdmin(forms.ModelForm):
    class Meta:
        model = Bookings
        fields = ('user', 'bookingDate', 'bookingPayment', 'bookingType', 'bookingDeposit', 'seatsChosen' )


#form for showing edit booking
class EditBookingForm(forms.ModelForm):
    class Meta:
        model = Bookings
        fields = ('seatsChosen', )


#form for showing seats chosen
class ChooseSeatsForm(forms.ModelForm):
    class Meta:
        model = Bookings
        fields = ('seatsChosen', )



