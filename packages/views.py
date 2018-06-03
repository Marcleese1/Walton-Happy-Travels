from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DeleteView
from . import models
from .models import Packages
from django.views.generic.edit import CreateView, UpdateView
import stripe
from WaltonHappyTravel2 import settings
from bookings.models import Bookings, Trip
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .forms import ChooseSeatsForm
import json
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail

class ViewPackages(ListView):
    model = models.Packages
    template_name = 'viewpackages.html'


#the function used by the customer to choose the amount of people that will be going on the trip
class ChooseSeats(UpdateView, LoginRequiredMixin):
    form_class = ChooseSeatsForm
    queryset = models.Packages.objects.all()
    #this function will remove the amount of seats chosen from the quantity of the package
    #it will then create a whole bunch of session variables to be used in the checkout
    def form_valid(self, form: ChooseSeatsForm):
        price = form.instance.price
        seatschosen = form.cleaned_data['seatsChosen']
        destination = form.instance.destination
        hotel = form.instance.hotelName
        duration = form.instance.duration
        departure = str(form.instance.departureDate)
        quan = form.instance.quantity
        id = form.instance.id
        type = form.instance.type
        quan -= form.cleaned_data['seatsChosen']
        self.request.session['quantity'] = quan
        self.request.session['seatsChosen'] = seatschosen
        self.request.session['price'] = price
        self.request.session['destination'] = destination
        self.request.session['hotelName'] = hotel
        self.request.session['duration'] = duration
        self.request.session['type'] = type
        self.request.session['id'] = id
        self.request.session['departureDate'] = departure
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
        bookingPayment=request.session['amount'],
        user=request.user,

    )
    trip = Trip(
        destination=request.session['destination'],
        duration=request.session['duration'],
        price=request.session['price'],
        hotelName=request.session['hotelName'],
        totalCost=request.session['amount']
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
        new_booking.save() and trip.save()

        send_mail(
            'Walton Happy Travels Package Booking',
            'Thank you '+request.user.email+' for Booking with Walton Happy Travels. Please find below the '+
            'details of your Booking'+"\n"+
            'Details:' +"\n"+ 'destination: '+ str(request.session['destination'])+"\n"+ 'duration: '
            + str(request.session['duration']) + ' Days' + "\n" + 'Departure Date: ' +
            str(request.session['departureDate']) + "\n" + 'Hotel Name: ' + str(request.session['hotelName']) +"\n"+
            'Number of People: ' + str(request.session['seatsChosen']) + "\n" + 'Total Cost: £'
            + request.session['amount'][:-2], 'WaltonHappyTravels@gmail.com',
            ['marcleesewalton@gmail.com'],
            fail_silently=False
        )

        return redirect("home")


#the payment for that initiates stripe and creates the sessions for seats chosen, price
#and then works out the amount the customer will have to pay for the booking
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


#allows the user to delete their Bookings
class Delete_Booking(DeleteView, LoginRequiredMixin):
    form_class = ChooseSeatsForm
    model = Bookings
    queryset = models.Bookings.objects.all()
    success_url = reverse_lazy('bookings_list')

class Delete_package(DeleteView, LoginRequiredMixin):
    model = Packages
    queryset = Packages.objects.all()
    success_url = reverse_lazy('viewpackages')
