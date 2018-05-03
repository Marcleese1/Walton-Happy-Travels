'''
import stripe
from WaltonHappyTravel2 import settings
from bookings.models import Bookings
from django.shortcuts import redirect,render

stripe.api_key = settings.STRIPE_SECRET_KEY


def checkout(request):
    new_booking = Bookings(
        customer="TEST@TEST.COM",
        BookingId="abc123",
        bookingDate="02/05/2018",
        bookingType="Flight",
        bookingPayment="2000",
        bookingDeposit="0"
    )
    if request.method == "POST":
        token = request.POST.get("stripeToken")

        try:
            charge = stripe.Charge.create(
                amount=2000,
                currenct = "gbp",
                source = token,
                description = "The Booking has been made"
            )
            new_booking.charge_id = charge.id
        except stripe.error.CardError as ce:
            return False, ce
        else:
            new_booking.save()
            return redirect("thank_you_page")


def payment_form(request):

    context = {"stripe_key": settings.STRIPE_PUBLIC_KEY}
    return render(request, "Payment.html", context)'''