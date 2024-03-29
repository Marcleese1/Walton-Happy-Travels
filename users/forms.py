# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Customer
from django.forms import ValidationError


# THE FORM TO CREATE A CUSTOMER
class CustomerCreationFormAdmin(UserCreationForm):
    error_messages = {
        'password_mismatch': "The two password fields didn't match.",
    }
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput,
                                help_text="Enter the same password as above, for verification.")

    class Meta:
        model = Customer
        fields = ('email',)

    def save(self, commit=True):
        customer = super(UserCreationForm, self).save(commit=False)
        customer.set_password(self.cleaned_data["password1"])
        if commit:
            customer.save()
        return customer


#THE FORM USED TO CREATE GENERAL USERS
class UserCustomerForm(UserCreationForm):
    error_messages = {
        'password_mismatch': "The two password fields didn't match.",
    }
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput,
                                help_text="Enter the same password as above, for verification.")

    class Meta:
        model = Customer
        fields = ('email',
                  'password1',
                  'password2',
                  'first_name',
                  'last_name',
                  'Address_Line_1',
                  'Address_Line_2',
                  'town',
                  'postCode',
                  'homePhone',
                  'PhoneNumber',)

    def save(self, commit=True):
        customer = super(UserCreationForm, self).save(commit=False)
        customer.set_password(self.cleaned_data["password1"])
        if commit:
            customer.save()
        return customer


# the form used for the edit customer view
# this is an override in it bringing in all of the information in the customer database
class CustomerChangeFormAdmin(UserChangeForm):
    class Meta:
        model = Customer
        fields = ('email', 'first_name', 'last_name', 'Address_Line_1', 'Address_Line_2', 'town', 'postCode',
                  'PhoneNumber', 'homePhone')

    def init(self, args, **kwargs):
        super(UserChangeForm, self).init(args, **kwargs)
        f = self.fields.get('user_permissions', None)
        if f is not None:
            f.queryset = f.queryset.select_related('content_type')


#allows the User to Delte their account
class DeactivateUserForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['is_active']

    def __init__(self, *args, **kwargs):
        super(DeactivateUserForm, self).__init__(*args,**kwargs)
        self.fields['is_active'].help_texts = "Check this box if you are sure you wish to delete your account"

    def clean_is_active(self):
        is_active = not(self.cleaned_data["is_active"])
        return is_active



