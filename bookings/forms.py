# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import Customer

#the form which allows the user to edit their details.
class EditForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['email', 'FirstName', 'LastName', 'Address_Line_1', 'Address_Line_2', 'town', 'postCode',
                 'PhoneNumber', 'homePhone']

