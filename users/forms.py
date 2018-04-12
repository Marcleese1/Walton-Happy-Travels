# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Customer


class CustomerCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Customer
        fields = ('email', 'FirstName', 'LastName')


class CustomerChangeForm(UserChangeForm):

    class Meta:
        model = Customer
        fields = UserChangeForm.Meta.fields
