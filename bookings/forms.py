# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from users.models import Customer
from django.contrib.auth import authenticate
from django import template
from.models import Bookings
from django.shortcuts import render
'''
class BookingForm(forms.ModelForm):
    def __init__(self, session=None, user=None, *args, **kwargs):
        self.user = user
        self.session = session
        super(BookingForm, self).__init__(*args, **kwargs)
        # fields that should remain blank / not required
        keep_blank = [
            'phone', 'notes', 'street2', 'title', 'user', 'session',
            'date_from', 'date_until', 'special_request', 'time_period',
            'time_unit', 'email', 'currency', 'total']
        # set all fields except the keep_blank ones to be required, since they
        # need to be blank=True on the model itself to allow creating Booking
        # instances without data
        for name, field in self.fields.items():
            if name not in keep_blank:
                self.fields[name].required = True


class BookingIDAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(BookingIDAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['email']=forms.EmailField(label=_("Email"), max_length=256)
        self.fields['password']=forms.CharField(label=_("Booking ID"), max_length=100)

    def clean_username(self):
        return self.cleaned_data['email'].lower()

    def clean(self):
        email = self.cleaned_data.get('email')
        booking_id = self.cleaned_data.get('password')

        if email and booking_id:
            self.user_cache= authenticate(username=email, password=booking_id)

            if self.user_cache is None:
                raise forms.ValidationError(_('we cannot find a valid booking ID for this email'' address.'))
            elif not self.user_cache.is_active:
                raise forms.ValidationError(self.error_messages['inactive'])
            self.check_for_test_cookie()
            return self.cleaned_data
'''
register = template.Library()


@register.simple_tag
def booking_list(request):
    bookings = Bookings.objects.all()
    return render(request, 'bookings/bookings_list', {'bookings': bookings})


#the form which allows the user to edit their details.
class EditForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['email', 'first_name', 'last_name', 'Address_Line_1', 'Address_Line_2', 'town', 'postCode',
                 'PhoneNumber', 'homePhone']




