# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Customer
from django.shortcuts import render
from django.http import HttpResponse, response


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


class UserCustomerForm(UserCreationForm):
    error_messages = {
        'password_mismatch': "The two password fields didn't match.",
    }
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput,
                                help_text="Enter the same password as above, for verification.")

    class Meta:
        model = Customer
        fields = ('email', 'password1', 'password2', 'first_name', 'last_name', 'Address_Line_1', 'Address_Line_2',
                  'town', 'postCode', 'homePhone', 'PhoneNumber')


class CustomerChangeFormAdmin(UserChangeForm):
    class Meta:
        model = Customer
        fields = '__all__'

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
        # Reverses true/false for your form prior to validation
        #
        # You can also raise a ValidationError here if you receive
        # a value you don't want, to prevent the form's is_valid
        # method from return true if, say, the user hasn't chosen
        # to deactivate their account
        is_active = not(self.cleaned_data["is_active"])
        return is_active




