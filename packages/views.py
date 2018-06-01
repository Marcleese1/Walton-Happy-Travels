from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DeleteView
from . import models
from django.views.generic.edit import CreateView, UpdateView
import stripe
from WaltonHappyTravel2 import settings
from bookings.models import Bookings, Trip
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .forms import ChooseSeatsForm
import json
from django.http import HttpResponse


class ViewPackages(ListView):
    model = models.Packages
    template_name = 'viewpackages.html'


class ChooseSeats(UpdateView, LoginRequiredMixin):
    form_class = ChooseSeatsForm
    queryset = models.Packages.objects.all()

    def form_valid(self, form: ChooseSeatsForm):
        price = form.instance.price
        seatschosen = form.cleaned_data['seatsChosen']
        destination = form.instance.destination
        hotel = form.instance.hotelName
        duration = form.instance.duration
        type = form.instance.type
        form.instance.quantity -= form.cleaned_data['seatsChosen']
        self.request.session['seatsChosen'] = seatschosen
        self.request.session['price'] = price
        self.request.session['destination'] = destination
        self.request.session['hotelName'] = hotel
        self.request.session['duration'] = duration
        self.request.session['type'] = type
        form.instance.save()
        return redirect('payment')


class EditPackage(UpdateView, LoginRequiredMixin):
    model = models.Packages
    template_name = 'editPackage.html'
    fields = ['price', 'quantity']
    success_url = reverse_lazy('viewpackages')


class PackageCreateView(LoginRequiredMixin, CreateView):
    model = models.Packages
    template_name = 'package_new.html'
    fields = ['destination', 'hotelName', 'departureDate', 'leavingTime', 'duration', 'price']
    success_url = reverse_lazy('home')


stripe.api_key = settings.STRIPE_SECRET_KEY


# function used for the checkout this funtction creates the booking ID the Date and how much is costs.
def checkout(request):

    new_booking = Bookings(
        bookingType=request.session['type'],
        seatsChosen=request.session['seatsChosen'],
        bookingPayment=request.session['amount']

    )
    trip = Trip(
        destination=request.session['destination'],
        duration=request.session['duration'],
        price=request.session['price'],
        hotelName=request.session['hotelName']
    )
    if request.method =="POST":
        token = request.POST.get("stripeToken")
    try:
        charge = stripe.Charge.create(
            amount= request.session['amount'],
            currency = "gbp",
            source = token,
            description = "booking successfully made"

        )
        new_booking.charge_id = charge.id
    except stripe.error.CardError as ce:
        return False, ce
    else:
        new_booking.save()
        trip.save()
        return redirect("home")


def payment_form(request):
    seats = request.session['seatsChosen']
    price = request.session['price']
    amount = seats * price
    request.session['amount'] = str(amount) + "00"
    print(seats)
    print(price)
    print(amount)
    context = {"stripe_key": settings.STRIPE_PUBLIC_KEY }
    return render(request, "Payment.html", context)

#allows the user to delete their account
class delete_booking(DeleteView):
    model = Bookings
    queryset = models.Bookings.objects.all()

    def addquantity(self, form: ChooseSeatsForm):
        form.instance.quantity += form.cleaned_data['seatsChosen']
        form.instance.save()
        return redirect('bookings_list')