# users/admin.py
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomerCreationForm, CustomerChangeForm
from .models import Customer


class CustomUserAdmin(UserAdmin):
    add_form = CustomerCreationForm
    form = CustomerChangeForm
    model = Customer
    list_display = ['id', 'email', 'password', 'Address_Line_1', 'Address_Line_2', 'postCode', 'PhoneNumber']

    ordering = ('email',)


admin.site.register(Customer, CustomUserAdmin)

