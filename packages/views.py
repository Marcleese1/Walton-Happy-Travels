from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from . import models
from django.views.generic.edit import CreateView, UpdateView
import stripe
from WaltonHappyTravel2 import settings
from bookings.models import Bookings
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .forms import ChooseSeatsForm
from django.contrib.messages.views import SuccessMessageMixin


class ViewPackages(ListView):
    model = models.Packages
    template_name = 'viewpackages.html'


class ChooseSeats(UpdateView, LoginRequiredMixin):
    form_class = ChooseSeatsForm
    queryset = models.Packages.objects.all()

    def form_valid(self, form: ChooseSeatsForm):
        form.instance.quantity -= form.cleaned_data['seatsChosen']
        form.instance.save()
        return redirect('viewpackages')


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
#def checkout(request):
#
 #   if request.method =="POST":
  #      token = request.POST.get("stripeToken")
   # try:
    #    charge = stripe.Charge.create(
     #       amount = 2000,
      #      currency = "gbp",
       #     source = token,
        #    description = "booking successfully made"

        #)
        #new_booking.charge_id = charge.id
    #except stripe.error.CardError as ce:
     #   return False, ce
    #else:
     #   new_booking.save()
      #  return redirect("home")

#def payment_form(request):
 #   context = {"stripe_key": settings.STRIPE_PUBLIC_KEY }
  #  return render(request, "Payment.html", context)