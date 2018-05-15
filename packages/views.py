from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from . import models
from django.views.generic.edit import CreateView
import stripe
from WaltonHappyTravel2 import settings
from bookings.models import Bookings
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import Packages
from users.models import Customer
from django.utils import timezone


class ViewPackages(ListView):
    model = models.Packages
    template_name = 'viewpackages.html'


class PackageCreateView(LoginRequiredMixin, CreateView):
    model = models.Packages
    template_name = 'package_new.html'
    fields = ['destination', 'hotelName', 'duration', 'price']
    success_url = reverse_lazy('home')


stripe.api_key = settings.STRIPE_SECRET_KEY


# function used for the checkout this funtction creates the booking ID the Date and how much is costs.
def checkout(request):
    new_booking = Bookings(
        customer_id=Customer.id,
        bookingDate=timezone.now,
        bookingType="Coach",
        bookingPayment=2000,
        bookingDeposit=0,
    )
    if request.method == "POST":
        token = request.POST["stripeToken"]

        try:
            charge = stripe.Charge.create(
                amount=2000,
                currency="gbp",
                source=token,
                description="The Booking has been made"
            )
            new_booking.charge_id = charge.id
        except stripe.error.CardError as ce:
            return False, ce
        else:
            new_booking.save()
            return redirect("home")


def payment_form(request):

    context = {"stripe_key": settings.STRIPE_PUBLIC_KEY}
    return render(request, "Payment.html", context)

