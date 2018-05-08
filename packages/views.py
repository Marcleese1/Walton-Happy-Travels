from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from . import models
from django.views.generic.edit import CreateView
import stripe
from WaltonHappyTravel2 import settings
from bookings.models import Bookings
from django.shortcuts import redirect, render
from django.urls import reverse_lazy


class ViewPackages(ListView):
    model = models.Packages
    template_name = 'viewpackages.html'


class PackageCreateView(LoginRequiredMixin, CreateView):
    model = models.Packages
    template_name = 'package_new.html'
    fields = ['destination', 'hotelName', 'duration', 'price']
    success_url = reverse_lazy('home')


stripe.api_key = settings.STRIPE_SECRET_KEY


def checkout(request):
    new_booking = Bookings(
        BookingId="a2dca2be49674e46aa9ccdd76eadf699",
        bookingDate="2018-05-03",
        bookingType="Flight",
        bookingPayment="200000",
        bookingDeposit="0"
    )
    if request.method == "POST":
        token = request.POST.get("stripeToken")

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
