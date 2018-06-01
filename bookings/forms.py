# users/forms.py
from django import forms
from django.contrib.auth.forms import UserChangeForm
from users.models import Customer
from django.contrib.auth import authenticate
from django import template
from.models import Bookings
from django.shortcuts import render


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