# users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomerCreationFormAdmin, CustomerChangeFormAdmin
from .models import Customer


#USED TO DISPLAY THE CUSTOMER INFORMATION ON THE ADMIN PAGE USING THE CUSTOM FORM
class CustomUserAdmin(UserAdmin):
    add_form = CustomerCreationFormAdmin
    form = CustomerChangeFormAdmin
    model = Customer
    list_display = ['email', 'password', 'Address_Line_1', 'Address_Line_2', 'postCode', 'PhoneNumber']
    fieldsets = (
        (None,
         {'fields': ('email', 'password', 'date_joined')}),
        ('Personal info',
         {'fields': ('first_name', 'last_name', 'Address_Line_1', 'Address_Line_2', 'town', 'postCode', 'PhoneNumber')}),
        ('Permissions',
         {'fields': ('is_staff', 'is_superuser','is_active', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active', 'Address_Line_1', 'Address_Line_2',
                       'town', 'postCode',
                       'PhoneNumber', 'homePhone')}
         ),
    )
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)


admin.site.register(Customer, CustomUserAdmin)

